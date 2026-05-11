---
name: wiki-ingest
description: "Ingest sources into the Obsidian wiki vault. Reads a source, extracts entities and concepts, creates or updates wiki pages, cross-references, and logs the operation. Supports files, URLs, and batch mode. Triggers on: ingest, process this source, add this to the wiki, read and file this, batch ingest, ingest all of these, ingest this url."
---

# wiki-ingest: Source Ingestion

Read the source. Write the wiki. Cross-reference everything. A single source typically touches 8-15 wiki pages.

**Syntax standard**: Write all Obsidian Markdown using proper Obsidian Flavored Markdown. Wikilinks as `[[Note Name]]`, callouts as `> [!type] Title`, embeds as `![[file]]`, properties as YAML frontmatter. If the kepano/obsidian-skills plugin is installed, prefer its canonical obsidian-markdown skill for Obsidian syntax reference. Otherwise, follow the guidance in this skill.

---

## Delta Tracking

Before ingesting any file, check `.raw/.manifest.json` to avoid re-processing unchanged sources.

```bash
# Check if manifest exists
[ -f .raw/.manifest.json ] && echo "exists" || echo "no manifest yet"
```

**Manifest format** (create if missing):
```json
{
  "sources": {
    ".raw/articles/article-slug-2026-04-08.md": {
      "hash": "abc123",
      "ingested_at": "2026-04-08",
      "pages_created": ["wiki/sources/article-slug.md", "wiki/entities/Person.md"],
      "pages_updated": ["wiki/index.md"]
    }
  }
}
```

**Before ingesting a file:**
1. Compute a hash: `md5sum [file] | cut -d' ' -f1` (or `sha256sum` on Linux).
2. Check if the path exists in `.manifest.json` with the same hash.
3. If hash matches, skip. Report: "Already ingested (unchanged). Use `force` to re-ingest."
4. If missing or hash differs, proceed with ingest.

**After ingesting a file:**
1. Record `{hash, ingested_at, pages_created, pages_updated}` in `.manifest.json`.
2. Write the updated manifest back.

Skip delta checking if the user says "force ingest" or "re-ingest".

---

## URL Ingestion

Trigger: user passes a URL starting with `https://`.

Steps:

1. **Fetch** the page using WebFetch.
2. **Clean** (optional): if `defuddle` is available (`which defuddle 2>/dev/null`), run `defuddle [url]` to strip ads, nav, and clutter. Typically saves 40-60% tokens. Fall back to raw WebFetch output if not installed.
3. **Derive slug** from the URL path (last segment, lowercased, spaces→hyphens, strip query strings).
4. **Save** to `.raw/articles/[slug]-[YYYY-MM-DD].md` with a frontmatter header:
   ```markdown
   ---
   source_url: [url]
   fetched: [YYYY-MM-DD]
   ---
   ```
5. Proceed with **Single Source Ingest** starting at step 2 (file is now in `.raw/`).

---

## Image / Vision Ingestion

Trigger: user passes an image file path (`.png`, `.jpg`, `.jpeg`, `.gif`, `.webp`, `.svg`, `.avif`).

Steps:

1. **Read** the image file using the Read tool. Claude can process images natively.
2. **Describe** the image contents: extract all text (OCR), identify key concepts, entities, diagrams, and data visible in the image.
3. **Save** the description to `.raw/images/[slug]-[YYYY-MM-DD].md`:
   ```markdown
   ---
   source_type: image
   original_file: [original path]
   fetched: YYYY-MM-DD
   ---
   # Image: [slug]

   [Full description of image contents, transcribed text, entities visible, etc.]
   ```
4. Copy the image to `_attachments/images/[slug].[ext]` if it's not already in the vault.
5. Proceed with **Single Source Ingest** on the saved description file.

Use cases: whiteboard photos, screenshots, diagrams, infographics, document scans.

---

## Single Source Ingest

