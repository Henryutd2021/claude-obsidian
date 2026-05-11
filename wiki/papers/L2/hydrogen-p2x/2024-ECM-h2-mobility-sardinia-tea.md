---
zotero_key: "83CEHMNG"
title: "Techno-economic assessment of renewable hydrogen production for mobility: A case study"
journal: "Energy Conversion and Management"
year: 2024
doi: "10.1016/j.enconman.2024.118513"
topic: [green-hydrogen, hydrogen-mobility, pem-electrolysis, photovoltaic-hydrogen, sardinia, techno-economic-analysis]
paper_type: [TEA, scenario-analysis, simulation]
main_contribution: [system-boundary-expansion, parameter-anchor, case-study-rigor, sensitivity-depth, engineering-feasibility]
method_type: [LCoH, NPV, IRR, payback-time, STC]
journal_role: applied_flagship
ingest_depth: A_deep
subdomain_primary:
  - hydrogen-p2x
subdomain_secondary:
  - integrated-energy-systems
  - re-tech-resources
  - energy-policy-economics
data_assets:
  main_pdf: true
  supplementary: false
  source_data: false
  data_statement: true
  code_statement: false
  code_repository: false
relevance_to_my_research: high
ingest_status: reviewed
address: c-000025
created: 2026-05-11
tags:
  - paper-analysis
  - L2
  - A-deep
---

# Techno-economic assessment of renewable hydrogen production for mobility: A case study

> Zotero: `83CEHMNG` · DOI: 10.1016/j.enconman.2024.118513 · Journal: Energy Conversion and Management (2024) · **L2 applied flagship**

## 1. Positioning

**One-sentence contribution**: **Evidence:** The paper evaluates a Sardinian hydrogen-valley case linking 12.5 MWp PV, a 5 MW PEM electrolyzer, battery buffer, 450 bar H2 storage, and urban buses with LCoH and investor metrics.

**Applied-paper sub-type**: **Evidence:** hydrogen system TEA plus mobility service-cost comparison.

**Primary value source(s)**: **Evidence:** Value comes from provider CAPEX quotes, finance assumptions, a PV-to-H2-to-bus boundary, and sensitivities for CAPEX, by-product revenue, export revenue, and H2 price. **Inference, high confidence:** It is an applied deployment paper.

## 2. Applied-strength table (11 dimensions)

| Dimension | Strength | Evidence | Reusable Element | Comment |
|---|---:|---|---|---|
| Model structure | 4 | **Evidence:** LCoH, NPV, IRR, payback, and bus STC are calculated. | **Lesson:** Pair cost and investor metrics. | Strong TEA, no optimizer. |
| System boundary | 5 | **Evidence:** PV, battery, electrolysis, compression, storage, and bus use are inside the boundary. | **Lesson:** Carry the chain to final service. | Main strength. |
| Data source | 4 | **Evidence:** Main CAPEX values use provider quotations; other values use literature and ARERA. | **Lesson:** Separate quote, authority, and literature data. | Good audit trail. |
| Parameter setting | 5 | **Evidence:** Tables 1 to 6 cover equipment, finance, CAPEX, OPEX, revenues, and buses. | **Lesson:** Put bankable values in tables. | Best bank source. |
| Case design | 4 | **Evidence:** Sardinia is justified by 1,577 kWh/kWp/yr PV yield. | **Lesson:** Justify by resource and scale. | Transfer needs recalculation. |
| Scenario design | 4 | **Evidence:** Self-produced PV, PPA/grid power, H2 prices, full CAPEX support, and bus options are compared. | **Lesson:** Make scenarios decision-facing. | Finance centered. |
| Sensitivity analysis | 4 | **Evidence:** CAPEX, oxygen price, electricity export price, and H2 selling price are varied. | **Lesson:** Split LCoH and investor drivers. | Deterministic only. |
| Uncertainty analysis | 2 | **Evidence:** Market uncertainty is discussed, but no distributions or Monte Carlo are used. | **Lesson:** Add probability for higher targets. | Qualitative uncertainty. |
| Results presentation | 4 | **Evidence:** Figures decompose CAPEX, OPEX, LCoH, cash flow, sensitivities, and bus STC. | **Lesson:** Decompose each headline metric. | Sequential, not compressed. |
| Engineering feasibility | 4 | **Evidence:** PEM operating pressure, stack life, degradation, battery buffer, and 450 bar storage are specified. | **Lesson:** Link TEA to equipment constraints. | Practical basis. |
| Policy relevance | 3 | **Evidence:** EU hydrogen valleys and funding of 4.0 to 4.5 EUR/kg are discussed. | **Lesson:** Tie incentives to break-even. | Context, not policy model. |

