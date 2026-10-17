#!/usr/bin/env python3
"""Validate, version, and package the shared Codex/Claude Code writing plugin."""

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
import zipfile

import yaml

ROOT = Path(__file__).resolve().parents[1]
MANIFESTS = ("plugin.json", ".claude-plugin/plugin.json")
CATALOGS = (".agents/plugins/marketplace.json", ".claude-plugin/marketplace.json")
SKILLS = ("ai-paper-writing", "ai-paper-review", "ai-paper-check")
RESOURCE_DIRS = ("skills", "shared")
# Runtime resources are text guidance and metadata. Do not bundle local outputs.
RESOURCE_SUFFIXES = {".md", ".yaml", ".yml", ".json"}
SEMVER = re.compile(r"(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\Z")


class UniqueSafeLoader(yaml.SafeLoader):
    """Reject duplicate fields instead of silently overwriting metadata."""


def unique_mapping(loader, node):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node)
        require(isinstance(key, str), "YAML metadata keys must be strings")
        require(key not in result, f"duplicate YAML key: {key}")
        result[key] = loader.construct_object(value_node)
    return result


UniqueSafeLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def read_yaml(text, location):
    try:
        data = yaml.load(text, Loader=UniqueSafeLoader)
    except (yaml.YAMLError, ValueError) as error:
        raise ValueError(f"{location}: invalid YAML: {error}") from error
    require(isinstance(data, dict), f"{location}: YAML must be a mapping")
    return data


def nonempty_string(value):
    return isinstance(value, str) and bool(value.strip())


def read_json(root, name):
    return json.loads((root / name).read_text(encoding="utf-8"))


def require(condition, message):
    if not condition:
        raise ValueError(message)


def package_files(root):
    files = [root / name for name in (*MANIFESTS, *CATALOGS, "README.md", "LICENSE")]
    for directory in RESOURCE_DIRS:
        folder = root / directory
        require(folder.is_dir() and not folder.is_symlink(), f"missing or symlinked resource directory: {directory}")
        for path in sorted(folder.rglob("*")):
            require(not path.is_symlink(), f"package contains a symlink: {path.relative_to(root)}")
            relative_parts = path.relative_to(folder).parts
            if any(part.startswith(".") or part == "__pycache__" for part in relative_parts):
                continue
            if path.is_file() and path.suffix in RESOURCE_SUFFIXES:
                files.append(path)
    return files


