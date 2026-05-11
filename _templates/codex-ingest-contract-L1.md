# Codex Ingest Contract — Top Paper Lab

You are an ingest agent for Henry's personal **Top Paper Lab** (TPL). Your job: take one Zotero paper key and produce a deep, structured reverse-engineering analysis in the TPL vault, plus a 7-file lightweight stub package. You receive (via prompt) the Zotero key, a pre-allocated page address, and a slug hint.

This contract is the single source of truth for what "done" means. Read it once at the top of your run. Then read `CLAUDE.md` (TPL constitution) and `_templates/paper-analysis.md` (the 18-section template) before you start writing.

You operate inside the vault root passed via `-C`. Sandbox mode is `workspace-write`.

---

## What you must produce

### 1. The analysis page

**Path**: `wiki/papers/{year}-{journal-short}-{slug}.md`

- `{year}` = 4-digit publication year (from Zotero metadata)
- `{journal-short}` = `NE` (Nature Energy), `J` (Joule), `NC` (Nature Communications), `N` (Nature), `NSus` (Nature Sustainability), `NCC` (Nature Climate Change), `OE` (One Earth). If the journal is not in this list, use a 2-4 letter slug you derive (e.g. `EES` for Energy & Environmental Science).
- `{slug}` = lowercase kebab-case, 3-6 words capturing the headline (`china-clean-h2-hta`, `space-solar-europe`, etc.). The slug hint passed via prompt is a suggestion; you may refine.

**Content**: All 18 sections from `_templates/paper-analysis.md`. Do not skip any section. If a section does not apply to this paper's archetype (e.g. "experimental controls" for a modeling paper), write "N/A for this archetype" plus one sentence justifying.

**Required appendix** (after section 18, before end of file): the `Pass-2 follow-up (deferred)` stub and a `## Cross-references` section. The Cross-references section MUST list:
- the Zotero parent key and main PDF attachment key (use the values you resolved during ingest)
- wikilinks to the 7 stub files in `.raw/papers/{KEY}/` (at minimum: `asset-status`, `data-availability`, `code-availability`)
- a `Related papers in this lab` bullet listing wikilinks to ANY existing `wiki/papers/*.md` that share a Zotero-traceable citation, a method family, a journal, or a case region. Scan `wiki/index.md`'s "Papers ingested" section before composing.
- a `Pattern pages it will inform after paper 10` placeholder bullet listing 2-4 candidate `patterns/*/...` slugs the analysis would inform
- a `Playbook pages it will inform after paper 20` placeholder bullet with 1-3 candidate `playbook/*` slugs

