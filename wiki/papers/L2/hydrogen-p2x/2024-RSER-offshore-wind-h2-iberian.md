---
zotero_key: "EHNWITKT"
title: "Assessment of hydrogen-based solutions associated to offshore wind farms: The case of the Iberian Peninsula"
journal: "Renewable and Sustainable Energy Reviews"
year: 2024
doi: "10.1016/j.rser.2023.114268"
topic: [offshore-wind, green-hydrogen, power-to-x, iberian-peninsula, floating-wind, day-ahead-market, lcoh, milp, forecasting]
paper_type: [TEA, optimization, simulation, data-driven, hybrid]
main_contribution: [system-boundary-expansion, case-study-rigor, parameter-anchor, sensitivity-depth, engineering-feasibility, policy-relevance]
method_type: [MILP, CNN, VMD, techno-economic-model, hourly-dispatch-optimization]
journal_role: applied_flagship
ingest_depth: A_deep
subdomain_primary:
  - hydrogen-p2x
subdomain_secondary:
  - power-systems
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
address: c-000027
created: 2026-05-11
tags:
  - paper-analysis
  - L2
  - A-deep
---

# Assessment of hydrogen-based solutions associated to offshore wind farms: The case of the Iberian Peninsula

## 1. Positioning

**One-sentence contribution**: **Evidence:** The paper compares conventional grid export, offshore electrolysis, and onshore electrolysis for Iberian floating offshore wind, using hourly dispatch, day-ahead forecasts, regulation costs, and 2020/2030/2050 cost cases.

**Applied-paper sub-type**: **Evidence:** Hydrogen system analysis plus techno-economic analysis plus hourly dispatch optimization, with CNN and VMD forecasting used to generate wind power and price inputs for day-ahead market bidding.

**Primary value source(s)**: **Inference, high confidence:** The value source is system-boundary design: molecule export versus electron export plus onshore grid flexibility. **Lesson:** For Henry's wind-solar-H2 work, make the boundary switch the core experiment and connect it to LCOH, NPV, and policy feasibility.

## 2. Applied-strength table (11 dimensions)

| Dimension | Strength (1-5) | Evidence | Reusable Element | Comment |
|---|---:|---|---|---|
| Model structure | 4 | **Evidence:** Section 3 models wind, PEMEL, cable, compressor, pipeline, storage, fuel cell, desalination, forecasting, and finance. | Modular H2 TEA. | **Lesson:** Swap blocks into Henry's models. |
| System boundary | 5 | **Evidence:** Sections 1 and 3 compare grid export, offshore electrolysis, and onshore electrolysis. | Electron versus molecule boundary. | **Lesson:** Put the boundary switch in the model and figures. |
| Data source | 4 | **Evidence:** Section 4 uses Wind Atlas data, TSO prices, regulation costs, 2015-2019 simulations, and 2010-2014 training data. | Resource plus market data. | **Inference, medium confidence:** Better than average-price TEA. |
| Parameter setting | 5 | **Evidence:** Tables 4 and 5 list CAPEX and OPEX by component for 2020, 2030, and 2050. | Cost bank rows. | **Lesson:** Make assumptions table-ready. |
| Case design | 4 | **Evidence:** Galicia sites at 25 km and 50 km are chosen for high wind speeds. | Distance-paired case. | **Inference, high confidence:** Tests resource gain versus transport cost. |
| Scenario design | 4 | **Evidence:** H2 price is 2-10 EUR/kg with 2020/2030/2050 years and capacity-ratio tests. | Price-year-sizing grid. | **Lesson:** Tie each axis to a decision. |
| Sensitivity analysis | 3 | **Evidence:** Price, year, distance, electrolyzer ratio, and fuel-cell ratio vary. | Scenario sensitivity. | **Inference, medium confidence:** No probability model. |
| Uncertainty analysis | 2 | **Evidence:** No Monte Carlo or distributional analysis is reported. | Gap note. | **Lesson:** Add CAPEX and price envelopes. |
| Results presentation | 4 | **Evidence:** Figs. 1-3 show cost, finance, and distance; Tables 2-6 cover forecasts, costs, and sizing. | Decision stack. | **Lesson:** Link results to choices. |
| Engineering feasibility | 4 | **Evidence:** The model includes PEMEL limits, 3.5 percent cable loss, compressor energy, pipeline sizing, desalination, and PEMFC efficiency. | Feasibility checklist. | **Lesson:** Include auxiliary loads. |
| Policy relevance | 3 | **Evidence:** Sections 1 and 5 discuss EU temporal correlation, geography, additionality, and grid-purchase rules. | Green-H2 policy context. | **Inference, medium confidence:** Context only, not hard constraints. |

