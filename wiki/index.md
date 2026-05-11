---
type: meta
title: "Top Paper Lab — Index"
updated: 2026-05-11
tags:
  - meta
  - index
status: evergreen
related:
  - "[[hot]]"
  - "[[log]]"
  - "[[papers.base]]"
  - "[[Wiki Map]]"
---

# Top Paper Lab — Index

Personal Karpathy-style wiki for reverse-engineering energy papers across two functional corpora:

- **L1 (top-journal exemplars)**: Nature, Nature Energy, Joule, Nature Communications, Nature Climate Change, One Earth, EES, Science Advances, PNAS — *teaches problem framing, contribution architecture, Discussion elevation, top-journal narrative*.
- **L2 (applied flagships, by subdomain)**: Applied Energy, Advances in Applied Energy, ECM, RSER, Renewable Energy, Energy & Buildings, IJHE, Joule of Energy Storage — *teaches model rigor, system boundary, parameter values, case-study justification, sensitivity design, engineering feasibility*.

The lab compounds analyses into subdomain hubs, bridges, patterns, knowledge banks, and a personal writing playbook. **L3 (technical-support journals) is manual-entry-only** — parameters flow into `wiki/banks/*` rows without standalone analysis pages.

Last reset: **2026-05-11** v2 architecture (two-layer corpus + 8 subdomains + connectivity layer).

Navigation: [[hot]] · [[log]] · [[usage|How to use this vault]] · [[Wiki Map]] · [[_meta/old-index|Pre-fork archive]]

---

## Wiki layout v2

| Top-level | Holds | Grows when |
|---|---|---|
| `wiki/papers/L1/` | L1 deep analyses (18-section, top-journal craft) — flat | Each L1 `/wiki-ingest` adds one |
| `wiki/papers/L2/{subdomain}/` | L2 analyses (10-section / 1-page / citation card), organized by primary subdomain | Each L2 `/wiki-ingest` adds one |
| [[subdomains]] | 8 subdomain hub pages — focused retrieval per subdomain | Phase 3 onward |
| [[bridges]] | Cross-subdomain bridge pages — interface patterns | Auto-emerge when 3+ papers span a pair |
| [[patterns]] | Cross-paper synthesis: `cross-cutting/` (intro/figure/discussion/archetype/contribution/methods-recurrent) + `subdomain/` + `bridges/` + `comparisons/` (top-vs-applied delta) | Phase 3 onward, then each ingest may update |
| [[banks]] | Knowledge banks: `parameter-bank/`, `sensitivity-bank/`, `method-bank/` (Phase 3); `case-study-bank/`, `figure-bank/`, `results-bank/` (Phase 4) | Each L2-A ingest contributes rows |
| [[playbook]] | Henry's writing principles: `top-journal-craft/`, `applied-paper-craft/`, `upgrade-playbook/`, `submission-tier-checklists/` | Distillation pass every ~20 ingests |
| [[projects]] | Henry's own manuscripts | Henry starts a new draft |
| [[_meta]] | Vocab + policy: `journal-role-vocab.md`, `subdomain-vocab.md`, `depth-policy.md`, `routing-rules.md` | Architecture changes |

Subfolders inside `patterns/`, `playbook/`, and `banks/` are created lazily as content demands. The 8-subdomain folders under `papers/L2/` are pre-scaffolded.

---

## 8 subdomains (controlled vocab)

| Slug | Hub | Covers |
|---|---|---|
| `integrated-energy-systems` | [[subdomains/integrated-energy-systems]] | 综合能源 · multi-energy · TEA · system optimization |
| `power-systems` | [[subdomains/power-systems]] | 电力系统 · smart grid · RE integration · microgrid · dispatch · markets |
| `hydrogen-p2x` | [[subdomains/hydrogen-p2x]] | 氢能 · P2X · fuel cell · long-duration storage |
| `re-tech-resources` | [[subdomains/re-tech-resources]] | 太阳能 · 风能 · RE tech & resource assessment |
| `building-urban` | [[subdomains/building-urban]] | 建筑节能 · building decarb · urban energy systems |
| `energy-policy-economics` | [[subdomains/energy-policy-economics]] | energy economics · policy · markets · socio-technical transitions |
| `lca-sustainability` | [[subdomains/lca-sustainability]] | LCA · carbon emissions · sustainability assessment |
| `ai-data-driven` | [[subdomains/ai-data-driven]] | AI / ML / data-driven energy methods · intelligent systems |

See [[_meta/subdomain-vocab|subdomain-vocab]] for full definitions and assignment rules. Bridge pages emerge under [[bridges]] when 3+ papers span a pair.

---

## Domains in scope (Henry's research focus)

- Renewable energy integration
- Wind-solar-hydrogen integrated systems
- Green hydrogen techno-economic analysis
- Energy system optimization
- Building energy saving and emission reduction
- Energy policy and cost analysis

