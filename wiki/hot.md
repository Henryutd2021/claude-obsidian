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

**2026-05-11**: Vault rebranded from `claude-obsidian` plugin vault to personal **Top Paper Lab**. Pre-fork content archived under `wiki/_meta/`. New 4-folder layout (`papers/ patterns/ playbook/ projects/`) created empty. `CLAUDE.md` rewritten as TPL constitution. `.gitignore` extended to exclude paper PDFs/SI/source-data. No papers ingested yet.

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

1. **Henry**: open Zotero desktop app → right-click `My Library` → New Collection → name it `Top Paper Lab`. (Should take ~10 seconds.)
2. **Claude Code** (next session): re-query `zotero_search_collections "Top Paper Lab"` → get real key → bulk `zotero_manage_collections add_to=[KEY]` with the 142 known item keys (stored in `.raw/zotero_manifest/top_paper_lab_manifest.csv`).
3. **Claude Code**: write `.raw/zotero_manifest/top_paper_lab_manifest.csv` with one row per paper (no `pdf_present` column — PDFs are always in Zotero; the relevant flag is `zotero_pdf_attached`).
4. **Henry**: pick the first seed paper (Nature Energy or Joule, most relevant to wind-solar-hydrogen / TEA).
5. **Claude Code**: scaffold `.raw/papers/{ZOTERO_KEY}/` with the 7 stub files; extract DA / CA from the publisher page via `defuddle` + Zotero MCP attachments; populate `asset-status.md`.
6. **Claude Code**: run `/wiki-ingest .raw/papers/{ZOTERO_KEY}/` — orchestrates `pre-review-brief` + `research-blueprint` + `academic-paper-reviewer` (quick assessment) → emits `wiki/papers/{year}-{journal-short}-{slug}.md`.
7. **Henry**: review the output. Iterate on `CLAUDE.md` if anything reads fluffy. Then 4 more pilots (different journals, different archetypes; include 1 from the comparison-tier later).

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
