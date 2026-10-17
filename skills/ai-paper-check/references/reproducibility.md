# Reproducibility materials

Assess whether a reader can reconstruct the reported procedure and identify the exact artifacts used. Apply only items relevant to the study and requested audit. Distinguish material that is documented, supplied, verified against artifacts, missing, or inapplicable. Documentation completeness does not establish successful reproduction; claim a rerun only when it was actually performed.

## Method, data, and evaluation protocol

1. Locate the complete pipeline, pseudocode or implementation, and training/inference instructions. Check preprocessing, intermediate outputs, numerical choices, edge cases, and post-processing against the main method description.
2. Identify dataset sources and versions, subsets, splits, exclusions, preprocessing, and applicable access or license conditions. Check overlap and leakage controls where relevant. Preserve material restrictions that prevent releasing data.
3. Identify model and tokenizer versions, exact checkpoints or API model identifiers, training access, and relevant API evaluation dates. Distinguish frozen snapshots from changing hosted services.
4. Specify baseline sources or implementations, configuration, supervision, data access, and compute or sampling budgets. Check that the settings used to produce reported results match those described.
5. Define metrics, scoring scripts, aggregation, correctness criteria, and evaluation or transfer protocols. For automated judges, include their model/version, prompts, decision rules, and calibration or validation procedure when used.
6. For human evaluation or annotation, document instructions, label definitions, annotator selection and counts as appropriate, assignment, disagreement handling, and quality-control procedures. Check applicable consent and disclosure requirements for the target venue.

## Hyperparameters and randomness

1. Record search ranges, search strategy and budget, selection criterion, validation split, and final values, including dataset-specific settings. Distinguish tuned parameters from fixed defaults and identify defaults by version.
2. Report seeds, repetitions, run-selection rules, stopping criteria, and the computation of uncertainty summaries. Explain unavailable randomness controls or nondeterministic operations when they materially affect repeatability.
3. Match the selected settings to the reported results and artifact configurations. Do not treat a proposed search range or a sample configuration as the configuration actually used.

## Software and resources

1. Identify the code revision or release, dependency versions, framework/runtime, and relevant operating-system, accelerator, driver, or CUDA environment. Provide environment or lock files when available; flag missing information without inventing versions.
2. Record hardware type and count, available or peak memory as relevant, numerical precision, batch size, parallelism, and relevant sequence-length or sampling settings.
3. Report applicable training and inference time, latency, throughput, memory use, generated/input token counts, model-call counts, and monetary cost when it supports a claim. Define measurement scope, units, workload, and whether preprocessing, warmup, auxiliary calls, or tuning are included.
4. Distinguish measured resource use from estimates. Check that efficiency comparisons use comparable hardware, budgets, and measurement boundaries, or explicitly state their differences.

## Prompts and executable reproduction

1. Supply exact system and user prompt templates, variable fields, demonstrations or few-shot examples, ordering, and any task- or model-specific variations. Check that these match the procedure used for the reported results.
2. Record decoding parameters, stopping conditions, token limits, sample counts, and output schemas.
3. Provide applicable entry commands, configuration files, input preparation, checkpoints, and a clear mapping from output artifacts to the reported tables and figures. Check supplied paths and dependencies; do not execute costly experiments merely to audit instructions.
4. Locate full results, logs, and aggregation scripts when supplied. Check artifact links and access instructions against the submission's anonymity requirements; distinguish a planned release from an available artifact.

Use the [appendix organization](../../../shared/appendix.md) to assign each item one authoritative home: method details, protocol, hyperparameters/resources, additional results, or prompts/annotation materials. Check consistency with the main text and link to exact destinations. Report omissions with their effect on reproduction and the concrete material needed; avoid requiring irrelevant artifacts simply to fill the checklist.