Trigger: user drops a file into `.raw/` or pastes content.

Steps:

1. **Read** the source completely. Do not skim.
2. **Discuss** key takeaways with the user. Ask: "What should I emphasize? How granular?" Skip this if the user says "just ingest it."
3. **Create** source summary in `wiki/sources/`. Use the source frontmatter schema from `references/frontmatter.md`. Assign an address per the **Address Assignment** section below.
4. **Create or update** entity pages for every person, org, product, and repo mentioned. One page per entity. Assign addresses to new entity pages.
5. **Create or update** concept pages for significant ideas and frameworks. Assign addresses to new concept pages.
6. **Update** relevant domain page(s) and their `_index.md` sub-indexes.
7. **Update** `wiki/overview.md` if the big picture changed.
8. **Update** `wiki/index.md`. Add entries for all new pages.
9. **Update** `wiki/hot.md` with this ingest's context.
10. **Append** to `wiki/log.md` (new entries at the TOP):
    ```markdown
    ## [YYYY-MM-DD] ingest | Source Title
    - Source: `.raw/articles/filename.md`
    - Summary: [[Source Title]]
    - Pages created: [[Page 1]], [[Page 2]]
    - Pages updated: [[Page 3]], [[Page 4]]
    - Key insight: One sentence on what is new.
    ```
11. **Check for contradictions.** If new info conflicts with existing pages, add `> [!contradiction]` callouts on both pages.

---

## Batch Ingest

Trigger: user drops multiple files or says "ingest all of these."

Steps:

1. List all files to process. Confirm with user before starting.
2. Process each source following the single ingest flow. Defer cross-referencing between sources until step 3.
3. After all sources: do a cross-reference pass. Look for connections between the newly ingested sources.
4. Update index, hot cache, and log once at the end (not per-source).
5. Report: "Processed N sources. Created X pages, updated Y pages. Here are the key connections I found."

Batch ingest is less interactive. For 30+ sources, expect significant processing time. Check in with the user after every 10 sources.

---

## Context Window Discipline

Token budget matters. Follow these rules during ingest:

- Read `wiki/hot.md` first. If it contains the relevant context, don't re-read full pages.
- Read `wiki/index.md` to find existing pages before creating new ones.
- Read only 3-5 existing pages per ingest. If you need 10+, you are reading too broadly.
- Use PATCH for surgical edits. Never re-read an entire file just to update one field.
- Keep wiki pages short. 100-300 lines max. If a page grows beyond 300 lines, split it.
- Use search (`/search/simple/`) to find specific content without reading full pages.

---

## Contradictions

> [!note] Custom callout dependency
> The `[!contradiction]` callout type used below is a **custom callout** defined in `.obsidian/snippets/vault-colors.css` (auto-installed by `/wiki` scaffold). It renders with reddish-brown styling and an alert-triangle icon when the snippet is enabled. If the snippet is missing, Obsidian falls back to default callout styling, so the page still works without the visual flourish. See [[skills/wiki/references/css-snippets.md]] for the four custom callouts (`contradiction`, `gap`, `key-insight`, `stale`).

When new info contradicts an existing wiki page:

On the existing page, add:
```markdown
> [!contradiction] Conflict with [[New Source]]
> [[Existing Page]] claims X. [[New Source]] says Y.
> Needs resolution. Check dates, context, and primary sources.
```

On the new source summary, reference it:
```markdown
> [!contradiction] Contradicts [[Existing Page]]
> This source says Y, but existing wiki says X. See [[Existing Page]] for details.
```

Do not silently overwrite old claims. Flag and let the user decide.

---

## What Not to Do

- **Source files under `.raw/` are immutable.** Do not modify the files that users drop there (articles, transcripts, images). The `.raw/.manifest.json` delta tracker and its `address_map` (DragonScale Mechanism 2) are the only files under `.raw/` that `wiki-ingest` itself maintains. Treat every other file under `.raw/` as read-only source content.
- Do not create duplicate pages. Always check the index and search before creating.
- Do not skip the log entry. Every ingest must be recorded.
- Do not skip the hot cache update. It is what keeps future sessions fast.

