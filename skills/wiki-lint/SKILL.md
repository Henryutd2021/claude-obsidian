---
name: wiki-lint
description: >
  Health check the Obsidian wiki vault. Finds orphan pages, dead wikilinks, stale claims,
  missing cross-references, frontmatter gaps, and empty sections. Creates or updates
  Dataview dashboards. Generates canvas maps. Triggers on: "lint", "health check",
  "clean up wiki", "check the wiki", "wiki maintenance", "find orphans", "wiki audit".
---

# wiki-lint: Wiki Health Check

Run lint after every 10-15 ingests, or weekly. Ask before auto-fixing anything. Output a lint report to `wiki/meta/lint-report-YYYY-MM-DD.md`.

---

## Lint Checks

Work through these in order:

1. **Orphan pages**. Wiki pages with no inbound wikilinks. They exist but nothing points to them.
2. **Dead links**. Wikilinks that reference a page that does not exist.
3. **Stale claims**. Assertions on older pages that newer sources have contradicted or updated.
4. **Missing pages**. Concepts or entities mentioned in multiple pages but lacking their own page.
5. **Missing cross-references**. Entities mentioned in a page but not linked.
6. **Frontmatter gaps**. Pages missing required fields (type, status, created, updated, tags).
7. **Empty sections**. Headings with no content underneath.
8. **Stale index entries**. Items in `wiki/index.md` pointing to renamed or deleted pages.
9. **Address validity** (DragonScale Mechanism 2). For every page that has an `address:` frontmatter field, validate the format. See the **Address Validation** section below.
10. **Semantic tiling** (DragonScale Mechanism 3, opt-in). Flag candidate duplicate pages (across all scanned types, not just concepts) via embedding cosine similarity. See the **Semantic Tiling** section below.

---

## Lint Report Format

Create at `wiki/meta/lint-report-YYYY-MM-DD.md`:

```markdown
---
type: meta
title: "Lint Report YYYY-MM-DD"
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [meta, lint]
status: developing
---

# Lint Report: YYYY-MM-DD

## Summary
- Pages scanned: N
- Issues found: N
- Auto-fixed: N
- Needs review: N

## Orphan Pages
- [[Page Name]]: no inbound links. Suggest: link from [[Related Page]] or delete.

## Dead Links
- [[Missing Page]]: referenced in [[Source Page]] but does not exist. Suggest: create stub or remove link.

## Missing Pages
- "concept name": mentioned in [[Page A]], [[Page B]], [[Page C]]. Suggest: create a concept page.

## Frontmatter Gaps
- [[Page Name]]: missing fields: status, tags

## Stale Claims
- [[Page Name]]: claim "X" may conflict with newer source [[Newer Source]].

## Cross-Reference Gaps
- [[Entity Name]] mentioned in [[Page A]] without a wikilink.
```

---

## Naming Conventions

Enforce these during lint:

| Element | Convention | Example |
|---------|-----------|---------|
| Filenames | Title Case with spaces | `Machine Learning.md` |
| Folders | lowercase with dashes | `wiki/data-models/` |
| Tags | lowercase, hierarchical | `#domain/architecture` |
| Wikilinks | match filename exactly | `[[Machine Learning]]` |

Filenames must be unique across the vault. Wikilinks work without paths only if filenames are unique.

---

## Writing Style Check

During lint, flag pages that violate the style guide:

- Not declarative present tense ("X basically does Y" instead of "X does Y")
- Missing source citations where claims are made
- Uncertainty not flagged with `> [!gap]`
- Contradictions not flagged with `> [!contradiction]`

---

## Dataview Dashboard

Create or update `wiki/meta/dashboard.md` with these queries:

````markdown
---
type: meta
title: "Dashboard"
updated: YYYY-MM-DD
---
# Wiki Dashboard

## Recent Activity
```dataview
TABLE type, status, updated FROM "wiki" SORT updated DESC LIMIT 15
```

## Seed Pages (Need Development)
```dataview
LIST FROM "wiki" WHERE status = "seed" SORT updated ASC
```

## Entities Missing Sources
```dataview
LIST FROM "wiki/entities" WHERE !sources OR length(sources) = 0
```

## Open Questions
```dataview
LIST FROM "wiki/questions" WHERE answer_quality = "draft" SORT created DESC
```
````

---

## Canvas Map

Create or update `wiki/meta/overview.canvas` for a visual domain map:

