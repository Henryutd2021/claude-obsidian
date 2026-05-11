---
type: meta
title: "Top Paper Lab v2 — Implementation Status"
updated: 2026-05-11
tags:
  - meta
  - handoff
  - v2
status: living
related:
  - "[[journal-role-vocab]]"
  - "[[subdomain-vocab]]"
  - "[[depth-policy]]"
  - "[[routing-rules]]"
---

# Top Paper Lab v2 — Implementation Status (2026-05-11)

This page is a session-handoff snapshot. **Read this first when continuing work after context clear.** Plan source-of-truth: `/Users/henry/.claude/plans/advanced-in-applied-energy-calm-moler.md`.

## One-paragraph state

TPL was rearchitected on 2026-05-11 from a single-track 22-paper top-journal lab to a **two-layer corpus** (L1 top-journal exemplars / L2 applied flagships) organized along **8 subdomains** with explicit **bridges** for cross-subdomain connectivity. Phases 1-3 (partial) are complete. 22 L1 papers, 0 L2 papers (Phase 2 pilot not yet triggered). All scaffolding, vocab, generators, contracts, and runners are in place. Three skill SKILL.md files need v2 updates and are the highest-priority unfinished item.

## What's working

### Vault structure (all in git, pushed to origin/main)

```
wiki/
  papers/L1/                 22 top-journal papers (frontmatter v2)
  papers/L2/{8 subdomains}/  empty, awaiting L2 pilot
  subdomains/                8 hub pages (auto-regenerable)
  bridges/                   11 bridge pages (auto-regenerable, ≥3-paper gate)
  patterns/
    cross-cutting/
      methods-recurrent/     3 patterns: additionality, plant-vs-aggregate, option-value
      archetype/             1 pattern: firm-clean-flexible-baseload
      intro|figure|discussion|contribution/  empty (have _about.md)
    subdomain/
      hydrogen-p2x/          1 pattern: merit-order
      ai-data-driven/        1 pattern: load-shape-and-flexibility
      re-tech-resources/     1 pattern: empirical-growth-envelope
      {5 others}/            empty (have _about.md)
    bridges/                 empty (have _about.md)
    comparisons/             empty (have _about.md) - L2-dependent
  banks/
    parameter-bank/          empty (have _about.md) - L2-dependent
    sensitivity-bank/        empty (have _about.md) - L2-dependent
    method-bank/             empty (have _about.md) - L2-dependent
  playbook/
    top-journal-craft/       3 v0.1 pages: intro-template, main-figure-rules, contribution-decision-tree
    applied-paper-craft/     empty (have _about.md) - L2-dependent
    upgrade-playbook/        empty (have _about.md) - L2-dependent
    submission-tier-checklists/  empty (have _about.md) - Phase 5
  projects/                  empty (have _about.md) - Henry's drafts
  _meta/
    journal-role-vocab.md
    subdomain-vocab.md
    depth-policy.md
    routing-rules.md
    subdomain-bridge-stats.md  (auto-generated)
    v2-status.md              (this file)
  papers.base                10 views, Obsidian-tested
  dashboard.base             6 views, Obsidian-tested
  index.md / hot.md / log.md
```

27 `_about.md` files explain each empty folder's purpose + trigger + source-of-truth. Use filename `_about.md` (NOT `README.md`) because `.obsidian/app.json` `userIgnoreFilters` hides README.md vault-wide.

### Frontmatter v2 (locked vocabulary)

Every paper-analysis page has:
- `journal_role`: `top_journal_exemplar` | `applied_flagship` | `technical_support` | `comparison_control`
- `ingest_depth`: `A_deep` | `B_medium` | `C_light`
- `subdomain_primary[]`: 1-2 entries; for L2, `[0]` decides folder placement
- `subdomain_secondary[]`: 0-3 entries; triggers bridge participation at ≥3-paper gate

8 subdomain slugs (locked): `integrated-energy-systems` · `power-systems` · `hydrogen-p2x` · `re-tech-resources` · `building-urban` · `energy-policy-economics` · `lca-sustainability` · `ai-data-driven`.

### Templates and contracts

| Template | Path | Sections | Codex cost target |
|---|---|---|---|
| L1 (renamed from paper-analysis.md) | `_templates/paper-analysis-L1.md` | 18 | ~$5 |
| L2-A (NEW, applied 10-section) | `_templates/paper-analysis-L2-A.md` | 10 | ~$2.5 |
| L2-B (NEW, one-page) | `_templates/paper-analysis-L2-B.md` | 6 | ~$1 |
| L2-C (NEW, citation marker) | `_templates/paper-analysis-L2-C.md` | 3 | ~$0.1 |
| Pattern (upgraded v2) | `_templates/pattern-page.md` | flexible | n/a |

Matching codex contracts at `_templates/codex-ingest-contract-L{1,2-A,2-B,2-C}.md`.

### Runners (executable, smoke-tested)