**Top 3 strengths**:
1. **Evidence:** The boundary runs from renewable generation to transport service.
2. **Evidence:** The parameter stack is dense enough for bank extraction.
3. **Lesson:** The paper shows how to serve both academic LCoH comparison and investor feasibility.

**Top 3 weaknesses or gaps**:
1. **Evidence:** No probabilistic uncertainty or robust design.
2. **Inference, medium confidence:** The bus comparison is not co-optimized with seasonal H2 storage or fleet operation.
3. **Lesson:** A top-tier version needs a transferable threshold claim, not only one Sardinian case.

## 3. Method blueprint

**Objective function**: **Evidence:** No design optimization is solved. LCoH is discounted costs minus by-product/export revenues divided by lifetime H2 production; NPV, IRR, payback, and bus STC are diagnostic metrics.

**Decision variables**: **Evidence:** The base design is fixed at 12.5 MWp PV, 5 MW PEM, 2 MWh battery, 450 bar H2 storage, and two 500 kg tanks. **Inference, high confidence:** Sensitivity variables act as design or market levers.

**Constraints**: **Evidence:** The analysis uses PV availability, electrolyzer demand of 58 kWh/kgH2, H2 output of 90 kg/h, compression to 450 bar, debt repayment, and a 25-year operating life. **Inference, medium confidence:** These are accounting constraints rather than a formal MILP.

**Inputs (data + parameters)**: **Evidence:** Key inputs are Sardinia PV yield, PEM performance, CAPEX/OPEX, 8% discount rate, 1.33% inflation, 70% debt, 6.14% loan interest, oxygen at 150 EUR/t, export electricity at 125.06 EUR/MWh, and bus assumptions.

**Outputs (decision + diagnostic metrics)**: **Evidence:** Outputs include 20.3094 M EUR CAPEX, 520,424 EUR/yr OPEX, LCoH of 4.09 or 2.97 EUR/kg after revenues, NPV/IRR/payback, and bus STC of 1.45 EUR/km for H2 versus 1.04 EUR/km for diesel.

**System boundary**: **Evidence:** Included: land, PV, battery buffer, PEM, water pre-treatment, H2/O2 compression, H2 storage, PV export, and bus fuel use. Excluded or simplified: wind, grid constraints, seasonal storage, permitting, and adoption policy.

**Temporal resolution**: **Evidence:** Design in 2024, construction in 2025, operation from 2026 to 2050. PV is annual/monthly, not hourly.

**Spatial resolution**: **Evidence:** Plant/site scale in south-west Sardinia, with transfer claimed mainly to Mediterranean areas with similar solar conditions.

**Method novelty (Inference)**: **Inference, high confidence:** The value is not method invention. It is the combination of project-cost data, revenue-adjusted LCoH, investor cash flow, and bus service economics.

**Transferable to Henry's work**: **Lesson:** Reuse the LCoH plus investor-metric structure, but add hourly wind-solar-H2 dispatch and endogenous sizing for Henry's projects.

## 4. Parameter & assumption table

| Parameter / Assumption | Value or range | Year / context | Source | Reusable? | Note |
|---|---|---|---|---|---|
| PV yield | 1,577 kWh/kWp/yr | Carbonia | Section 2.1 | yes | Solar-H2 case anchor. |
| Electrolyzer size | 5 MW PEM | Base case | Table 1 | yes | Central plant scale. |
| Specific power | 58 kWh/kgH2 | PEM operation | Table 1 | yes | Core LCoH driver. |
| Compression energy | 1.7 kWh/kgH2 | 450 bar | Section 2.2 | yes | Refueling energy input. |
| Total CAPEX | 20.3094 M EUR | Base case | Table 4 | yes | Includes land, PV, battery, H2 system. |
| Electrolyzer CAPEX | 1,260 EUR/kW | 5 MW provider quote | Table 3 | yes | High-value bank row. |
| PV CAPEX | 760 EUR/kW | 12.5 MWp provider quote | Section 3.1 | yes | High-value bank row. |
| Total OPEX | 520,424 EUR/yr | First operation year | Table 5 | yes | Conclusion rounds to about 526,000 EUR/yr. |
| Finance | 70% debt, 6.14% interest, 8% discount | 2025 to 2050 project | Table 2 | yes | Project-finance anchor. |
| Revenue prices | 150 EUR/t O2; 125.06 EUR/MWh export power | 2024 base | Section 3.3 | yes | Revenue-side sensitivity. |
| H2 bus assumptions | 0.10 kg/km, 650,000 EUR/bus, 65,000 km/yr | Bus comparison | Table 6 | yes | Converts H2 to transport service. |

