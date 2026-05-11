---
zotero_key: "DBULMZ89"
title: "Impacts of renewable hydrogen production from wind energy in electricity markets on potential hydrogen demand for light-duty vehicles"
journal: "Applied Energy"
year: 2019
doi: "10.1016/j.apenergy.2018.10.067"
topic: [renewable-hydrogen, wind-to-hydrogen, light-duty-vehicles, ercot, electricity-markets, texas-triangle, electrolyzer-dispatch]
paper_type: [modeling, TEA, optimization, scenario-analysis, simulation]
main_contribution: [system-boundary-expansion, parameter-anchor, case-study-rigor, sensitivity-depth, engineering-feasibility, policy-relevance]
method_type: [LP, Pyomo, CPLEX, first-order-engineering-model, county-level-demand-model]
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
  data_statement: false
  code_statement: false
  code_repository: false
relevance_to_my_research: high
ingest_status: reviewed
address: c-000028
created: 2026-05-11
tags:
  - paper-analysis
  - L2
  - A-deep
---

# Impacts of renewable hydrogen production from wind energy in electricity markets on potential hydrogen demand for light-duty vehicles

> Zotero: `DBULMZ89` · DOI: `10.1016/j.apenergy.2018.10.067` · Journal: Applied Energy (2019) · L2 applied flagship

## 1. Positioning

**One-sentence contribution**: Evidence: The paper links a county-level LDV hydrogen demand model with an hourly wind-to-hydrogen LP that chooses between selling ERCOT wind electricity and producing hydrogen at a marginal hydrogen price.

**Applied-paper sub-type**: Evidence: Hydrogen system analysis plus electricity-market dispatch plus demand-potential estimation, with Texas as the main case and six other U.S. markets as sensitivity cases.

**Primary value source(s)**: Inference, high confidence: The value is the demand-supply coupling: demand is mapped spatially, while supply is optimized temporally against day-ahead prices. Lesson: For Henry's wind-solar-H2 work, pair a demand geography with an hourly dispatch rule so the case speaks to both siting and operation.

## 2. Applied-strength table (11 dimensions)

| Dimension | Strength (1-5) | Evidence | Reusable Element | Comment |
|---|---:|---|---|---|
| Model structure | 4 | Evidence: Section 3 demand equations plus LP Eq. 8a-8d. | Demand-dispatch workflow. | Lesson: Couple space and time. |
| System boundary | 4 | Evidence: LDV demand, wind, hub prices, electrolysis, compression, grid sale. | Electron/molecule allocation. | Inference, high confidence: Transport and storage excluded. |
| Data source | 4 | Evidence: EIA, Census, NHTS, ERCOT, and six ISO/RTO datasets. | Public-data stack. | Lesson: Trace every dataset. |
| Parameter setting | 4 | Evidence: 67 MPGe, 25 MPG, ratio 2.5, 75 percent efficiency, $0-5/kg H2. | Screening assumptions. | Inference, medium confidence: Simple but reusable. |
| Case design | 5 | Evidence: Texas combines wind, ERCOT, H2 infrastructure, and Triangle demand. | Texas H2 case. | Lesson: Make resource-market-demand tension visible. |
| Scenario design | 4 | Evidence: Hubs, years, H2 prices, efficiencies, and markets are varied. | Scenario grid. | Lesson: Link axes to decisions. |
| Sensitivity analysis | 4 | Evidence: Section 4.6 compares seven electricity markets. | Cross-market sensitivity. | Inference, high confidence: Strong transfer test. |
| Uncertainty analysis | 2 | Evidence: No Monte Carlo or distributions. | Gap for Henry. | Lesson: Add price, CAPEX, and wind uncertainty. |
| Results presentation | 4 | Evidence: Figs. 5-19 span maps, thresholds, and heatmaps. | Map plus dispatch stack. | Inference, high confidence: Audit-friendly. |
| Engineering feasibility | 3 | Evidence: Electrolysis and compression included; delivered H2 cost excluded. | Marginal-dispatch layer. | Lesson: Add infrastructure cost. |
| Policy relevance | 3 | Evidence: Texas is compared with ZEV states. | ZEV transport framing. | Inference, medium confidence: Context, not constraint. |

