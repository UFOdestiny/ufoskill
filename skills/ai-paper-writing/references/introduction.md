# Introduction

The introduction should let a reader explain the research question, why existing solutions leave it open, what insight changes the approach, and what the paper establishes.

Build this reasoning in an order appropriate to the paper:

1. Specify the task and a concrete consequence of the unresolved problem. Supply only the background needed to understand the gap.
2. Describe the closest relevant approach fairly, then identify the precise limitation under relevant assumptions. Avoid portraying an entire literature as incapable because one baseline has a weakness.
3. State the key insight and the reasoning or supplied observation behind it. Bridge the limitation to the proposed mechanism; do not jump from “existing methods struggle” to a branded architecture.
4. Explain the technical change at an intuitive level and why it addresses the limitation. Defer symbols, implementation, and secondary design details.
5. Close with the supported contributions, using the paper-type guidance below.

The earlier introduction functions have no fixed paragraph count. Combine them when clearer, and introduce a technical challenge only if it explains an actual design decision. A detailed observation may deserve a later section; here retain the insight needed to understand the contribution.

For each novelty statement, complete the comparison mentally: “Compared with [closest approach], this work changes [specific assumption, information, operation, objective, or finding], which enables [supported consequence].” Use natural prose rather than repeating this template. Distinguish novelty of the mechanism from strength of the benchmark result.

## Contribution block by paper type

For an empirical method paper, default to three concise paragraphs beginning with **Conceptually,**, **Technically,**, and **Empirically,**, in that order. Use inline paragraph openings, bold when appropriate. Preserve this preferred paragraph form unless the user requests another format. A local edit elsewhere does not authorize restructuring the introduction.

**Conceptually,** state the central insight, problem formulation, or perspective and explain how it addresses the specific limitation established earlier. Make clear what the reader should understand differently and why that matters. Position the insight against the closest relevant idea using community-standard terms.

**Technically,** identify the concrete mechanism that realizes that insight: the consequential operation, objective, estimator, algorithm, or analysis, and how it changes the relevant prior approach. Explain what the technical change enables. Keep implementation details and equations in the method section; use established author-chosen names without inventing branded components.

**Empirically,** state what the experiments establish, under which relevant settings and comparisons, and how this supports the contribution. Select the main finding and, when necessary, a representative quantitative comparison. Include mechanism evidence, efficiency, or generalization only when actually evaluated. Preserve consequential exceptions and avoid a catalogue of benchmark numbers.

When using the empirical block, connect insight → realization → validation. Give each paragraph a distinct informational role while keeping the same central contribution and claim scope. Do not repeat the same novelty sentence three times or imply three independent discoveries merely because there are three paragraphs.

Populate roles from supplied research; mark genuinely missing evidence with a precise placeholder when drafting. Adapt automatically when the paper is not an empirical method paper:

| Paper type | Contribution emphasis |
| --- | --- |
| Theory | Problem or conceptual distinction, formal result and assumptions, significance or implications; experiments are optional. |
| Analysis | Question, supported finding, explanation and scope; no invented method contribution. |
| Dataset | Coverage gap, construction, validation and supported uses. |
| System | Design requirement, architecture, measured system properties under stated conditions. |

Use the roles and number of paragraphs the actual contribution needs. Do not manufacture a mechanism or experimental result, or label a proof as empirical evidence. Preserve an explicit user-selected structure while identifying any unsupported requested claim.

Finish with a clear view of what the paper establishes. Avoid duplicating the abstract's result list or adding a generic roadmap that contributes no orientation. The reader should reach the setup already understanding why the proposed work is needed.
