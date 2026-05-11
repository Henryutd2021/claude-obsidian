---
type: meta
title: "Hot Cache"
updated: 2026-05-11
tags:
  - meta
  - hot-cache
status: evergreen
related:
  - "[[index]]"
  - "[[log]]"
---

# Recent Context

Navigation: [[index]] · [[log]] · [[Wiki Map]]

## Last Updated

**2026-05-11**: 16 papers ingested in one day across 3 batches (6 + 5 + 5). Codex-cli delegation pattern validated across 15 of 16 papers (1 Opus-composed). Batch 3 ran 5 parallel codex jobs in ~9 min wall-clock (fastest batch yet — local Zotero cache path is well-warmed). All 5 batch-3 receipts pass: 18 sections, 5/5/5/5 KB outputs, banned-word clean, em-dash clean, three-label discipline applied. Address counter 3 -> 19.

**Batch 3 papers (5):**
- `c-000014` Wolfram et al. 2024 One Earth — H2 economy 22% cost reduction (first One Earth paper)
- `c-000015` Ueckerdt et al. 2021 NCC — H2 e-fuels potential and risks (deviation: no Zotero PDF; used publisher + preprint fallback)
- `c-000016` Berrill et al. 2022 NCC — US residential decarbonization (first building-energy paper)
- `c-000017` Helveston, He & Davidson 2022 Nature — solar PV supply chain cost savings (US$67B globalization dividend 2008-2020)
- `c-000018` Odenweller et al. 2022 NE — green H2 probabilistic feasibility envelope

**Batch 3 archetype gains (5 new archetypes added on top of 11):**
- Global IAM option-value scenario pairs (Wolfram)
- Perspective-synthesis with quantified merit-order (Ueckerdt)
- National stock-level building-decarbonization scenario frame (Berrill)
- Counterfactual cost-savings on supply chain geography (Helveston)
- Monte-Carlo feasibility envelope from analog-technology growth distributions (Odenweller)

## Vault audit (this session)

Pre-fork plugin scaffolding moved to [[_meta/dropped-plugin-scaffold]]: `AGENTS.md`, `GEMINI.md`, `WIKI.md`, `bin/`, `commands/`, `agents/`, `docs/`, `.github/`, `.windsurf/`, `.cursor/`. Root is now TPL-only: `_templates/`, `hooks/`, `scripts/`, `skills/`, `tests/`, `wiki/`, plus `README.md` (rewritten 392 -> 108 lines, TPL-focused), `CLAUDE.md`, `CHANGELOG.md`, `ATTRIBUTION.md`, `LICENSE`, `Makefile`. Folder name kept as `claude-obsidian` to avoid disrupting iCloud sync + git remote — accepted cosmetic mismatch with TPL branding.

## Papers ingested so far

| Addr | Year | Journal | Slug | Author | Composed by |
|---|---|---|---|---|---|
| c-000003 | 2022 | NE | china-hta-clean-hydrogen | Yang | Opus 4.7 (me) |
| c-000004 | 2024 | NE | h2-additionality-time-matching | Giovanniello | codex |
| c-000005 | 2023 | N | china-pv-wind-3844-plants | Wang | codex |
| c-000006 | 2025 | J | space-based-solar-europe | Che | codex |
| c-000007 | 2023 | NC | endogenous-learning-green-h2-europe | Zeyen | codex |
| c-000008 | 2021 | NE | kikstra-covid-energy-demand-scenarios | Kikstra | codex |
| c-000009 | 2015 | N | china-fossil-cement-co2-revised | Liu | codex |
| c-000010 | 2023 | NCC | net-zero-investment-shifts-europe | Klaaßen & Steffen | codex |
| c-000011 | 2020 | J | data-center-load-migration-curtailment | Zheng | codex |
| c-000012 | 2023 | NC | rooftop-pv-china-carbon | Zhang | codex |
| c-000013 | 2021 | NE | national-wind-solar-growth-dynamics | Cherp | codex |

Year spread: 2015, 2020, 2021 (x2), 2022, 2023 (x4), 2024, 2025 — covers a decade of top-tier energy modeling. Journal spread: NE x4, N x2, NC x2, J x2, NCC x1. 10 of 11 by codex; 1 by Opus 4.7.

