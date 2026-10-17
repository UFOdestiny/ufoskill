# MySKILL

Three English-language skills for writing, reviewing, and checking AI/ML/NLP research papers in **Codex and Claude Code**. They share one scientific argument, terminology policy, and evidence standard, with section guidance loaded only when needed.

Version: see `plugin.json`. Plugin and marketplace: `myskill`. Install ID: `myskill@myskill`. This repository is a self-hosted GitHub marketplace, not an official-directory listing.

## Choose a skill

| Task | Codex | Claude Code |
| --- | --- | --- |
| Plan, draft, revise, or compress a paper | `$myskill:ai-paper-writing` | `/myskill:ai-paper-writing` |
| Diagnose argument, novelty framing, or readability | `$myskill:ai-paper-review` | `/myskill:ai-paper-review` |
| Check notation, acronyms, figures/tables, reproducibility, citations, numbers, or submission rules | `$myskill:ai-paper-check` | `/myskill:ai-paper-check` |

Examples:

```text
$myskill:ai-paper-writing Revise the introduction around our central insight. Preserve the method and use community-standard terminology.
$myskill:ai-paper-review Review the method and experiments for missing logical connections, unsupported claims, and unnecessary numerical narration. Do not edit files.
$myskill:ai-paper-check Verify the cited claims and numerical consistency, then build the LaTeX project using its existing command.
```

In Claude Code, replace the first token with the corresponding `/myskill:...` command. Natural-language requests can also trigger skill selection. Discussion follows the user's language; manuscript prose defaults to English. Local paragraph edits stay local. Tool-dependent verification is reported as incomplete when the required sources or toolchain are unavailable.

## Install

Codex CLI with plugin support:

```bash
codex plugin marketplace add UFOdestiny/MySKILL
codex plugin add myskill@myskill
```

Start a new session and select a skill through `/skills` or invoke its namespaced name, such as `$myskill:ai-paper-writing`.

Claude Code:

```bash
claude plugin marketplace add UFOdestiny/MySKILL
claude plugin install myskill@myskill
```

Start a new session or run `/reload-plugins`. To test this checkout before publishing, replace `UFOdestiny/MySKILL` with `.` in the marketplace-add command. Remote installation uses the version pushed to GitHub, not unpublished local edits.

Install the **complete plugin**. The three skills share resources inside the plugin; copying one skill directory alone omits required files. Remove an obsolete standalone installation of `ai-paper-writing` if it causes duplicate discovery.

## Writing architecture

The shared argument is **problem → specific prior limitation → insight → contribution → evidence → supported implication**. The contribution may be a mechanism, theorem, finding, dataset, or system property. Novelty comes from the concrete difference and its supported consequence. Standard community terms take priority over invented labels. Results prose explains findings and representative comparisons; it does not recite tables. Direct writing retains real assumptions, uncertainty, and failures.

Each section has a distinct responsibility, described in the [writing entrypoint](skills/ai-paper-writing/SKILL.md). For empirical method papers, the [introduction guide](skills/ai-paper-writing/references/introduction.md) defaults to **Conceptually**, **Technically**, and **Empirically** paragraphs. It adapts directly to theory, analysis, dataset, and system papers and respects explicitly requested formats. Other paragraph and component counts remain flexible. The default [empirical-paper budget](shared/page-budget.md) gives experiments 36% and method 28% of counted narrative space; it adapts to paper type and actual venue rules.

The [appendix](shared/appendix.md) is organized by purpose: proofs and derivations first when present, then method details, experimental protocol, hyperparameters and resources, additional results, diagnostics, and prompts or annotation materials. Omit unused categories. Keep essential assumptions and claim-changing evidence in the main text.

The [design rationale](shared/design-rationale.md) records the architectural choices and paper examples that informed them. Scientific evidence constraints, user task boundaries, and editorial defaults are distinguished in the shared principles. The percentages and appendix order are preferences, not conference requirements or scientific correctness criteria.

