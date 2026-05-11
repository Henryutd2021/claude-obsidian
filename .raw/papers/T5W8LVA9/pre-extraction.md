# Pre-extraction hint for T5W8LVA9

This file exists only to warn the next agent about an attachment-resolution trap. There is no extracted analysis here.

## Attachment trap

The Zotero parent item `T5W8LVA9` has TWO PDF children:

- `DM5DMFZD` — `Wang et al. - 2023 - Accelerating the energy transition towards photovoltaic and wind in China.pdf` — **this is the main paper**
- `UVK9RAXN` — `41586_2023_6180_MOESM2_ESM.pdf` — this is the Supplementary Information

When you call `mcp__zotero__zotero_get_item_fulltext` with `item_key=T5W8LVA9` (the parent), the Zotero MCP in this environment may return the **Peer Review File / Author Rebuttal** text rather than the main paper. That text reads as rebuttal-format ("REVIEWER COMMENT 1", "We thank the reviewer...") and lacks Methods / References / Acknowledgements as standalone sections.

If you get rebuttal-format text from the parent key call, immediately re-call `mcp__zotero__zotero_get_item_fulltext` with `item_key=DM5DMFZD` instead. The receipt's `fulltext_source` field must record which key you ultimately read.

## Headline numbers from the abstract (cached, for cross-checking)

- PV+wind generation requirement: 1 -> 10-15 PWh/yr by 2060
- Projected gap (CFED extrapolation): only 5-9.5 PWh/yr by 2060
- Optimization result: 9 -> 15 PWh/yr (lifts ceiling)
- Mean abatement cost: US$97 -> US$6 / tCO2
- Annualised investment ramp: US$77B -> US$127B (2020s) -> US$426B (2050s) per year
- 3,844 utility-scale plants individually optimized
- Co-benefit: income for residents in poorest regions