Archetype spread (10 archetypes across 11 papers):
- Modeling-optimization + policy-relevant (Yang, Giovanniello, Zeyen, Wang, Kikstra)
- Method-instantiation-as-object (Wang plant-by-plant)
- Policy dispute resolved by boundary diagnosis (Giovanniello)
- Emerging-tech TEA with cost-threshold framing (Che)
- Endogenous-learning integration (Zeyen)
- Demand-side shock as scenario lever (Kikstra, Zheng partially)
- Data-correction as primary contribution (Liu — counterpoint to modeling papers)
- Meta-analysis as primary contribution (Klaaßen)
- Cross-system load-flexibility / demand-mitigation (Zheng)
- Bottom-up resource assessment + grid-parity overlay (Zhang)
- Empirical growth-curve fitting / feasibility benchmark (Cherp)

## Cross-paper anchors emerging (seeds for paper-10 pattern synthesis)

We crossed the paper-10 pattern-update gate per CLAUDE.md. Patterns can now begin to emerge, but the discipline is still bottom-up: a pattern page is only created when at least 2 papers genuinely inform it (CLAUDE.md "orphan pattern" lint check).

### Already supported by 2+ papers (ready for pattern stub)

- **`patterns/methods/additionality-counterfactuals`**: Giovanniello 2024 NE (paper 2) explicitly diagnoses Zeyen 2023 NC (paper 5) framework as "non-compete" additionality. 2 supporting papers — both have reciprocal `[!contradiction]` callouts already.
- **`patterns/methods/plant-vs-aggregate-resolution`**: Yang 2022 NE (paper 1, TIMES-VEDA 780+ processes), Wang 2023 N (paper 3, 3,844 individual plant sites), Zhang 2023 NC (paper 10, 354-city rooftop-level), Cherp 2021 NE (paper 11, 60-country growth-curve fitting). 4 supporting papers spanning 4 resolution levels.
- **`patterns/methods/exogenous-shock-as-scenario`**: Che 2025 J (paper 4, technological), Kikstra 2021 NE (paper 6, demand-side), Zheng 2020 J (paper 9, spatial load-migration). 3 supporting papers.
- **`patterns/methods/cost-trajectory-treatment`**: Yang 2022 NE (exogenous IRENA/BNEF), Zeyen 2023 NC (endogenous learning curves), plus implicit treatment in Wang 2023 N, Che 2025 J. 4 supporting papers.
- **`patterns/methods/national-vs-continental-case`**: Yang/Wang/Zhang on China (paper 1, 3, 10), Cherp on 60 countries (paper 11), Zeyen on Europe (paper 5), Klaaßen on Europe (paper 8). National-case vs continental-coupled tension.

### Emerging archetype clusters

- **Demand-side as the lever**: Zheng 2020 J (load migration), Kikstra 2021 NE (COVID demand), Giovanniello 2024 NE (H2 time-matching is also a demand-side design choice). 3 papers — `patterns/archetypes/demand-side-mitigation`.
- **Data correction / inventory revision**: Liu 2015 N. 1 paper so far; needs at least 1 more for pattern stub (Olivier/EDGAR/PRIMAP comparator papers are likely candidates from the manifest).
- **Meta-analysis as primary contribution**: Klaaßen & Steffen 2023 NCC. 1 paper so far — `patterns/archetypes/meta-analysis-primary` premature.
- **Plant-level / city-level resolution**: Wang 2023 N (utility-scale 3,844 plants), Zhang 2023 NC (rooftop in 354 cities). 2 papers — `patterns/methods/plant-level-or-city-level-spatial` ready.

### Codex-detected anchors (batch 2, contract V2 worked)

UELISBYS (Zheng 2020 J) is the first paper where codex itself emitted explicit cross-paper Cross-references during generation:
- linked to Che 2025 J on "threshold-based system TEA"
- linked to Kikstra 2021 NE on "demand-side load-change framing"
- linked to Giovanniello 2024 NE on "hourly grid-emissions + flexible H2 policy"

This proves contract V2 fixed the batch-1 problem (codex pages without cross-references). Future batches should not require manual retrofitting of the Cross-references section.

