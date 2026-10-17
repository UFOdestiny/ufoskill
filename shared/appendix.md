# Organize the appendix by purpose, with proofs first

The appendix is a navigable record for verification, reproduction, and deeper analysis. Every major appendix section should answer a distinct reader question and point back to the relevant main-text claim or section. Use informative titles, exact cross-references, and a short orientation sentence. Add a compact contents list when the supplement is long.

Default to this order for applicable material, with proofs first when present. Adapt to explicit author preferences or reader dependencies. Omit inapplicable categories and reletter the remaining sections; do not create empty sections, invent theorems, or duplicate content to fill A–G.

| Default order | Purpose and contents |
| --- | --- |
| A. Proofs and Derivations | Complete proofs in main-statement order; precise assumptions; auxiliary lemmas placed before their use or linked clearly; intermediate derivations and boundary cases. Restate a main claim only as needed to make its proof readable, preserving its conditions exactly. |
| B. Method and Implementation Details | Full pseudocode; training and inference procedures; preprocessing; numerical stability; edge cases; implementation choices omitted from the main explanation. |
| C. Experimental Protocol | Dataset versions, splits and exclusions; model/checkpoint versions; baseline implementations; metric definitions; evaluation procedures; correctness judgments and data-leakage controls when relevant. |
| D. Hyperparameters and Resources | Search ranges, selection criterion and validation split, final values, seeds and repetitions, hardware, runtime and resource accounting. Distinguish measured costs from estimates. |
| E. Additional Results | Complete per-task/per-model matrices, additional benchmarks, repetitions and uncertainty, extended comparisons. State how these results affect the main finding. |
| F. Ablations and Diagnostic Analysis | Secondary ablations, sensitivity analyses, mechanism diagnostics, failure cases, and qualitative examples. Keep a central ablation in the main text when the contribution depends on it. |
| G. Prompts and Annotation Materials | Exact prompt templates and variable fields, decoding details not already in protocol, annotation instructions, label definitions, and quality-control procedures when applicable. |

## Main text and appendix boundary

In the main text retain the central statement, assumptions needed to judge its applicability, why it matters, and enough reasoning to connect it to the method. For an empirical paper with supporting theory, give proof intuition and send the full proof and algebra here. A theory paper may require more proof in the main text; apply the same reader-need test rather than moving all mathematics automatically.

Retain the headline evidence, essential comparison conditions, and any result that materially narrows the main claim. An appendix can expand a failure analysis; it must not conceal a known failure behind an unrestricted main-text conclusion. If evidence changes the conclusion, acknowledge it where that conclusion is stated.

## Cross-reference and duplication discipline

At the main-text omission, say what the reader will find and link the exact appendix section, theorem, table, or algorithm. Avoid vague “see supplementary material.” In the appendix, identify which main-text claim the material supports and define any additional notation locally.

Assign each detail one authoritative home. Protocol owns evaluation design; the resource section owns search and compute; the prompt section owns exact prompt text. Link between them instead of repeating configuration blocks that can drift. Distinguish additional results from diagnostics by the question answered, not by which experiment was run last. Split a catchall “Additional Analysis” section when its contents serve unrelated purposes.
