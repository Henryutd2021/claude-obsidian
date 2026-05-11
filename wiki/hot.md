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

**2026-05-11**: 6 papers ingested in one day. Codex-cli delegation pattern validated across 5 papers (gpt-5.5 + xhigh via `_templates/codex-ingest-contract.md`). All 5 codex outputs pass quality bar (18 sections, banned-words, em-dash, 3-label discipline, 5+5+5+5 KB outputs). Address counter 3 -> 9. Wall-clock for 3-paper parallel batch: ~13 min total (9:58 launch -> 10:11 last complete).

## Papers ingested so far

| Addr | Year | Journal | Slug | Author | Composed by |
|---|---|---|---|---|---|
| c-000003 | 2022 | NE | china-hta-clean-hydrogen | Yang | Opus 4.7 (me) |
| c-000004 | 2024 | NE | h2-additionality-time-matching | Giovanniello | codex gpt-5.5 xhigh |
| c-000005 | 2023 | N | china-pv-wind-3844-plants | Wang | codex gpt-5.5 xhigh |
| c-000006 | 2025 | J | space-based-solar-europe | Che | codex gpt-5.5 xhigh |
| c-000007 | 2023 | NC | endogenous-learning-green-h2-europe | Zeyen | codex gpt-5.5 xhigh |
| c-000008 | 2021 | NE | kikstra-covid-energy-demand-scenarios | Kikstra | codex gpt-5.5 xhigh |

Year spread: 2021-2025 (5 of 5 years). Journal spread: NE x3, N, NC, J. Method spread: TIMES-VEDA, DOLPHYN, plant-by-plant GIS optimization, PyPSA-Eur, sector-coupled with endogenous learning, IAM with demand-side shock.

## Cross-paper anchors emerging (seeds for paper-10 pattern synthesis)

- **Paper 1 (Yang 2022 NE) vs Paper 3 (Wang 2023 N)** = methodological contrast inside top-tier energy modeling: TIMES-VEDA black-box workhorse with 780+ processes vs plant-by-plant geospatial optimization at 3,844 sites. Both win on boundary expansion + headline monetization. Wang's "method-as-object" visual only works at plant-level resolution.
- **Paper 2 (Giovanniello 2024 NE) vs Paper 5 (Zeyen 2023 NC)** = direct citation tension. Paper 2 explicitly diagnoses Zeyen's framework as "non-compete" additionality (contracted H2 resources optimized *after* non-H2 grid investment), which is why Zeyen's annual matching looks safe. Co-ingest gives a same-batch primary-vs-meta pair, exactly the kind of seed needed for `patterns/methods/additionality-counterfactuals`.
- **Paper 2 (Giovanniello, US) vs Paper 5 (Zeyen, Europe)** = same problem (electrolyser time-matching) on two grids, two model classes (DOLPHYN vs sector-coupled IAM with endogenous learning), reaching incompatible policy advice. Anchor for `patterns/regions/us-vs-europe-h2-policy`.
- **Paper 1 (Yang, China H2) vs Paper 5 (Zeyen, Europe H2)** = same fuel, opposite case design (single-country vs continental-coupled, exogenous costs vs endogenous learning). Anchor for `patterns/methods/cost-trajectory-treatment`.
- **Paper 4 (Che 2025 Joule SBSP) vs Paper 6 (Kikstra 2021 NE COVID)** = both use exogenous shock as the analytical lever (one technological, one demand-side). Anchor for `patterns/methods/exogenous-shock-as-scenario`.

## Codex delegation state

- Contract: `_templates/codex-ingest-contract.md`
- Wrapper: `scripts/codex-ingest-paper.sh <KEY> <ADDR> [SLUG]`
- Sandbox: `workspace-write`. Known limitation: codex's Zotero MCP fails in this sandbox; codex auto-falls-back to (a) local Zotero SQLite + storage cache, or (b) publisher HTML, depending on what is available. `fulltext_source` field in receipt records which path was taken (main-pdf | publisher-html | unknown).
- Cost per paper: ~200-230k tokens at xhigh reasoning, 8-12 minutes wall-clock when run in parallel.
- Reproducibility: every codex output is in `.raw/papers/{KEY}/`: 7 stub files + `codex-stdout.log` + `codex-stderr.log` + `codex-receipt.json`. The stderr is ~70-660 KB per run (codex's internal reasoning trace).

## Pending followups

1. **Henry**: attach a PDF to Zotero parent `M9HYZCZE` (Che 2025 Joule SBSP) so future SI / source-data analysis can run. Currently `main_pdf: false` in the frontmatter.
2. **CLAUDE.md amendment** (deferred until after paper 5; reached at paper 6): formalize PDF-only-as-default + L2/L3 opt-in tiering for SI/data/code (per the conversation about workload vs value).
3. **Lint pass**: run `/wiki-lint` after this batch to catch any banned-word slips codex may have justified weakly, plus cross-page contradictions between papers 1/3 (method choices) and papers 2/5 (additionality framework).
4. **Manifest CSV quoting bug** (known): the v1 manifest does not quote string fields with internal commas; affects ~6 of 142 rows. Defer to a later cleanup pass.

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