```json
{
  "nodes": [
    {
      "id": "1",
      "type": "file",
      "file": "wiki/overview.md",
      "x": 0, "y": 0,
      "width": 300, "height": 140,
      "color": "1"
    }
  ],
  "edges": []
}
```

Add one node per domain page. Connect domains that have significant cross-references. Colors map to the CSS scheme: 1=blue, 2=purple, 3=yellow, 4=orange, 5=green, 6=red.

---

## Address Validation (DragonScale Mechanism 2 MVP)

**Opt-in feature.** Address Validation runs only if the vault is using DragonScale, detected by:

```bash
if [ -x ./scripts/allocate-address.sh ] && [ -f ./.vault-meta/address-counter.txt ]; then
  DRAGONSCALE_ADDRESSES=1
else
  DRAGONSCALE_ADDRESSES=0
fi
```

When `DRAGONSCALE_ADDRESSES=0`, skip this entire section. Missing `address:` fields are not flagged, not even informationally. Pages that happen to have an `address:` field are passed through unvalidated (treat as user-managed metadata).

When `DRAGONSCALE_ADDRESSES=1`, proceed with the rollout baseline and checks below.

Rollout baseline: **2026-04-23** (Phase 2 ship date in vaults that adopted DragonScale on that day). Vaults that adopted DragonScale later should override this baseline by setting the earliest `created:` date of any addressed page as their personal rollout date. Record the chosen baseline at the top of `.vault-meta/legacy-pages.txt` as a commented line: `# rollout: YYYY-MM-DD`.

### Classification rule (applied per page)

Before validating anything, classify the page:

| Classification | Criteria |
|---|---|
| **Meta / fold / excluded** | File is in `wiki/folds/` OR filename in `{_index.md, index.md, log.md, hot.md, overview.md, dashboard.md, dashboard.base, Wiki Map.md, getting-started.md}`. Address not required. |
| **Post-rollout (must have address)** | `type` is not meta/fold AND frontmatter `created:` date is >= 2026-04-23 AND file path is NOT in the legacy baseline manifest. |
| **Legacy (backfill-eligible)** | `type` is not meta/fold AND frontmatter `created:` date is < 2026-04-23 OR file path IS in the legacy baseline manifest. Address not required until backfill. |

**Legacy baseline manifest**: optional file at `.vault-meta/legacy-pages.txt`, one relative path per line. Pages listed there are treated as legacy regardless of `created:` date. Use this to grandfather pages whose `created:` metadata is wrong or missing.

### Validation checks (run in order)

1. **Format check**: any page with `address:` set must match one of:
   - `^c-[0-9]{6}$` — post-rollout creation address.
   - `^l-[0-9]{6}$` — legacy-backfill address.
   - Pages under `wiki/folds/` use `fold_id`, not `address`; do not apply the `c-`/`l-` regex there.

2. **Uniqueness check**: no two pages share the same address value. Report both paths.

3. **Counter consistency**: `./scripts/allocate-address.sh --peek` returns the next counter value. Every observed `c-NNNNNN` must satisfy `NNNNNN < peek_value`. Violation = counter drift.

4. **Post-rollout enforcement**: every page classified as "post-rollout (must have address)" that LACKS the `address:` field is a lint **error**, not informational. This prevents the silent-regression path where a new page skips address assignment.

5. **Legacy identification**: every page classified as "legacy" that LACKS an address is informational. The lint report lists them under "Pending backfill" with total count.

6. **Address-map consistency** (`.raw/.manifest.json`): for every page path in `address_map`, the page must exist and its frontmatter `address` must match the mapping. Mismatches are errors (either a rename dropped the map update, or a manual edit diverged).

### Lint posture summary

- Pages that HAVE an address with bad format: **error**.
- Pages that HAVE colliding addresses: **error**.
- Pages classified **post-rollout** WITHOUT an address: **error**.
- Pages classified **legacy** WITHOUT an address: **informational** (expected).
- Meta and fold pages without `address`: **ignored** (not applicable).
- Counter drift (observed counter >= peek): **error**.
- Address-map mismatch: **error**.

Lint only observes. Do NOT auto-assign missing addresses during lint. Assignment is `wiki-ingest`'s responsibility only.

### Output section in the lint report