---

## TPL Mode: Top Paper Lab v2 paper-package ingest

**Trigger**: source path is `.raw/papers/{ZOTERO_KEY}/`, or the user passes a Zotero key (8 uppercase alphanumeric chars) with the word "ingest", or `wiki/_meta/journal-role-vocab.md` exists. When triggered, this mode REPLACES "Single Source Ingest" above; do not run the generic source flow on a TPL paper.

### Vault detection

```bash
if [ -f wiki/_meta/journal-role-vocab.md ] && [ -d wiki/papers/L1 ] && [ -d wiki/papers/L2 ]; then
  TPL_V2=1
else
  TPL_V2=0
fi
```

If `TPL_V2=0`, fall back to generic single-source ingest. Everything below assumes `TPL_V2=1`.

### Step 1. Classify the paper

Before touching any wiki file, determine `(journal_role, ingest_depth, subdomain_primary[], subdomain_secondary[])`.

1. **Read `.raw/papers/{KEY}/metadata.json`** for journal + title + DOI.
2. **Read `wiki/_meta/journal-role-vocab.md`** journal lock list to assign `journal_role`. Defaults:
   - Nature / NE / Joule / NC / NCC / Nature Sustainability / One Earth / EES / Science / Sci Adv / PNAS → `top_journal_exemplar`
   - Applied Energy / AiAE / ECM / RSER / RE / Energy & Buildings / Energy / Energy Policy / ERSS / ESR → `applied_flagship`
   - IJHE / J. Energy Storage / Solar Energy / Wind Energy / J. Power Sources / IEEE Trans → `technical_support` (manual-only, abort here)
3. **Read `wiki/_meta/subdomain-vocab.md`** to assign 1-2 `subdomain_primary` and 0-3 `subdomain_secondary` from the 8 locked slugs.
4. **If `journal_role == applied_flagship`, choose `ingest_depth`** per `wiki/_meta/depth-policy.md`:
   - 2+ "yes" on (direct method reuse / parameter or case anchor / subdomain coverage need) → `A_deep`
   - 1 "yes" → `B_medium`
   - 0 "yes" → `C_light`
   - Default if uncertain → `B_medium`.
5. **If `journal_role == top_journal_exemplar`** → `ingest_depth` is always `A_deep` (locked by depth-policy).
6. **If `journal_role == technical_support`** → do NOT generate a paper-analysis page. Instead, append a row to the relevant `wiki/banks/*` page with the Zotero citation and stop. Document in `log.md`.

Stop and ask Henry only if the classification is genuinely ambiguous (e.g., Cell Reports Physical Science borderline cases). Otherwise proceed with the default.

### Step 2. Allocate the address

```bash
ADDR=$(./scripts/allocate-address.sh)   # e.g. c-000026
```

Single-writer policy: only this session calls the allocator. Codex never allocates.

### Step 3. Dispatch to the correct codex runner

| `(journal_role, ingest_depth)` | Runner | Args |
|---|---|---|
| `top_journal_exemplar, A_deep` | `scripts/codex-ingest-paper.sh` | `<KEY> <ADDR> [SLUG_HINT]` |
| `applied_flagship, A_deep` | `scripts/codex-ingest-paper-L2.sh` | `<KEY> <ADDR> <SLUG_HINT> A_deep <PRIMARY_SUBDOMAIN>` |
| `applied_flagship, B_medium` | `scripts/codex-ingest-paper-L2.sh` | `<KEY> <ADDR> <SLUG_HINT> B_medium <PRIMARY_SUBDOMAIN>` |
| `applied_flagship, C_light` | `scripts/codex-ingest-paper-L2.sh` | `<KEY> <ADDR> <SLUG_HINT> C_light <PRIMARY_SUBDOMAIN>` |

