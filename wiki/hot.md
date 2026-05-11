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

## Next actions (in order)

1. Henry: organize Zotero — create top-level collection `Top Paper Lab` with all the top-tier energy papers he's collected. Apply minimal tags (`journal/{NatureEnergy|NatureCommunications|Joule|EES|AppliedEnergy|...}`, `topic/{green-hydrogen|renewable-integration|...}`, `status/candidate`).
2. Claude Code via Zotero MCP: build `.raw/zotero_manifest/top_paper_lab_manifest.csv` (one row per paper, fields per `CLAUDE.md` Ingest workflow).
3. Henry picks one seed paper (most-relevant Nature Energy or Joule).
4. Asset completion: download SI + extract Data Availability / Code Availability into `.raw/papers/{ZOTERO_KEY}/`. PDFs and SI files stay gitignored.
5. `/wiki-ingest .raw/papers/{ZOTERO_KEY}/` — produces `wiki/papers/{year}-{journal}-{slug}.md` with Evidence / Inference / Lesson labels + 5 permanent notes + 5 writing/research lessons + 5 future questions.
6. Henry reviews; iterate on `CLAUDE.md` if anything weak. Then 4 more pilots.

## Constraints (from TPL constitution)

- Three required labels on every important claim: `Evidence:` (in paper/SI/DA/CA) · `Inference:` (derived) · `Lesson:` (transferable to my work).
- Anti-fluff: no "innovative / important / rigorous / high-impact / comprehensive / well-written" without concrete justification.
- Don't diffuse-update pattern pages until paper 10 (patterns emerge bottom-up).
- Zotero is bibliographic source of truth; YAML frontmatter only stores TPL-specific fields.
- `.raw/papers/{KEY}/main.pdf`, `supplementary/`, `source-data/` are gitignored.

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
