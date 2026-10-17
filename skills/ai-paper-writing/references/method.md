# Method and supporting theory

The method should let the reader reconstruct the mechanism and understand why it addresses the problem. Start with an overview that connects the insight to the sequence of operations. Use a figure or short algorithm when it clarifies dependencies, not as a required ornament.

For each substantive operation, explain its purpose, input, transformation, output, and connection to the rest of the method. Present intuition before symbols, then give the equation or precise procedure and explain its terms. Use community-standard operation names. Do not force two or three components, invent branded modules, or split a single operation to make the contribution look larger.

State how the operations combine into training, inference, optimization, or decision making. Make objective, constraints, normalization, and important edge conditions clear. Separate training-time and inference-time requirements. Discuss computational cost when it affects the comparison or applicability; distinguish measured runtime from theoretical complexity.

A reader should be able to trace one input through the method without guessing an undefined symbol or consulting an appendix for the central operation. Put full pseudocode, implementation details, routine algebra, and exhaustive edge cases in the appendix when space is limited, while retaining assumptions that determine the method's validity.

## Theory placement

Include a theorem only when it is part of the supplied research and advances the argument. In an empirical paper, keep essential definitions, the central statement, its conditions, its relevance to the method, and a short proof intuition in the main text. Send the full proof, auxiliary lemmas, and intermediate derivations to the first appendix section using an exact reference.

A theorem's scope must match its assumptions. Do not present an idealized result as a guarantee for untested practical settings. Do not hide restrictive assumptions in the proof appendix or remove conditions while shortening a statement. For a theory paper, retain enough main-text proof development to convey the actual intellectual contribution.

An equation needs surrounding explanation: what it computes, why that quantity is appropriate, and how it is used. Avoid chains of derivations that interrupt the mechanism's narrative without helping the reader understand it.
