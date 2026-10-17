# Behavioral evaluation

These 12 synthetic tasks test scope control, factual fidelity, paper-type adaptation, and useful outputs. They are development fixtures, not research evidence or a comprehensive quality benchmark. They are excluded from the installed plugin; never expose `criteria` to the tested agent. Package tests do not execute these tasks or establish writing quality.

## Run and compare

1. Prepare fresh workspaces with `python3 scripts/evaluate.py prepare /tmp/myskill-candidate`. Use a different directory for each baseline or candidate run. Preparation refuses to overwrite prior runs.
2. Record the tested skill revision, client version, model, reasoning effort, and date in `run.json`. Use the same model, settings, tool access, and input files for baseline and candidate. Keep skill loading separate so only the intended version is available. For a no-skill baseline, remove the invocation line and record that difference.
3. Start a fresh session for each case, with its `workspace/` as the working directory. Supply only `prompt.txt` and workspace inputs, with the selected plugin enabled. For Claude invocation, replace `$myskill:` with `/myskill:`. Keep outputs outside the workspace except requested manuscript edits. Save the final response to the case's `response.md`; retain tool transcripts separately if auditing tool use. Do not let the agent read grading criteria or other cases.
4. Have a reviewer inspect the response, source changes, and case criteria. Randomize baseline/candidate labels for blind comparison. Do not have the authoring run certify itself. Record a `review.json` per case using the rubric below. Review tools used and unavailable verification; mechanical checks cannot detect unauthorized browsing or invented claims.
5. Run `python3 scripts/evaluate.py score /tmp/myskill-candidate`. It reports scope violations, protected-literal changes, and review status. Exit 0 requires all cases passed; 1 means failed or incomplete; 2 indicates invalid input. An untouched prepared workspace is **not_run**, never a pass.

## Review rubric

Score each dimension 0 (fails), 1 (partly meets), or 2 (meets). Use each case's criteria as evidence, not exact target wording.

- **faithfulness:** preserves facts, numerical meaning, assumptions, citations, and verification limits; flags unsupported claims accurately.
- **task_success:** completes the requested artifact or diagnosis, follows scope and paper type, and avoids unnecessary questions or stages.
- **usability:** clear and actionable output, prioritized findings or readable prose, appropriate detail, and minimal duplicate reporting.

Set `critical_failure` for fabricated evidence, materially strengthened claims, or unauthorized actions. Mechanical scope failures also fail the case. Passing requires no critical failure, faithfulness 2, every other score at least 1, and total at least 5/6. Exact-literal checks cover only explicitly protected source text; semantic equivalence and factual correctness still require review.

```json
{
  "faithfulness": 2,
  "task_success": 2,
  "usability": 1,
  "critical_failure": false,
  "evidence": "Example format only: cite actual response passages and file locations."
}
```

Report all 12 cases, unresolved reviews, critical failures, and paired quality changes. Record latency, tokens, and tools only when measured by the host; do not substitute word count for token usage. For extraction-heavy tasks, inspect source coverage. Small differences need repeated runs before claiming reliability gains. These fixtures complement held-out real manuscript tasks; passing them does not establish universal superiority.
