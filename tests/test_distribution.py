"""Exercise the shipped archive, version gates, and native plugin loading."""

import hashlib
import importlib.util
import json
import os
from pathlib import Path
import queue
import re
import shutil
import subprocess
import tempfile
import threading
import time
import unittest
from unittest.mock import patch
import zipfile

ROOT = Path(__file__).resolve().parents[1]
# Native installation tests must use an explicitly selected executable: shell
# account wrappers may discard CLAUDE_CONFIG_DIR and mutate the live profile.
CLAUDE_BIN = os.environ.get("UFOSKILL_CLAUDE_BIN")
spec = importlib.util.spec_from_file_location("manage", ROOT / "scripts/manage.py")
manage = importlib.util.module_from_spec(spec)
spec.loader.exec_module(manage)


def copy_package(destination):
    """Copy only distributable inputs, excluding local environments and runs."""
    for source in manage.package_files(ROOT):
        target = destination / source.relative_to(ROOT)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)


class DistributionTests(unittest.TestCase):
    def test_skill_is_self_contained_and_all_guides_are_reachable(self):
        with tempfile.TemporaryDirectory() as temp:
            skill = Path(temp) / "writing"
            shutil.copytree(ROOT / "skills/writing", skill)
            pending = [skill / "SKILL.md"]
            visited = set()
            while pending:
                page = pending.pop().resolve()
                if page in visited:
                    continue
                self.assertTrue(page.is_relative_to(skill))
                self.assertTrue(page.is_file(), str(page))
                visited.add(page)
                for target in re.findall(r"\]\(([^)]+)\)", page.read_text(encoding="utf-8")):
                    if "://" not in target and not target.startswith("#"):
                        pending.append(page.parent / target.split("#")[0])
            self.assertEqual(visited, {p.resolve() for p in skill.rglob("*.md")})

    @unittest.skipUnless(shutil.which("codex"), "Codex CLI is not installed")
    def test_codex_reads_one_skill_from_archive(self):
        with tempfile.TemporaryDirectory(prefix="ufoskill-codex-") as temp:
            base = Path(temp)
            manage.build(base)
            plugin = base / "plugin"
            with zipfile.ZipFile(next(base.glob("*.zip"))) as package:
                package.extractall(plugin)
            # Read-only discovery through the native server; no model call or user-config edit.
            proc = subprocess.Popen(
                ["codex", "app-server", "--stdio"], stdin=subprocess.PIPE,
                stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True, bufsize=1,
            )
            output = queue.Queue()

            def read_output():
                for line in proc.stdout:
                    output.put(line)
                output.put(None)

            reader = threading.Thread(target=read_output, daemon=True)
            reader.start()

            def request(request_id, method, params):
                proc.stdin.write(json.dumps({"jsonrpc": "2.0", "id": request_id,
                                             "method": method, "params": params}) + "\n")
                proc.stdin.flush()
                deadline = time.monotonic() + 30
                while time.monotonic() < deadline:
                    line = output.get(timeout=max(0, deadline - time.monotonic()))
                    self.assertIsNotNone(line, "Codex server closed before responding")
                    response = json.loads(line)
                    if response.get("id") == request_id:
                        self.assertNotIn("error", response)
                        return response["result"]
                self.fail(f"Codex server timed out: {method}")

            try:
                request(1, "initialize", {
                    "clientInfo": {"name": "ufoskill-validation", "version": manage.validate()},
                    "capabilities": {"experimentalApi": True},
                })
                detail = request(2, "plugin/read", {
                    "marketplacePath": str(plugin / ".agents/plugins/marketplace.json"),
                    "pluginName": "ufoskill",
                })["plugin"]
                self.assertEqual({s["name"] for s in detail["skills"]},
                                 {"ufoskill:writing"})
                for skill in detail["skills"]:
                    entry = Path(skill["path"])
                    self.assertTrue(entry.is_relative_to(plugin))
                    self.assertTrue((entry.parent / "references/general.md").is_file())
                    self.assertIn(f'${skill["name"]}', skill["interface"]["defaultPrompt"])
            finally:
                proc.terminate()
                try:
                    proc.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    proc.kill()
                    proc.wait()
                reader.join(timeout=5)
                proc.stdin.close()
                proc.stdout.close()

    @unittest.skipUnless(shutil.which("codex"), "Codex CLI is not installed")
    def test_codex_discovers_plugin(self):
        result = subprocess.run(
            ["codex", "-c", 'marketplaces.UFOdestiny.source_type="local"',
             "-c", "marketplaces.UFOdestiny.source=" + json.dumps(str(ROOT)),
             "plugin", "list", "--marketplace", "UFOdestiny", "--available", "--json"],
            capture_output=True, text=True, check=True, timeout=45,
        )
        plugins = json.loads(result.stdout)
        candidates = plugins["available"] + plugins["installed"]
        # Listing an installed plugin reports its installed version, even when
        # the marketplace points at a newer checkout. Archive loading is tested
        # independently above; discovery verifies identity and source here.
        self.assertTrue(any(p["pluginId"] == "ufoskill@UFOdestiny"
                            and p["marketplaceSource"]["source"] == str(ROOT)
                            for p in candidates))

    @unittest.skipUnless(CLAUDE_BIN and shutil.which(CLAUDE_BIN),
                         "Set UFOSKILL_CLAUDE_BIN to a native Claude executable")
    def test_claude_installs_archive_and_loads_one_skill(self):
        with tempfile.TemporaryDirectory(prefix="ufoskill-client-") as temp:
            base = Path(temp)
            manage.build(base)
            plugin = base / "plugin"
            with zipfile.ZipFile(next(base.glob("*.zip"))) as package:
                package.extractall(plugin)
            env = dict(os.environ, CLAUDE_CONFIG_DIR=str(base / "config"), NO_COLOR="1")
            for args in (("marketplace", "add", str(plugin)), ("install", "ufoskill@UFOdestiny")):
                subprocess.run([CLAUDE_BIN, "plugin", *args], env=env, check=True,
                               capture_output=True, text=True, timeout=45)
            result = subprocess.run([CLAUDE_BIN, "plugin", "details", "ufoskill"], env=env,
                                    check=True, capture_output=True, text=True, timeout=45)
            self.assertRegex(result.stdout, r"Skills\s+\(1\)")
            self.assertIn("writing", result.stdout)
            # Check resources in the host's installed copy, not just the source ZIP.
            installed = list((base / "config/plugins/cache").rglob("skills/writing/references/general.md"))
            self.assertEqual(len(installed), 1)
            self.assertEqual(manage.validate(installed[0].parents[3]), manage.validate())

    def test_archive_is_reproducible_and_self_contained(self):
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp)
            manage.build(output)
            archive = next(output.glob("*.zip"))
            first = archive.read_bytes()
            manage.build(output)
            self.assertEqual(first, archive.read_bytes())
            checksum = (output / "SHA256SUMS").read_text().split()[0]
            self.assertEqual(checksum, hashlib.sha256(first).hexdigest())
            unpacked = output / "unpacked"
            with zipfile.ZipFile(archive) as package:
                names = package.namelist()
                self.assertTrue(all(not n.startswith(("/", "../")) for n in names))
                self.assertTrue(all(not n.startswith((".git/", "tests/", "dist/")) for n in names))
                package.extractall(unpacked)
            self.assertEqual(manage.validate(), manage.validate(unpacked))
            for source in manage.package_files(ROOT):
                self.assertEqual((unpacked / source.relative_to(ROOT)).read_bytes(), source.read_bytes())

    def test_missing_and_unshipped_references_are_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            copy = Path(temp) / "repo"
            copy_package(copy)
            guide = copy / "skills/writing/references/general.md"
            original = guide.read_text()
            for target in ("missing.md", "../../../scripts/manage.py", "../../../../outside.md"):
                with self.subTest(target=target):
                    guide.write_text(original + f"\n[broken reference]({target})\n")
                    with self.assertRaisesRegex(ValueError, "missing or unshipped reference"):
                        manage.validate(copy)
            guide.write_text(original)
            guide.unlink()
            with self.assertRaisesRegex(ValueError, "missing or unshipped reference"):
                manage.validate(copy)

    def test_extra_skills_are_rejected_at_any_depth(self):
        with tempfile.TemporaryDirectory() as temp:
            copy = Path(temp) / "repo"
            copy_package(copy)
            for relative in ("skills/review/SKILL.md", "skills/nested/writing/SKILL.md"):
                with self.subTest(path=relative):
                    extra = copy / relative
                    extra.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copyfile(copy / "skills/writing/SKILL.md", extra)
                    with self.assertRaisesRegex(ValueError, "exactly one writing skill"):
                        manage.validate(copy)
                    extra.unlink()

    def test_symlinked_resources_are_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            copy = Path(temp) / "repo"
            copy_package(copy)
            (copy / "skills/writing/references/external").symlink_to(ROOT / "skills/writing/references", target_is_directory=True)
            with self.assertRaisesRegex(ValueError, "symlink"):
                manage.validate(copy)

    def test_local_outputs_are_excluded_from_package(self):
        with tempfile.TemporaryDirectory() as temp:
            copy = Path(temp) / "repo"
            copy_package(copy)
            outputs = (
                "skills/writing/references/.env", "skills/writing/references/.env.local", "skills/writing/references/.cache/draft.md",
                "skills/writing/references/notes.md.bak", "skills/writing/references/build.log", "skills/writing/references/preview.zip",
                "skills/writing/__pycache__/cached.pyc",
            )
            for name in outputs:
                path = copy / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(b"local output")
            with patch.object(manage, "ROOT", copy):
                manage.build(copy / "dist")
                with zipfile.ZipFile(next((copy / "dist").glob("*.zip"))) as package:
                    self.assertTrue(set(outputs).isdisjoint(package.namelist()))
                    self.assertIn("skills/writing/references/general.md", package.namelist())
                    self.assertIn("skills/writing/agents/openai.yaml", package.namelist())

    def test_release_tag_must_match_version(self):
        version = manage.validate()
        self.assertEqual(version, manage.validate(tag=f"v{version}"))
        with self.assertRaises(ValueError):
            manage.validate(tag="v999.0.0")

    def test_yaml_syntax_types_and_duplicate_fields_are_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            copy = Path(temp) / "repo"
            copy_package(copy)
            entry = copy / "skills/writing/SKILL.md"
            original = entry.read_text(encoding="utf-8")
            body = original.split("---", 2)[2]
            for fields in (
                "name: writing\ndescription: [broken",
                "name: writing\ndescription: [valid, yaml, wrong, type]",
                "name: writing\ndescription: true",
                "name: writing\ndescription: first\ndescription: second",
            ):
                with self.subTest(fields=fields):
                    entry.write_text(f"---\n{fields}\n---{body}", encoding="utf-8")
                    with self.assertRaises(ValueError):
                        manage.validate(copy)
            entry.write_text("---\nname: writing\ndescription: >\n  A valid multiline description.\n---" + body,
                             encoding="utf-8")
            self.assertEqual(manage.validate(copy), manage.validate())
            entry.write_text(original, encoding="utf-8")
            interface = copy / "skills/writing/agents/openai.yaml"
            original = interface.read_text(encoding="utf-8")
            for broken in (
                "invalid: [\n# $ufoskill:writing\n",
                original.replace("default_prompt:", "other_field:"),
                original.replace("$ufoskill:writing", "$ufoskill:writing-extra"),
                original.replace("allow_implicit_invocation: true", 'allow_implicit_invocation: "true"'),
                original + "\npolicy: {}\n",
            ):
                with self.subTest(interface=broken):
                    interface.write_text(broken, encoding="utf-8")
                    with self.assertRaises(ValueError):
                        manage.validate(copy)

    def test_bump_updates_all_hosts_and_rejects_downgrade(self):
        with tempfile.TemporaryDirectory() as temp:
            copy = Path(temp) / "repo"
            copy_package(copy)
            with patch.object(manage, "ROOT", copy):
                manage.bump("999.0.0")
                self.assertEqual(manage.validate(), "999.0.0")
                with self.assertRaises(ValueError):
                    manage.bump("0.1.0")
                manifest = copy / ".claude-plugin/plugin.json"
                data = json.loads(manifest.read_text())
                data["version"] = "0.1.0"
                manifest.write_text(json.dumps(data))
                with self.assertRaises(ValueError):
                    manage.validate()

if __name__ == "__main__":
    unittest.main()
