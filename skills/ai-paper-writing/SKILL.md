---
name: ai-paper-writing
description: Plan, draft, revise, polish, or compress AI, ML, NLP, and LLM research papers and individual sections. Use for manuscript prose and organization, including revisions based on reviews. Review-only requests belong to ai-paper-review; citation, build, and submission audits belong to ai-paper-check.
---

# AI Paper Writing

Read the [shared principles](../../shared/principles.md), then only the guides needed below.

## Work from the supplied research

Identify the requested scope, manuscript files, intended reader, and available evidence. Reuse the existing outline, notation, bibliography, and author decisions. For a new paper or substantial reorganization, establish the [paper plan](../../shared/paper-plan.md) before drafting. For a local edit, inspect the surrounding argument and relevant evidence without expanding into a full-paper process.

Introduce the question and intuition before dense notation. Each paragraph advances one step; explain each operation's purpose and connections. State novelty through a concrete technical difference. Replace defensive filler with scientific content, preserving real limitations. Interpret results rather than reciting table cells. Recommend missing experiments separately from completed results.

## Load guidance by section or task

| Requested work | Reference and responsibility |
| --- | --- |
| Title or abstract | [Title and abstract](references/title-abstract.md): communicate the task, contribution, and supported takeaway. |
| Introduction | [Introduction](references/introduction.md): establish the gap and insight; select the contribution structure for the paper type. |
| Related work | [Related work](references/related-work.md): position the contribution against the closest ideas and assumptions. |
| Setup or motivation | [Setup and observations](references/setup-observations.md): define the task and justify the design from actual observations. |
| Method or supporting theory | [Method](references/method.md): explain how the mechanism works and why each operation is needed. |
| Experimental results | [Experiments](references/experiments.md): test the claims and interpret the evidence. |
| Conclusion or limitations | [Conclusion and limitations](references/conclusion-limitations.md): state the supported answer and its boundary. |
| Page allocation or compression | [Page budget](../../shared/page-budget.md): prioritize experimental evidence for empirical papers. |
| Supplementary material | [Appendix](../../shared/appendix.md): organize by purpose, with proofs first when present. |

For a full draft, read the applicable section guides and allocation guidance. For one section, load its guide plus a neighboring guide only if a dependency or transition needs repair. Keep title, abstract, introduction, results, and conclusion consistent when authorized changes affect their shared claims.

## Revise and deliver

Draft in the requested format; use LaTeX-ready prose when editing LaTeX. Retain valid labels, citation keys, equations, and values. Introduce new citations only after checking authoritative sources when available; otherwise mark the citation or claim as unverified. Do not turn a local prose task into a bibliography-wide audit.

After editing, check the affected argument for unsupported strengthening, term drift, missing reader context, unnecessary number repetition, and defensive filler. Keep real assumptions and counterevidence visible. For a requested review-and-rewrite, use [ai-paper-review](../ai-paper-review/SKILL.md) for diagnosis and implement the revisions here; do not repeatedly hand the task back and forth.

Use the existing project build command and engine after substantial LaTeX changes when available. Read the [build guidance](../ai-paper-check/references/latex-submission.md) when changes affect compilation, references, or layout. Inspect the rendered PDF for layout work. Deliver the requested text or edits, briefly explain consequential changes, and identify unresolved evidence or verification. Report a draft as a draft when compilation or source verification remains unavailable.
