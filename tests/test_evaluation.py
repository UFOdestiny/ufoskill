"""Test evaluation bookkeeping, not a model's manuscript performance."""

import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("evaluate", ROOT / "scripts/evaluate.py")
evaluate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(evaluate)


class EvaluationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.run = Path(self.temp.name) / "run"
        evaluate.prepare(self.run)
        self.cases = {c["id"]: c for c in evaluate.cases()}

    def assess(self, name):
        return evaluate.assess_case(self.cases[name], self.run / name)

    def finish(self, name):
        folder = self.run / name
        (folder / "response.md").write_text("Synthetic test output, not a model evaluation.\n", encoding="utf-8")
        (folder / "review.json").write_text(json.dumps({
            "faithfulness": 2, "task_success": 2, "usability": 2,
            "critical_failure": False, "evidence": "Synthetic evaluator test only.",
        }), encoding="utf-8")

    def test_cases_are_unique_and_routes_and_paths_are_valid(self):
        self.assertEqual(len(evaluate.cases()), 12)
        self.assertEqual(len(self.cases), 12)
        for case in self.cases.values():
            self.assertTrue((ROOT / "skills" / case["skill"] / "SKILL.md").is_file())
            self.assertTrue(case["prompt"] and case["criteria"])
            for path in list(case["files"]) + case["allowed_changes"]:
                self.assertFalse(Path(path).is_absolute())
                self.assertNotIn("..", Path(path).parts)

    def test_unrun_and_unreviewed_are_not_passes(self):
        self.assertEqual(evaluate.score(self.run)["counts"]["not_run"], 12)
        folder = self.run / "theory-review"
        (folder / "response.md").write_text("Review output", encoding="utf-8")
        self.assertEqual(self.assess("theory-review")["status"], "needs_review")
        with self.assertRaises(FileExistsError):
            evaluate.prepare(self.run)

    def test_readonly_edit_fails_even_with_positive_review(self):
        self.finish("theory-review")
        (self.run / "theory-review/workspace/paper.md").write_text("Unauthorized rewrite", encoding="utf-8")
        result = self.assess("theory-review")
        self.assertEqual(result["status"], "failed")
        self.assertIn("unauthorized change: paper.md", result["mechanical_failures"])

    def test_protected_math_and_unrequested_files_fail(self):
        self.finish("preserve-theorem")
        folder = self.run / "preserve-theorem/workspace"
        source = folder / "theorem.tex"
        source.write_text(source.read_text(encoding="utf-8").replace("convex", "arbitrary"), encoding="utf-8")
        (folder / "paper-plan.md").write_text("Unexpected plan", encoding="utf-8")
        result = self.assess("preserve-theorem")
        self.assertEqual(result["status"], "failed")
        self.assertEqual(len(result["mechanical_failures"]), 2)

    def test_review_threshold_and_evidence_are_required(self):
        self.finish("numerical-conflict")
        self.assertEqual(self.assess("numerical-conflict")["status"], "passed")
        path = self.run / "numerical-conflict/review.json"
        review = json.loads(path.read_text(encoding="utf-8"))
        review["critical_failure"] = True
        path.write_text(json.dumps(review), encoding="utf-8")
        self.assertEqual(self.assess("numerical-conflict")["status"], "failed")
        review["evidence"] = ""
        path.write_text(json.dumps(review), encoding="utf-8")
        with self.assertRaises(ValueError):
            self.assess("numerical-conflict")

    def test_allowed_edit_and_missing_workspace(self):
        self.finish("review-and-rewrite")
        source = self.run / "review-and-rewrite/workspace/conclusion.md"
        source.write_text("Accuracy improves on dataset A under the tested budget.\n", encoding="utf-8")
        self.assertEqual(self.assess("review-and-rewrite")["status"], "passed")
        missing = evaluate.assess_case(self.cases["analysis-introduction"], self.run / "absent")
        self.assertEqual(missing["status"], "failed")


if __name__ == "__main__":
    unittest.main()
