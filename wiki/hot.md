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

**2026-05-11**: First paper ingested. [[papers/2022-NE-china-hta-clean-hydrogen|Yang et al. 2022, *Nature Energy*]] (Zotero `PIQKGJNB`, address `c-000003`). 8 new files (1 analysis page + 7 `.raw/papers/PIQKGJNB/` stubs). Address counter 3 -> 4. `scripts/allocate-address.sh` patched for macOS (mkdir-based lock fallback when GNU `flock` is unavailable). Vault rebrand from earlier today still in effect; pre-fork content archived under `wiki/_meta/`.

## Most recent ingest

[[papers/2022-NE-china-hta-clean-hydrogen]] — Yang, Nielsen, Song, McElroy. *Nature Energy* 7, 955-965 (2022). Archetype: modeling-optimization + policy-relevant. Headline: integrated TIMES-class least-cost optimization, 4 scenarios, 780+ technological processes, 2020-2060; clean hydrogen reaches 65.7 Mt/yr by 2060 and avoids US$1.72T cumulative investment vs no-hydrogen net-zero. Top transferable craft: two-stage gap construction (field-level + case-level), three-unit headline number framing (USD + GDP% + Mt), break-even sensitivity reporting (+87% H2-cost to tie ZERO-NH), figures sequenced one-per-reviewer-concern.

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