**Top 3 strengths**:
1. Evidence: Links LDV demand with hourly wind-H2 production.
2. Evidence: Uses 2011-2015 ERCOT wind and hub prices.
3. Evidence: Tests seven markets and four efficiencies.

**Top 3 weaknesses or gaps**:
1. Evidence: Facility and H2 transport costs are excluded.
2. Evidence: Non-ERCOT markets use Texas wind.
3. Inference, high confidence: The LP is a screen, not infrastructure planning.

## 3. Method blueprint

**Objective function**: Evidence: Eq. 8a maximizes annual revenue from grid electricity sale plus hydrogen production across 8760 hourly steps.

**Decision variables**: Evidence: The LP chooses electricity sold to grid `x_g`, electricity used for hydrogen `x_h`, and hourly hydrogen production `h_t`.

**Constraints**: Evidence: Eq. 8b allocates wind output, Eq. 8c converts electricity to H2 with `alpha`, and Eq. 8d enforces nonnegative variables.

**Inputs (data + parameters)**: Evidence: Inputs include county demand data, FCEV/ICE efficiency, ERCOT wind, hub and ISO/RTO prices, electrolyzer efficiency, compression energy, and H2 price.

**Outputs (decision + diagnostic metrics)**: Evidence: Outputs include H2 demand, H2 production, price thresholds, electrolyzer capacity, capacity factor, and market heatmaps.

**System boundary**: Evidence: Inside the boundary are LDV gasoline displacement, wind allocation, electrolysis, compression, and revenue from grid sale or H2. Inference, high confidence: H2 storage, pipeline or truck delivery, refueling stations, water, fixed O&M, and emissions accounting are outside scope.

**Temporal resolution**: Evidence: One-hour intervals over 8760 time steps.

**Spatial resolution**: Evidence: Demand is U.S. county-level; supply centers on Texas wind and ERCOT hubs.

**Method novelty (Inference)**: Inference, high confidence: The reusable contribution is not the LP itself; it is the coupling of county LDV demand with market-responsive wind-H2 production.

**Transferable to Henry's work**: Lesson: Use this LP as a screening module, then extend it with storage state, electrolyzer CAPEX, delivered H2 cost, carbon rules, and hybrid wind-solar supply.

## 4. Parameter & assumption table

| Parameter / Assumption | Value or range | Year / context | Source | Reusable for Henry? | Note |
|---|---|---|---|---|---|
| LDV H2 demand | 53.3 / 5.3 / 3.9 billion kg/year | U.S. / Texas / Texas Triangle | Abstract, Fig. 5 | yes | Demand benchmarks. |
| FCEV fuel economy | 67 MPGe | Toyota Mirai basis | Section 3.1 | yes | Used for H2 demand conversion. |
| ICE fuel economy | 25 MPG | LDV baseline | Section 3.1 | yes | Gasoline baseline. |
| FCEV/ICE ratio | 2.5 | 67 MPGe / 25 MPG | Section 3.1 | yes | Gasoline to H2. |
| Electrolyzer efficiency | 75 base; 60/75/90/100 sweep | ERCOT and sensitivity cases | Sections 4.2-4.3 | yes | Core production sensitivity. |
| Compression energy context | 4.07 kWh/kg H2 | 700 bar | Section 3.2 | yes | Check source units before reuse. |
| H2 price sweep | $0-5/kg, $0.1 step | Sensitivity case | Section 4.3 | yes | Dispatch revenue axis. |
| Wind-H2 production | 0.84 billion kg/year | 2015 Texas wind, 75 percent, $4/kg | Fig. 11 | yes | 22 percent of Triangle demand. |
| ERCOT thresholds | $21.6/MWh and $82.6/MWh | $1/kg and $4/kg H2 | Fig. 14 | yes | Dispatch thresholds. |
| Electrolyzer CAPEX proxy | $900/kW | Capital scale only | Section 4.5 | maybe | Not full delivered-cost TEA. |

**Parameters worth migrating into `wiki/banks/parameter-bank/`**: `ldv-hydrogen-demand.md`, `fcev-ice-conversion.md`, `electrolyzer-efficiency.md`, `hydrogen-price-sweep.md`, `ercot-h2-price-threshold.md`, `wind-h2-production-potential.md`.