**Top 3 strengths**:
1. **Evidence:** System-boundary comparison across grid export, offshore electrolysis, and onshore electrolysis.
2. **Evidence:** Tables 4 and 5 provide component cost inputs by year.
3. **Evidence:** The hourly MILP connects forecasts, grid trades, H2, storage, fuel cell, and regulation costs.

**Top 3 weaknesses or gaps**:
1. **Evidence:** No stochastic uncertainty treatment for CAPEX, electricity prices, or regulation prices.
2. **Inference, high confidence:** EU H2 rules are discussed after the model rather than encoded.
3. **Evidence:** Data are on request and no code statement is provided.

## 3. Method blueprint

**Objective function**: **Evidence:** The day-ahead MILP maximizes forecasted electricity and H2 revenue; the real-time MILP maximizes electricity plus H2 revenue minus regulation costs.

**Decision variables**: **Evidence:** Hourly bid, electricity sale or purchase, electrolyzer input, H2 production and sale, storage level, fuel-cell output, imbalance, and binary operating flags.

**Constraints**: **Evidence:** Section 3.2 covers energy balance, electrolyzer limits, storage reserve, regulation-cost calculation, fuel-cell conversion, and binary switching.

**Inputs (data + parameters)**: **Evidence:** Hourly wind, day-ahead price, imbalance prices, H2 price, 104.5 MW wind farm, PEMEL parameters, compressor energy, transmission loss, cost tables, 7 percent discount rate, and loan terms.

**Outputs (decision + diagnostic metrics)**: **Evidence:** Optimal electrolyzer and fuel-cell ratios, H2 production, grid trades, regulation costs, LCOH, LCOE, NPV, and IRR.

**System boundary**: **Evidence:** Inside are floating wind, grid export, electrolysis, pipeline or cable, compression, storage, fuel cell, desalination, market bidding, and finance. **Inference, high confidence:** Permitting, vessels, supply chain, and life-cycle emissions are outside.

**Temporal resolution**: **Evidence:** Hourly dispatch and forecasts; 2010-2014 training; 2015-2019 simulation; 2020/2030/2050 cost years.

**Spatial resolution**: **Evidence:** Two Galicia plant sites: 25 km from shore at 43.93, -8.21 and 50 km from shore at 44.14, -8.32.

**Method novelty (Inference)**: **Inference, high confidence:** The method contribution is coupling imbalance-cost-aware dispatch with offshore wind to H2 TEA, not inventing a new MILP or CNN.

**Transferable to Henry's work**: **Lesson:** Reuse the two-stage pattern: forecast market/resource, then optimize day-ahead commitment and real-time correction.

## 4. Parameter & assumption table

