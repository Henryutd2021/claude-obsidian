---
zotero_key: H4VD5GZN
title: "Opportunities for flexible electricity loads such as hydrogen production from curtailed generation"
journal: "Advances in Applied Energy"
year: 2021
doi: "10.1016/j.adapen.2021.100051"
topic: [flexible-loads, curtailment, hydrogen-production, renewable-integration, macro-energy-modeling]
paper_type: [modeling, optimization, scenario-analysis, simulation]
main_contribution: [system-boundary-expansion, parameter-anchor, case-study-rigor, sensitivity-depth, engineering-feasibility]
method_type: [linear-optimization, macro-energy-model, MEM]
journal_role: applied_flagship
ingest_depth: A_deep
subdomain_primary:
  - power-systems
subdomain_secondary:
  - hydrogen-p2x
  - integrated-energy-systems
data_assets:
  main_pdf: true
  supplementary: false
  source_data: true
  data_statement: true
  code_statement: true
  code_repository: true
relevance_to_my_research: high
ingest_status: reviewed
address: c-000029
created: 2026-05-11
tags:
  - paper-analysis
  - L2
  - A-deep
---

# Opportunities for flexible electricity loads such as hydrogen production from curtailed generation

## 1. Positioning

**One-sentence contribution**: **Evidence:** Ruggles et al. use a least-cost CONUS macro energy model to test how much flexible electrolysis load can use otherwise unused or curtailed generation before it drives new capacity.

**Applied-paper sub-type**: **Evidence:** Renewable integration optimization plus hydrogen flexible-load analysis.

**Primary value source(s)**: **Evidence:** The value comes from the 0 to 1 flexible-load sweep, the MC_firm versus MC_flex cost split, and a reusable 2019 technology-parameter table. **Inference (high):** The contribution is framing, not solver design: hydrogen is treated as an annual flexible sink competing for surplus power.

## 2. Applied-strength table (11 dimensions)

| Dimension | Strength (1-5) | Evidence | Reusable Element | Comment |
|---|---:|---|---|---|
| Model structure | 4 | **Evidence:** Section 2.2 defines capacity, dispatch, storage, balance, flexible-load, and H2 equations. | Annual flexible-load LP. | **Inference (high):** Strong for system behavior, weak for nodal operations. |
| System boundary | 4 | **Evidence:** Fig. 1 includes generation, firm load, electrolysis, batteries, and demand response, but no H2 end use. | Power to H2 boundary. | **Lesson:** State H2 delivery and offtake exclusions early. |
| Data source | 4 | **Evidence:** Section 2.1 uses 2017 CONUS load, MERRA-2 weather, EIA costs, and NREL H2A assumptions. | Hourly weather-load alignment. | **Inference (medium):** Single-year design limits weather-risk claims. |
| Parameter setting | 5 | **Evidence:** Table 2 lists CAPEX, O&M, lifetimes, fixed costs, efficiencies, and variable costs in 2019 USD. | Bank-ready technology assumptions. | **Lesson:** Put all asset assumptions in one table. |
| Case design | 4 | **Evidence:** CONUS is modeled as a lossless copper plate using high-output wind and solar regions. | Lower-bound surplus case. | **Inference (high):** The idealization clarifies mechanism but hides congestion. |
| Scenario design | 4 | **Evidence:** Table 1 defines Dispatch, Dispatch+Renew+Storage, and Renew+Storage. | Technology-stack ladder. | **Lesson:** Use a three-scenario ladder for flexibility mechanisms. |
| Sensitivity analysis | 4 | **Evidence:** Main text points to cost, demand-response, aggregation, and PGP variants. | Sensitivity menu. | **Inference (medium):** Some ranges sit only in SI. |
| Uncertainty analysis | 2 | **Evidence:** No Monte Carlo, stochastic weather, or multi-year weather model appears in the main text. | Gap template. | **Lesson:** Add weather and price uncertainty for bankable H2 claims. |
| Results presentation | 4 | **Evidence:** Figs. 2 to 6 link costs, generation use, capacity, dispatch, H2 cost, and time availability. | Cost to operations figure stack. | **Inference (high):** Strong but not compressed. |
| Engineering feasibility | 3 | **Evidence:** Current-cost assets and PEM H2A assumptions are used, but H2 storage and transport are excluded. | Capacity-factor framing. | **Lesson:** Pair low-cost H2 claims with offtake scope. |
| Policy relevance | 3 | **Evidence:** Section 4.2 benchmarks against the DOE target of less than 2 USD/kg H2. | Policy target comparison. | **Inference (medium):** Market design is thin. |