## 5. Case study design

**Case selected**: Evidence: The main case is Texas and ERCOT, with U.S. county LDV demand and supply-side wind-to-H2 dispatch using Texas wind output and ERCOT hub prices.

**Why this case**: Evidence: The paper cites Texas wind capacity, ERCOT's standalone grid, existing H2 infrastructure, high CO2 emissions, and the Texas Triangle. Inference, high confidence: The case works because wind-rich west Texas and demand-rich urban Texas are not co-located.

**Representativeness**: Inference, medium confidence: Texas represents wind-heavy markets with nighttime low prices and large transport demand. It is less representative for solar-led markets or regions without H2 infrastructure.

**Data realism**: Evidence: The study uses observed gasoline, population, rurality, travel, wind, and day-ahead price datasets.

**Generalizability (Inference)**: Inference, medium confidence: The demand method transfers across U.S. counties; the supply method transfers where hourly renewable output and price series exist.

**Lesson for Henry's own case design**: Lesson: Pick a case where resource, market, and demand form a visible tension. That gives reviewers a reason to care about the geography.

## 6. Sensitivity / uncertainty / robustness

**Sensitivity variables and ranges**:

| Variable varied | Range | Finding | Source | Henry use |
|---|---|---|---|---|
| H2 price | $0-5/kg, $0.1 steps | Production rises and levels off above $3/kg. | Figs. 11-12 | Revenue threshold sweep. |
| Electrolyzer efficiency | 60/75/90/100 percent | Higher efficiency raises threshold electricity prices. | Fig. 15 | Technology sweep. |
| ERCOT hub | Houston, North, South, West | West negative prices favor low-price H2 in 2011, 2012, and 2015. | Table 2 | Locational price test. |
| Year | 2011-2015 | At $4/kg, production rises mainly with wind additions. | Fig. 10 | Buildout sensitivity. |
| Market | ERCOT, SPP, MISO, PJM, NYISO, ISO-NE, CAISO | Most markets favor early-morning H2 at $1/kg; CAISO daytime is less attractive. | Figs. 18-19 | Transfer test. |

**Most influential variable (Evidence)**: Evidence: Marginal H2 price changes the dispatch threshold from $21.6/MWh at $1/kg to $82.6/MWh at $4/kg in Fig. 14.

**Uncertainty analysis present**: Evidence: No stochastic uncertainty analysis is reported; the paper uses historical comparisons and scenario sweeps.

**Robustness checks present**: Evidence: County gasoline estimates are checked against EIA state totals, with 1.32 percent average deviation and 5.1 percent maximum deviation in Fig. 9. Evidence: Market transfer is explored with seven ISO/RTO price series.

**Missing analyses (gaps)**: Inference, high confidence: Missing axes include CAPEX learning, O&M, storage, delivery, water, adoption, curtailment, and carbon intensity.

**Lesson for Henry's sensitivity design**: Lesson: Keep the price-threshold and cross-market sweeps, but add delivered-cost and infrastructure-cost sweeps before making a finance claim.

## 7. Results & figures table

