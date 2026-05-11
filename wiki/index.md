---
type: meta
title: "Top Paper Lab — Index"
updated: 2026-05-11
tags:
  - meta
  - index
status: evergreen
related:
  - "[[hot]]"
  - "[[log]]"
  - "[[papers.base]]"
  - "[[Wiki Map]]"
---

# Top Paper Lab — Index

Personal Karpathy-style wiki for reverse-engineering top-tier energy papers (Nature Energy / Joule / Nature Communications / EES / Science Advances / PNAS), with Applied Energy / Renewable Energy as a control group. The lab compounds per-paper analyses into cross-paper patterns and a personal high-impact-paper writing playbook.

Last reset: **2026-05-11** (rebrand from `claude-obsidian` plugin vault to personal Top Paper Lab). Pre-2026-05-11 vault content is archived under `wiki/_meta/`.

Navigation: [[hot]] · [[log]] · [[Wiki Map]] · [[_meta/old-index|Pre-fork archive]]

---

## Wiki layout (4 folders)

| Folder | Holds | Grows when |
|---|---|---|
| [[papers]] | One Markdown file per paper analyzed (deep 16-section reverse-engineering report) | Each `/wiki-ingest` adds one |
| [[patterns]] | Cross-paper synthesis pages (contribution archetypes, Intro / Methods / Figures / Discussion patterns, journal profiles, reviewer perspectives, research gaps) | Auto-synthesis runs at paper 10, then each ingest may update a pattern page |
| [[playbook]] | Henry's transferable writing principles (Intro template, main-figure design, case-study justification, contribution decision tree, pre-submission checklist) | Distillation pass every ~20 ingests |
| [[projects]] | Henry's own paper drafts; per-paper working files | Henry starts a new manuscript |

Subfolders inside `patterns/` and `playbook/` are created lazily as content demands. Do not pre-scaffold empty taxonomy.

---

## Domains in scope (Henry's research focus)

- Renewable energy integration
- Wind-solar-hydrogen integrated systems
- Green hydrogen techno-economic analysis
- Energy system optimization
- Building energy saving and emission reduction
- Energy policy and cost analysis

---

## Operations available

| Skill / command | Use |
|---|---|
| `/wiki-ingest <zotero-key or path>` | Orchestrates `pre-review-brief` + `research-blueprint` to produce a paper analysis under [[papers]] |
| `/wiki-query <question>` | Reads `hot.md` → `index.md` → `papers.base` → drills into pattern pages; saves valuable Q&A back into [[playbook]] |
| `/wiki-lint` | TPL-specific checks: weak/empty lessons, paper-vs-paper contradictions, crowded gaps, orphan patterns, missing Zotero links |
| `/wiki-fold` | Rolls up `log.md` entries — triggers first auto-synthesis at log size 2^k = 8 |
| `/autoresearch <topic>` (or no topic) | Boundary-first frontier surfacing; fills under-covered patterns from web/Zotero |
| `/save` | File this conversation as a [[playbook]] page |
| `/canvas` | Visual map of paper relationships |
| `mcp__zotero__*` | Read/write Zotero metadata, PDF locations, tags, collections |

ARS plugin skills wired in:
- `pre-review-brief` — per-paper deep analysis core
- `research-blueprint` — venue/journal structural fingerprint
- `academic-paper-reviewer` — critical-perspective pass (Devil's Advocate among the simulated reviewers)
- `ars-lit-review` — cross-paper annotated bibliography (used at synthesis time)
- `nature-citation` / `nature-figure` / `nature-polishing` / `nature-response` / `nature-data` — Henry's own drafting side (under [[projects]])

---

## Current state

- Pre-fork content under [[_meta/old-index|wiki/_meta/]]: 46 pages, mostly LLM-Wiki / DragonScale / SEO ecosystem research, kept for self-reference, not active material.
- Address counter at `c-000004` (3 addresses allocated so far).

## Papers ingested

1. [[papers/2022-NE-china-hta-clean-hydrogen|Yang et al. 2022, Nature Energy]] — *Breaking the hard-to-abate bottleneck in China's path to carbon neutrality with clean hydrogen*. Zotero `PIQKGJNB`. Address `c-000003`. Archetype: modeling-optimization + policy-relevant. Headline: US$1.72T avoided cumulative investment under ZERO-H vs ZERO-NH, 65.7 Mt H2/yr by 2060.

---

## Dashboard

[[papers.base]] — Obsidian Bases view of all ingested papers (journal, year, paper_type, main_contribution, status).