**Top 3 strengths**:
1. **Evidence:** Table 2 is bank-ready.
2. **Evidence:** The load-fraction sweep locates the surplus-exhaustion threshold.
3. **Lesson:** Split MC_firm and MC_flex to show who pays for capacity.

**Top 3 weaknesses or gaps**:
1. **Evidence:** Section 4.5 assumes lossless CONUS transmission.
2. **Evidence:** The model uses only 2017 weather and load.
3. **Inference (high):** H2 storage, delivery, offtake, and price access remain outside scope.

## 3. Method blueprint

**Objective function**: **Evidence:** Section 2.2 minimizes fixed capacity costs, variable generation costs, and demand-response penalties.

**Decision variables**: **Evidence:** Installed capacity plus hourly dispatch, storage state, electrolysis, and demand response.

**Constraints**: **Evidence:** Capacity bounds, dispatch bounds, storage balance, hourly system balance, annual flexible load, and H2 production.

**Inputs (data + parameters)**: **Evidence:** 2017 hourly CONUS load, MERRA-2 resource CFs, EIA costs, Lazard batteries, and NREL H2A electrolysis.

**Outputs (decision + diagnostic metrics)**: **Evidence:** Capacities, dispatch, unused generation, average cost, MC_firm, MC_flex, H2 cost, and electrolyzer CF.

**System boundary**: **Evidence:** Inside are generation, batteries, demand response, firm load, and electrolysis. Outside are H2 storage, delivery, end use, nodal congestion, subsidies, and extra weather stress tests.

**Temporal resolution**: **Evidence:** One-hour time steps over 8,760 hours in 2017.

**Spatial resolution**: **Evidence:** CONUS copper plate with resource profiles from the top 25% of MERRA-2 cells by annual CF.

**Method contribution (Inference)**: **Inference (high):** Standard LP; the contribution is the flexible-load sweep and cost attribution.

**Transferable to Henry's work**: **Lesson:** Sweep flexible-load fraction, report MC_flex separately, and show when H2 shifts from surplus user to capacity driver.

## 4. Parameter & assumption table

| Parameter / Assumption | Value or range | Year / context | Source | Reusable for Henry? | Note |
|---|---|---|---|---|---|
| Wind fixed capital investment | 1,300 USD/kWe | 2019 | **Evidence:** Table 2 | yes | 43% aggregate CF. |
| Solar PV fixed capital investment | 1,300 USD/kWe | 2019 | **Evidence:** Table 2 | yes | 28% aggregate CF. |
| Natural gas with 90% CCS CAPEX | 2,600 USD/kWe | 2019 | **Evidence:** Table 2 | yes | Dispatchable proxy. |
| Electrolysis facility CAPEX | 1,100 USD/kWe | 2019 | **Evidence:** Table 2 | yes | Stack, BoP, compressor. |
| Battery storage CAPEX | 370 USD/kWhe | 2019 | **Evidence:** Table 2 | yes | Energy-capacity basis. |
| Electrolysis facility efficiency | 61% LHV | H2A | **Evidence:** Section 2.1 and Table 2 | yes | Includes BoP and compressor. |
| Battery round-trip efficiency | 90% | Li-ion | **Evidence:** Table 2 | yes | Storage balance. |
| Battery self-discharge | 1% per month | Li-ion | **Evidence:** Section 2.1 | yes | Storage loss. |
| Flexible load fraction sweep | 0 to 1 by 0.01 | all scenarios | **Evidence:** Section 2.1 | yes | 101 cases. |

