---
type: meta
title: "Hot Cache"
updated: 2026-05-11
tags:
  - meta
  - hot-cache
status: evergreen
related:
  - "[[index]]"
  - "[[log]]"
  - "[[_meta/v2-status]]"
---

# Recent Context

Navigation: [[index]] · [[log]] · [[usage|How to use this vault]] · [[Wiki Map]]

## Last Updated

**2026-05-11, late-evening session (batch 5: first L2 production)**

Henry handed 9 paper titles, all H2 / offshore wind / curtailment / mobility cluster. 8 dispatched in parallel via codex (1 L1 + 5 L2-A + 2 L2-B); 1 IJHE paper skipped per L3 policy. 1 of 8 self-aborted (ACSSCE not in vocab: codex correctly refused). 7 ingested clean.

## Snapshot

- **Papers**: 23 L1 + 6 L2 = **29** total.
- **Address counter**: 33 (c-000003 through c-000032 in use; c-000031 reserved-unused for Shi).
- **Subdomain hubs**: 8, regenerated this session.
- **Bridges**: **14** (11 → 14; 3 new emerged at 3+ gate this batch).
- **Pattern pages**: 7 (no change this batch: L1-only patterns; awaits curation).
- **Playbook v0.1**: 3 pages (no change).
- **Banks**: ~110 candidate rows pending dedup curation. Staging page: [[banks/_batch-2026-05-11-staging]].
- **All 3 SKILL.md files updated for v2 routing** (uncommitted; staged in working tree).

## Batch 5 papers

L1: `c-000032` Borlaug 2021 NE HD-truck depot charging (power-systems primary).

L2-A all hydrogen-p2x primary:
- `c-000025` Pettinau 2024 ECM Sardinia H2 mobility
- `c-000026` McDonagh 2020 AE offshore-wind H2 hybrid investor
- `c-000027` Calado 2024 RSER Iberian offshore wind H2
- `c-000028` Nagasawa 2019 AE wind to LDV H2 ERCOT

L2-A non-H2-primary:
- `c-000029` Ruggles 2021 AiAE flexible loads + H2 curtailment (power-systems primary). Caldeira group. **Bank-row champion** (23 candidates).

L2-B:
- `c-000030` Feng 2017 AE multi-model wind forecasting (ai-data-driven primary).

## Cross-paper anchors emerging from batch 5

Already-pattern-supported clusters thickened:
- **`patterns/subdomain/hydrogen-p2x/merit-order`**: Wolfram + Ueckerdt (L1) plus McDonagh + Calado + Pettinau (L2-A) on configuration ranking. **5 papers**, can promote merit-order page to L1+L2 evidence.
- **`patterns/methods-recurrent/option-value-scenario-pairs`**: McDonagh's 3 OWF-H2 configurations fits the option-value pattern. **5 papers** now.

Promising new pattern stubs (require Henry decision):
- **`patterns/subdomain/hydrogen-p2x/offshore-vs-onshore-electrolyzer`**: Calado (explicit), McDonagh (implicit), arguably Scolaro/Pettinau. **2-4 papers**, ready for stub.
- **`patterns/methods-recurrent/dual-perspective-tea-investor`**: Pettinau (LCOH + NPV/IRR/payback), McDonagh (NPV only), Nagasawa (LP marginal-price + demand model). **3 papers**, ready for stub. This pattern is highly relevant for SMR-DC.
- **`patterns/methods-recurrent/flexible-load-as-system-asset`**: Ruggles (CONUS macro), Zheng (cross-site DC migration), Colangelo (cluster field trial). **3 papers**, ready for stub. Direct SMR-DC ancestor.

## Open decisions (Henry)

1. **Shi 2020 ACSSCE** (c-000031 reserved-unused): add ACS Sustainable Chemistry & Engineering to `applied_flagship` vocab list and re-dispatch? Or treat as L3 manual bank? Quick call: it's energy-system-focused not chemistry-focused. Recommendation: add to vocab.
2. **Scolaro 2022 IJHE**: codex policy currently skips IJHE (L3 technical_support). Paper looks solid (3+ stars, "Done", offshore wind H2 Germany ancillary services). Override and treat as L2? Recommendation: yes: promote IJHE for paper-by-paper override only.
3. **Bank curation**: ~110 candidate rows in staging. Define merge keys + materialize into bank pages? Half day of work, big jump in usefulness.

## Active machinery state (unchanged from earlier)

- DragonScale: counter 33; tiling not run this batch; fold not yet (log < 16).
- Codex: 7 of 8 dispatches OK; ACSSCE self-abort is **correct policy enforcement**, not a bug.
- iCloud + git: 5+ auto-commits during batch, no conflicts observed.
- v2 SKILL.md files (wiki-ingest, wiki-lint, wiki-query): staged-uncommitted, exercised via this batch implicitly.

## Style preferences (carried over)

No em dashes (U+2014) or `--` as punctuation. Short, direct. Parallel tool calls when independent.