If the analysis explicitly contradicts an existing wiki/papers/*.md page on a substantive Inference or Result claim, add a `> [!contradiction]` callout in the Cross-references section naming the other paper and the disagreement in one sentence. The orchestrating session will also add a reciprocal callout on the other page.

**Frontmatter** (YAML, before the first heading):

```yaml
---
zotero_key: <KEY>
title: "<exact title from Zotero, quoted>"
journal: "<exact journal name>"
year: <integer>
doi: "<DOI as string>"
topic: [<lowercase-kebab tags relevant to Henry's scope>]
paper_type: [<modeling | TEA | scenario-analysis | experimental | data-driven | review | perspective | optimization | integrated-assessment | empirical-econometric | policy-analysis>]
main_contribution: [<system-boundary-expansion | method-novelty | data-novelty | counterintuitive-result | comprehensive-assessment | policy-relevance | mechanism-clarification | sectoral-coverage>]
method_type: [<framework names like TIMES-VEDA, GAMS, GTAP, REMIND, MESSAGE, GCAM, plant-by-plant-optimization, Monte-Carlo-TEA, LCA, etc.>]
data_assets:
  main_pdf: <true|false based on Zotero children>
  supplementary: <true|false>
  source_data: <true|false>
  data_statement: <true|false based on whether you extracted it>
  code_statement: <true|false>
  code_repository: <true|false based on actual repo link>
relevance_to_my_research: <high | medium | low based on TPL scope: renewable energy integration, wind-solar-hydrogen, green-hydrogen TEA, energy system optimization, building energy/decarbonization, energy policy/cost>
ingest_status: reviewed
address: <ADDRESS passed in prompt, e.g. c-000004>
created: <today's date as YYYY-MM-DD>
tags:
  - paper-analysis
---
```

The `address` field MUST be exactly what was passed to you in the prompt. You do NOT allocate addresses. The vault has a single-writer counter at `scripts/allocate-address.sh`; under no circumstances run it.

### 2. Paper package (7 stub files)

**Directory**: `.raw/papers/{KEY}/`

Files (all text-only, total directory size should stay under ~50 KB):

| File | Content |
|---|---|
| `metadata.json` | Cached Zotero metadata subset (key, title, authors, journal, volume, issue, pages, year, doi, url, item_type, tags, collections count, child_attachments list with their keys, child_notes list, topic tags, paper_type tags, method_type tags, main_contribution tags, relevance_to_my_research, tpl_address, fetched_at). |
| `zotero-attachments.md` | Markdown pointer table to Zotero attachments by key + type + filename + Zotero storage path. Plus a "What is missing from Zotero" subsection. |
| `data-availability.md` | Verbatim quote of the paper's DA statement plus a structural classification table (has dataset DOI? has repo? on-request clause? Source Data file? FAIR-compliance assessment) plus a "Lesson for my own DA statements" paragraph. |
| `code-availability.md` | Verbatim quote of the paper's CA statement plus the same structural classification + lesson. |
| `repository-links.md` | Every external URL the paper references that points to a repository / dataset / model documentation / project page. Plus a "Verification" note that links have NOT been independently checked at ingest time. |
| `article-page.md` | Optional defuddled landing page snapshot. If you cannot reach the publisher landing page in this sandbox, write a placeholder noting the deferred status and the URL that would be defuddled. |
| `asset-status.md` | Checklist of what is in Zotero vs missing (PDF, SI, Source Data, DA extracted, CA extracted, external repo). Plus "What to do next on this paper" notes. |

### 3. End-of-run JSON receipt (printed to stdout)

After writing all files, print exactly one JSON object to stdout (no surrounding prose, no markdown fences):

```json
{
  "zotero_key": "...",
  "address": "c-NNNNNN",
  "wiki_page": "wiki/papers/{year}-{js}-{slug}.md",
  "wiki_page_size_kb": 0,
  "stub_dir": ".raw/papers/{KEY}/",
  "stub_count": 7,
  "frontmatter_complete": true,
  "section_count": 18,
  "banned_words_check": "passed | failed: <words found>",
  "em_dash_check": "passed | failed",
  "three_label_discipline": "applied | partial | missing",
  "permanent_notes_count": 5,
  "writing_lessons_count": 5,
  "research_design_lessons_count": 5,
  "future_questions_count": 5,
  "fulltext_source": "main-pdf | peer-review-file | abstract-only | unknown",
  "warnings": ["..."],
  "deviations_from_contract": ["..."]
}
```

The receipt is parsed programmatically. Any deviation from this schema breaks the integration.

---

## Quality bar (non-negotiable)

### Three-label discipline (CLAUDE.md core rule)

Every substantive claim about the paper's contribution, design, or fit must be labeled inline with one of:

- `Evidence:` — directly supported by paper text / figure / table / SI / DA / CA / referenced repo. Cite section, figure number, or page.
- `Inference:` — your interpretation, derived from the paper but not literally stated. Mark confidence (high / medium / low).
- `Lesson:` — transferable insight for Henry's own research or writing. Must state *what to do* concretely, not *what's good*.

A page that uses none of these labels for substantive claims fails the quality bar.

### Anti-fluff (CLAUDE.md core rule)

The following words are **banned** unless followed in the same sentence by a concrete justification:

`innovative · important · rigorous · comprehensive · novel · significant · high-impact · seminal · well-written · clear · elegant · groundbreaking`

To use any of them, you must specify *what aspect* concretely (which dimension is novel? which audience cares? which methodological choice proves rigor? what axis is the comprehensiveness across?). If you cannot make the concrete claim, do not use the abstract word. The receipt's `banned_words_check` should be `passed`. Run a self-check before finalizing.

### Style

- No em dashes (U+2014). No double-hyphen (`--`) as punctuation. Use periods, commas, colons, parentheses, or single hyphens.
- Short, direct prose. Tables for cross-paper data. Prose for argumentation.
- Quote the paper's DA and CA verbatim. Do not paraphrase them.
- For numerical claims, include the unit, the year/scenario context, and (where useful) the source figure/table.

### 18-section template fidelity

All 18 sections from `_templates/paper-analysis.md` must be present and substantive. Specifically:

- §3 (12-dimension value-source diagnosis) must fill all 12 rows of the table.
- §5 (Intro paragraph table) must have one row per Intro paragraph the paper actually has; do not pad to 5 if the paper has 7, do not pad to 7 if it has 5. Identify the gap paragraph explicitly.
- §10 (Figures argument-function) must enumerate every main-text figure. Extended Data figures separately if applicable.
- §17 (KB outputs) must have exactly 5 permanent notes + 5 writing lessons + 5 research-design lessons + 5 future research questions. Each permanent note ends with an `Evidence:` and a `Lesson:`.
- §18 (Final summary) must include Top 3 lessons, Top 3 to transfer, Top 3 to NOT blindly copy, and the one-line takeaway.

---

## Procedure

1. Read `CLAUDE.md` and `_templates/paper-analysis.md`. Then re-read this contract once.
2. Determine the paper from the Zotero key passed in the prompt.
3. **Resolve the main PDF carefully.** Use the Zotero plugin to call `zotero_get_item_metadata` and `zotero_get_item_children`. A paper may have multiple PDF children: the main paper, supplementary, and *the Peer Review File* (Nature Portfolio standard). The Peer Review File is NOT the article. If `zotero_get_item_fulltext` on the parent key returns text that starts with "REVIEWER COMMENTS" or "REVIEWS OF" or that reads like rebuttal-format, you have the wrong attachment; call `zotero_get_item_fulltext` against the specific main-PDF child key instead. The `fulltext_source` field in the JSON receipt must record which one you ended up reading.
4. If `.raw/papers/{KEY}/pre-extraction.md` exists, read it first as a structural starter. It is a trusted summary produced earlier in the session. Verify against the fulltext before quoting from it.
5. Compose the analysis page using the 18-section template. Apply three-label discipline and anti-fluff rules throughout.
6. Write the 7 stub files. Quote the DA and CA verbatim.
7. Run a self-check before printing the receipt:
   - Frontmatter: are all required fields present and the `address` exactly as passed?
   - Banned-word scan: any of the banned words appearing without same-paragraph concrete justification?
   - Em-dash scan: any U+2014 or `--`?
   - 18 sections: all H2 headings 1 through 18 present?
   - KB counts: exactly 5 / 5 / 5 / 5?
8. Print the JSON receipt to stdout. Single object. No preamble. No fences.

---

## What you must NOT do

- Do not edit `CLAUDE.md`, `_templates/*.md` (you read them, you don't change them), or any file under `scripts/`, `.vault-meta/`, or `hooks/`.
- Do not allocate addresses. The `address` field is given to you.
- Do not update `wiki/index.md`, `wiki/log.md`, `wiki/hot.md`, or `.raw/zotero_manifest/top_paper_lab_manifest.csv`. The orchestrating session handles those.
- Do not write outside `wiki/papers/` and `.raw/papers/{KEY}/`.
- Do not commit. Do not run `git` at all.
- Do not download or cache the PDF / SI / source-data binaries into the vault. The Zotero storage path is the source of truth.

---

## On failure

If you cannot complete the analysis (e.g. fulltext is empty, key is invalid, metadata returns a non-article type), do NOT write a partial analysis page. Instead, write a single file at `.raw/papers/{KEY}/codex-ingest-failure.md` describing exactly what went wrong (which tool failed, what was returned, what would be needed to retry), and print a receipt with `"deviations_from_contract": ["..."]` and `"wiki_page": null`. The orchestrating session will redirect.