---

## Operations available

> **First time here?** Read [[usage|How to use this vault]] for the practical user manual (7 things you can do, query patterns, project-paper workflow, troubleshooting).

| Skill / command | Use |
|---|---|
| `/wiki-ingest <zotero-key or path>` | Orchestrates `pre-review-brief` + `research-blueprint` to produce a paper analysis under [[papers]] |
| `/wiki-query <question>` | Reads `hot.md` → `index.md` → `papers.base` → drills into pattern pages; saves valuable Q&A back into [[playbook]] |
| `/wiki-lint` | TPL-specific checks: weak/empty lessons, paper-vs-paper contradictions, crowded gaps, orphan patterns, missing Zotero links |
| `/wiki-fold` | Rolls up `log.md` entries — triggers first auto-synthesis at log size 2^k = 8 |
| `/autoresearch <topic>` (or no topic) | Boundary-first frontier surfacing; fills under-covered patterns from web/Zotero |
| `/save` | File this conversation as a [[playbook]] page |
| `/canvas` | Visual map of paper relationships |
| `mcp__zotero__*` | Read/write Zotero metadata, PDF locations, tags, collections |

ARS plugin skills wired in:
- `pre-review-brief` — per-paper deep analysis core
- `research-blueprint` — venue/journal structural fingerprint
- `academic-paper-reviewer` — critical-perspective pass (Devil's Advocate among the simulated reviewers)
- `ars-lit-review` — cross-paper annotated bibliography (used at synthesis time)
- `nature-citation` / `nature-figure` / `nature-polishing` / `nature-response` / `nature-data` — Henry's own drafting side (under [[projects]])

---

## Current state

- Pre-fork content under [[_meta/old-index|wiki/_meta/]]: 46 pages, mostly LLM-Wiki / DragonScale / SEO ecosystem research, kept for self-reference, not active material.
- Address counter at `c-000033` (29 TPL paper addresses in use: `c-000003` through `c-000032`; `c-000031` reserved-unused for Shi 2020 ACSSCE pending vocab decision).

## Papers ingested

Ordered by ingest sequence (address order):

1. [[papers/L1/2022-NE-china-hta-clean-hydrogen|Yang et al. 2022, Nature Energy]] — *Breaking the hard-to-abate bottleneck in China's path to carbon neutrality with clean hydrogen*. Zotero `PIQKGJNB`. Address `c-000003`. Archetype: modeling-optimization + policy-relevant. Headline: US$1.72T avoided cumulative investment under ZERO-H vs ZERO-NH, 65.7 Mt H2/yr by 2060.
2. [[papers/L1/2024-NE-h2-additionality-time-matching|Giovanniello et al. 2024, Nature Energy]] — *The influence of additionality and time-matching requirements on the emissions from grid-connected hydrogen production*. Zotero `8IMLJZAH`. Address `c-000004`. Archetype: policy dispute resolved by boundary diagnosis (DOLPHYN capacity-expansion). Headline: compete vs non-compete additionality framework reconciles Ricks 2023 vs Zeyen 2023 conflict; phased policy = annual matching now, hourly phase-in post-2030.
3. [[papers/L1/2023-N-china-pv-wind-3844-plants|Wang et al. 2023, Nature]] — *Accelerating the energy transition towards photovoltaic and wind in China*. Zotero `T5W8LVA9`. Address `c-000005`. Archetype: plant-by-plant geospatial optimization at national scale. Headline: 9 -> 15 PWh/yr by 2060; mean abatement cost US$97 -> US$6/tCO2 across 3,844 utility-scale plants.
4. [[papers/L1/2025-J-space-based-solar-europe|Che et al. 2025, Joule]] — *Assess space-based solar power for European-scale power system decarbonization*. Zotero `M9HYZCZE`. Address `c-000006`. Archetype: emerging-tech TEA + threshold mapping (PyPSA-Eur). Headline: SBSP becomes decision-relevant when cost + availability cross system-cost thresholds tied to long-duration storage and H2 economics.
5. [[papers/L1/2023-NC-endogenous-learning-green-h2-europe|Zeyen et al. 2023, Nature Communications]] — *Endogenous learning for green hydrogen in a sector-coupled energy model for Europe*. Zotero `T3YPX6LR`. Address `c-000007`. Archetype: methodological endogeneization (learning curves built into sector-coupled optimization). **Same-batch anchor**: paper 2 (Giovanniello 2024 NE) explicitly diagnoses Zeyen's framework as "non-compete" additionality.
6. [[papers/L1/2021-NE-kikstra-covid-energy-demand-scenarios|Kikstra et al. 2021, Nature Energy]] — *Climate mitigation scenarios with persistent COVID-19-related energy demand changes*. Zotero `QDU6TZYF`. Address `c-000008`. Archetype: demand-side shock as scenario lever in integrated-assessment models. Headline: persistent COVID-style demand reductions can ease mitigation cost trajectories even without supply-side changes.
7. [[papers/L1/2015-N-china-fossil-cement-co2-revised|Liu et al. 2015, Nature]] — *Reduced carbon emission estimates from fossil fuel combustion and cement production in China*. Zotero `H998SFTH`. Address `c-000009`. Archetype: emissions-inventory data correction with policy-relevant magnitude. Headline: bottom-up reanalysis cuts Chinese 2000-2013 fossil-fuel + cement CO2 estimates by 14% (~2.9 GtCO2 in 2013) below international inventories.
8. [[papers/L1/2023-NCC-net-zero-investment-shifts-europe|Klaaßen & Steffen 2023, Nature Climate Change]] — *Meta-analysis on necessary investment shifts to reach net zero pathways in Europe*. Zotero `A4EZAC5U`. Address `c-000010`. Archetype: meta-analysis as primary contribution. Headline: harmonizes 21 European scenarios; clean-energy investment must rise ~10x while fossil drops ~9x by 2050 to align with 1.5 C.
9. [[papers/L1/2020-J-data-center-load-migration-curtailment|Zheng et al. 2020, Joule]] — *Mitigating curtailment and carbon emissions through load migration between data centers*. Zotero `UELISBYS`. Address `c-000011`. Archetype: cross-system load-flexibility as demand-side mitigation. Headline: spatial load migration between US data centers can absorb wind/solar curtailment at near-zero marginal cost.
10. [[papers/L1/2023-NC-rooftop-pv-china-carbon|Zhang et al. 2023, Nature Communications]] — *Carbon mitigation potential afforded by rooftop photovoltaic in China*. Zotero `CRAKEP8V`. Address `c-000012`. Archetype: bottom-up resource assessment with policy-implication ladder. Headline: rooftop PV in 354 Chinese cities can deliver ~70% of China's 2030 PV target at retail-grid parity in most urban regions.
11. [[papers/L1/2021-NE-national-wind-solar-growth-dynamics|Cherp et al. 2021, Nature Energy]] — *National growth dynamics of wind and solar power compared to the growth required for global climate targets*. Zotero `L8UI4RX3`. Address `c-000013`. Archetype: empirical growth-curve fitting as decarbonization-feasibility benchmark. Headline: ex-post logistic fits to wind/solar deployment in 60 countries show only a few have hit the rates required for 1.5 C; "leader country" growth rates are the empirical ceiling.
12. [[papers/L1/2024-OE-h2-economy-22pct-cost-reduction|Wolfram et al. 2024, One Earth]] — *The hydrogen economy can reduce costs of climate change mitigation by up to 22%*. Zotero `73CKKQFI`. Address `c-000014`. Archetype: global IAM option-value scenario pairs (GCAM with/without H2, plus end-use exclusions). Headline: 3-9% H2 share of 2050 final energy yields 15-22% mitigation-cost reduction; international shipping ranked top-value end use (~6.4%). First One Earth paper in the lab.
13. [[papers/L1/2021-NCC-h2-efuels-potential-risks|Ueckerdt et al. 2021, Nature Climate Change]] — *Potential and risks of hydrogen-based e-fuels in climate change mitigation*. Zotero `UIWZD5EE`. Address `c-000015`. Archetype: risk-perspective on H2 e-fuels with quantified efficiency, cost, and emissions consequences of premature deployment vs delayed scale-up. Headline: e-fuel routes deliver only 16-48% electricity-to-useful-energy efficiency (2-10x more renewable electricity than direct electrification); 2050 mitigation costs EUR20-270/tCO2 only after deep scale-up; should be rationed to sectors inaccessible to direct electrification.
14. [[papers/L1/2022-NCC-residential-decarbonization-us|Berrill et al. 2022, Nature Climate Change]] — *Decarbonization pathways for the residential sector in the United States*. Zotero `VMSZ42JG`. Address `c-000016`. Archetype: national stock-level building decarbonization scenario modeling (108 pathways: 3 housing-stock × 4 new-housing × 3 renovation × 3 supply paths). Headline: combined renovation + electrification + smaller homes + multifamily growth + clean grid reaches 91% reduction by 2050. First building-energy paper in the lab.
15. [[papers/L1/2022-N-solar-pv-supply-chain-cost-savings|Helveston, He & Davidson 2022, Nature]] — *Quantifying the cost savings of global solar photovoltaic supply chains*. Zotero `B6LNILBU`. Address `c-000017`. Archetype: counterfactual cost-savings analysis on the globalized PV supply chain. Headline: globalized PV module markets saved installers US$67B cumulatively 2008-2020 across the three largest deployers (China $36B + US $24B + Germany $7B); quantifies the price of decoupling.
16. [[papers/L1/2022-NE-green-h2-probabilistic-feasibility|Odenweller et al. 2022, Nature Energy]] — *Probabilistic feasibility space of scaling up green hydrogen supply*. Zotero `KRT75D4W`. Address `c-000018`. Archetype: Monte-Carlo feasibility envelope built on historical analog technology growth distributions (Wright's-law-fit ensemble). Headline: even on the upper feasibility envelope, green hydrogen supply meets <1% of 2030 final energy in 1.5 C scenarios; the gap is structural, not target-setting.
17. [[papers/L1/2023-J-smr-industrial-process-heat-tea|Vanatta et al. 2023, Joule]] — *Technoeconomic analysis of small modular reactors decarbonizing industrial process heat*. Zotero `XUGL6XPD`. Address `c-000019`. Archetype: profit-maximizing MILP over 5 SMR designs × 421 industrial natural-gas-fueled processes in ERCOT/SPP. Headline: SMRs not economic for heat-alone at 2021 gas prices, but serve 125 SPP processes once heat supply is paired with wholesale electricity revenue. **Direct framework for SMR + co-located demand TEA**.
18. [[papers/L1/2022-NE-flexible-nuclear-deep-decarb|Duan et al. 2022, Nature Energy]] — *Stylized least-cost analysis of flexible nuclear power in deeply decarbonized electricity systems*. Zotero `SYZJZS6F`. Address `c-000020`. Archetype: Macro Energy Model, 42 country-level regions, hourly linear optimization. Headline: flexible nuclear + thermal energy storage is excluded under moderate cuts but enters least-cost portfolios beyond ~80% emissions reduction, especially where wind resources are weak and grid-flexibility substitutes are absent.
19. [[papers/L1/2024-NE-flexible-geothermal-decarb-systems|Ricks et al. 2024, Nature Energy]] — *The role of flexible geothermal power in decarbonized electricity systems*. Zotero `5CAVXPE9`. Address `c-000021`. Archetype: capacity-expansion (GenX) embedding flexible vs inflexible EGS with ResFrac-informed reservoir behavior; 11-zone Western Interconnection in 2045. Headline: EGS flexibility changes system value and deployment far more than EGS LCOE; firm-flexible clean baseload is a different system asset from firm-inflexible.
20. [[papers/L1/2025-NE-smr-policy-module-learning|Vanatta, Stewart & Craig 2025, Nature Energy]] — *The role of policy and module manufacturing learning in industrial decarbonization by small modular reactors*. Zotero `SYGLCEMJ`. Address `c-000022`. Archetype: profit-maximizing deployment model, 4 SMR designs × 925 US industrial facilities, 2030-2050 horizon. Headline: SMR deployment is gated by delivered gas price, FOAK-cost escalation, factory learning, carbon tax and ITC — not by direct early subsidies. **Pair with Vanatta 2023 J (same Michigan group)** for cascaded methodology.
21. [[papers/L1/2022-J-data-center-energy-estimates-review|Mytton & Ashtine 2022, Joule]] — *Sources of data center energy estimates: A comprehensive review*. Zotero `52W57HP5`. Address `c-000023`. Archetype: provenance-audit meta-review of 258 estimates across 46 publications (2007-2021), tracing 676 source links. Headline: data-center energy estimate reliability is driven by source provenance (private market data, broken links, vague methods, future extrapolation), not by one bad number. **Critical methodology source for any DC-load paper**.
22. [[papers/L1/2026-NE-ai-data-centres-grid-interactive|Colangelo et al. 2026, Nature Energy]] — *AI data centres as grid-interactive assets*. Zotero `KWNBZ8FA`. Address `c-000024`. Archetype: production-cluster field trial (256-GPU AI cluster in Phoenix) as evidence base. Headline: software workload orchestration can reduce cluster power 25% for 3 hours during grid peaks while keeping QoS thresholds intact. **First field-trial paper in the lab** (vs all-modeling so far).

---

## Dashboards

- [[papers.base]] — 10 views over all paper analyses (L1 + L2): All papers · L1 exemplars · L2 deep · L2 medium · By subdomain · By archetype · Bridges activity · Drafts · High-relevance backlog · Upgrade candidates.
- [[dashboard.base]] — Cross-folder health: subdomain hubs · pattern pages · bank pages · bridge pages · playbook pages · stale pages · empty placeholders.

---

## Architecture references (v2)

- [[_meta/journal-role-vocab|journal-role-vocab]] — what counts as L1 vs L2 vs L3
- [[_meta/subdomain-vocab|subdomain-vocab]] — 8 subdomain slugs and assignment rules
- [[_meta/depth-policy|depth-policy]] — A_deep / B_medium / C_light selection rules
- [[_meta/routing-rules|routing-rules]] — which pages get updated when paper of role X / depth Y is ingested
