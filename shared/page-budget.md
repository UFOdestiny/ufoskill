# Allocate space to the evidence

Use this starting budget for an **empirical method paper**. These percentages are editorial defaults, not venue rules or a measured norm across accepted papers. Reserve space for experiments before expanding method exposition.

| Content | Share of counted narrative space |
| --- | ---: |
| Abstract | 3% |
| Introduction | 15% |
| Related work | 7% |
| Problem setup | 5% |
| Method | 28% |
| Experiments and analysis | 36% |
| Conclusion | 3% |
| Limitations and discussion | 3% |

Count figures, tables, equations, captions, and algorithms inside their host section. An observation section draws space from the method or experiments according to its purpose; it does not add free space. If setup or related work is integrated into another section, transfer its allocation instead of duplicating it.

Verify page accounting for the exact venue, year, and track when preparing a submission or making a venue-specific allocation. Account for references and any mandatory separate material first. If a category is excluded from the main-text limit, remove its weight and renormalize the remaining weights over the eligible space. For example, with a 9-page narrative budget and excluded limitations, the experiment starting budget is `9 × 36 / 97 ≈ 3.34` pages. This is an example, not a claim about any venue's rules.

Use the budget to identify tradeoffs, not to force paragraph lengths. An unfamiliar mechanism may need more explanation. A theory paper may need substantial main-text proof development; an analysis paper may combine results and method; a dataset paper may prioritize construction and validation. Make a departure explicit in the paper plan when useful.

## Compress in order of scientific value

1. Remove repeated motivation, restated contributions, generic background, and table-by-table narration.
2. Consolidate notation and duplicate protocol descriptions; shorten sentences without deleting dependencies.
3. Move full proofs, auxiliary derivations, implementation details, exhaustive result matrices, and secondary analyses to the [appropriate appendix](appendix.md).
4. Keep the core mechanism, assumptions, fair comparison conditions, strongest evidence, and consequential failures accessible in the main text.
5. Rebuild and inspect actual page use when a toolchain is available. Rebalance content before considering layout adjustments allowed by the template.

Do not satisfy a page limit by shrinking fonts, violating margins, making unreadable tables, or hiding the conditions needed to judge the central claim. Do not fill spare space with a redundant new section.