```markdown
## Address Validation

- Counter state: `$(./scripts/allocate-address.sh --peek)`
- Highest c- address observed: c-XXXXXX
- Post-rollout pages checked: N (X passing, Y errors)
- Legacy pages pending backfill: M

### Errors
- [[Page Name]]: invalid address format `{value}`. Expected `c-NNNNNN` or `l-NNNNNN`.
- [[Page A]] and [[Page B]] share address `c-000042`.
- [[Post-Rollout Page]]: missing address. Page created 2026-04-25 (post-rollout); address required. Run wiki-ingest or manually run `./scripts/allocate-address.sh` and add to frontmatter.
- [[Page Name]] has address `c-000100` but counter peek is `50`. Counter drift; run `./scripts/allocate-address.sh --rebuild`.
- `.raw/.manifest.json` maps `wiki/foo.md` -> `c-000010` but page frontmatter has `c-000012`. Resolve mismatch.

### Pending backfill (informational)
- M legacy pages without addresses. See `.vault-meta/legacy-pages.txt` for the canonical legacy set, or filter by `created:` < 2026-04-23.
```

---

## Semantic Tiling (DragonScale Mechanism 3 MVP, opt-in)

**Opt-in feature.** Semantic tiling flags candidate duplicate *pages* (not just concept pages — see Scope below) using embedding cosine similarity. Local ollama only by default; remote endpoints require an explicit override flag.

### Detection and delegation

```bash
if [ -x ./scripts/tiling-check.py ] && command -v python3 >/dev/null 2>&1; then
  ./scripts/tiling-check.py --peek > /tmp/tiling-peek.json 2>/dev/null
  PEEK_EXIT=$?
  case $PEEK_EXIT in
    0)  TILING_READY=1 ;;                                  # ready
    2)  TILING_READY=0 ; echo "tiling ERROR: usage error (exit 2); inspect /tmp/tiling-peek.json" ;;
    3)  TILING_READY=0 ; echo "tiling ERROR: cache corrupt (exit 3); inspect .vault-meta/tiling-cache.json" ;;
    4)  TILING_READY=0 ; echo "tiling ERROR: vault exceeds scale hard-fail (exit 4); batching required" ;;
    10) TILING_READY=0 ; echo "tiling skipped: ollama not reachable (exit 10)" ;;
    11) TILING_READY=0 ; echo "tiling skipped: run 'ollama pull nomic-embed-text' to enable (exit 11)" ;;
    *)  TILING_READY=0 ; echo "tiling ERROR: unexpected exit code $PEEK_EXIT from tiling-check.py --peek" ;;
  esac
else
  TILING_READY=0
  echo "tiling skipped: scripts/tiling-check.py or python3 not available"
fi
```

Inspect `/tmp/tiling-peek.json` (structured diagnostics: script path, python interpreter, ollama URL, cache state, thresholds state) whenever the status is ambiguous. Never collapse unknown exits into "unknown status" silently.

When `TILING_READY=1`:

```bash
./scripts/tiling-check.py --report wiki/meta/tiling-report-YYYY-MM-DD.md
REPORT_EXIT=$?
case $REPORT_EXIT in
  0)  echo "tiling report written" ;;
  2)  echo "tiling ERROR: usage error during --report" ;;
  3)  echo "tiling ERROR: cache corrupt during --report" ;;
  4)  echo "tiling ERROR: scale hard-fail during --report" ;;
  10) echo "tiling ERROR: ollama became unreachable between --peek and --report" ;;
  11) echo "tiling ERROR: model became unavailable between --peek and --report" ;;
  *)  echo "tiling ERROR: unexpected exit code $REPORT_EXIT from tiling-check.py --report" ;;
esac
```

### Scope (what the helper scans)

- Includes: every `.md` under `wiki/` **except** the exclusion set below. The scope is "candidate tileable pages," not just `type: concept`.
- Excludes (path): anything under `wiki/folds/` or `wiki/meta/`.
- Excludes (filename): `_index.md`, `index.md`, `log.md`, `hot.md`, `overview.md`, `dashboard.md`, `Wiki Map.md`, `getting-started.md`.
- Excludes (frontmatter): `type: meta` or `type: fold`.
- Excludes (security): symlinks. Any page file that is a symlink, or whose resolved path escapes the vault root, is skipped.

If you place a real concept under `wiki/meta/` it will be excluded by path regardless of content. Keep concepts in their canonical folders.

### How the helper works

- Computes one embedding per included page via the ollama `nomic-embed-text` model by default.
- Caches embeddings at `.vault-meta/tiling-cache.json`, keyed on `sha256(model + body)` so model drift auto-invalidates. Frontmatter is not part of the hash or the embedding input — pure frontmatter edits (tag changes, status bumps) do not trigger recomputation.
- Orphans are GC'd: when a cached page path no longer exists on disk, its entry is dropped on save.
- Concurrent-safe: exclusive flock on `.vault-meta/.tiling.lock` around cache I/O; per-PID temp file for atomic writes.

