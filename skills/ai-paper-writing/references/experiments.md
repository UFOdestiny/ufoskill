# Experiments and analysis

Organize the evaluation around the paper's claims. A useful default order is essential setup → main result → contribution-critical ablations → generalization or robustness → efficiency and failure analysis. Adapt this order to the actual argument. Explicit research-question labels are optional; do not create RQs or experiments merely to fill a template.

## Establish a fair comparison

Give the dataset/task, model access, baselines, metrics and their direction, and evaluation conditions needed to interpret the main result. Surface budget, supervision, data, or implementation differences that materially affect fairness. Link full protocol, hyperparameters, seeds, and resources to their specific appendix homes.

Identify what each experiment can establish. Overall performance supports utility under the tested conditions. Ablations test a component's contribution under the chosen controls. Robustness requires relevant variation. Efficiency requires a defined resource comparison. A ranking metric alone does not support a calibration claim.

## Interpret the main result

Lead with the finding, cite the table or figure, choose the comparison needed to assess magnitude, and explain the supported consequence. Keep one main scientific point per paragraph. Usually one or two numerical comparisons are enough; use more only when the reasoning needs them. The full matrix belongs in the table.

### Example: from table narration to a finding

Synthetic supplied evidence: Table 2 reports accuracy at the same sampling budget: baseline/proposed scores are 70/74 on A, 80/81 on B, and 75/73 on C. No significance test or mechanism diagnostic is supplied.

Before: “We get 74 on A, 81 on B, and 73 on C. The baseline gets 70, 80, and 75. Our mechanism consistently improves performance.”

After: “At the matched sampling budget, the method improves accuracy on A and B, with the largest gain on A (70% to 74%; Table 2). The decline on C (75% to 73%) shows that the benefit does not extend across all three datasets.”

The revision selects a representative gain and the consequential exception. It does not infer causality or significance from the scores. These illustrative values are not evidence for a user's manuscript.

Use averages only with an explicit aggregation rule; avoid mixing incomparable metric scales. Preserve uncertainty, repetitions, and statistical-test conditions when supplied. Do not infer statistical significance from the size of a gain or boldface. Verify whether a difference is absolute, relative, or in percentage points before stating it.

## Explain mechanism and boundaries

Use ablations to address plausible alternative explanations: extra compute, more data, stronger supervision, or a different backbone when relevant. State what is held fixed and what changes. Discuss negative ablations honestly; they may narrow the claimed role of a component. If a needed control is absent, identify the evidence gap rather than writing as if it exists.

Include generalization, cost, sensitivity, and failure analyses when they answer the paper's claims. Keep contribution-critical analyses in the main text. Move exhaustive matrices and secondary diagnostics to the appendix, acknowledging any result that changes the main conclusion.

Tables and captions should make metrics, direction, aggregation, and comparison conditions intelligible. Highlighting must follow the stated comparison rule, including ties and uncertainty where relevant. Do not redesign experiments or alter values during a prose-only task.