```text
plugin.json                        Portable plugin manifest
.claude-plugin/                     Claude manifest and marketplace
.agents/plugins/marketplace.json   Codex marketplace
skills/
  ai-paper-writing/                Writing entrypoint and section guides
  ai-paper-review/                 Argument and presentation review
  ai-paper-check/                  Evidence, build, and submission checks
shared/                            Canonical principles, paper plan,
                                   findings, page budget, appendix, design rationale
```

[Writing](skills/ai-paper-writing/SKILL.md), [review](skills/ai-paper-review/SKILL.md), and [checks](skills/ai-paper-check/SKILL.md) read the same [principles](shared/principles.md) and reuse the same [paper plan](shared/paper-plan.md) when substantial work needs one. No planning artifact is required for a paragraph edit. No external skill suite, model, MCP service, or cloud workflow is required to use the plugin.

## Update and uninstall

Claude third-party marketplace auto-update is off by default. Enable it through `/plugin` → **Marketplaces** → **myskill** → **Enable auto-update**. Reload plugins or start a new session after updates.

Manual updates:

```bash
# Codex
codex plugin marketplace upgrade myskill
codex plugin add myskill@myskill

# Claude Code
claude plugin marketplace update myskill
claude plugin update myskill@myskill
```

Start a new Codex session after updating. Background update behavior depends on the client; this repository installs no additional scheduled updater.

```bash
codex plugin remove myskill@myskill
claude plugin uninstall myskill@myskill
```

## Validate and release

Development validation requires Python 3.10+ and PyYAML; using the installed skills requires neither Python nor this dependency:

```bash
python3 -m pip install -r requirements-dev.txt
python3 scripts/manage.py validate
python3 -m unittest discover -s tests -v
python3 scripts/manage.py build
```

The validator checks both manifests, parses skill frontmatter and agent YAML with duplicate-key and field-type checks, and verifies local Markdown resource links across the shipped package. The reproducible ZIP includes manifests, marketplaces, skill/shared Markdown, YAML and JSON resources, README, and license. Hidden resource files, local outputs, development scripts, tests, evaluation fixtures, dependencies, and caches stay outside the archive. Output: `dist/myskill-<version>.zip` and `dist/SHA256SUMS`, using the manifest version.

Git tracks the source, tests, evaluation fixtures, and host manifests. `.gitignore` excludes local environments, editor/assistant state, build products, and scratch directories while preserving `.agents/plugins/marketplace.json`. Keep local evaluation runs under `eval-runs/` or outside the repository; keep logs under `logs/`. Release archives are generated by the build and attached to releases rather than committed.

Client test baseline: Codex CLI **0.163.0**, Claude Code **2.1.292**. Tests cover Codex marketplace and three-skill discovery from the archive, Claude installation and three-skill discovery, installed shared resources, archive completeness, broken resource links, symlinks, and version consistency. Native tests skip locally if a client is unavailable; CI installs the pinned clients. These tests verify packaging and loading, not model writing quality. The development suite in `evals/` supplies 12 behavioral tasks, a blind-review rubric, and an offline preparation/scoring tool. See `evals/README.md` in the repository. It covers local edits, theory and dataset papers, unsupported claims, numerical conflicts, and combined review/rewrite. Unrun or unreviewed tasks cannot pass. These are evaluation infrastructure, not measured model-quality gains.

GitHub Actions is optional release automation. It runs the same validation and tests, builds the archive, and publishes that verified artifact when a version tag is pushed. It does not run while you write papers, perform skill inference, or control client auto-updates. Local installation and validation work without Actions.

For a release, validate the tree, review and commit the files, and push the default branch. Create and push a tag matching the manifest version (`v<version>`). For later releases, use `python3 scripts/manage.py bump <new-version>` first. Published skill changes need a new version. Marketplace users follow the configured repository source; pushing only a tag does not update the default branch. The Actions release job uses the repository's built-in token with `contents: write`.

Format references: [OpenAI plugin standard](https://developers.openai.com/plugins/build/plugins), [Claude plugin reference](https://code.claude.com/docs/en/plugins-reference), [marketplaces](https://code.claude.com/docs/en/plugin-marketplaces), and [plugin updates](https://code.claude.com/docs/en/discover-plugins#keep-plugins-updated).