### Security posture

- Defaults to `http://127.0.0.1:11434`. `OLLAMA_URL` env override is accepted **only** with `--allow-remote-ollama` because page bodies are POSTed as embedding input.
- Symlinks and vault-root escapes are rejected.

### Default bands (conservative seeds, NOT calibrated)

| Band | Similarity | Report section |
|---|---|---|
| Error | `>= 0.90` | **Errors** — strong near-duplicate, likely the same concept |
| Review | `0.80 - 0.90` | **Review** — possible tile overlap; human judgement needed |
| Pass | `< 0.80` | not emitted |

**These values are conservative seeds, not literature-backed interpolation.** Published reference points: Sentence Transformers `community_detection` defaults to 0.75; Quora-duplicate calibrations land around 0.7715-0.8352 depending on objective. The 0.80 review floor is already stricter than at least one cited Quora optimum, so expect **false negatives** against those baselines. Reduce the review floor during calibration if you want more sensitivity.

### Calibration procedure (manual, one-time per vault)

1. Run the helper with defaults. Capture the **Review** band pairs.
2. Temporarily lower `bands.review` to `0.70` in `.vault-meta/tiling-thresholds.json` to surface a wider sample. Aim for >=50 pairs spanning 0.70-0.95.
3. Label each pair: `duplicate`, `similar`, `distinct`.
4. Pick bands such that: (a) the `error` band contains >= 95% true duplicates; (b) the `review` band captures `similar` pairs without swamping the report with `distinct` ones.
5. Edit `.vault-meta/tiling-thresholds.json`: set new `bands.error` and `bands.review`, set `calibrated: true`, set `calibration_pairs_labeled` to the label count.
6. Re-run lint. Report footer now says `calibrated: true`.

### Scale

- Cold-cache cost is O(N) POSTs to ollama. Warm-cache cost is O(N^2) cosines in pure Python.
- Helper prints a warning at > 500 pages and hard-fails (exit 4) at > 5000. Revisit the implementation (batching, vectorized cosine, or external tooling) before exceeding either limit.

### Lint report embed

```markdown
## Semantic Tiling
See [[tiling-report-YYYY-MM-DD]] for the full pair listing.
- Errors (>=0.90): N pairs
- Review (0.80-0.90): M pairs
- Calibrated: true|false
```

### Invariants

- Read-only. `tiling-check.py` never modifies wiki pages.
- No auto-merge. Duplicates are listed, never resolved.
- Cache is incremental and model-scoped. Unchanged pages are not re-embedded.
- Exit codes: `0` ok, `2` usage error, `3` cache corrupt, `4` scale hard-fail, `10` ollama unreachable, `11` model missing. Surface all of them; do not collapse into a single "unknown" bucket.

---

## TPL v2 Lint Checks

**Opt-in feature.** TPL v2 lint runs only when the vault has adopted the two-layer corpus (detected by presence of `wiki/_meta/journal-role-vocab.md` AND `wiki/papers/L1/` AND `wiki/papers/L2/`). Otherwise skip this section.

```bash
if [ -f wiki/_meta/journal-role-vocab.md ] && [ -d wiki/papers/L1 ] && [ -d wiki/papers/L2 ]; then
  TPL_V2=1
else
  TPL_V2=0
fi
```

Run TPL v2 checks **in addition to** the generic checks above, not in place of them.

### TPL-1. Frontmatter v2 vocab check

For every paper-analysis page under `wiki/papers/L1/**/*.md` and `wiki/papers/L2/**/*.md`:

| Required field | Allowed values | Severity |
|---|---|---|
| `journal_role` | `top_journal_exemplar` · `applied_flagship` · `technical_support` · `comparison_control` | error if missing or out-of-vocab |
| `ingest_depth` | `A_deep` · `B_medium` · `C_light` | error if missing or out-of-vocab |
| `subdomain_primary` | array of 1-2 entries from the 8 subdomain slugs | error if missing, empty, or contains out-of-vocab slug |
| `subdomain_secondary` | array of 0-3 entries from the 8 subdomain slugs (may be empty) | error only if a listed entry is out-of-vocab |
| `address` | `c-NNNNNN` (post-rollout) or `l-NNNNNN` (legacy) | error if missing on post-rollout page |

