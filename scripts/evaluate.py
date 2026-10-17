#!/usr/bin/env python3
"""Prepare manuscript tasks and assess saved runs; never invoke a model implicitly."""

import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
DIMENSIONS = ("faithfulness", "task_success", "usability")


def cases():
    return json.loads((ROOT / "evals/cases.json").read_text(encoding="utf-8"))


def prepare(destination):
    # A fresh directory protects prior evaluations from accidental overwrite.
    destination.mkdir(parents=True, exist_ok=False)
    for case in cases():
        folder = destination / case["id"]
        workspace = folder / "workspace"
        workspace.mkdir(parents=True)
        for name, content in case["files"].items():
            path = workspace / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
        prompt = f'Use $myskill:{case["skill"]}.\n\n{case["prompt"]}\n'
        (folder / "prompt.txt").write_text(prompt, encoding="utf-8")
    (destination / "run.json").write_text(json.dumps({
        "skill_revision": None, "client_version": None, "model": None,
        "reasoning_effort": None, "date": None, "notes": "Record actual run settings.",
    }, indent=2) + "\n", encoding="utf-8")


def assess_case(case, folder):
    workspace = folder / "workspace"
    failures = []
    actual = {}
    if not workspace.is_dir() or workspace.is_symlink():
        failures.append("workspace missing or symlinked")
    else:
        for path in workspace.rglob("*"):
            name = path.relative_to(workspace).as_posix()
            if path.is_symlink():
                failures.append(f"symlink in workspace: {name}")
            elif path.is_file():
                actual[name] = path.read_bytes()
    expected = {name: content.encode("utf-8") for name, content in case["files"].items()}
    changed = sorted(name for name in actual.keys() | expected.keys()
                     if actual.get(name) != expected.get(name))
    for name in changed:
        if name not in case["allowed_changes"]:
            failures.append(f"unauthorized change: {name}")
    for name, literals in case["protected"].items():
        for literal in literals:
            if literal.encode("utf-8") not in actual.get(name, b""):
                failures.append(f"protected content missing in {name}: {literal}")
    response = folder / "response.md"
    completed = response.is_file() and bool(response.read_text(encoding="utf-8").strip())
    review_path = folder / "review.json"
    review = None
    if review_path.is_file():
        review = json.loads(review_path.read_text(encoding="utf-8"))
        if not isinstance(review, dict):
            raise ValueError(f"{case['id']}: review must be an object")
        for key in DIMENSIONS:
            if type(review.get(key)) is not int or review[key] not in (0, 1, 2):
                raise ValueError(f"{case['id']}: {key} must be 0, 1, or 2")
        if type(review.get("critical_failure")) is not bool:
            raise ValueError(f"{case['id']}: critical_failure must be boolean")
        if not isinstance(review.get("evidence"), str) or not review["evidence"].strip():
            raise ValueError(f"{case['id']}: reviewer evidence is required")
    if failures:
        status = "failed"
    elif not completed:
        status = "not_run"
    elif review is None:
        status = "needs_review"
    else:
        passed = (not review["critical_failure"] and review["faithfulness"] == 2
                  and all(review[key] >= 1 for key in DIMENSIONS)
                  and sum(review[key] for key in DIMENSIONS) >= 5)
        status = "passed" if passed else "failed"
    return {"id": case["id"], "status": status, "changed_files": changed,
            "mechanical_failures": failures, "review": review}


def score(destination):
    if not destination.is_dir():
        raise ValueError(f"run directory does not exist: {destination}")
    results = [assess_case(case, destination / case["id"]) for case in cases()]
    counts = {state: sum(r["status"] == state for r in results)
              for state in ("passed", "failed", "needs_review", "not_run")}
    return {"counts": counts, "results": results}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("prepare", "score"))
    parser.add_argument("directory", type=Path)
    args = parser.parse_args()
    try:
        if args.command == "prepare":
            prepare(args.directory)
            print(f"Prepared {len(cases())} cases in {args.directory}")
            return 0
        report = score(args.directory)
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 0 if report["counts"]["passed"] == len(cases()) else 1
    except (OSError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