`PRIMARY_SUBDOMAIN` is `subdomain_primary[0]` (the first entry). For L1 papers, the runner does not need it; the page lands flat in `wiki/papers/L1/`.

The runner does its own arg validation; it will reject malformed addresses or non-vocab subdomain slugs.

### Step 4. Verify the codex receipt

After the runner completes, read `.raw/papers/{KEY}/codex-receipt.json`. Required fields:

- `zotero_key`, `address`, `wiki_page`, `journal_role`, `ingest_depth`, `subdomain_primary`, `pages_updated[]`, `fulltext_source`.

Checks:

1. **Page exists at the expected path**:
   - L1 → `wiki/papers/L1/{year}-{journal-short}-{slug}.md`
   - L2 → `wiki/papers/L2/{subdomain_primary[0]}/{year}-{journal-short}-{slug}.md`
2. **Frontmatter v2 complete**: `journal_role`, `ingest_depth`, `subdomain_primary`, `address` all set and matching the dispatched values.
3. **Page size within band**:
   - L1 A_deep: 18-35 KB
   - L2-A: 12-18 KB
   - L2-B: 4-6 KB
   - L2-C: < 500 B body (excluding frontmatter)
4. **Three-label discipline**: substantive claims tagged with `Evidence:`, `Inference:`, or `Lesson:` (banned-word + label discipline in CLAUDE.md).
5. **`bank-candidates.md` present for L2-A** (parameter / sensitivity / method rows the orchestrating session merges into `wiki/banks/*`).

If any check fails, do NOT integrate. Write `.raw/papers/{KEY}/integration-blocked.md` describing the failure and stop.

### Step 5. Integrate (orchestrator responsibilities only; codex never touches these)

1. **Update manifest CSV** `.raw/zotero_manifest/top_paper_lab_manifest.csv`: set `ingest_status=ingested`, `review_status=unreviewed`, backfill `journal_role`, `ingest_depth`, `subdomain_primary` (semicolon-joined), `subdomain_secondary` (semicolon-joined), `use_tags`, `notes` for this row.
2. **Update `wiki/index.md`** with one bullet under "Papers ingested": `- [[year-journal-slug]] : one-line hook (L1 | L2-A | L2-B | L2-C)`.
3. **Update `wiki/hot.md`** with the most-recent-ingest pointer (paper title, slug, address, archetype tag, two-sentence takeaway).
4. **Append `wiki/log.md`** at the TOP (new entries top): `## [YYYY-MM-DD] ingest | {paper short title} ({journal_role} {ingest_depth})` with the same fields as the generic log entry plus `journal_role`, `ingest_depth`, `subdomain_primary`.
5. **Merge bank rows from `.raw/papers/{KEY}/bank-candidates.md`** (L2-A only) into the relevant `wiki/banks/parameter-bank/*.md`, `wiki/banks/sensitivity-bank/*.md`, `wiki/banks/method-bank/*.md` pages. Cite the new paper page as supporting evidence; cite the Zotero key.
6. **Regenerate hub and bridge pages** (preserves Henry-note blocks):
   ```bash
   python3 scripts/subdomain-bridge-stats.py
   python3 scripts/generate-subdomain-hubs.py
   python3 scripts/generate-bridges.py
   ```
7. **Bridge emergence check**: after regeneration, any new bridge page that just crossed the 3-paper gate gets a one-line log mention.

### Step 6. Cross-page synthesis gate (paper count threshold)

Until the lab has 10 L1 paper-analysis pages, the wiki only contains singletons. **Do not diffuse-update pattern pages on each ingest before paper 10.** Pattern pages emerge bottom-up from the first `/wiki-fold` auto-synthesis (triggered at log size = 8 ingest entries, k=3).