**Parameters worth migrating into `wiki/banks/parameter-bank/`**: `pem-electrolyzer-specific-power.md`, `pem-electrolyzer-capex-5mw.md`, `pv-hydrogen-sardinia-yield.md`, `hydrogen-compression-energy-450bar.md`, `h2-bus-consumption-cost.md`, `oxygen-byproduct-price.md`, `hydrogen-valley-finance-assumptions.md`.

## 5. Case study design

**Case selected**: **Evidence:** South-west Sardinia PV-H2 plant producing about 300 t/yr H2 for urban buses.

**Why this case**: **Evidence:** The site has high PV productivity and about 1,500 PV full-load hours. **Inference, high confidence:** It is a review-friendly case because resource quality, project timing, and a visible transport use are aligned.

**Representativeness**: **Evidence:** The conclusion says results are site-specific but transferable to Mediterranean areas with similar solar conditions. **Inference, medium confidence:** Windier or lower-irradiance regions need a fresh dispatch and cost calculation.

**Data realism**: **Evidence:** Main CAPEX values use provider quotations; PV resource comes from PVGIS; export price comes from ARERA; bus values come from literature.

**Generalizability (Inference)**: **Inference, medium confidence:** The method generalizes better than the numbers.

**Lesson for Henry's own case design**: **Lesson:** Pick cases where resource, end-use demand, equipment scale, and policy signal are all explicit before equations appear.

## 6. Sensitivity / uncertainty / robustness

**Sensitivity variables and ranges**:

| Variable | Range | Finding | Source |
|---|---|---|---|
| CAPEX | plus/minus 20% | **Evidence:** PV and electrolyzer CAPEX have low LCoH impact; other components are nearly negligible. | Fig. 11 |
| Oxygen price | 150 EUR/t base, 50% lower, zero | **Evidence:** 50% lower O2 raises net LCoH to 3.23 EUR/kg; zero O2 raises it to 3.48 EUR/kg. | Fig. 12 |
| Electricity export price | 125.06 EUR/MWh base, half-price | **Evidence:** Half export price raises net LCoH to 3.27 EUR/kg. | Fig. 12 |
| H2 selling price | 5, 8, and break-even above 5.25 EUR/kg | **Evidence:** 5 EUR/kg gives NPV -0.89 M EUR and IRR 7.48%; 8 EUR/kg gives NPV about 8.84 M EUR, IRR 12.80%, and 13-year payback. | Figs. 7, 13 |
| Public funding | 100% CAPEX support, H2 at 2 EUR/kg | **Evidence:** NPV is about 8.45 M EUR; theoretical LCoH is 0.84 EUR/kg before revenue credits. | Fig. 8 |
| Electricity supply | Self-produced PV versus PPA/grid at 200 EUR/MWh | **Evidence:** PPA/grid case raises LCoH to 7.23 EUR/kg, or 6.72 EUR/kg with oxygen revenue. | Fig. 10 |

**Most influential variable (Evidence)**: H2 selling price dominates investor feasibility; oxygen and export-power prices dominate revenue-adjusted LCoH.

**Uncertainty analysis present**: **Evidence:** Partial only. Deterministic sensitivity is present; Monte Carlo, distributions, Bayesian analysis, and robust design are absent.

**Robustness checks present**: **Evidence:** Partial. The paper checks alternative electricity procurement and full CAPEX funding, but not alternate weather years, model structures, fleet schedules, or seasonal storage.

**Missing analyses (gaps)**: **Inference, high confidence:** Missing checks include hourly PV-H2 matching, PV-wind sizing, seasonal H2 storage for the 45-bus implication, and support phase-out.

