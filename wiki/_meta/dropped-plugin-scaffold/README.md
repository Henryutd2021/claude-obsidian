# Dropped plugin scaffold

This directory holds the plugin-distribution scaffolding that the vault used while it was the reference vault for the public [`claude-obsidian` plugin v1.6.0](https://github.com/AgriciDaniel/claude-obsidian). On 2026-05-11 the vault forked into Henry's personal Top Paper Lab. The scaffolding below is no longer load-bearing for TPL operations but is preserved here so fork history is recoverable without digging through git.

## What is in this directory

| Path | Original role | Why archived |
|---|---|---|
| `AGENTS.md` | Codex CLI / OpenCode install guide for the plugin's skills | TPL agents are governed by `_templates/codex-ingest-contract.md` directly, not by a cross-platform install file |
| `GEMINI.md` | Gemini CLI install guide | Same |
| `WIKI.md` | Generic LLM Wiki schema reference doc | Superseded by `CLAUDE.md` (the TPL constitution) |
| `bin/` | Plugin install scripts (`setup-vault.sh`, `setup-dragonscale.sh`, `setup-multi-agent.sh`) | One-time setup is done; scripts can be re-run from here if a fresh vault is ever needed |
| `commands/` | Plugin slash-command definitions (`wiki.md`, `save.md`, `canvas.md`, `autoresearch.md`) | Replaced by direct skill invocation under `skills/` |
| `agents/` | Plugin agent definitions (`wiki-ingest.md`, `wiki-lint.md`) | Replaced by `skills/wiki-ingest/` and `skills/wiki-lint/` |
| `docs/` | Plugin documentation (`install-guide.md`, `dragonscale-guide.md`, `releases/v1.6.0.md`) | Install guide no longer relevant; DragonScale guide can be referenced here if needed |
| `.github/` | GitHub Actions and Copilot instructions for plugin CI | Not relevant for a personal vault |
| `.windsurf/` | Windsurf IDE rules for the plugin | Not relevant |
| `.cursor/` | Cursor IDE rules for the plugin | Not relevant |
| `.claude-plugin/` | Plugin manifest (`plugin.json`, `marketplace.json`) | Plugin distribution role dropped |

## What stayed active at the vault root

Operations that TPL still uses:

- `scripts/` — `allocate-address.sh`, `tiling-check.py`, `boundary-score.py`, `codex-ingest-paper.sh`
- `skills/` — 11 wiki operation skills (`wiki-ingest`, `wiki-query`, `wiki-lint`, `wiki-fold`, `save`, `autoresearch`, `canvas`, `defuddle`, `obsidian-bases`, `obsidian-markdown`, `wiki`)
- `hooks/` — `hooks.json` (SessionStart, PostCompact, PostToolUse auto-stage, Stop)
- `_templates/` — `paper-analysis.md`, `codex-ingest-contract.md`, `pattern-page.md`, `project-page.md`
- `tests/`, `Makefile` — DragonScale automation (`make test` still works for `allocate-address.sh`, `tiling-check.py`, `boundary-score.py`)
- `wiki/`, `.raw/`, `.vault-meta/` — wiki content + paper packages + DragonScale state

## How to retrieve old behavior

If a TPL operation ever needs something that lived in the plugin scaffold, prefer copying the specific file you need back to root rather than restoring the whole archive. The fork is intentionally pruned; resurrecting plugin distribution at the root would undo the rebrand.

To re-run a setup script:

```bash
bash wiki/_meta/dropped-plugin-scaffold/bin/setup-dragonscale.sh
```

To read the DragonScale design doc:

```bash
$EDITOR wiki/_meta/dropped-plugin-scaffold/docs/dragonscale-guide.md
```