**Parameters worth migrating into `wiki/banks/parameter-bank/`**: wind-capex-2019, solar-pv-capex-2019, gas-ccs-capex-2019, pem-electrolysis-capex-h2a, battery-storage-capex-2019, pem-electrolysis-efficiency, battery-roundtrip-efficiency.

## 5. Case study design

**Case selected**: **Evidence:** A CONUS-scale electricity system in 2017 with historical hourly firm load, MERRA-2 wind and solar profiles, and a generic flexible load represented by PEM electrolysis.

**Why this case**: **Evidence:** The authors seek system behavior, not a future forecast. **Inference (high):** CONUS preserves weather-load correlation while smoothing local resource noise.

**Representativeness**: **Inference (medium):** Good for large-area planning, weak for nodal implementation because congestion is removed.

**Data realism**: **Evidence:** Load and weather are historical, costs are 2019 estimates, and H2 assumptions come from NREL H2A. **Inference (medium):** Market access to MC_flex is the weak point.

**Generalizability (Inference)**: **Inference (high):** The method transfers; the 25% threshold depends on region, storage, dispatchable capacity, and market rules.

**Lesson for Henry's own case design**: **Lesson:** Preserve hourly weather-load correlation, then label idealizations as bounds rather than forecasts.

## 6. Sensitivity / uncertainty / robustness

| Variable or design choice | Range or contrast | Finding | Source | Gap |
|---|---|---|---|---|
| Flexible load fraction | 0 to 1 by 0.01 | **Evidence:** MC_flex stays low early; expansion accelerates near 0.2 to 0.3. | Sections 2.1, 3.1, 4.3 | Strong main sweep. |
| Technology stack | three scenarios | **Evidence:** More flexibility reduces zero-marginal-cost surplus. | Table 1, Section 4.4 | Good contrast. |
| Demand response | included versus excluded | **Evidence:** Exclusion raises capacity, surplus, and cost. | Sections 3.3, 4.4 | SI details. |
| Asset cost reductions | current versus lower-cost | **Evidence:** Main conclusions do not materially change. | Section 4.5, S.12 | Exact ranges in SI. |
| Power-to-gas-to-power | absent versus available | **Evidence:** In Renew+Storage, PGP cuts cost about 10% and curtailment about 60%. | Section 4.4, S.18 | SI-driven. |
| Transmission geography | CONUS copper plate versus constrained regions | **Inference (high):** Smaller regions likely raise surplus and cost. | Section 4.5 | Discussion only. |
| Weather years | 2017 only | **Evidence:** Single-year optimization is acknowledged. | Section 4.5 | No multi-year uncertainty. |

**Most influential variable (Evidence)**: Flexible load fraction; beyond roughly 0.2, systems move from using surplus to building capacity.

**Uncertainty analysis present**: **Evidence:** Partial scenario brackets and SI checks, but no Monte Carlo, stochastic optimization, or multi-year weather ensemble.

**Robustness checks present**: **Evidence:** Demand-response exclusion, cost reductions, PGP option, and resource aggregation are discussed through SI pointers.

**Missing analyses (gaps)**: **Inference (high):** Missing checks include nodal constraints, price formation, H2 delivery, offtake, multi-year droughts, and imperfect foresight.

**Lesson for Henry's sensitivity design**: **Lesson:** Pair any headline threshold with a stress table for transmission, weather year, electrolyzer CAPEX, storage duration, and price access.

## 7. Results & figures table

