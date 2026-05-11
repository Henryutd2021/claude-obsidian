---
type: meta
title: "Bank staging — Batch 5 (2026-05-11)"
created: 2026-05-11
updated: 2026-05-11
tags:
  - meta
  - banks
  - staging
status: pending-curation
related:
  - "[[banks/parameter-bank/_about]]"
  - "[[banks/sensitivity-bank/_about]]"
  - "[[banks/method-bank/_about]]"
  - "[[log]]"
---

# Bank staging — Batch 5 (2026-05-11)

First L2 ingest batch produced 5 `bank-candidates.md` files. **Rows are not yet materialized into individual bank pages** because TPL has no dedup-key schema defined yet for cross-paper merge (this is an open issue called out in the systems review).

This page is the orchestrator's tracking entry until the curation pass. Henry: review the per-paper candidates, decide merge keys, then promote into `wiki/banks/{parameter,sensitivity,method}-bank/{slug}.md` pages.

## Sources

| Paper | Address | Candidates file | Param rows | Sens rows | Method rows |
|---|---|---|---|---|---|
| Pettinau 2024 ECM | c-000025 | `.raw/papers/83CEHMNG/bank-candidates.md` | ~14 | ~4 | ~4 |
| McDonagh 2020 AE | c-000026 | `.raw/papers/4UG5EFDW/bank-candidates.md` | ~11 | ~4 | ~4 |
| Calado 2024 RSER | c-000027 | `.raw/papers/EHNWITKT/bank-candidates.md` | ~11 | ~5 | several |
| Nagasawa 2019 AE | c-000028 | `.raw/papers/DBULMZ89/bank-candidates.md` | ~14 | ~5 | ~4 |
| Ruggles 2021 AiAE | c-000029 | `.raw/papers/H4VD5GZN/bank-candidates.md` | ~10 | ~6 | ~7 |
| Feng 2017 AE | c-000030 | `.raw/papers/W86HHD6H/bank-candidates.md` | 0 | 1 | 3 |

Approximate total: ~60 parameter + ~25 sensitivity + ~25 method = **~110 candidate rows**.

## Known overlaps (likely merge targets)

Quick scan of the candidate files surfaces these cross-paper parameter overlaps:

- **PEM electrolyzer CAPEX**: Pettinau, McDonagh, Calado, Ruggles, Nagasawa all report values across 2020-2050 horizons. Merge into one `parameter-bank/pem-electrolyzer-capex.md` with year-stratified rows + per-paper citation.
- **Offshore wind LCOE / CAPEX**: McDonagh, Calado both report. Possibly cross-cite to Borlaug if relevant.
- **Discount rate / project finance assumptions**: Pettinau, McDonagh, Calado, Nagasawa all explicit. Merge into a `parameter-bank/project-finance-assumptions.md` with assumption table.
- **H2 sale price sensitivity**: McDonagh, Calado, Nagasawa, Ruggles all sweep. Likely a single `sensitivity-bank/hydrogen-price-sweep.md` with paper-specific result ranges.
- **Capacity factor (wind, solar)**: most papers. Subset depending on geography.

## Curation procedure (proposed)

1. Decide merge keys (parameter rows: name + units + tech-vintage triplet?).
2. Create one `wiki/banks/{bank}/{slug}.md` per logical row, with multi-paper citation list and a value range or per-paper table.
3. Cross-link each materialized bank row back to the originating paper pages.
4. Update lint TPL-10 once schema is defined to enforce dedup.

Until then: each L2-A page itself already contains Parameter / Sensitivity / Method cards in its body (per the L2-A template), so the information is not lost. The bank promotion is a discoverability enhancement, not a primary record.