After paper 10, on each ingest, additionally update **only the pattern pages this paper genuinely informs** (not all). Each lesson added to a pattern page must back-link to the originating `wiki/papers/L1/*.md` or `wiki/papers/L2/*/*.md` page. Routing matrix is `wiki/_meta/routing-rules.md`.

### Step 7. No-pollution rule (orchestrator-enforced at integration time)

When adding a new entry to a pattern or playbook page, refuse the add if the rule below is violated:

| Target page | Allowed primary evidence | Allowed supplementary evidence |
|---|---|---|
| `patterns/cross-cutting/{intro,figure,discussion,archetype,contribution}/*` | L1 only | none |
| `playbook/top-journal-craft/*` | L1 only | none |
| `patterns/cross-cutting/methods-recurrent/*` | L1 + L2 | (n/a) |
| `patterns/comparisons/*` | L1 + L2 (by design) | (n/a) |
| `patterns/subdomain/{slug}/*` | L1 + L2 | (n/a) |
| `patterns/bridges/{A}--{B}/*` | L1 + L2 | (n/a) |
| `playbook/applied-paper-craft/*`, `playbook/upgrade-playbook/*`, `playbook/submission-tier-checklists/*` | L2 (primary) + L1 (contrast) | (n/a) |

If an integration step would violate this rule, write the new evidence under `patterns/comparisons/*` or `patterns/cross-cutting/methods-recurrent/*` instead, and note in the log why the proposed location was redirected.

### Step 8. Style and discipline (re-stated, lint-enforced)

- **Banned-word scan**: `innovative · important · rigorous · comprehensive · novel · significant · high-impact · seminal · well-written · clear · elegant · groundbreaking` may appear only with a same-sentence concrete justification. See CLAUDE.md "Anti-fluff rule".
- **No em dashes (U+2014)** and no `--` as punctuation.
- **Verify before quoting**: any LLM-generated claim about a paper must be checked against the actual paper text before promotion from `papers/` to `patterns/` or `playbook/`.
- **Zotero is source of truth**: do not duplicate full Zotero fields into wiki YAML beyond the cached subset (`zotero_key`, `title`, `journal`, `year`, `doi`, `topic`, `paper_type`, `main_contribution`, `method_type`, `data_assets`, `relevance_to_my_research`, `ingest_status`, `address`).

### TPL mode: what the orchestrator never delegates

| Delegated to codex runner | Kept in the orchestrating session |
|---|---|
| Reading the paper + composing `wiki/papers/L1/*.md` or `wiki/papers/L2/*/*.md` | Address allocation |
| Writing stub files in `.raw/papers/{KEY}/` | `manifest.csv` row update |
| Writing `bank-candidates.md` (L2-A) | Merging `bank-candidates.md` rows into `wiki/banks/*` |
| Self-checking page size / banned words / section count | `index.md`, `hot.md`, `log.md` integration |
| Emitting the JSON receipt | Hub + bridge regeneration |
| | Routing-matrix enforcement and no-pollution rule |
| | Pattern + playbook updates (post-paper-10 gate) |

---

## Address Assignment (DragonScale Mechanism 2 MVP)

**Opt-in feature**. DragonScale address assignment runs only if `scripts/allocate-address.sh` is present AND `.vault-meta/` exists. Otherwise, skip this entire section and proceed with ingest normally.

**Feature detection (run at start of every ingest)**:

```bash
if [ -x ./scripts/allocate-address.sh ] && [ -d ./.vault-meta ]; then
  DRAGONSCALE_ADDRESSES=1
else
  DRAGONSCALE_ADDRESSES=0
fi
```

When `DRAGONSCALE_ADDRESSES=0`, pages are created without an `address:` frontmatter field, and `wiki-lint`'s Address Validation section is skipped entirely (missing addresses are not flagged in any severity). This preserves default plugin behavior for vaults that have not adopted DragonScale.

When `DRAGONSCALE_ADDRESSES=1`, proceed with the rest of this section.

---