| Parameter / Assumption | Value or range | Year / context | Source | Reusable for Henry? | Note |
|---|---|---|---|---|---|
| Wind farm capacity | 104.5 | MW | 2015-2019 Iberian simulation, Section 4 | yes | Plant scale for floating offshore wind plus H2 TEA. |
| Offshore sites | 25 and 50 | km from shore | Galicia case, Section 4 | yes | Distance pair tests cable/pipeline cost versus higher wind speed. |
| Electrical transmission loss | 3.5 | percent of transmitted energy | Section 3.1 | yes | Useful default for offshore electrical export sensitivity. |
| Compressor energy | 1 | kWh/kg H2 | Compress 30 to 100 bar, Section 3.1 | yes | Direct H2 balance parameter. |
| Discount rate | 7 | percent | Economic model, Section 4.2 | yes | Finance baseline for LCOH and NPV cases. |
| Project lifetime | 25 | years | Economic model, Section 4.2 | yes | Standard TEA horizon. |
| Floating offshore wind CAPEX | 4.532, 2.354, 1.533 | M EUR/MW in 2020, 2030, 2050 | Table 4 | yes | Strong parameter-bank row for offshore wind H2. |
| Electrolyzer CAPEX | 700, 395, 175 | k EUR/MW in 2020, 2030, 2050 | Table 4 | yes | Bank-ready PEMEL cost trajectory. |
| Storage CAPEX | 439, 397, 325 | EUR/kg in 2020, 2030, 2050 | Table 4 | yes | H2 storage cost input. |
| Hydrogen price sweep | 2 to 10 | EUR/kg, step 2 EUR/kg | Section 4 | yes | Compact profitability sweep. |

**Parameters worth migrating into `wiki/banks/parameter-bank/`**: `floating-offshore-wind-capex.md`, `pem-electrolyzer-capex.md`, `hydrogen-storage-capex.md`, `fuel-cell-capex.md`, `offshore-transmission-loss.md`, `compressor-specific-energy.md`, `offshore-wind-h2-finance-assumptions.md`, `hydrogen-price-sweep.md`.

## 5. Case study design

**Case selected**: **Evidence:** Offshore Galicia, Iberian Peninsula; 25 km and 50 km sites; 104.5 MW floating offshore wind; MIBEL and Portuguese TSO market data; 2020/2030/2050 cost cases.

**Why this case**: **Evidence:** Section 4 says the sites have high wind speeds close to shore. **Inference, high confidence:** Deep water makes floating wind relevant, and Iberian renewable penetration makes grid-purchased H2 a live policy issue.

**Representativeness**: **Inference, medium confidence:** Strong for deep-water offshore regions; weaker for shallow-water fixed-bottom systems.

**Data realism**: **Evidence:** The study uses historical wind speeds, real day-ahead prices, real regulation costs, and multi-year forecast training.

**Generalizability (Inference)**: **Inference, medium confidence:** Transferable if hourly wind, price, imbalance cost, distance, and local policy data are available.

**Lesson for Henry's own case design**: **Lesson:** Pair cases so that one physical axis is visible. Here the axis is shore distance. For Henry's work, use paired cases such as grid-constrained versus unconstrained, wind-dominant versus solar-dominant, or coastal versus inland H2 delivery, then keep all other assumptions traceable.

## 6. Sensitivity / uncertainty / robustness

**Sensitivity variables and ranges**:

| Variable varied | Range | Finding | Source | Henry use |
|---|---|---|---|---|
| Hydrogen sale price | 2 to 10 EUR/kg | Higher H2 price improves profitability; low price pushes onshore ratio to 5 percent. | Section 4, Table 6, Fig. 2 | Break-even sweep. |
| Scenario year | 2020, 2030, 2050 | LCOH falls from 2020 to 2030 and further by 2050. | Fig. 1, Conclusions | Learning trajectory. |
| Electrolyzer ratio | 5 to 100 percent | Offshore optimum mostly 90-95 percent; onshore 5 percent at 2 EUR/kg and 100 percent at 4 EUR/kg. | Table 6 | Co-sizing. |
| Fuel-cell ratio | optimal reported as 5 percent | Fuel cell use is rare because H2-to-power value is low. | Section 5.2 | Optional flexibility. |
| Distance from shore | 25 and 50 km | The 50 km site benefits from stronger wind despite transport cost. | Fig. 1, Fig. 3 | Siting tradeoff. |

**Most influential variable (Evidence)**: **Evidence:** Grid purchase ability drives the onshore advantage: at the 50 km site, LCOH is 5.84, 3.42, and 2.57 EUR/kg for onshore electrolysis versus 8.98, 4.37, and 2.68 EUR/kg for offshore electrolysis in 2020, 2030, and 2050.

**Uncertainty analysis present**: **Evidence:** Partial. Scenario brackets are used, but no Monte Carlo, distributions, confidence intervals, or regret analysis is reported.