**Lesson for Henry's sensitivity design**: **Lesson:** Vary resource/weather, product prices, finance, and end-use utilization separately; report which metric each variable moves.

## 7. Results & figures table

| Item | Shows | Argument function | Type | Lesson for Henry |
|---|---|---|---|---|
| Fig. 1 | Carbonia PV monthly output | Case resource basis | Applied-typical | **Lesson:** Start economics with local resource evidence. |
| Fig. 2 | Plant configuration | System boundary | Applied-typical | **Lesson:** Cost tables should map to this boundary. |
| Fig. 3 | Electrolyzer degradation | Lifetime output decline | Applied-typical | **Lesson:** Include degradation in long-life TEA. |
| Fig. 4 | Battery capacity vs availability | Storage sizing logic | Applied-typical | **Lesson:** Use sizing curves to avoid arbitrary buffers. |
| Figs. 5, 6 | CAPEX and OPEX shares | Cost-driver decomposition | Applied-typical | **Lesson:** Split investment and operation shares. |
| Figs. 7, 8 | Cash flow with H2 price and CAPEX grant | Investor feasibility | Applied-typical | **Lesson:** Show cumulative cash flow, not only NPV. |
| Figs. 9, 10 | LCoH under self-PV and purchased electricity | Procurement comparison | Applied-typical | **Lesson:** Benchmark self-supply against PPA/grid power. |
| Figs. 11, 12 | CAPEX and revenue sensitivities | Robustness of LCoH | Applied-typical | **Lesson:** Revenue sensitivity can beat CAPEX sensitivity. |
| Fig. 13 | H2 price effect on NPV/IRR | Market-price risk | Applied-typical | **Lesson:** Use NPV and IRR together. |
| Fig. 14 | H2 vs diesel bus STC shares | Explains bus-cost gap | Applied-typical | **Lesson:** Decompose service cost, not fuel cost alone. |
| Tabs. 1, 4 to 7 | PEM, cost, and bus assumptions/results | Parameter bank and end-use comparison | Applied-typical | **Lesson:** Tables should connect equipment, costs, and service economics. |

## 8. Comparison with top-journal style

**What makes this an applied paper (vs. Nature Energy / Joule)?** **Inference, high confidence:** It asks whether one localized project is finance-feasible, not where hydrogen valleys outperform alternatives in general.

**Where is this paper already close to top-journal quality?** **Evidence:** The boundary reaches final transport service, core CAPEX is quotation-backed, and the bus result is uncomfortable: cheaper H2 fuel does not overcome H2 bus capital cost.

**To upgrade this paper to top-journal target, the author would need to**:
- **Lesson:** Reframe from Sardinia TEA to a threshold question: when do local H2 valleys beat diesel and battery alternatives?
- **Lesson:** Expand to multiple Mediterranean PV, wind, and hybrid sites.
- **Lesson:** Add hourly dispatch and seasonal H2 storage sizing.
- **Lesson:** Compare H2, diesel, battery, and e-fuel buses under consistent carbon and subsidy assumptions.
- **Lesson:** Compress the figure stack into one threshold map plus supporting decompositions.

**Upgrade lesson for Henry**: **Lesson:** Use the case as evidence, but make the contribution a transferable design threshold.

## 9. Direct value for Henry

**Citable background claims**: **Evidence:** EU hydrogen-valley framing, grey-H2 cost near 1 to 2 EUR/kg, and renewable-H2 cost near 3 to 8 EUR/kg. Recheck before reuse.

**Reusable methods / model components**: **Lesson:** Reuse LCoH plus NPV/IRR/payback and STC, with gross and revenue-adjusted LCoH kept separate.

**Reusable parameters or data**: **Evidence:** 58 kWh/kgH2 PEM use, 1,260 EUR/kW electrolyzer CAPEX, 760 EUR/kW PV CAPEX, 1.7 kWh/kg H2 compression, 150 EUR/t oxygen, 125.06 EUR/MWh export power, and H2 bus values.

**Case-study design lessons**: **Lesson:** Choose the end-use first, then size production and storage around service demand.

**Sensitivity-design lessons**: **Lesson:** Vary market prices and finance terms alongside CAPEX; this paper shows CAPEX is not always the binding risk.

