# Problem setup and motivating observations

## Setup: define the task the method actually solves

Specify inputs, outputs, available information, constraints, and the objective or evaluation target. State assumptions that affect applicability: access to logits or hidden states, supervision, reference answers, sampling budget, training access, or distribution conditions when relevant.

Introduce only notation used by the method or analysis, close to its first use. Define overloaded terms explicitly. Keep an uncertainty score distinct from the task used to evaluate it and from a calibrated probability. Do not turn preliminaries into a textbook survey or place substantial method contributions here without explaining them as such.

A short setup can live within the method. A standalone section is useful only when its definitions or assumptions support several later sections.

## Observation: connect evidence to a design decision

Use a separate motivation or observation section when a real finding materially explains the mechanism. State the question, minimal protocol, observed pattern, and design implication. Identify what is measured and what remains a hypothesis. A small diagnostic is not proof that the mechanism causes the final improvement.

Include enough setup to interpret the observation and defer its full protocol to the appendix if appropriate. If no motivating experiment exists, explain the conceptual reasoning directly; do not invent measurements or require a new experiment merely to populate this section.

Avoid repeating the introduction's gap or the experiments' full result analysis. The section earns its space by making a subsequent design choice easier to understand.