**Robustness checks present**: **Evidence:** Forecasts are compared to persistence baselines, and two offshore distances are compared.

**Missing analyses (gaps)**: **Inference, high confidence:** Missing axes include PPA premium, hard additionality constraints, degradation, curtailment, carbon-intensity threshold, cable/pipeline cost curves, and balancing-market revenue.

**Lesson for Henry's sensitivity design**: **Lesson:** Separate sizing, policy compliance, and finance uncertainty; add stress tests for future CAPEX and prices.

## 7. Results & figures table

| Item | Shows | Argument function | Applied-typical or top-journal-typical? | Lesson for Henry |
|---|---|---|---|---|
| Fig. 1 | **Evidence:** LCOE/LCOH by distance and year. | Compares three system boundaries. | Applied-typical | Lead with the cost ranking. |
| Fig. 2 | **Evidence:** NPV and IRR at 25 km. | Converts cost into finance. | Applied-typical | Pair LCOH with investor metrics. |
| Fig. 3 | **Evidence:** NPV by distance. | Tests resource-distance tradeoff. | Applied-typical | Make geography part of the result. |
| Tab. 1 | **Evidence:** Literature LCOH by source and electrolyzer type. | Benchmarks outputs. | Applied-typical | Anchor TEA results against prior ranges. |
| Tab. 2 | **Evidence:** Wind forecast MAPE is 33 percent at 25 km and 23 percent at 50 km. | Validates wind forecast. | Applied-typical | Report forecast error before optimization. |
| Tab. 3 | **Evidence:** Price forecast MAPE is 6 percent versus persistence at 18 percent. | Validates price forecast. | Applied-typical | Validate market forecast separately. |
| Tab. 4 | **Evidence:** CAPEX by component and year. | Cost backbone. | Applied-typical | Make parameters bankable. |
| Tab. 5 | **Evidence:** OPEX by component and year. | Operating-cost backbone. | Applied-typical | Separate CAPEX and OPEX. |
| Tab. 6 | **Evidence:** Optimal electrolyzer ratios. | Turns scenarios into sizing rules. | Applied-typical | End with decisions, not only plots. |

## 8. Comparison with top-journal style

**What makes this an applied paper (vs. Nature Energy / Joule)?** **Inference, high confidence:** It answers a regional engineering economics question rather than a field-level rule for offshore H2.

**Where is this paper already close to top-journal quality?** **Inference, medium confidence:** The boundary contrast could support a broader rule about onshore flexibility versus offshore molecule export.

**To upgrade this paper to a top-journal target, the author would need to**:
- **Lesson:** Reframe from local cost ranking to conditions where grid flexibility beats molecule export.
- **Lesson:** Encode EU temporal, geographic, and additionality rules as constraints.
- **Lesson:** Expand from two sites to a deep-water offshore wind map.
- **Lesson:** Add uncertainty envelopes for CAPEX, PPA premiums, and imbalance prices.
- **Lesson:** Compress the mechanism: grid option, price arbitrage, and reduced offshore dependence.

**Upgrade lesson for Henry**: **Lesson:** Turn local optimization into a system-design rule under policy constraints.

## 9. Direct value for Henry

**Citable background claims**: **Evidence:** AC cable losses are cited at 1-5 percent, pipeline loss at 0.1 percent, and EU RFNBO rules use temporal correlation, geography, and additionality.

**Reusable methods / model components**: **Evidence:** The two-stage day-ahead and real-time MILP is reusable for electrolyzer dispatch with power sale, power purchase, H2 production, and storage.

**Reusable parameters or data**: **Evidence:** Tables 4 and 5 give component CAPEX/OPEX by year; Section 4.2 gives finance assumptions. **Lesson:** Use as priors, then refresh costs.

**Case-study design lessons**: **Lesson:** Choose cases with physical and market logic: deep water, high renewable share, and available market data.

**Sensitivity-design lessons**: **Lesson:** Tie axes to decisions: H2 price, year, distance, electrolyzer ratio, and fuel-cell ratio.