**Figure types worth borrowing**: **Lesson:** Borrow the boundary diagram, CAPEX/OPEX split, cash-flow curve, LCoH breakdown, and service-cost split.

**Future research questions inspired by this paper**:
1. **Lesson:** What PV-wind-battery-H2 sizing minimizes bus STC hourly?
2. **Lesson:** How much seasonal H2 storage serves 45 buses?
3. **Lesson:** Which support mechanism cuts risk per tCO2 avoided?
4. **Lesson:** When does local H2 beat delivered H2 for fleets?
5. **Lesson:** How durable are oxygen and export-power revenues?

## 10. KB outputs (mandatory)

### Technical Method Card

- **Method name**: PV-to-H2-to-mobility TEA with LCoH, NPV, IRR, payback, and STC.
- **Applicable problem**: **Evidence:** Local renewable-H2 projects with production, storage, and final service in one boundary.
- **Inputs**: PV resource, plant size, PEM performance, costs, finance, revenue prices, vehicle costs, mileage.
- **Outputs**: LCoH, net LCoH, cash flow, NPV, IRR, payback, STC, bus CO2.
- **Key assumptions**: Fixed design, annual PV summary, no stack replacement, zero terminal value, 70% debt.
- **Advantages**: **Evidence:** It shows cost comparison and investor feasibility together.
- **Limitations**: **Evidence:** No hourly optimization, probability, or seasonal storage sizing.
- **How to migrate into Henry's work**: **Lesson:** Keep the finance structure, add hourly dispatch and endogenous sizing.

### Parameter Card

| Parameter | Value | Unit | Year | Source | Bank page candidate |
|---|---|---|---|---|---|
| PV specific yield | 1,577 | kWh/kWp/yr | 2024 case | Section 2.1 | `pv-hydrogen-sardinia-yield.md` |
| PEM specific power | 58 | kWh/kgH2 | 2024 case | Table 1 | `pem-electrolyzer-specific-power.md` |
| PEM CAPEX | 1,260 | EUR/kW | 2024 quote | Table 3 | `pem-electrolyzer-capex-5mw.md` |
| PV CAPEX | 760 | EUR/kW | 2024 quote | Section 3.1 | `utility-pv-capex-mediterranean.md` |
| H2 compression energy | 1.7 | kWh/kgH2 | 450 bar | Section 2.2 | `hydrogen-compression-energy-450bar.md` |
| H2 bus fuel use | 0.10 | kg/km | Bus comparison | Table 6 | `h2-bus-consumption-cost.md` |

### Case Study Card

- **Case**: South-west Sardinia PV-H2 plant for urban buses, 2024 design, 2025 construction, 2026 to 2050 operation.
- **Selection logic**: **Evidence:** High PV productivity, medium plant scale, hydrogen-valley framing, and bus use.
- **Data realism**: **Evidence:** Main CAPEX values use provider quotations; other values use literature or Italian regulatory data.
- **Generalizability**: **Inference, medium confidence:** Strong as a method template, limited as a direct cost result.
- **Transferability to Henry's projects**: **Lesson:** Use it for finance-aware H2 case design, then add dispatch and multi-resource sizing.

### 5 Applied-Paper Writing Lessons

1. **Lesson:** Put the system boundary before the cost tables.
2. **Lesson:** Identify which costs are quotations and which are scaled literature values.
3. **Lesson:** Report both LCoH and investor metrics.
4. **Lesson:** Add an end-use service comparison.
5. **Lesson:** Show when lower fuel cost still fails because capital cost dominates.

### 5 Upgrade Notes (how to lift this kind of paper toward L1)

1. **Lesson:** Convert the single case into threshold maps.
2. **Lesson:** Replicate across multiple resource regions.
3. **Lesson:** Couple PV variability, storage, electrolyzer use, and bus demand hourly.
4. **Lesson:** Add probabilistic uncertainty or scenario ensembles.
5. **Lesson:** Build one summary figure explaining when H2 mobility wins or fails.

### 5 Future Research Questions

1. **Lesson:** What hybrid PV-wind-battery-H2 design minimizes bus STC?
2. **Lesson:** When does oxygen revenue change project finance?
3. **Lesson:** How should grants split between electrolyzers, buses, and offtake?
4. **Lesson:** What fleet size justifies local production?
5. **Lesson:** How do grid upgrade costs change the bus comparison?
