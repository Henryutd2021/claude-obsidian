# Zotero Manifest

This directory holds the inventory of papers Henry has curated in Zotero for the **Top Paper Lab**.

## Storage model

PDFs, supplementary information, source-data archives, and any other paper binaries live in **Zotero's own storage directory** (`~/Zotero/storage/{ITEM_ID}/`), **not** in this iCloud-synced repo. The TPL vault stores analyses (in `wiki/papers/*`), lightweight per-paper text stubs (in `.raw/papers/{KEY}/`), and this manifest (here). Everything heavy stays in Zotero.

When a skill needs the actual PDF or an SI file, it calls:

- `mcp__zotero__zotero_get_item_fulltext` — to read the main PDF as text
- `mcp__zotero__zotero_get_item_children` — to list and locate any attachment (PDF, SI, data, notes)

Zotero desktop must be running for these calls to work.

## `top_paper_lab_manifest.csv`

One row per paper in the Zotero collection `Top Paper Lab`. Maintained by Claude Code via the Zotero MCP server (`mcp__zotero__zotero_get_collection_items`).

Columns:

| Column | Type | Meaning |
|---|---|---|
| `zotero_key` | string | Zotero item key (8 chars). Primary key — also names the `.raw/papers/{zotero_key}/` text-stub folder. |
| `title` | string | Paper title (cached from Zotero). |
| `authors` | string | First three authors + "et al." if more. |
| `journal` | string | Journal name (one of: Nature, Nature Energy, Joule, Nature Communications, Nature Sustainability, Nature Climate Change, One Earth). |
| `year` | integer | Publication year. |
| `doi` | string | DOI. |
| `zotero_pdf_attached` | bool | True if Zotero has a PDF attachment for this item. Verified via `zotero_get_item_children`. |
| `zotero_si_attached` | bool | True if Zotero has at least one supplementary attachment. |
| `da_extracted` | bool | True if `.raw/papers/{key}/data-availability.md` has been populated from the paper. |
| `ca_extracted` | bool | True if `.raw/papers/{key}/code-availability.md` has been populated. |
| `external_repo` | string | URL of an external data/code repo if any (GitHub / Zenodo / Code Ocean / Figshare). Empty otherwise. |
| `priority` | int | 1 (highest) to 5. Set by Henry when curating. |
| `ingest_status` | enum | `candidate` (in collection, not yet ingested) / `assets-checked` (stubs scaffolded, DA/CA extracted) / `ingested` (wiki/papers/*.md exists) / `reviewed` (Henry has read and approved the analysis). |
| `review_status` | enum | `unreviewed` / `light-review` / `deep-review`. |

## How to (re)build the manifest

In a Claude Code session at the vault root, ask:

> Build the Top Paper Lab manifest. Use Zotero MCP to read all items in the `Top Paper Lab` collection. Write `.raw/zotero_manifest/top_paper_lab_manifest.csv` with one row per item per the schema in this README. For each item, also call `zotero_get_item_children` to populate `zotero_pdf_attached` and `zotero_si_attached`. Set `ingest_status = candidate` for items not already further along.

## How to extend with new papers

Add the paper to Zotero (drag PDF or `mcp__zotero__zotero_add_by_doi`). Put it in the `Top Paper Lab` collection. Re-run the manifest build. The new row appears with `ingest_status = candidate`. No file dropping into the vault required.

## Known scope (as of 2026-05-11)

Henry's 7 in-scope journals: **Nature, Nature Energy, Joule, Nature Communications, Nature Sustainability, Nature Climate Change, One Earth**. A `publicationTitle is "<journal>"` advanced search at fork-time turned up **142 items** across these journals:

| Journal | Count |
|---|---|
| Nature | 5 |
| Nature Energy | 74 |
| Joule | 36 |
| Nature Communications | 20 |
| Nature Sustainability | 2 |
| Nature Climate Change | 4 |
| One Earth | 1 |
| **Total** | **142** |

Two duplicates noted (same Jakhmola 2026 Nature Energy paper indexed twice; same Jenkins 2021 Mission Net-Zero America paper in Joule indexed twice).
