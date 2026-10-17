# Notation and abbreviations

Check the requested material in reading order, including equations, algorithms, captions, and appendix references. Reuse the paper plan's glossary if available, but verify actual usage in the manuscript. For a local excerpt, inspect earlier definitions when available; otherwise identify the context needed instead of declaring a definition missing from the whole paper.

## Symbols and mathematical meaning

1. Define every symbol before or at its first use, including symbols that first appear in a figure, algorithm, or displayed expression.
2. Keep one meaning per symbol within its scope. Flag reuse for an unrelated concept; distinguish a clearly declared local variable from accidental global overloading.
3. Use one symbol for one concept unless a change is explicitly justified. Check that a renamed quantity has not left inconsistent occurrences elsewhere.
4. Make scalars, vectors, matrices, sets, functions, distributions, and indices distinguishable through definitions and consistent notation. Preserve the manuscript's coherent convention rather than imposing a new typography system.
5. Check superscripts, subscripts, hats, bars, boldface, and capitalization for consistent meaning. Distinguish an index from an exponent and an estimate from the underlying quantity.
6. Define index ranges, dimensions, domains, and relevant units. Check dimensional compatibility of operations where the definitions permit it; flag missing information rather than guessing a tensor shape.
7. Check that prose, equations, algorithms, figures, tables, and implementation descriptions refer to the same quantities and operations. Preserve distinctions between a probability, score, loss, and evaluation metric.
8. Check theorem statements and assumptions against their proofs and appendix restatements. Keep main-text and appendix definitions aligned, and explain any additional local notation where introduced.

## Acronyms: explain the first occurrence

1. Expand each technical acronym or initialism at first use using the established full term followed by the abbreviation, for example, `large language model (LLM)`. A term's familiarity in the community does not by itself replace this check.
2. Treat the abstract and main text as independently readable: an expansion in the abstract does not replace expansion at first use in the main text. Count an earlier heading, caption, or algorithm occurrence when checking reading order; if a heading uses an unexplained acronym, expand the heading or explain it immediately in the associated text.
3. Give standalone figures and tables enough local explanation to interpret their abbreviations, using the caption, legend, or table note. For a separately distributed supplement, reintroduce abbreviations needed to read it independently. Do not demand repeated expansion in every ordinary subsection.
4. Keep the full form, abbreviation, capitalization, and pluralization consistent. Flag one abbreviation used for different concepts, multiple abbreviations for the same concept, and a full form that does not match the intended community term.
5. Prefer the full term when an abbreviation is used only once or adds little readability. Do not invent an expansion for an author-chosen method name, dataset name, identifier, or proper name that has no established full form; verify its source and introduce what it denotes. Preserve exact citation titles, code identifiers, and standard unit symbols.

Use the shared finding format, identifying the current symbol or abbreviation, missing definition or conflict, and its effect on meaning. For uncertain definitions, include the source or context needed. Apply renaming consistently only when repair is authorized and the intended meaning is established. This checklist does not prescribe equation environments or layout.
