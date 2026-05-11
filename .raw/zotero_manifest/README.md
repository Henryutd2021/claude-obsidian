# Zotero Manifest

This directory holds the inventory of papers Henry has curated in Zotero for the **Top Paper Lab**.

## `top_paper_lab_manifest.csv`

One row per paper in the Zotero collection `Top Paper Lab`. Generated and maintained by Claude Code via the Zotero MCP server (`mcp__zotero__zotero_get_collection_items`).

Columns:

| Column | Type | Meaning |
|---|---|---|
| `zotero_key` | string | Zotero item key (8 chars). Primary key — also names the `.raw/papers/{zotero_key}/` folder. |
| `title` | string | Paper title (cached from Zotero). |
| `authors` | string | First three authors + "et al." if more. |
| `journal` | string | Journal name. |
| `year` | integer | Publication year. |
| `doi` | string | DOI. |
| `topic` | string (semicolon-sep) | Henry's domain tags (e.g., `green-hydrogen;TEA`). |
| `pdf_present` | bool | True if `.raw/papers/{key}/main.pdf` exists locally. |
| `si_present` | bool | True if `.raw/papers/{key}/supplementary/` has files. |
| `da_extracted` | bool | True if `.raw/papers/{key}/data-availability.md` has been populated. |
| `ca_extracted` | bool | True if `.raw/papers/{key}/code-availability.md` has been populated. |
| `code_repo` | string | URL of code repo if any (GitHub / Zenodo / Code Ocean). Empty otherwise. |
| `priority` | int | 1 (highest) to 5. Set by Henry when curating. |
| `ingest_status` | enum | `candidate` / `assets-complete` / `ingesting` / `drafted` / `reviewed`. |
| `review_status` | enum | `unreviewed` / `light-review` / `deep-review`. |

## How to (re)build the manifest

In a Claude Code session at the vault root, instruct:

> Build the Top Paper Lab manifest. Use Zotero MCP to read all items in the `Top Paper Lab` collection. Write `.raw/zotero_manifest/top_paper_lab_manifest.csv` with one row per item. Set `ingest_status = candidate` for any item not already in a more advanced state. Do not modify wiki/.

Claude Code will use `mcp__zotero__zotero_get_collection_items` and related tools.

## How to extend with new papers

Add the paper to Zotero (drag the PDF or use `mcp__zotero__zotero_add_by_doi`). Put it in the `Top Paper Lab` collection. Re-run the manifest build. The new row appears with `ingest_status = candidate`.
