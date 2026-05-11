# Zotero Attachments

| Key | Type | Filename | Zotero storage path | Status |
|---|---|---|---|---|
| N/A | N/A | N/A | N/A | No child attachments could be resolved for `UIWZD5EE` in this sandbox. |

## What is missing from Zotero

- Main article PDF: missing according to `.raw/zotero_manifest/top_paper_lab_manifest.csv`.
- Supplementary information: missing according to `.raw/zotero_manifest/top_paper_lab_manifest.csv`, although the publisher page lists Supplementary Information.
- Source data file: not attached in Zotero. The publisher Data Availability statement points to carculator, carculator_truck and Zenodo ref. 59.
- Peer Review File: not resolved. No peer-review attachment was available to confuse with the main paper.

Resolution note: MCP calls `zotero_get_item_metadata` and `zotero_get_item_children` both returned `user cancelled MCP tool call`; direct local API access was blocked by sandbox networking.
