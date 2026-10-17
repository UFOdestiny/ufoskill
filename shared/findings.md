# Findings and verification status

Use for reviews and technical audits, including diagnosis preceding an authorized rewrite. Keep one finding per issue across skills; reuse its identifier when tracking a revision. A short task needs no separate report file or identifiers.

**Location → issue → evidence → impact → next action**

Evidence is a source anchor, value, diagnostic, or explicit reasoning. Include current and verified values when relevant. Make the action concrete enough to implement; do not rewrite whole sections during review alone.

Keep evidence status separate from severity:

| Status | Meaning |
| --- | --- |
| Confirmed | Available evidence establishes the issue. |
| Unverified | A specific source, context, or tool is missing; state what would resolve it. |
| Not applicable | The check does not apply to this study or task. |

For confirmed findings, use **critical** for invalid central claims or blocked requested readiness, **major** for material reasoning, reproducibility, or clarity problems, and **minor** for local corrections. Label editorial suggestions **optional**, not correctness failures. Do not count unverified items as confirmed defects or manufacture findings to fill categories. Report checks with no issues in a brief coverage statement rather than empty finding rows.

Lead with the most consequential confirmed findings, then decision-relevant unresolved checks. State scope and sources consulted. Add an ordered revision plan only when changes depend on one another; include strengths only when worth preserving. Scores require a user request. For combined review-and-rewrite, mark findings addressed or unresolved after the affected checks; do not duplicate the report.
