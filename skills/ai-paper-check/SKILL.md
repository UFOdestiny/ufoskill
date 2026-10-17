---
name: ai-paper-check
description: Check AI research manuscripts for notation and acronym consistency, figures and tables, reproducibility materials, citation and numerical accuracy, LaTeX builds, and venue requirements. Use for technical audits, compilation repair, and submission checks. Scientific argument review belongs to ai-paper-review; prose rewriting belongs to ai-paper-writing.
---

# AI Paper Check

Read the [shared principles](../../shared/principles.md). Verify factual and technical properties against supplied artifacts or authoritative sources. Check the requested scope; a bibliography audit, build repair, and submission check are distinct tasks.

## Select the relevant checks

| Task | Guidance |
| --- | --- |
| Citation metadata, cited claims, BibTeX, numerical or terminology consistency | [Evidence and citation checks](references/evidence-citations.md) |
| Symbol definitions, consistent notation, and acronym expansion at first use | [Notation and abbreviations](references/notation-abbreviations.md) |
| Figure and table references, captions, axes, legends, values, and highlighting | [Figures and tables](references/figures-tables.md) |
| Experimental protocols, software, resources, prompts, and reproduction instructions | [Reproducibility materials](references/reproducibility.md) |
| LaTeX compilation, labels, PDF layout, anonymity, page limits, submission package | [Build and submission checks](references/latex-submission.md) |
| Main/appendix correspondence and proof placement | [Appendix organization](../../shared/appendix.md) |

Establish the source of truth before correcting anything: result files or logs, manuscript equations, authoritative publication records, or official venue instructions. Reuse existing verified records when applicable. The author's paper plan records intent; it does not override contradictory evidence.

Load the detailed checklists that match the request. For a full technical manuscript audit, include notation, figures/tables, and applicable reproducibility materials alongside evidence and build checks. A targeted acronym or figure check does not require auditing the entire submission package.

Keep a check-only task read-only. Fix identified defects when repair is requested or implied, preserving valid citation keys, values, scientific meaning, and the existing build engine. Resolve ambiguities from available evidence; when an authoritative value is unavailable, report the conflict rather than selecting a plausible value. Continue independent checks when one source or tool is unavailable.

## Report verified scope

Use the [findings contract](../../shared/findings.md). State the files and checks covered, evidence consulted, and remaining blockers for the requested readiness decision.

A successful build does not verify scientific claims. Matching BibTeX metadata does not establish that a source supports the cited sentence. Passing technical checks does not certify novelty, acceptance, or the full scientific argument. Use [ai-paper-review](../ai-paper-review/SKILL.md) only for a requested or materially needed argument assessment; do not start an automatic review-and-rewrite cycle.