- `scripts/codex-ingest-paper.sh <KEY> <ADDR> [SLUG]` — L1 runner (renamed paths, validated)
- `scripts/codex-ingest-paper-L2.sh <KEY> <ADDR> <SLUG> <DEPTH> <PRIMARY_SUBDOMAIN>` — L2 runner; all 5 arg-validation paths tested

### Generators (re-runnable, idempotent)

| Script | What it does | Output |
|---|---|---|
| `scripts/subdomain-bridge-stats.py` | Scans wiki/papers/**/*.md frontmatter | `wiki/_meta/subdomain-bridge-stats.md` |
| `scripts/generate-subdomain-hubs.py` | Generates 8 hub pages from frontmatter | `wiki/subdomains/{slug}.md` |
| `scripts/generate-bridges.py` | Generates bridge pages for pairs ≥3 papers | `wiki/bridges/{A--B}.md` |
| `scripts/generate-empty-folder-about.py` | Adds `_about.md` to empty folders | `wiki/**/_about.md` |

Hub and bridge generators preserve `<!-- HENRY-NOTE-START --> ... <!-- HENRY-NOTE-END -->` blocks across regeneration.

### One-shot migration scripts (already run, kept for reference)

- `scripts/migrate-v2-frontmatter.py` — added v2 fields to 22 L1 papers
- `scripts/migrate-v2-manifest.py` — extended manifest CSV schema + L2 staging file
- `scripts/visibility-fix-henry-notes.py` — converted HENRY-NOTE HTML comments to italics

### Manifest

- `.raw/zotero_manifest/top_paper_lab_manifest.csv` — 142 rows, schema extended to 20 cols (journal_role, ingest_depth, subdomain_primary, subdomain_secondary, use_tags, notes added). 22 ingested rows backfilled.
- `.raw/zotero_manifest/l2_candidate_manifest.csv` — header-only staging file for L2 picks.

### Obsidian Bases dashboards (1.12.7, both rendering)

- `wiki/papers.base` — 10 views: All / L1 / L2-deep / L2-medium / By subdomain / By archetype / Bridges / Drafts / High-relevance / Upgrade candidates
- `wiki/dashboard.base` — 6 views: Subdomain hubs / Pattern pages / Bank pages / Bridge pages / Playbook pages / Folder-about navigation

Bases footguns discovered: avoid nested `or` inside top-level `and` filter; avoid `formula.X` as groupBy target; avoid `file.size` comparison.

## What's not yet done

### HIGH PRIORITY (do next session)

**Three skill SKILL.md updates** to make `/wiki-*` commands fully v2-aware. Without these, the slash commands still operate on v1 routing.

