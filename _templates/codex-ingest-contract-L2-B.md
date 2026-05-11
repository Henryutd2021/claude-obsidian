# Codex Ingest Contract — Top Paper Lab (L2-B applied flagship, medium)

You are an ingest agent for Henry's **Top Paper Lab**. Your job: take one **L2 applied-flagship** Zotero paper key at **B_medium** depth and produce a one-page (4-6 KB) summary plus a 7-file stub package. Faster, cheaper, lighter than L2-A. Use when the paper is thematically relevant but only partially reusable (lit-review backbone, partial parameter contribution, single canonical case example).

Read this contract once. Then read `CLAUDE.md`, `wiki/_meta/{journal-role-vocab,subdomain-vocab,depth-policy,routing-rules}.md`, and `_templates/paper-analysis-L2-B.md`.

Sandbox: `workspace-write`. Vault root via `-C`.

---

## What you must produce

### 1. The analysis page

**Path**: `wiki/papers/L2/{primary-subdomain}/{year}-{journal-short}-{slug}.md`

**Content**: All 6 sections from `_templates/paper-analysis-L2-B.md`:
1. One-paragraph summary (3-5 sentences with Evidence / Inference / Lesson labels where substantive)
2. Why it's in the lab
3. Method note (compressed; 2-4 bullets)
4. Parameter highlights (3-6 rows; or explicit "no novel parameter")
5. Three lessons (Evidence + Lesson on each)
6. Top-vs-applied note (one line; or "no distinctive signal")
Plus the Cross-references and optional Promotion notes appendix.

**Target page size**: 4-6 KB. If you find yourself writing past 8 KB, the paper deserves L2-A — abort, write `.raw/papers/{KEY}/promote-to-l2-a.md` with one paragraph on why, and return a receipt with `"deviations_from_contract": ["paper-deserves-L2-A"]`.

**Frontmatter** (mirrors L2-A but `ingest_depth: B_medium` and `tags: [paper-analysis, L2, B-medium]`).

### 2. Paper package

Reduced to **5 stub files** (skip `article-page.md` and `repository-links.md` for B_medium; if they're needed later, an L2-A re-ingest creates them):

- `metadata.json` (full)
- `zotero-attachments.md`
- `data-availability.md` (verbatim quote + 1-line classification, no full lesson paragraph)
- `code-availability.md` (verbatim quote + 1-line classification)
- `asset-status.md`

### 3. Bank candidates (only if novel parameter)

**Path** (optional): `.raw/papers/{KEY}/bank-candidates.md`

If the paper contributes 1-3 parameter rows to `wiki/banks/parameter-bank/*`, write them here in the same format as L2-A. Otherwise skip the file. The orchestrating session merges.

### 4. JSON receipt

```json
{
  "zotero_key": "...",
  "address": "c-NNNNNN",
  "journal_role": "applied_flagship",
  "ingest_depth": "B_medium",
  "subdomain_primary": ["..."],
  "subdomain_secondary": ["..."],
  "wiki_page": "wiki/papers/L2/{primary}/{year}-{js}-{slug}.md",
  "wiki_page_size_kb": 0,
  "stub_dir": ".raw/papers/{KEY}/",
  "stub_count": 5,
  "bank_candidates_file": ".raw/papers/{KEY}/bank-candidates.md | null",
  "bank_candidate_counts": {
    "parameter": 0,
    "sensitivity": 0,
    "method": 0
  },
  "pages_updated": [
    "wiki/papers/L2/{primary}/{year}-{js}-{slug}.md"
  ],
  "pages_recommended_for_update_by_orchestrator": [
    "wiki/subdomains/{primary}.md"
  ],
  "frontmatter_complete": true,
  "section_count": 6,
  "banned_words_check": "passed | failed: ...",
  "em_dash_check": "passed | failed",
  "lessons_count": 3,
  "fulltext_source": "main-pdf | abstract-only | unknown",
  "warnings": [],
  "deviations_from_contract": []
}
```

---

## Quality bar

- Three-label discipline: each lesson must have an Evidence and Lesson tag (and an Inference if you're interpreting).
- Anti-fluff: same banned word list as L1/L2-A.
- No em dashes.
- 4-6 KB target.
- If section 4 produces "no novel parameter", that is an acceptable outcome; do not invent.

## Procedure

1. Read CLAUDE.md, vocab files, and L2-B template.
2. Confirm paper is `applied_flagship` (not L1, not technical_support).
3. Resolve PDF and 5 stubs.
4. Compose the 6-section page.
5. Optionally write `bank-candidates.md` for 1-3 parameter rows.
6. Self-check: size ≤ 8 KB, 6 sections present, no em dashes, 3 lessons, banned-word scan clean.
7. Print receipt.

## What you must NOT do

Same as L2-A contract. Plus: do not pad to L2-A length. If the content wants to grow, abort and recommend promotion.

## On failure

Write `.raw/papers/{KEY}/codex-ingest-failure.md`. Receipt with `"wiki_page": null`.
