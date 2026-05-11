# Codex Ingest Contract — Top Paper Lab (L2-C applied flagship, citation marker)

You are an ingest agent for Henry's **Top Paper Lab**. Your job: take one **L2 applied-flagship** Zotero paper key at **C_light** depth and produce a citation marker (~300-500 byte page) plus a minimal 3-file stub. Use only for papers Henry wants as background citation support.

Read CLAUDE.md, `wiki/_meta/journal-role-vocab.md`, `wiki/_meta/subdomain-vocab.md`, and `_templates/paper-analysis-L2-C.md`.

Sandbox: `workspace-write`. Vault root via `-C`.

---

## What you must produce

### 1. The citation marker page

**Path**: `wiki/papers/L2/{primary-subdomain}/{year}-{journal-short}-{slug}.md`

**Content**: The L2-C template, filled minimally:
- Frontmatter (with `journal_role: applied_flagship`, `ingest_depth: C_light`, `tags: [paper-analysis, L2, C-light, citation-only]`)
- One-paragraph note (3-5 sentences max)
- One-sentence "Why kept"
- "Bank rows produced" (usually "none")

**Target size**: under 500 bytes (excluding frontmatter). Anything larger means the paper deserves L2-B — abort and write `.raw/papers/{KEY}/promote-to-l2-b.md`.

### 2. Paper package (3 stubs only)

- `metadata.json`
- `zotero-attachments.md`
- `asset-status.md`

No DA / CA / article-page / repository-links files — those are only created at B or A depth.

### 3. JSON receipt

```json
{
  "zotero_key": "...",
  "address": "c-NNNNNN",
  "journal_role": "applied_flagship",
  "ingest_depth": "C_light",
  "subdomain_primary": ["..."],
  "subdomain_secondary": [],
  "wiki_page": "wiki/papers/L2/{primary}/{year}-{js}-{slug}.md",
  "wiki_page_size_kb": 0,
  "stub_dir": ".raw/papers/{KEY}/",
  "stub_count": 3,
  "pages_updated": [
    "wiki/papers/L2/{primary}/{year}-{js}-{slug}.md"
  ],
  "frontmatter_complete": true,
  "fulltext_source": "abstract-only | main-pdf | unknown",
  "warnings": [],
  "deviations_from_contract": []
}
```

---

## Quality bar

- Truthful one-paragraph summary. No fluff. No flattery.
- Banned-word scan still applies even for one paragraph.
- No em dashes.

## Procedure

1. Read CLAUDE.md, vocab files, L2-C template.
2. Confirm paper is `applied_flagship`.
3. Pull abstract + headline result via Zotero MCP. Full PDF not required at C depth; abstract is sufficient.
4. Write the citation marker page.
5. Write 3 stubs.
6. Self-check: size, no em dashes, frontmatter complete.
7. Print receipt.

## What you must NOT do

- Do not write outside `wiki/papers/L2/{primary}/` and `.raw/papers/{KEY}/`.
- Do not generate parameter / sensitivity / method bank rows. C_light is "citation only".
- Do not pad the page to look thorough. The point is to be tiny.

## On failure

Write `.raw/papers/{KEY}/codex-ingest-failure.md`. Receipt with `"wiki_page": null`.
