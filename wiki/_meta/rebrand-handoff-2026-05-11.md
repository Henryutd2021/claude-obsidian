---
type: meta
title: "Rebrand handoff 2026-05-11"
date: 2026-05-11
tags:
  - meta
  - handoff
status: evergreen
---

# Top Paper Lab rebrand — handoff notes

This file records the 2026-05-11 fork from `claude-obsidian` plugin vault to personal **Top Paper Lab**. It is reference-only; the active machinery lives in `CLAUDE.md`, `wiki/index.md`, and `wiki/hot.md`.

## What changed (in order)

**Phase 1 — Plugin de-scaffold**
- Moved `.claude-plugin/` → `wiki/_meta/dropped-plugin-scaffold/.claude-plugin/`.
- Rewrote top of `README.md` to declare the fork; preserved attribution to upstream `AgriciDaniel/claude-obsidian`.
- Added 2026-05-11 entry to `CHANGELOG.md`.

**Phase 2 — Wiki re-skeleton**
- Created `wiki/papers/`, `wiki/patterns/`, `wiki/playbook/`, `wiki/projects/` (all empty).
- Moved pre-fork content into `wiki/_meta/`: `canvases/`, `comparisons/`, `concepts/`, `entities/`, `folds/`, `meta/`, `questions/`, `sources/`, `getting-started.md`, `overview.md`.
- Snapshot of old `hot.md` → `wiki/_meta/old-hot.md`; old `index.md` → `wiki/_meta/old-index.md`.
- Rewrote `wiki/index.md`, `wiki/hot.md` for TPL identity and scope.
- Appended `## [2026-05-11] retheme` entry to top of `wiki/log.md` (preserved all prior history).
- Replaced `wiki/Wiki Map.canvas` with a 4-folder topology canvas.
- Added 3 templates to `_templates/`: `paper-analysis.md`, `pattern-page.md`, `project-page.md`.

**Phase 3 — Constitution**
- Rewrote `CLAUDE.md` as the TPL constitution. Defines: source-of-truth hierarchy, three required labels (Evidence / Inference / Lesson), anti-fluff word list, 4-folder layout, ingest workflow (orchestrating `pre-review-brief` + `research-blueprint` + `academic-paper-reviewer`), cross-page-update gate (paper-10 threshold), query/lint workflows, DragonScale machinery role, Zotero MCP integration, YAML frontmatter, skill catalogue, discipline guardrails.
- Extended `.gitignore` to exclude `.raw/papers/**/main.pdf`, `.raw/papers/**/supplementary/`, `.raw/papers/**/source-data/`, `.raw/papers/**/*.pdf`, `.raw/papers/**/*.zip`. Lightweight text files in those folders (`metadata.json`, `data-availability.md`, etc.) remain tracked.

**Phase 4 — Manifest + dashboard**
- Created `.raw/zotero_manifest/` directory with stub `top_paper_lab_manifest.csv` (header only) and `README.md` documenting the manifest schema and rebuild instructions.
- Created `wiki/papers.base` (Obsidian Bases) with 6 views: All papers, By contribution type (card), NE + Joule + NC, Applied Energy (control), Drafts needing review, High-relevance backlog.
- Added `!wiki/papers.base` exception to `.gitignore` so the dashboard is tracked.

**Phase 5 — Verification**
- `python3 tests/test_boundary_score.py` → all green.
- `python3 tests/test_tiling_check.py` → all green.
- `bash tests/test_allocate_address.sh` → **fails because macOS lacks `flock`**. This is a pre-existing environmental issue (commits `16d9923` + `8b28e48` from the DragonScale phase). Not caused by the rebrand. Resolve by `brew install util-linux` if Henry wants the address allocator to work on this machine; otherwise the lab works without addresses for now (the `address:` frontmatter field stays empty).

## What did NOT change (kept intact)

- All 11 skills under `skills/`.
- All scripts under `scripts/`.
- DragonScale state under `.vault-meta/` (counter at 3, thresholds, legacy-pages baseline).
- All hooks (SessionStart, PostCompact, PostToolUse, Stop).
- `Makefile`, `bin/setup-*.sh`, `tests/`.
- Folder path of the vault — still `.../claude-obsidian/`. Obsidian title bar still shows "claude-obsidian"; if Henry wants the display name to read "Top Paper Lab", rename the vault entry in Obsidian's vault switcher (right-click the vault → Rename) — this is an Obsidian system-level setting that lives in `~/Library/Application Support/obsidian/obsidian.json`, not in this repo.

## Next actions for Henry

1. **Organize Zotero**: create a top-level collection called `Top Paper Lab` and drag in the curated NE / NC / Joule / EES / SciAdv / PNAS papers plus 5–10 Applied Energy / Renewable Energy controls. Apply minimal tags (`journal/{...}`, `topic/{green-hydrogen|renewable-integration|wind-solar-hydrogen|...}`, `status/candidate`).
2. **Open a Claude Code session** at the vault root and ask:
   > Build the Top Paper Lab manifest. Use Zotero MCP to read all items in the `Top Paper Lab` collection. Write `.raw/zotero_manifest/top_paper_lab_manifest.csv` with one row per item per the schema in `.raw/zotero_manifest/README.md`. Set `ingest_status = candidate` for every row.
3. **Pick one seed paper** — ideally the Nature Energy or Joule paper most relevant to wind-solar-hydrogen TEA. Note the Zotero key (8 chars).
4. **Drop the PDF + SI** into `.raw/papers/{KEY}/`. Both are gitignored automatically. Add the publisher landing page snapshot and extract Data Availability + Code Availability statements (manually or via `defuddle` + a brief Claude Code session).
5. **Run** `/wiki-ingest .raw/papers/{KEY}/`. This will:
   - Read paper package
   - Call `pre-review-brief` to position the paper against Henry's library
   - Call `research-blueprint <journal>` to load venue fingerprint
   - Call `academic-paper-reviewer` in quick-assessment mode for critical perspective
   - Compose `wiki/papers/{year}-{journal-short}-{slug}.md` using the `paper-analysis.md` template
   - Update `wiki/index.md`, `wiki/log.md`, `wiki/hot.md`
6. **Review the output**. If anything reads as fluffy or unsupported, iterate on `CLAUDE.md`'s anti-fluff list before paper 2.
7. **Repeat for 4 more papers** — different journals, different archetypes, including 1 Applied Energy as control.
8. **At paper 5**: ask Claude Code to run `/wiki-fold` over `log.md`. The first auto-synthesis lands in `wiki/folds/`. Promote durable claims into named `wiki/patterns/{topic}/` pages.
9. **At paper 20**: distill into `wiki/playbook/` — the 5 canonical playbook docs (Intro template, Figure design, Case-study justification, Contribution decision tree, Pre-submission checklist).
10. **When drafting a new manuscript**, create `wiki/projects/{paper-name}/` from `_templates/project-page.md` and consult the lab via `/wiki-query`.

## Files of interest (read order if returning cold)

1. `wiki/hot.md` — recent session context
2. `wiki/index.md` — navigation
3. `CLAUDE.md` — constitution
4. `wiki/papers.base` (open in Obsidian) — dashboard
5. `.raw/zotero_manifest/README.md` — manifest schema
6. `_templates/paper-analysis.md` — what each `wiki/papers/*` page contains
7. `wiki/_meta/old-index.md` — pre-fork content reference, if needed
