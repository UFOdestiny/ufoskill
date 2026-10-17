# LaTeX builds and submission checks

## Build the existing project

Inspect project instructions and the existing Makefile, build script, or documented command before choosing a tool. Preserve the engine and bibliography backend. When no command exists and the project supports pdfLaTeX, a possible fallback is `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`, with the actual root file substituted. Do not impose that command on XeLaTeX or LuaLaTeX projects.

For substantial source or bibliography changes, establish a baseline when useful and rebuild afterward. Inspect the first blocking error, locate its source, correct it within the authorized scope, and retry. Stop unchanged retries when an unavailable dependency or an out-of-scope repair prevents progress; report the concrete obstacle.

Prioritize missing files, syntax or environment errors, bibliography failures, undefined citations/references, duplicate labels, and labels attached to the wrong object. Inspect the logs after a successful exit. Do not suppress errors just to produce a PDF.

Use appropriate equation environments and automatic labels for referenced formulas. Preserve mathematical meaning when breaking long equations. Correct visible overflow, unreadable tables, broken bibliography output, and misplaced floats. Harmless underfull warnings do not require exhaustive cleanup. Keep template fonts and margins intact.

## Inspect the rendered artifact

For layout work or final submission checks, inspect the compiled PDF, including figures, tables, equations, references, page breaks, and appendix navigation. Compilation alone cannot establish visual quality. If rendering or visual inspection is unavailable, state that limitation explicitly.

Check exact main-to-appendix references and theorem and assumption consistency. Assess appendix order against the selected organization; a departure from the proof-first preference is not a submission violation. Count pages using the venue's accounting rules, not just the PDF's total page count.

## Verify current submission requirements

For a venue-specific check, establish venue, year, track, and submission stage. Consult current official instructions for the template, page limits and exclusions, anonymity, supplementary material, mandatory statements or checklists, permitted external links, and artifact requirements. Do not copy last year's rules or infer requirements from the layout of accepted papers.

Check only applicable requirements and record the official source. Distinguish mandatory violations from editorial preferences. If the target venue is unspecified, complete generic technical checks and leave venue compliance unresolved; do not guess the target.

Before declaring technical submission readiness, account for build status, references, numerical conflicts, placeholders, visual inspection, and applicable venue requirements. A real defect blocks the relevant check; a missing tool or source leaves it unverified. Report those states separately. Technical readiness does not certify the scientific contribution or replace an argument review.
