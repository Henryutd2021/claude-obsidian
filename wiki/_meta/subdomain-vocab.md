---
type: meta
title: "Subdomain controlled vocabulary"
updated: 2026-05-11
tags:
  - meta
  - vocab
status: evergreen
related:
  - "[[journal-role-vocab]]"
  - "[[depth-policy]]"
---

# subdomain: controlled vocabulary (8 slugs, locked)

Frontmatter fields:
- `subdomain_primary`: 1-2 entries, ordered. For L2 papers, `subdomain_primary[0]` decides the file location under `wiki/papers/L2/{slug}/`.
- `subdomain_secondary`: 0-3 entries. Papers participating in bridges only.

A paper with 3+ primary subdomains files under `wiki/papers/L2/_cross/` (rare: usually only perspectives / cross-disciplinary syntheses).

## The 8 slugs

| Slug | Covers (CN + EN) | Typical L1 contributions | Typical L2 contributions |
|---|---|---|---|
| `integrated-energy-systems` | 综合能源 · multi-energy systems · TEA · system-level optimization · energy hubs · sector coupling | Field-level integrated-system framing, scenario-based decarbonization architectures | MILP/MIQP for energy hub design, TEA workflows, system boundary definition, multi-energy dispatch |
| `power-systems` | 电力系统 · smart grid · RE-grid integration · microgrid · dispatch · markets · grid stability | System-level grid transition narratives, market-design field papers | Unit commitment, OPF formulations, microgrid sizing, dispatch optimization, market simulation |
| `hydrogen-p2x` | 氢能 · P2X · fuel cell · electrolyzer · long-duration storage (H2-based) · ammonia · e-fuels | Hydrogen-economy framing, additionality/policy framing, LCOE/LCOH at field level | Electrolyzer sizing, H2 storage sizing, CFR design, hourly H2 balance, fuel-cell modeling, LCOH decomposition |
| `re-tech-resources` | 太阳能 · 风能 · solar/wind tech · resource assessment · capacity factor maps · plant-level | Resource-feasibility framings (PV potential, wind growth dynamics) | Capacity factor models, panel/turbine selection, site-level production simulation |
| `building-urban` | 建筑节能 · building decarb · urban energy systems · district energy · heat pump systems | Stock-level / national building decarb framings | Building energy simulation, retrofit packages, heat-pump COP modeling, district heating design |
| `energy-policy-economics` | energy economics · policy · markets · socio-technical transitions · investment / finance | Policy framings, meta-analyses, investment-shift narratives | Policy scenario simulations, cost-benefit analysis, market design under policy, learning-curve fits |
| `lca-sustainability` | LCA · carbon emissions inventory · environmental impact · sustainability assessment · ecosystem | Emissions-inventory revisions, system-level LCA framings | Cradle-to-gate LCA, life-cycle GHG accounting, supply-chain emissions, hotspot analysis |
| `ai-data-driven` | AI / ML / data-driven energy methods · intelligent energy systems · data center as energy load | Methodology framings about AI in energy *(papers whose subject matter is AI/data)* | New ML algorithms for forecasting/dispatch, data-driven anomaly detection, digital twins, surrogate modeling |

## Rules

1. **`ai-data-driven` is for papers whose subject matter is AI/data**, not just for any paper that happens to use a neural network. A PyPSA paper using an LSTM for resource forecasting is `power-systems` (primary) + `ai-data-driven` (secondary). A paper proposing a new transformer architecture for grid dispatch is `ai-data-driven` (primary).
2. **Data center papers are a special case**: they sit at the interface of `power-systems` (load side) and `ai-data-driven` (load source). Use both with `ai-data-driven` as secondary unless the paper is methodologically about AI itself.
3. **Hydrogen + power systems is the most common bridge.** Most H2 papers will be `hydrogen-p2x` primary + `power-systems` secondary (or vice versa).
4. **`integrated-energy-systems` is the catch-all for system-level work that combines 3+ vectors** (electricity, heat, gas, transport, etc.). If a paper is system-level but really about *one* vector, prefer the specific subdomain.
5. **`subdomain_secondary` triggers bridge participation.** A paper appearing on both `hydrogen-p2x` (primary) and `power-systems` (secondary) becomes evidence for `wiki/bridges/hydrogen-p2x--power-systems.md`.

## Subdomain hub pages

Each subdomain has a dedicated hub at `wiki/subdomains/{slug}.md`. The hub lists papers in that subdomain (split by `journal_role` and `ingest_depth`), subdomain-specific patterns, subdomain-specific banks, and outward bridges.

## Bridge emergence gate

A bridge page at `wiki/bridges/{A}--{B}.md` is created when **3+ papers** list both subdomains in their `subdomain_primary[]` or `subdomain_secondary[]`. Pairs below 3 papers stay implicit (visible only as Bases-computed counts on the hub pages).