## Codex delegation state

- Contract: `_templates/codex-ingest-contract.md`
- Wrapper: `scripts/codex-ingest-paper.sh <KEY> <ADDR> [SLUG]`
- Sandbox: `workspace-write`. Known limitation: codex's Zotero MCP fails in this sandbox; codex auto-falls-back to (a) local Zotero SQLite + storage cache, or (b) publisher HTML, depending on what is available. `fulltext_source` field in receipt records which path was taken (main-pdf | publisher-html | unknown).
- Cost per paper: ~200-230k tokens at xhigh reasoning, 8-12 minutes wall-clock when run in parallel.
- Reproducibility: every codex output is in `.raw/papers/{KEY}/`: 7 stub files + `codex-stdout.log` + `codex-stderr.log` + `codex-receipt.json`. The stderr is ~70-660 KB per run (codex's internal reasoning trace).

## Pending followups

1. ~~**Henry**: attach a PDF to Zotero parent `M9HYZCZE`~~ — **done 2026-05-11**. Attachment `5UKTL4KK` ("Submitted Version" / author manuscript) now in Zotero. Page frontmatter updated to `main_pdf: true`. Note: the analysis page itself was composed before this PDF was attached, so the original `fulltext_source` was publisher HTML; a Pass-2 trigger on [[papers/2025-J-space-based-solar-europe]] would re-derive from the now-available PDF if wording precision matters in a pattern page.
2. **CLAUDE.md amendment** (deferred until after paper 5; reached at paper 6): formalize PDF-only-as-default + L2/L3 opt-in tiering for SI/data/code (per the conversation about workload vs value).
3. **Lint pass**: run `/wiki-lint` after this batch to catch any banned-word slips codex may have justified weakly, plus cross-page contradictions between papers 1/3 (method choices) and papers 2/5 (additionality framework).
4. ~~**Manifest CSV quoting bug**~~ — **false alarm, no fix needed**. Original diagnosis was based on an `awk -F','` count (which doesn't honor CSV quoting); a proper `csv.reader` pass returns 14 fields per row across all 142 rows. The CSV is RFC-4180 compliant.

## What this vault is now

Personal Karpathy-style LLM Wiki specialized for reverse-engineering top-tier energy papers and compounding the analyses into Henry's own high-impact-paper writing playbook. Built on the existing claude-obsidian v1.6.0 plugin machinery (DragonScale fold/address/tile/boundary + 11 skills) plus the ARS plugin and Nature-family skills already loaded in this session.

## Henry's research scope

Renewable energy integration · wind-solar-hydrogen integrated systems · green hydrogen techno-economic analysis · energy system optimization · building energy saving & emission reduction · energy policy and cost analysis.

## Status of the Zotero side (2026-05-11)

Henry confirmed 7 in-scope journals: **Nature · Nature Energy · Joule · Nature Communications · Nature Sustainability · Nature Climate Change · One Earth**. A scan via `zotero_advanced_search` against `publicationTitle is "<journal>"` returns **142 papers** across these 7 journals (Nature 5 · Nature Energy 74 · Joule 36 · Nature Communications 20 · Nature Sustainability 2 · Nature Climate Change 4 · One Earth 1; includes 2 Zotero-side duplicate item-key pairs).

**`Top Paper Lab` collection exists in Zotero (key `TKIB4DFM`)**. Henry created it manually in the Zotero UI after the MCP `zotero_create_collection` was found to return success without persisting. Henry then dragged in 142 papers, including 2 stray Nature-family items (`ZNUP7SNR` Nature Food + `GF9LAAMT` Nature Reviews Earth & Environment) that he is removing in the UI to stay strict-7-journal.

**MCP write-phantom bug confirmed**: both `zotero_create_collection` and `zotero_manage_collections` (add_to / remove_from) return success messages but the changes do not persist. All Zotero-side membership edits must be done manually in the Zotero UI (or via Zotero's own scripting). MCP **reads** are reliable; only writes are phantom.

The CSV manifest at `.raw/zotero_manifest/top_paper_lab_manifest.csv` mirrors my 142-paper search result. Up to ±4 rows may drift from the actual Zotero collection (Henry's removal of the 2 strays, plus my 2 same-paper duplicate keys he may have deduplicated). When ingesting, Zotero is the source of truth — the CSV is just a working manifest.

## Storage discipline (architecture-level)

PDFs / SI / source-data files **stay in Zotero's storage** (`~/Zotero/storage/{ITEM_ID}/`). They are NEVER copied into this iCloud-synced repo. When a skill needs full-text, it calls `mcp__zotero__zotero_get_item_fulltext`; when it needs an attachment path, `mcp__zotero__zotero_get_item_children`. `.raw/papers/{KEY}/` only holds ~5–10 KB of text metadata stubs (DA / CA statements, repository links, defuddled landing page, asset checklist).

## Next actions (in order)

1. **Henry** (in Zotero UI): remove `ZNUP7SNR` (Nature Food) and `GF9LAAMT` (Nature Reviews Earth & Environment) from the `Top Paper Lab` collection so it stays 7-journal-strict. MCP remove calls are phantom — must be done in the UI. (~5 seconds.)
2. **Henry**: pick the first seed paper. Recommended: most-relevant Nature Energy or Joule paper on wind-solar-hydrogen / TEA. Note the Zotero key (8 chars).
3. **Claude Code** (next session): scaffold `.raw/papers/{ZOTERO_KEY}/` with 7 stub files (`metadata.json`, `zotero-attachments.md`, `data-availability.md`, `code-availability.md`, `repository-links.md`, `article-page.md`, `asset-status.md`). Read metadata via `mcp__zotero__zotero_get_item_metadata`; list PDF/SI paths via `zotero_get_item_children`; defuddle the publisher landing page; extract DA/CA statements.
4. **Claude Code**: run `/wiki-ingest .raw/papers/{ZOTERO_KEY}/` — orchestrates `pre-review-brief` + `research-blueprint <journal>` + `academic-paper-reviewer` (quick-assessment) over the Zotero PDF (pulled via `mcp__zotero__zotero_get_item_fulltext`) → emits `wiki/papers/{year}-{journal-short}-{slug}.md` per `_templates/paper-analysis.md`.
5. **Henry**: review the output. If anything reads fluffy or unsupported, iterate on `CLAUDE.md` anti-fluff word list before paper 2. Then 4 more pilots (different journals, different archetypes; include 1 from a non-7-journal control like Applied Energy or Renewable Energy later for the quality-jump diagnosis).

## Constraints (from TPL constitution)

- Three required labels on every important claim: `Evidence:` (in paper/SI/DA/CA) · `Inference:` (derived) · `Lesson:` (transferable to my work).
- Anti-fluff: no "innovative / important / rigorous / high-impact / comprehensive / well-written" without concrete justification.
- Don't diffuse-update pattern pages until paper 10 (patterns emerge bottom-up).
- Zotero is bibliographic + binary source of truth. The vault stores analysis, not the source PDFs.
- `.raw/papers/{KEY}/` is text-only; `.gitignore` catches accidental binary drops as defense-in-depth.
- Zotero desktop app must be running for MCP read/write to work reliably.

## Plugin lineage

This vault was the reference vault for the public [`claude-obsidian` plugin v1.6.0](https://github.com/AgriciDaniel/claude-obsidian) until 2026-05-11. Upstream plugin continues independently; this fork is personal-use only. Plugin scaffold (`.claude-plugin/`) moved to `wiki/_meta/dropped-plugin-scaffold/`.

## Active machinery (inherited, still works)

- **DragonScale Memory v1.6.0**: `wiki-fold` (log rollups), `allocate-address.sh` (page address counter at 3), `tiling-check.py` (semantic dupe lint), `boundary-score.py` (frontier surfacing for `/autoresearch`).
- **Hooks**: SessionStart, PostCompact, PostToolUse (auto-stages wiki/, .raw/, .vault-meta/), Stop.
- **Test target**: `make test` covers `tests/test_allocate_address.sh`, `tests/test_tiling_check.py`, `tests/test_boundary_score.py`. Zero ollama dependency for core tests.

## Style preferences (carried over from the prior hot cache)

- No em dashes (U+2014) or `--` as punctuation.
- Short, direct responses. No trailing summaries.
- Parallel tool calls when independent.