| Item | Shows | Argument function | Applied-typical or top-journal-typical? | Lesson for Henry |
|---|---|---|---|---|
| Fig. 1 | Evidence: Workflow. | Model coupling. | applied-typical | Lesson: Workflow first. |
| Fig. 2 | Evidence: Efficiency curve. | Conversion input. | applied-typical | Lesson: Show physics. |
| Fig. 3 | Evidence: Wind split. | Operating choice. | applied-typical | Lesson: Draw the boundary. |
| Fig. 4 | Evidence: West hub prices. | Low-price window. | applied-typical | Lesson: Show price shape. |
| Fig. 5 | Evidence: County demand map. | Demand clusters. | top-journal-typical | Lesson: Map demand. |
| Fig. 6 | Evidence: State demand plus ZEV states. | Policy comparison. | applied-typical | Lesson: Use compact overlays. |
| Fig. 7 | Evidence: County demand histogram. | Demand skew. | applied-typical | Lesson: Pair map and histogram. |
| Fig. 8 | Evidence: Rural/urban intensities. | Correction factor. | applied-typical | Lesson: Show adjustments. |
| Fig. 9 | Evidence: EIA deviation. | Demand validation. | applied-typical | Lesson: Add checks. |
| Fig. 10 | Evidence: H2 by hub/year/price. | Price effect. | applied-typical | Lesson: Split price cases. |
| Fig. 11 | Evidence: H2 by efficiency/price. | Plateau above $3/kg. | applied-typical | Lesson: Use two-axis sweeps. |
| Fig. 12 | Evidence: Difference plot. | Marginal response. | applied-typical | Lesson: Show derivatives. |
| Fig. 13 | Evidence: Hourly H2 at $1/$4. | 1-6 a.m. window. | applied-typical | Lesson: Use hourly box plots. |
| Fig. 14 | Evidence: Price-H2 thresholds. | Dispatch rule. | applied-typical | Lesson: Extract thresholds. |
| Fig. 15 | Evidence: Threshold curves. | General rule. | top-journal-typical | Lesson: Build decision curves. |
| Fig. 16 | Evidence: Capacity and factor. | Sizing link. | applied-typical | Lesson: Report capacity factor. |
| Fig. 17 | Evidence: CAPEX and revenue scale. | Finance scale. | applied-typical | Lesson: Scope finance claims. |
| Fig. 18 | Evidence: Market heatmaps. | Seven-market comparison. | top-journal-typical | Lesson: Make sensitivity visual. |
| Fig. 19 | Evidence: $1/kg market box plots. | Transfer test. | applied-typical | Lesson: Show distributions. |
| Tab. 1 | Evidence: ZEV and Texas demand. | Policy table. | applied-typical | Lesson: Keep policy compact. |
| Tab. 2 | Evidence: Hub price statistics. | West hub rationale. | applied-typical | Lesson: Use price tables. |

## 8. Comparison with top-journal style

**What makes this an applied paper (vs. Nature Energy / Joule)?** Inference, high confidence: The paper asks an engineering feasibility question for one technology route and one main case. The central claim is regional and operational, not a field-level reframing of hydrogen mobility or renewable integration.

**Where is this paper already close to top-journal style?** Inference, medium confidence: Figs. 5, 15, and 18 have wider use because they map demand, turn dispatch into threshold curves, and compare markets.

**To upgrade this paper to a top-journal target, the author would need to**:
- Lesson: Reframe from a Texas supply-demand case to a general rule for market, resource, and demand alignment.
- Lesson: Replace Texas wind dropped into other markets with regional wind profiles and demand clusters.
- Lesson: Add delivered H2 cost, storage, transport, and refueling infrastructure.
- Lesson: Include emissions accounting and FCEV adoption scenarios.
- Lesson: Merge demand geography, threshold curves, and market heatmaps into one design-rule figure.

**Upgrade lesson for Henry**: Lesson: Turn local dispatch into a general siting rule.

## 9. Direct value for Henry

**Citable background claims**: Evidence: U.S., Texas, and Texas Triangle LDV H2 demand are 53.3, 5.3, and 3.9 billion kg/year. Evidence: 2015 Texas wind could produce 0.84 billion kg H2/year, about 22 percent of Texas Triangle demand.

**Reusable methods / model components**: Evidence: Eq. 8a-8d gives a minimal LP for choosing grid sale versus H2 production. Lesson: Use it as a screening model before adding storage and infrastructure.

**Reusable parameters or data**: Evidence: Reusable values include 67 MPGe FCEV, 25 MPG ICE, 2.5 fuel ratio, 75 percent base electrolyzer efficiency, $0-5/kg H2 price sweep, and ERCOT hub prices.

**Case-study design lessons**: Lesson: Choose cases where resource, market, and demand are each visible and imperfectly aligned.

**Sensitivity-design lessons**: Lesson: Use three layers: H2 price for revenue, electrolyzer efficiency for conversion, and market series for transferability.

**Figure types worth borrowing**: Lesson: Borrow the county demand map, threshold electricity-price curves, time-of-day box plots, and cross-market heatmaps.