| Item | Shows | Argument function | Applied-typical or top-journal-typical? | Lesson for Henry |
|---|---|---|---|---|
| Fig. 1 | Power system and electrolysis boundary. | Model map. | applied-typical | **Lesson:** Separate assets, carriers, and demands. |
| Fig. 2 | MC_firm, MC_flex, average cost, and unused generation. | Core mechanism. | top-journal-typical | **Lesson:** Pair economic threshold with physical surplus. |
| Fig. 3 | Capacity expansion versus flexible-load fraction. | New-build trigger. | applied-typical | **Lesson:** Show capacity response. |
| Fig. 4 | 48-hour Dispatch peak window on 20 July 2017. | Dispatch check. | applied-typical | **Lesson:** Add one peak-window dispatch plot. |
| Fig. 5 | H2 cost and electrolyzer CF. | H2 economics. | applied-typical | **Lesson:** Split electricity and electrolyzer fixed cost. |
| Fig. 6 | Electrolyzer CF by hour and month. | Temporal availability. | top-journal-typical | **Lesson:** Show seasonal failure modes. |
| Table 1 | Scenario technology stacks. | Scenario framing. | applied-typical | **Lesson:** Make scenarios compact. |
| Table 2 | Asset costs and technical assumptions. | Parameter anchor. | applied-typical | **Lesson:** Build bank-ready assumption tables. |
| Table 3 | Model nomenclature. | Equation support. | applied-typical | **Lesson:** Define symbols for capacity, dispatch, and cost. |

## 8. Comparison with top-journal style

**What makes this an applied paper (vs. Nature Energy / Joule)?** **Inference (high):** It is organized around an engineering model experiment and reusable cost thresholds, not a national transition narrative or market-design claim.

**Where is this paper already close to top-journal quality?** **Evidence:** It links surplus capacity to load and renewable variability, then shows when H2 exhausts that slack. **Inference (medium):** Fig. 2 and Fig. 6 are closest to L1 style.

**To upgrade this paper to a top-journal target, the author would need to**:
- **Lesson:** Reframe from flexible-load use to market allocation of surplus electricity.
- **Lesson:** Expand the boundary from electrolysis input electricity to H2 storage, delivery, offtake, and competing flexible loads.
- **Lesson:** Replace the CONUS copper plate with multi-region or nodal constraints.
- **Lesson:** Add multi-year weather and imperfect-foresight robustness to defend the reliability claim.
- **Lesson:** Compress the figures into one mechanism figure plus one threshold or market-design figure.

**Upgrade lesson for Henry**: **Lesson:** The L2 version reports cost thresholds; the L1 version must explain who captures surplus power, under what market rule, and with what planning consequence.

## 9. Direct value for Henry

**Citable background claims**: **Evidence:** Systems can supply roughly 25% extra flexible load with small expansion while average costs fall about 10% to 20%.

**Reusable methods / model components**: **Lesson:** Reuse the annual flexible-load constraint, MC attribution, scenario ladder, and availability plots.

**Reusable parameters or data**: **Evidence:** Table 2 gives 2019 costs and efficiencies; Section 2.1 gives 2017 CONUS load and MERRA-2 resource construction.

**Case-study design lessons**: **Lesson:** For H2 load papers, make the flexible demand scalable from negligible to dominant, rather than choosing one fixed electrolyzer size.

**Sensitivity-design lessons**: **Lesson:** Treat flexible-load fraction as the main sweep, then add sensitivity layers for storage, demand response, transmission, and price access.

**Figure types worth borrowing**: **Lesson:** Borrow Fig. 2's paired cost-surplus structure, Fig. 4's peak dispatch check, and Fig. 6's hour-month availability view.

**Future research questions inspired by this paper**: **Lesson:** Test thresholds under nodal prices, data-center loads, H2 storage, multi-year droughts, and mixed flexible demand.

## 10. KB outputs (mandatory)

### Technical Method Card