| File | What to add | Effort |
|---|---|---|
| `skills/wiki-ingest/SKILL.md` | Route by `journal_role` to L1 contract vs L2 runner. Take depth + primary-subdomain args. | ~30 min |
| `skills/wiki-lint/SKILL.md` | New lint rules: flag missing `journal_role`/`ingest_depth`/`subdomain_primary`; no-pollution rule (L1-only patterns can't cite L2 primary); bank-row routing audit; L2-A page-size ceiling; orphan bridges <3 papers; over-analyzed L2 pages. | ~20 min |
| `skills/wiki-query/SKILL.md` | Layer-aware routing: Intro/figure/discussion questions → L1 evidence only; Methods/parameters → banks + L2; comparison questions → patterns/comparisons. | ~20 min |

### MEDIUM PRIORITY (when convenient)

| Item | Source | Effort |
|---|---|---|
| 4 remaining cross-paper anchors as pattern stubs | hot.md anchors: `cost-trajectory-treatment`, `national-vs-continental-case`, `exogenous-shock-as-scenario`, `cost-multi-unit-reporting` (figure pattern) | ~1.5 h |
| `CHANGELOG.md` v2 transition entry | Manual write | 5 min |
| `CLAUDE.md` "Cross-project access" section update for L1/L2 path split | Manual edit | 5 min |
| Playbook v0.1 → v0.2 enrichment | Read all 22 papers' §5 Intro tables + §10 figure tables; refine intro-template + main-figure-rules + contribution-decision-tree from grounded reads | half day (22 × ~30 KB) |

### DEFERRED until L2 pilot lands

These are correctly waiting on at least 3 L2-A pilots to produce contrast / bank rows / examples:

- `patterns/comparisons/*` — top-vs-applied delta library (intrinsically L1+L2)
- `banks/parameter-bank/`, `sensitivity-bank/`, `method-bank/` row data — primarily L2-A fed
- `playbook/applied-paper-craft/` — needs L2 evidence
- `playbook/upgrade-playbook/` — needs `patterns/comparisons/*` accumulated
- `playbook/submission-tier-checklists/` — Phase 5 (~month 6), needs full corpus

### NOT YET DUE (Phase 4-5)

- `scripts/quota-check.sh` — triggers when L2 count > 30
- Quarterly `scripts/tiling-check.py` + `scripts/boundary-score.py`
- End-to-end `/wiki-query` verification on a Henry manuscript draft

## Next-session options (Henry picks)

| Path | Time | Value |
|---|---|---|
| **A. Finish 3 SKILL.md updates** | ~70 min | Closes the v2 architecture loop at the skill layer. Prerequisite for clean L2 pilot. |
| **B. Trigger L2 pilot (3 L2-A + 2 L2-B + 1 L2-C)** | ~30 min Henry + 1-2 h codex + verify | Unlocks `patterns/comparisons/*`, banks, applied-paper-craft. Cost ~$8. |
| **C. Henry drafts SMR-DC in `wiki/projects/`** using existing patterns + playbook v0.1 + 8 hubs + 11 bridges as checklist | 2-4 h | The real test of whether v2 vault serves Henry's writing goal. |

Recommended order: **A → C → B**. A makes the lab self-consistent. C tests it on a real manuscript. B fills the remaining content gaps based on what C surfaced.

## Commit SHA rollback chain (origin/main)

| SHA | Stage | What it captured |
|---|---|---|
| `c2a19e5` | Phase 0 snapshot | Pre-v2 state — 22 papers, original 6-view papers.base, no v2 anything |
| `0a67fde` | Phase 1 end | Taxonomy plumbing: vocab files + 22 frontmatters + git mv to L1/ + manifest schema + papers.base 10 views + dashboard.base + scaffold |
| `27c73cb` | Phase 2 end | L2 templates + 3 codex contracts + L2 runner |
| `de9106c` | Phase 3 partial | 8 subdomain hubs + 11 bridges + auto-stats |
| `fbc5d97` | Option B | 7 pattern pages + 3 playbook v0.1 |
| `bb2366e` | Visibility fixes | 27 _about.md + 29 HENRY-NOTE italics |
| `49d5d32` + auto | Dashboard fixes | Simplified dashboard.base + .gitignore exception fix |
| `1848286` (current HEAD) | Dashboard enriched | Property columns added |

To roll back: `git reset --hard <SHA>` (will not lose work since everything is pushed to origin/main).

## Known footguns and conventions

| Footgun | Workaround |
|---|---|
| `.obsidian/app.json` `userIgnoreFilters` hides `README.md` anywhere in vault | Use `_about.md` filename (underscore-prefixed, not in filter list, sorts to top of folder) |
| `.gitignore` has `*.base` then explicit unignore rules | When adding new `.base` files, append to `!wiki/...` unignore list |
| Obsidian Bases nested `and: { or: [...] }` filter at top level → empty render | Use top-level single combinator (just `and` or just `or`); push folder filters down into each view |
| Obsidian Bases `groupBy: formula.X` → may fail silently | Use a real frontmatter field (e.g., `type`, `status`) for groupBy |
| Obsidian Bases `file.size < N` filter | Untested; avoid |
| Obsidian caches `.base` views across sessions | Cmd+Q + full restart to force re-parse |
| HTML comments invisible in Obsidian reading mode | Wrap visible text in `<!-- HENRY-NOTE-START --> ... <!-- HENRY-NOTE-END -->` markers but put italics or plain markdown between them |
| `wiki/_meta/dropped-plugin-scaffold/` legacy folder | Untouched; pre-fork content |
| codex sandbox Zotero MCP failures | codex auto-falls-back to local Zotero SQLite or publisher HTML; `fulltext_source` in receipt records which path |

## What v2 architecture is for (one-paragraph reminder)

**L1 (top_journal_exemplar) teaches Henry cross-domain writing craft**: problem framing, contribution architecture, Intro structure, figure narrative, Discussion elevation. Lives flat in `wiki/papers/L1/` because L1 papers span subdomains by nature. Always `A_deep` ingest.

**L2 (applied_flagship) teaches subdomain-specific technical depth**: model rigor, system boundary, parameter values, case-study justification, sensitivity design, engineering feasibility. Organized by primary subdomain in `wiki/papers/L2/{slug}/` because L2 value clusters tightly to one subdomain. Tiered depth A/B/C for cost-controlled scaling to ~100 L2 papers/year.

**L3 (technical_support) = manual entry only**: parameters from IJHE / J. Energy Storage / etc. flow into `wiki/banks/*` rows with Zotero citations, no paper-analysis page generated.

**Connectivity layer**: 8 subdomain hubs for focused retrieval + bridge pages (≥3-paper gate) for cross-subdomain interface patterns. Independence and connectivity simultaneously.

**No-pollution rule** (lint-enforced): pattern pages under `patterns/cross-cutting/{intro,figure,discussion,archetype,contribution}/` and `playbook/top-journal-craft/` must NOT cite L2 as primary evidence. L2 appears in `patterns/comparisons/` and `patterns/cross-cutting/methods-recurrent/` as contrast / supplement.

## How to continue work in a fresh session

1. Read this page first.
2. Read the plan: `/Users/henry/.claude/plans/advanced-in-applied-energy-calm-moler.md`.
3. Skim `wiki/hot.md` and the last log entry in `wiki/log.md` for the most recent ops.
4. Pick a path (A / B / C above) and announce intent to Henry.

End of handoff.
