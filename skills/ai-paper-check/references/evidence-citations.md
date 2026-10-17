# Evidence, citation, and numerical checks

## Claims and source records

For the requested citation scope, verify the intended work against its official paper, proceedings, publisher page, ACL Anthology, OpenReview, arXiv version record, or persistent identifier. Prefer the primary text for claim support and authoritative exported metadata for bibliographic fields. Distinguish conference, workshop, Findings, journal, and preprint versions; do not combine fields from different versions.

Check title, author order, venue, year, publication status, persistent identifier, and volume/pages when applicable. Check relevant corrections or withdrawal status when assessing current validity. Search-result snippets and plausible generated BibTeX are insufficient verification. An abstract may support a high-level claim but usually cannot verify a detailed protocol or theorem condition.

Read enough of the source to assess the nearby claim: task, assumptions, information access, reported finding, and applicable setting. Flag claims stronger than the source, citations to the wrong work, and comparisons that conceal a different budget or supervision regime. Preserve material qualifications.

Audit BibTeX for duplicate keys or duplicated works, incorrect entry types, conflicting version fields, capitalization, escaping, malformed braces, and broken identifiers. Preserve valid keys when repairing metadata. In the shared finding format, identify the citation key and field, with current and verified values in the evidence.

If browsing is unavailable, use supplied primary sources and identify what remains unverified. Do not block an unrelated prose edit on an entire bibliography audit. For a requested full citation audit, list coverage and unresolved entries rather than claiming complete verification.

## Numbers and terms

Trace headline values and comparisons to the supplied tables, result artifacts, or logs. Compare abstract, introduction, results, conclusion, captions, and appendix when within scope. Check metric direction, units, denominators, aggregation, rounding, percentage points versus relative percentages, repetitions, and uncertainty.

Distinguish measured results from estimates and planned experiments. A best-case gain must not become an average gain. Check highlighting against the stated table rule. When sources disagree, identify both locations and their conditions; do not silently replace raw results with manuscript values.

Check that definitions, symbols, theorem assumptions, and method names agree across the manuscript and supplement. Apply the shared community-terminology principle. Flag a semantic mismatch, such as treating discrimination as calibration, with the relevant definition; do not infer a new scientific result from a consistency check.

Check figure/table/algorithm references and captions against their actual objects. Verify main-text statements and appendix expansions have the same scope. Missing original artifacts limit numerical verification even when every manuscript location agrees.

## Example: conflicting numbers without original results

Synthetic input: abstract reports 84.2% accuracy; Table 1 reports 82.4% for the same named setting. No logs or result files are supplied. The request is check-only.

**Confirmed / major:** abstract and Table 1 → numerical conflict → 84.2% versus 82.4%, both labeled as the same setting → headline result cannot be reconciled → obtain the result artifact and aggregation rule, then correct the affected locations. The inconsistency is confirmed; the correct value remains **unverified**. Leave both values unchanged until the authoritative result and repair scope are established. Agreement after copying either value would not verify the measurement.
