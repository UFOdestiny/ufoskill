# Design rationale and paper examples

## Why three skills with shared references

Writing, review, and technical verification produce different outputs and have different evidence needs. Their separate entrypoints make requests easier to route: a critique should not silently rewrite the manuscript, and a successful build should not become a scientific endorsement. Section guides remain references within writing because drafting an introduction and drafting a method should preserve the same story, definitions, and evidence boundaries.

The [shared principles](principles.md) are the canonical policy. The [paper plan](paper-plan.md) is an optional compact record of the manuscript's argument and terminology, carried across tasks. The [page budget](page-budget.md) and [appendix guide](appendix.md) are shared by drafting and review. This avoids maintaining competing copies of the same rules.

Section guides own editorial defaults and paper-type adaptations. The introduction guide retains the preferred three-paragraph contribution block for empirical methods while adapting to theory, analysis, datasets, and systems. Review links directly to these guides. Shared principles own evidence and scope; the [findings contract](findings.md) owns report fields and verification states. Examples illustrate decisions; development evaluations test behavior separately from package loading.

## What the paper examples support

These examples informed narrative choices, not a universal template. They are illustrative papers from the supplied reading collection and public proceedings, not a systematic survey of all accepted papers. Selection does not endorse every stylistic choice in a paper.

| Example | Structural observation | Transferable decision |
| --- | --- | --- |
| [Deep Think with Confidence, ICLR 2026](https://proceedings.iclr.cc/paper_files/paper/2026/hash/98257285340854262185500e59bc0f28-Abstract-Conference.html) | The confidence-quality observation precedes the method; evaluation distinguishes offline and online use. | Let a real observation explain a design choice; organize evaluation around the method's claims. |
| [Efficient Hallucination Detection for LLMs Using Uncertainty-Aware Attention Heads, ICML 2026](https://proceedings.mlr.press/v306/vazhentsev26a.html) | Attention-pattern analysis motivates the method; supplementary sections separate setup, ablations, extended results, and errors. | Make the insight-to-mechanism connection explicit and group appendix content by reader purpose. |
| [Learning Uncertainty from Sequential Internal Dispersion in Large Language Models, ACL 2026](https://aclanthology.org/2026.acl-long.1862/) | Proofs, computational details, experimental settings, and extra results have distinct appendix homes, starting with proofs. | Keep the main explanation readable while providing direct routes to mathematical and experimental verification. |
| [Reasoning Models Better Express Their Confidence, NeurIPS 2025](https://papers.nips.cc/paper_files/paper/2025/hash/95ee7181fe256439dca74ec794b33bb6-Abstract-Conference.html) | The empirical finding precedes analyses of confidence adjustment; additional results and experimental details are separate. | An analysis paper can lead with the finding instead of forcing a conventional method-first structure. |
| [Integrating Local and Global Entropy for Uncertainty Quantification in LLMs, 2026 preprint](https://arxiv.org/html/2606.09875v1) | The public preprint explains complementary uncertainty information and separates derivations from the main account. | Explain what each signal contributes before presenting its combination; preserve standard mathematical terminology. |

The final row refers to the inspected preprint, not a verified camera-ready manuscript. Paper-specific details should be checked against the version used when citing them in research. These examples are not automatically citations for a user's manuscript.

The experiment-first percentages are this plugin's editorial defaults. Proof-first appendix ordering is the selected organizational preference. Neither is claimed as a rule of ICLR, ICML, NeurIPS, or ACL. Exact submission requirements must come from the official instructions for the target year and track.