Every **newly created non-meta wiki page** gets a stable address in its frontmatter:

```yaml
address: c-000042
```

Format: `c-<6-digit-counter>`. The `c-` prefix stands for "creation-order counter." Zero-padded.

Rollout baseline: **2026-04-23** (Phase 2 ship date). Pages with `created:` >= this date are post-rollout and MUST have an address (unless excluded below). Pages with `created:` earlier are legacy-exempt until a deliberate backfill pass assigns `l-NNNNNN` addresses.

### Required tool: `scripts/allocate-address.sh`

Address allocation is delegated to an atomic Bash helper. The helper uses `flock` on `.vault-meta/.address.lock` to prevent read-use-increment races and recovers the counter by scanning existing frontmatter if the counter file is missing.

```bash
ADDR=$(./scripts/allocate-address.sh)
# ADDR is now e.g. "c-000042"; counter is already incremented
```

**CRITICAL**: never use the Write or Edit tool on `.vault-meta/address-counter.txt`. That would fire the PostToolUse hook, which runs `git add wiki/ .raw/` and can accidentally commit unrelated pending wiki changes under a generic message. Counter mutation is **only** permitted through the helper script (Bash tool).

### Helper modes

- `./scripts/allocate-address.sh` — atomically reserves and returns the next address.
- `./scripts/allocate-address.sh --peek` — prints the next value without reserving (safe, read-only).
- `./scripts/allocate-address.sh --rebuild` — recomputes the counter from the highest observed `c-NNNNNN` in existing frontmatter. Never resets to 1 silently if pages already have addresses. Run this if the counter file is suspected corrupt.

### Assignment procedure (per new page)

1. Before writing a new non-meta page, call `./scripts/allocate-address.sh` and capture the output.
2. Include `address: c-XXXXXX` in the page's frontmatter.
3. Record the path-to-address mapping in `.raw/.manifest.json` under a new top-level key `address_map` (see schema below).

### `address_map` in `.raw/.manifest.json`

```json
{
  "sources": { ... },
  "address_map": {
    "wiki/concepts/Example.md": "c-000042",
    "wiki/entities/Another.md": "c-000043"
  }
}
```

On re-ingest of the same source (whether by `--force` or a changed hash), always consult `address_map` first. If the target page path has a prior address, REUSE it. Do not allocate a new one.

On a page rename, the skill must update the `address_map` key (old path -> new path) while preserving the address value.

### Exclusions (do NOT assign an address to)

- Meta files: `_index.md`, `index.md`, `log.md`, `hot.md`, `overview.md`, `dashboard.md`, `dashboard.base`, `Wiki Map.md`, `getting-started.md`.
- Fold pages under `wiki/folds/` (they use their own deterministic `fold_id`).
- Pre-rollout legacy pages (`created:` < 2026-04-23). Legacy pages get `l-NNNNNN` addresses only via a deliberate backfill operation.

### Idempotency rules

- If a page being (re)written already has an `address:` field in its current content, REUSE it. Do not allocate a new one.
- If a source is re-ingested and `address_map` has a mapping for the target path, reuse that mapping.
- If the source has been ingested before AND the target page has no address AND the page `created:` date is post-rollout, allocate an address and record it. This covers the case where an older ingest produced a page before Phase 2 rollout; the rollout cutoff still applies (pages dated pre-2026-04-23 stay legacy).

### Concurrency policy

- **Single-writer only** in Phase 2. Do not run parallel ingests from multiple Claude sessions or sub-agents that assign addresses. The `flock` in the helper prevents counter corruption but does not serialize page writes themselves.
- Sub-agents (codex, general-purpose) that are dispatched for research or review MUST NOT call the allocator. They are read-only in this respect.
- Multi-writer support is a deferred feature.

### Batch ingest

Assign addresses sequentially during single-source-ingest for each source. Do not pre-reserve a block of counter values. The helper is cheap (one lock, one integer read/write).