8 subdomain slugs (locked, `wiki/_meta/subdomain-vocab.md`): `integrated-energy-systems` · `power-systems` · `hydrogen-p2x` · `re-tech-resources` · `building-urban` · `energy-policy-economics` · `lca-sustainability` · `ai-data-driven`. Special slug `_cross` is allowed only as a folder name under `wiki/papers/L2/_cross/`, not as a `subdomain_primary` entry.

### TPL-2. Folder-placement audit

| Rule | Severity |
|---|---|
| `journal_role: top_journal_exemplar` page lives under `wiki/papers/L1/` (flat) | error if elsewhere |
| `journal_role: applied_flagship` page lives under `wiki/papers/L2/{subdomain_primary[0]}/` | error if elsewhere |
| Paper under `wiki/papers/L2/{slug}/` has `subdomain_primary[0] == {slug}` | error on mismatch |
| Paper under `wiki/papers/L2/_cross/` has `>= 3` entries in `subdomain_primary` | error if fewer |
| `journal_role: technical_support` page exists under `wiki/papers/**` at all | error (technical-support is manual bank-row only; no paper-analysis page) |

### TPL-3. No-pollution rule

Pages under the following paths must NOT cite L2 papers as **primary** evidence:

- `wiki/patterns/cross-cutting/intro/**`
- `wiki/patterns/cross-cutting/figure/**`
- `wiki/patterns/cross-cutting/discussion/**`
- `wiki/patterns/cross-cutting/archetype/**`
- `wiki/patterns/cross-cutting/contribution/**`
- `wiki/playbook/top-journal-craft/**`

Detection: for each pattern/playbook page in the above paths, scan wikilinks. Resolve each link to a paper-analysis page if possible. If the linked page has `journal_role: applied_flagship` AND the link appears in a section labeled "Primary evidence", "Supporting papers", or similar (not "Contrast", "Counterexample", "Supplementary"), flag as error.

L2 papers may appear in `patterns/comparisons/*` (by design), `patterns/cross-cutting/methods-recurrent/*` (as supplementary, must be labeled), `patterns/subdomain/*`, `patterns/bridges/*`, and `playbook/applied-paper-craft/*` · `playbook/upgrade-playbook/*` · `playbook/submission-tier-checklists/*`.

### TPL-4. Routing-matrix audit

For every L1 and L2-A paper-analysis page with a corresponding `.raw/papers/{KEY}/codex-receipt.json`, cross-check the receipt's `pages_updated[]` against the routing matrix in `wiki/_meta/routing-rules.md`.

| Source | Always-updates pages (must be in receipt) |
|---|---|
| L1-A | `papers/L1/{slug}.md`, `subdomains/{primary[0]}.md`, `subdomains/{primary[1]}.md` (if present), `log.md`, `hot.md`, `index.md` |
| L2-A | `papers/L2/{primary[0]}/{slug}.md`, `subdomains/{primary[0]}.md`, `subdomains/{primary[1]}.md` (if present), bank rows in `banks/{parameter,sensitivity,method}-bank/*`, `log.md`, `hot.md`, `index.md` |
| L2-B | `papers/L2/{primary[0]}/{slug}.md`, `log.md` |
| L2-C | `papers/L2/{primary[0]}/{slug}.md` (small card), `log.md` |

Missing always-updates entry → error. Missing conditional entry → informational.

### TPL-5. Page-size band check

Read each paper-analysis page's body size in bytes (excluding frontmatter):

| Page class | Body band | Action outside band |
|---|---|---|
| L1 A_deep | 18-35 KB | error if < 12 KB (likely template-only); warn if > 40 KB |
| L2-A | 12-18 KB | error if < 8 KB or > 22 KB |
| L2-B | 4-6 KB | error if < 2 KB (scope creep into C_light) or > 8 KB (scope creep into A_deep) |
| L2-C | < 500 B | error if > 1 KB (over-analyzed) |

### TPL-6. Orphan / under-fed bridges

Scan `wiki/bridges/*.md`. For each bridge page `{A}--{B}.md`:

1. Count papers across `wiki/papers/L1/**` and `wiki/papers/L2/**` whose `subdomain_primary ∪ subdomain_secondary` contains both `A` and `B`.
2. If count < 3 → error: orphan bridge (gate is 3 papers).
3. If count >= 3 but the bridge page's "Supporting papers" section lists fewer than `count`, warn: stale bridge content. Suggest re-running `scripts/generate-bridges.py`.

