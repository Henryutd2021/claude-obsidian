
# Top Paper Lab

> **Personal fork from [claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) v1.6.0.** This vault was the upstream plugin's reference vault until 2026-05-11. It is now Henry's personal **Top Paper Lab**, a Karpathy-style LLM Wiki specialized for reverse-engineering top-tier energy papers (Nature, Nature Energy, Joule, Nature Communications, Nature Sustainability, Nature Climate Change, One Earth) and distilling a personal high-impact-paper writing playbook. The upstream `claude-obsidian` plugin continues at the link above; this fork drops the plugin distribution role.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Upstream: claude-obsidian](https://img.shields.io/badge/Upstream-claude--obsidian_v1.6.0-8B5CF6)](https://github.com/AgriciDaniel/claude-obsidian)

The lab ingests papers Henry has already curated in Zotero (via Zotero MCP), runs structured 18-section reverse-engineering analysis per paper, and compounds the per-paper outputs into cross-paper pattern pages and a personal writing playbook. The constitution lives in [`CLAUDE.md`](CLAUDE.md). Navigation starts at [`wiki/index.md`](wiki/index.md) and [`wiki/hot.md`](wiki/hot.md).

---

## What lives where

```
.                                 vault root
|-- wiki/                         active wiki
|   |-- index.md                  navigation hub
|   |-- hot.md                    recent context (read first on session start)
|   |-- log.md                    append-only ingest log
|   |-- papers.base               Obsidian Bases dashboard over papers/
|   |-- papers/                   one .md per ingested paper analysis
|   |-- patterns/                 cross-paper synthesis (lazy subfolders)
|   |-- playbook/                 personal writing principles
|   |-- projects/                 Henry's own manuscripts in progress
|   |-- _meta/                    pre-fork archive + dropped plugin scaffold
|   |-- Wiki Map.canvas           visual layout
|-- _templates/                   paper-analysis.md, codex-ingest-contract.md, ...
|-- skills/                       11 wiki operation skills (wiki-ingest, wiki-query, ...)
|-- scripts/                      DragonScale machinery + codex-ingest-paper.sh wrapper
|-- hooks/                        SessionStart, PostToolUse auto-commit, Stop
|-- tests/                        DragonScale test suite (run with `make test`)
|-- .raw/papers/{KEY}/            per-paper 7-stub package (metadata.json, DA/CA, ...)
|-- .raw/zotero_manifest/         CSV manifest of the curated Top Paper Lab collection
`-- .vault-meta/                  DragonScale state (address counter, tiling cache)
```

The plugin-distribution scaffolding that used to sit at the root (`bin/`, `commands/`, `agents/`, `docs/`, `AGENTS.md`, `GEMINI.md`, `WIKI.md`, `.github/`, `.windsurf/`, `.cursor/`) is archived under [`wiki/_meta/dropped-plugin-scaffold/`](wiki/_meta/dropped-plugin-scaffold/). See its [README](wiki/_meta/dropped-plugin-scaffold/README.md) for what was moved and why.

---

## How to add a paper

Two paths, both governed by the same 18-section [paper-analysis template](_templates/paper-analysis.md) and the three-label discipline (`Evidence:` / `Inference:` / `Lesson:`) plus the anti-fluff word list in [`CLAUDE.md`](CLAUDE.md).

**Path A: Claude Code composes**
Drop a Zotero key into a Claude Code session. Claude reads the paper via Zotero MCP, scaffolds the seven `.raw/papers/{KEY}/` stub files, allocates a `c-NNNNNN` address, and writes `wiki/papers/{year}-{journal-short}-{slug}.md`. Tight cross-reference coupling, slower (about 15 minutes per paper), context-bounded after a few papers.

**Path B: Delegate to codex-cli**
Run `scripts/codex-ingest-paper.sh <ZOTERO_KEY> <ADDRESS> [SLUG_HINT]`. Codex follows the standing contract at [`_templates/codex-ingest-contract.md`](_templates/codex-ingest-contract.md), writes everything under `wiki/papers/` and `.raw/papers/{KEY}/`, and emits a JSON receipt at `.raw/papers/{KEY}/codex-receipt.json`. Parallel-friendly (3-5 jobs at once), about 200-230k tokens and 8-12 minutes wall-clock per paper. Address allocation and index/log/hot/manifest integration stay with Claude Code (single-writer policy).

Hybrid is the recommended workflow: Path A for the first paper of a new archetype or journal, Path B for batches of 3-5 similar papers, then a Claude Code consolidation pass to add Cross-references and contradiction callouts.

---

## DragonScale machinery

Active mechanisms inherited from the upstream plugin (still in regular use):

- `scripts/allocate-address.sh` reserves the next `c-NNNNNN` page address under a portable lock (`flock` on Linux, `mkdir` fallback on macOS).
- `skills/wiki-fold/` rolls up `wiki/log.md` entries into period summaries at `2^k` ingest boundaries (k=3, first synthesis at 8 papers).
- `scripts/tiling-check.py` catches semantic duplication between pattern pages.
- `scripts/boundary-score.py` surfaces under-researched pattern areas for `/autoresearch`.

Tests:

```bash
make test
```

(Covers `allocate-address.sh`, `tiling-check.py`, `boundary-score.py`. No ollama dependency for the default test set.)

---

## Cross-project consult

To consult the lab from another Claude Code project, add this to that project's `CLAUDE.md`:

```markdown
## Top Paper Lab consult

Path: /Users/henry/Library/Mobile Documents/iCloud~md~obsidian/Documents/claude-obsidian/

When the question is about top-tier energy-paper writing strategy, contribution framing, or journal fit:
1. Read wiki/hot.md (recent context).
2. Read wiki/index.md.
3. Search wiki/papers/ and wiki/patterns/ for relevant pages.
4. Cite specific paper-analysis pages.

Do NOT consult for anything outside renewable energy / wind-solar-hydrogen / TEA / energy-system-optimization / building decarbonization scope.
```

---

## Scope

Renewable energy integration, wind-solar-hydrogen integrated systems, green hydrogen techno-economic analysis, energy system optimization, building energy saving and emission reduction, energy policy and cost analysis. Anything outside this scope should be answered without consulting the lab.

---

<details>
<summary>Plugin lineage (pre-fork history)</summary>

This vault was the reference vault for the public [`claude-obsidian` plugin v1.6.0](https://github.com/AgriciDaniel/claude-obsidian) up to 2026-05-11. The plugin is Claude + Obsidian knowledge companion built on Andrej Karpathy's [LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f), with 11 skills, multi-agent support, and the optional DragonScale Memory extension (log folds, deterministic page addresses, semantic tiling lint, boundary-first autoresearch).

Upstream documentation, install scripts, and IDE rules are preserved at [`wiki/_meta/dropped-plugin-scaffold/`](wiki/_meta/dropped-plugin-scaffold/). For the canonical project, see the upstream repository. For change history, see [`CHANGELOG.md`](CHANGELOG.md).

</details>
