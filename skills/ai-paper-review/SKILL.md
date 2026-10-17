---
name: ai-paper-review
description: Review an existing AI, ML, NLP, or LLM manuscript for argument, novelty framing, evidence alignment, terminology, readability, section responsibilities, page balance, and appendix organization. Use for manuscript critique or a revision plan without rewriting. Technical citation, numerical, build, and venue audits belong to ai-paper-check.
---

# AI Paper Review

Read the [shared principles](../../shared/principles.md). Review the requested scope without editing the manuscript or author's plan.

## Reconstruct and assess

Recover the problem, closest prior limitation, insight, contribution, evidence, and supported implication. Reuse an existing [paper plan](../../shared/paper-plan.md) as a statement of intent, then test it against the manuscript. Distinguish a missing explanation from missing research.

- **Contribution:** identify the concrete difference from closest work and the support for each advertised claim. Do not certify novelty from an incomplete literature search.
- **Coherence:** find the first missing dependency, undefined concept, abrupt transition, or repeated argument. Explain its consequence for the reader.
- **Meaning:** flag misleading terminology, unsupported causal explanations, strengthened claims, and selectively reported results.
- **Presentation:** identify table narration, defensive filler, and details that obscure the central evidence. Preserve meaningful uncertainty and established author names.

Load a guide only for the section under review:

| Scope | Direct guidance |
| --- | --- |
| Title or abstract | [Title and abstract](../ai-paper-writing/references/title-abstract.md) |
| Gap and contribution structure | [Introduction](../ai-paper-writing/references/introduction.md) |
| Positioning | [Related work](../ai-paper-writing/references/related-work.md) |
| Task or motivation | [Setup and observations](../ai-paper-writing/references/setup-observations.md) |
| Mechanism or theory | [Method](../ai-paper-writing/references/method.md) |
| Evaluation and interpretation | [Experiments](../ai-paper-writing/references/experiments.md) |
| Closing claims | [Conclusion and limitations](../ai-paper-writing/references/conclusion-limitations.md) |
| Allocation or supplement | [Page budget](../../shared/page-budget.md), [appendix](../../shared/appendix.md) |

Judge each section against its purpose and paper type. Editorial defaults are preferences, not scientific acceptance criteria. Verify material comparisons or terminology against authoritative sources when needed; keep unavailable verification unresolved.

## Deliver findings

Use the [findings contract](../../shared/findings.md), prioritizing consequential issues. For review-and-rewrite, carry the same findings to [writing](../ai-paper-writing/SKILL.md) and implement authorized revisions. Use [technical checks](../ai-paper-check/SKILL.md) for necessary factual verification; a handoff does not mean verification passed.

### Example: theory paper review

Synthetic input: “For convex, L-smooth functions, Theorem 1 proves the bound under independent samples.” The conclusion says “The bound holds for arbitrary objectives.” No experiments are supplied; review only is requested.

**Confirmed / critical:** conclusion → scope exceeds the theorem → Theorem 1 requires convexity, smoothness, and independent samples → the central guarantee is overstated → restore those conditions in the conclusion. Missing experiments and an absent Empirically paragraph are not defects by themselves. Leave source files unchanged and do not claim to have verified the proof.