**Future research questions inspired by this paper**:
1. Lesson: How does delivered H2 cost change when ERCOT wind-to-H2 dispatch includes pipelines, trucks, storage, and refueling stations?
2. Lesson: Does adding solar smooth the low-price production window or dilute the nighttime wind-price advantage?
3. Lesson: Which U.S. market best overlaps low electricity prices, renewable output, and LDV demand clusters?
4. Lesson: How much FCEV adoption is needed before electrolyzer sizing changes?
5. Lesson: How do carbon-intensity constraints alter price-threshold dispatch?

## 10. KB outputs (mandatory)

### Technical Method Card

- **Method name**: County LDV H2 demand plus hourly wind-H2 price-threshold dispatch.
- **Applicable problem**: Evidence: Estimate LDV H2 demand and dispatch wind electricity between grid sale and H2.
- **Inputs**: Evidence: County demand data, wind output, prices, electrolyzer efficiency, compression energy, and H2 price.
- **Outputs**: Evidence: H2 demand, production, price thresholds, electrolyzer sizing, and market comparisons.
- **Key assumptions**: Evidence: One-hour resolution, 8760 steps, 75 percent base efficiency, 2.5 FCEV/ICE ratio, and no delivered-cost model.
- **Advantages**: Inference, high confidence: Fast screening before detailed TEA.
- **Limitations**: Evidence: Facility and transport costs are excluded; non-ERCOT markets use Texas wind.
- **How to migrate into Henry's work**: Lesson: Add storage, CAPEX, transport, carbon rules, and hybrid wind-solar supply.

### Parameter Card

| Parameter | Value | Unit | Year | Source | Bank page candidate |
|---|---:|---|---|---|---|
| LDV H2 demand | 53.3 / 5.3 / 3.9 | billion kg/year | U.S. / Texas / Texas Triangle | Abstract, Fig. 5 | `ldv-hydrogen-demand.md` |
| FCEV/ICE ratio | 2.5 | ratio | 67 MPGe / 25 MPG | Section 3.1 | `fcev-ice-conversion.md` |
| Electrolyzer efficiency | 75 | percent | base case | Sections 4.2-4.4 | `electrolyzer-efficiency.md` |
| H2 price sweep | 0-5 | USD/kg | sensitivity | Section 4.3 | `hydrogen-price-sweep.md` |
| Wind-H2 production | 0.84 | billion kg/year | 2015 Texas wind, $4/kg, 75 percent | Fig. 11 | `wind-h2-production-potential.md` |
| ERCOT price thresholds | 21.6 / 82.6 | USD/MWh | $1/kg / $4/kg H2 | Fig. 14 | `ercot-h2-price-threshold.md` |

### Case Study Card

- **Case**: Evidence: U.S. county demand with Texas, ERCOT, and the Texas Triangle as the integrated case.
- **Selection logic**: Evidence: Texas combines wind capacity, ERCOT prices, H2 infrastructure, and large LDV demand.
- **Data realism**: Evidence: Uses public gasoline, population, travel, wind, and price datasets.
- **Generalizability**: Inference, medium confidence: Transfers where hourly renewable output and prices exist.
- **Transferability to Henry's projects**: Lesson: Use as screening template, then add delivered-cost infrastructure.

### 5 Applied-Paper Writing Lessons

1. Lesson: Pair spatial demand with temporal production.
2. Lesson: Make case selection rest on resource, market, and demand facts.
3. Lesson: Validate bottom-up demand estimates.
4. Lesson: Convert dispatch results into reusable threshold curves.
5. Lesson: State missing delivered-cost elements directly.

### 5 Upgrade Notes (how to lift this kind of paper toward L1)

1. Lesson: Use local renewable profiles for each market.
2. Lesson: Add H2 transport, storage, and refueling costs.
3. Lesson: Model FCEV adoption, not only full potential demand.
4. Lesson: Add emissions and carbon-intensity constraints.
5. Lesson: Build one synthesis figure linking demand, thresholds, and market classes.

### 5 Future Research Questions

1. Lesson: What is delivered LCOH after transport and storage?
2. Lesson: Where do wind, solar, low-price hours, and LDV demand overlap?
3. Lesson: How does electrolyzer sizing change under partial FCEV adoption?
4. Lesson: Can west Texas storage serve Texas Triangle demand?
5. Lesson: What carbon rule turns thresholds into green H2 schedules?
