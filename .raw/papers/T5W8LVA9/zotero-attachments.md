# Zotero Attachments

| Key | Type | Filename | Zotero storage path | Status |
|---|---|---|---|---|
| DM5DMFZD | Main PDF | Wang et al. - 2023 - Accelerating the energy transition towards photovoltaic and wind in China.pdf | Unresolved in this sandbox | Identified by pre-extraction hint as the main article PDF |
| UVK9RAXN | Supplementary Information PDF | 41586_2023_6180_MOESM2_ESM.pdf | Unresolved in this sandbox | Identified by pre-extraction hint as SI |

## What is missing from Zotero

- Evidence: The pre-extraction hint says the parent item has a main PDF and SI PDF, but live Zotero MCP calls returned `user cancelled MCP tool call`.
- Evidence: The local Zotero helper reported the local API preference was enabled, but access to `127.0.0.1:23119` failed with `Operation not permitted`.
- Inference: Confidence high. The attachment keys are reliable enough for routing, but storage paths could not be verified in this run.
- Lesson: Re-run Zotero MCP outside this sandbox before relying on local attachment paths.