- **Method name**: **Evidence:** Macro energy model with annual flexible-load sweep.
- **Applicable problem**: **Lesson:** Use to test how much flexible demand a grid can absorb before capacity and marginal costs rise.
- **Inputs**: **Evidence:** Hourly load, wind and solar CFs, costs, efficiencies, scenario assets, flexible-load fraction.
- **Outputs**: **Evidence:** Capacity mix, dispatch, unused generation, MC_firm, MC_flex, average cost, H2 cost, electrolyzer CF.
- **Key assumptions**: **Evidence:** Perfect foresight, CONUS copper plate, 2017 weather and load, current costs, no H2 delivery, no H2 end use.
- **Advantages**: **Inference (high):** Low complexity makes the mechanism legible and parameter migration easy.
- **Limitations**: **Evidence:** Section 4.5 flags copper-plate transmission, one year, no learning rates, no subsidies, and limited extreme-weather handling.
- **How to migrate into Henry's work**: **Lesson:** Add a flexible-load sweep and report where flexible demand stops using surplus and starts driving capacity.

### Parameter Card

| Parameter | Value | Unit | Year | Source | Bank page candidate |
|---|---:|---|---:|---|---|
| Wind CAPEX | 1,300 | USD/kWe | 2019 | Table 2 | wind-capex-2019.md |
| Solar PV CAPEX | 1,300 | USD/kWe | 2019 | Table 2 | solar-pv-capex-2019.md |
| Gas CCS CAPEX | 2,600 | USD/kWe | 2019 | Table 2 | gas-ccs-capex-2019.md |
| Electrolysis facility CAPEX | 1,100 | USD/kWe | 2019 | Table 2 | pem-electrolysis-capex-h2a.md |
| Battery storage CAPEX | 370 | USD/kWhe | 2019 | Table 2 | battery-storage-capex-2019.md |
| Electrolysis facility efficiency | 61 | % LHV | 2019 | Section 2.1 and Table 2 | pem-electrolysis-efficiency.md |
| Battery round-trip efficiency | 90 | % | 2019 | Table 2 | battery-roundtrip-efficiency.md |
| Battery self-discharge | 1 | % per month | 2019 | Section 2.1 | battery-self-discharge.md |

### Case Study Card

- **Case**: **Evidence:** CONUS 2017 hourly load and MERRA-2 wind/solar with electrolytic H2 as flexible load.
- **Selection logic**: **Inference (high):** Large-area case isolates surplus and preserves load-weather correlation.
- **Data realism**: **Evidence:** Historical load and weather, current-cost assets, H2A electrolysis assumptions.
- **Generalizability**: **Inference (medium):** The method generalizes; the threshold needs regional grid, storage, and market recalibration.
- **Transferability to Henry's projects**: **Lesson:** Use as a base design for wind-solar-H2 sizing and flexible-load studies.

### 5 Applied-Paper Writing Lessons

1. **Lesson:** Start with surplus power versus flexible-asset utilization, then quantify both.
2. **Lesson:** Put the scenario definitions before equations so readers know which assets can solve the balance problem.
3. **Lesson:** Use one assumption table for costs, lifetimes, efficiencies, and variable costs.
4. **Lesson:** Convert system-level electricity results into the sector metric readers care about, here USD/kg H2.
5. **Lesson:** Classify boundary exclusions as lower-bound or upper-bound mechanisms.

### 5 Upgrade Notes (how to lift this kind of paper toward L1)

1. **Lesson:** Add regional congestion and nodal price formation so the flexible-load opportunity becomes place-specific.
2. **Lesson:** Model H2 storage, transport, and offtake to convert low-cost electricity into delivered H2 value.
3. **Lesson:** Compare electrolysis against other flexible loads competing for the same surplus generation.
4. **Lesson:** Use multi-year weather and imperfect forecasts to test whether the threshold survives reliability stress.
5. **Lesson:** Add contracts or tariffs that let flexible loads access MC_flex.

### 5 Future Research Questions

1. **Lesson:** How does the 25% flexible-load threshold change under zonal or nodal transmission limits?
2. **Lesson:** Can flexible data-center demand compete with electrolysis for surplus VRE without raising firm-load costs?
3. **Lesson:** What H2 storage duration is needed when electrolysis capacity factors collapse in July and August?
4. **Lesson:** Which tariff design lets electrolyzers access low MC_flex while paying a fair share of capacity cost?
5. **Lesson:** How do SMR-backed firm generation and VRE surplus change the cost split between firm and flexible loads?