**Figure types worth borrowing**: **Lesson:** Borrow the cost comparison, finance comparison, and sizing table; add a policy-feasibility panel.

**Future research questions inspired by this paper**: **Lesson:** Test additionality, pipeline versus HVDC thresholds, PPA premiums, hybrid storage, and wind-solar forecast complementarity.

## 10. KB outputs (mandatory)

### Technical Method Card

- **Method name**: Hourly offshore wind-H2 TEA with forecast-coupled dispatch.
- **Applicable problem**: **Evidence:** Offshore versus onshore electrolyzer placement under market and H2 revenue.
- **Inputs**: **Evidence:** Hourly wind, prices, imbalance costs, H2 price, CAPEX/OPEX, limits, storage, finance.
- **Outputs**: **Evidence:** LCOH, LCOE, NPV, IRR, ratios, grid trades, regulation costs.
- **Key assumptions**: **Evidence:** PEMEL; 104.5 MW; 25 years; 7 percent discount rate; 80 percent loan.
- **Advantages**: **Inference, high confidence:** Joins plant sizing and market operation.
- **Limitations**: **Evidence:** Data on request; no code statement; no Monte Carlo; policy not constrained.
- **How to migrate into Henry's work**: **Lesson:** Forecast commitments first, then optimize real-time sale, H2, storage, and penalties.

### Parameter Card

| Parameter | Value | Unit | Year | Source | Bank page candidate |
|---|---:|---|---|---|---|
| Floating offshore wind CAPEX | 4.532 / 2.354 / 1.533 | M EUR/MW | 2020 / 2030 / 2050 | Table 4 | `floating-offshore-wind-capex.md` |
| Electrolyzer CAPEX | 700 / 395 / 175 | k EUR/MW | 2020 / 2030 / 2050 | Table 4 | `pem-electrolyzer-capex.md` |
| Storage CAPEX | 439 / 397 / 325 | EUR/kg | 2020 / 2030 / 2050 | Table 4 | `hydrogen-storage-capex.md` |
| Electrical transmission loss | 3.5 | percent | Model assumption | Section 3.1 | `offshore-transmission-loss.md` |
| Compressor energy | 1 | kWh/kg H2 | 30 to 100 bar | Section 3.1 | `compressor-specific-energy.md` |
| Discount rate | 7 | percent | Economic case | Section 4.2 | `project-finance-assumptions.md` |

### Case Study Card

- **Case**: **Evidence:** Galicia offshore wind, 25 km and 50 km sites, 104.5 MW, 2015-2019 simulation, 2020/2030/2050 costs.
- **Selection logic**: **Evidence:** High wind speeds close to shore and deep-water relevance for floating wind.
- **Data realism**: **Evidence:** Historical wind, MIBEL prices, TSO regulation costs, multi-year training.
- **Generalizability**: **Inference, medium confidence:** Transferable to other deep-water offshore wind regions if market and resource data are available.
- **Transferability to Henry's projects**: **Lesson:** Use a distance-resource-market triangle for H2 cases.

### 5 Applied-Paper Writing Lessons

1. **Lesson:** Open with the system-boundary contrast.
2. **Lesson:** Put costs in year-indexed component tables.
3. **Lesson:** Validate forecasts before dispatch optimization.
4. **Lesson:** Convert optimization into sizing rules.
5. **Lesson:** State green-H2 policy conditions early.

### 5 Upgrade Notes (how to lift this kind of paper toward L1)

1. **Lesson:** Turn additionality into dispatch constraints.
2. **Lesson:** Add cross-region coverage.
3. **Lesson:** Add cost and price uncertainty bands.
4. **Lesson:** Use one mechanism figure for the onshore advantage.
5. **Lesson:** Test balancing-market revenue and PPA premium.

### 5 Future Research Questions

1. **Lesson:** What distance makes H2 pipeline export beat electrical export?
2. **Lesson:** How does hourly RFNBO compliance change sizing?
3. **Lesson:** When does a fuel cell help with imbalance costs?
4. **Lesson:** How cheap must offshore platforms become?
5. **Lesson:** Can wind-solar complementarity reduce regulation costs?