def validate(root=None, tag=None):
    root = (ROOT if root is None else root).resolve()
    manifests = [read_json(root, name) for name in MANIFESTS]
    version = manifests[0]["version"]
    require(SEMVER.fullmatch(version), "version must be MAJOR.MINOR.PATCH")
    for name, manifest in zip(MANIFESTS, manifests):
        require(manifest["name"] == "myskill", f"{name}: unexpected plugin name")
        require(manifest["version"] == version, f"{name}: version drift")
        require(manifest["description"] and manifest["author"]["name"], f"{name}: missing metadata")
    require(manifests[0]["$schema"] == "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
            "portable manifest must declare the Agent Plugins schema")
    portable_metadata = {k: v for k, v in manifests[0].items() if k != "$schema"}
    require(portable_metadata == manifests[1], "portable and Claude plugin metadata differ")
    for name in CATALOGS:
        catalog = read_json(root, name)
        require(catalog["name"] == "myskill", f"{name}: unexpected marketplace name")
        require(len(catalog["plugins"]) == 1, f"{name}: expected one plugin")
        plugin = catalog["plugins"][0]
        require(plugin["name"] == "myskill", f"{name}: plugin identity drift")
        source = plugin["source"]
        path = source["path"] if isinstance(source, dict) else source
        require(path == "./", f"{name}: source must resolve to the repository root")
        if name.startswith(".claude"):
            require(catalog["owner"]["name"], "Claude marketplace needs an owner")
        else:
            require(source["source"] == "local", "Codex catalog must use a local source")
            require(plugin["policy"] == {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
                    "unexpected Codex install policy")
    actual_skills = {p.parent.name for p in (root / "skills").glob("*/SKILL.md")}
    require(actual_skills == set(SKILLS), "expected writing, review, and check skills")
    for name in SKILLS:
        skill = root / "skills" / name
        entry = (skill / "SKILL.md").read_text(encoding="utf-8")
        frontmatter = re.match(r"\A---\n(.*?)\n---(?:\n|$)", entry, re.DOTALL)
        require(frontmatter, f"{name}: skill needs YAML frontmatter")
        fields = read_yaml(frontmatter[1], f"{name}/SKILL.md")
        require(fields.get("name") == name and nonempty_string(fields.get("description")),
                f"{name}: skill name or description is missing")
        require("../../shared/principles.md" in entry, f"{name}: shared principles link is missing")
        interface = skill / "agents/openai.yaml"
        require(interface.is_file(), f"{name}: Codex interface is missing")
        agent = read_yaml(interface.read_text(encoding="utf-8"), str(interface.relative_to(root)))
        ui = agent.get("interface")
        require(isinstance(ui, dict), f"{name}: interface must be a mapping")
        for key in ("display_name", "short_description", "default_prompt"):
            require(nonempty_string(ui.get(key)), f"{name}: {key} must be a nonempty string")
        require(re.search(r"\$myskill:" + re.escape(name) + r"(?![\w-])", ui["default_prompt"]),
                f"{name}: default prompt must invoke its own skill")
        policy = agent.get("policy", {})
        require(isinstance(policy, dict), f"{name}: policy must be a mapping")
        if "allow_implicit_invocation" in policy:
            require(type(policy["allow_implicit_invocation"]) is bool,
                    f"{name}: allow_implicit_invocation must be a boolean")
    files = package_files(root)
    shipped = {p.resolve() for p in files}
    for file in files:
        require(file.is_file() and not file.is_symlink(), f"missing or symlinked package file: {file}")
        text = file.read_text(encoding="utf-8")
        require("\ufffd" not in text, f"invalid replacement character in {file}")
        if file.suffix == ".md":
            for match in re.finditer(r"\]\(([^)]+)\)", text):
                target = match[1]
                if "://" in target or target.startswith("#"):
                    continue
                resolved = (file.parent / target.split("#")[0]).resolve()
                require(resolved.is_relative_to(root) and resolved in shipped and resolved.is_file(),
                        f"missing or unshipped reference in {file.relative_to(root)}: {target}")
    if tag:
        require(tag == f"v{version}", f"tag {tag!r} does not match v{version}")
    return version


def bump(version):
    require(SEMVER.fullmatch(version), "version must be MAJOR.MINOR.PATCH")
    current = validate()
    require(tuple(map(int, version.split("."))) > tuple(map(int, current.split("."))),
            f"new version must be greater than {current}")
    for name in MANIFESTS:
        data = read_json(ROOT, name)
        data["version"] = version
        (ROOT / name).write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    validate()
    print(f"Version updated: {current} -> {version}")


def build(output):
    version = validate()
    output.mkdir(parents=True, exist_ok=True)
    archive = output / f"myskill-{version}.zip"
    files = package_files(ROOT)
    # Stable paths, timestamps, and permissions make builds reproducible.
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as package:
        for file in sorted(files):
            info = zipfile.ZipInfo(file.relative_to(ROOT).as_posix(), (2020, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            package.writestr(info, file.read_bytes())
    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    (output / "SHA256SUMS").write_text(f"{digest}  {archive.name}\n", encoding="utf-8")
    print(archive)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    check = sub.add_parser("validate")
    check.add_argument("--tag", help="Require a release tag matching the package version")
    version = sub.add_parser("bump")
    version.add_argument("version")
    package = sub.add_parser("build")
    package.add_argument("--output", type=Path, default=ROOT / "dist")
    args = parser.parse_args()
    try:
        if args.command == "validate":
            print(f"Validated MySKILL {validate(tag=args.tag)}")
        elif args.command == "bump":
            bump(args.version)
        else:
            build(args.output)
    except (ValueError, KeyError, OSError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