### TPL-7. Banned-word scan (anti-fluff)

For every page under `wiki/papers/**`, `wiki/patterns/**`, `wiki/playbook/**`:

Words requiring same-sentence concrete justification: `innovative · important · rigorous · comprehensive · novel · significant · high-impact · seminal · well-written · clear · elegant · groundbreaking`.

Detection: word appears AND the same sentence does not contain a concrete qualifier (one of: "in [aspect]", "for [audience/outcome]", "across [axis]", a parenthetical, or a colon-introduced specification). False-positive rate will be non-zero; lint posture is **warning**, not error.

### TPL-8. Three-label discipline

For every page under `wiki/papers/**`, `wiki/patterns/**`, `wiki/playbook/**`:

1. Each substantive claim paragraph SHOULD start with one of `Evidence:`, `Inference:`, or `Lesson:` (warning if many paragraphs in body have none).
2. Every line containing `Lesson:` MUST link to at least one `wiki/papers/L1/**` or `wiki/papers/L2/**` page (error if absent).
3. `Inference:` claims SHOULD declare confidence (high/medium/low). Warning if absent.

### TPL-9. Style: em dashes and double-hyphen punctuation

For every page under `wiki/**`:
- Em dash (Unicode U+2014) anywhere outside fenced code blocks: error.
- ` -- ` (double-hyphen as punctuation) outside fenced code blocks → error.
- Inside fenced code blocks: ignored.

### TPL-10. Stale bank rows

For every row in `wiki/banks/{parameter,sensitivity,method,case-study,figure,results}-bank/*.md`:

- Row should cite at least one wiki paper page or a Zotero key with the `tpl:role/technical_support` tag.
- Row missing both citations → error.
- Row cites a paper page that no longer exists → error (dead link).

### TPL-11. Over-analyzed L2 (promotion signal, not error)

If an L2-A paper page is cited 3+ times across `wiki/patterns/cross-cutting/**` pages: surface as **informational** under "Promotion candidates". Henry may want to re-ingest under the L1 contract per `depth-policy.md` rule "L2-A to L1 promotion".

### TPL-12. Crowded research-gap entries

For every `wiki/patterns/research-gap-map/*` entry: if it has >= 10 supporting papers, surface as **informational** (the gap is no longer a gap; consider retiring the entry or splitting it).

### TPL output section in the lint report

```markdown
## TPL v2

### Errors
- [[2024-AE-h2-balancing]]: missing `subdomain_primary`.
- [[2024-Joule-electrolyzer-merit-order]]: page lives at `papers/L1/...` but `journal_role: applied_flagship`. Move to `papers/L2/hydrogen-p2x/` or fix the role.
- [[patterns/cross-cutting/intro/empirical-anchor]]: cites L2 paper [[2023-AE-pv-cf-china]] as primary evidence. Move to `patterns/comparisons/` or `patterns/cross-cutting/methods-recurrent/`.
- [[banks/parameter-bank/electrolyzer-capex]]: row "ALK 600 EUR/kW" missing paper citation.

### Warnings
- [[2024-NE-flexibility-options]]: uses "rigorous" without same-sentence concrete justification.
- [[bridges/hydrogen-p2x--power-systems]]: 5 papers detected, but "Supporting papers" section lists 3. Re-run scripts/generate-bridges.py.

### Informational
- Promotion candidate: [[2023-AE-hub-design]] cited 4× across patterns/cross-cutting. Eligible for L2-A → L1 promotion.
- Crowded gap: [[patterns/research-gap-map/cost-trajectory-treatment]] has 12 supporting papers. Consider retirement.

### Stats
- L1 papers checked: 22 (22 pass, 0 errors)
- L2 papers checked: 0 (pilot pending)
- Orphan bridges: 0
- Banned-word warnings: N
- No-pollution violations: M
```

---

## Before Auto-Fixing

Always show the lint report first. Ask: "Should I fix these automatically, or do you want to review each one?"

Safe to auto-fix:
- Adding missing frontmatter fields with placeholder values
- Creating stub pages for missing entities
- Adding wikilinks for unlinked mentions

Needs review before fixing:
- Deleting orphan pages (they might be intentionally isolated)
- Resolving contradictions (requires human judgment)
- Merging duplicate pages
- TPL-2 folder-placement errors (a move can break wikilinks; ask first)
- TPL-3 no-pollution violations (the link is real evidence; the question is *where it should live*)
- TPL-11 promotion candidates (only Henry decides whether to re-ingest)
