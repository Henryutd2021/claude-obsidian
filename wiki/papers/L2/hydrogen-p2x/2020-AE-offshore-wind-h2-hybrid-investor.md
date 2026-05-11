---
zotero_key: 4UG5EFDW
title: "Hydrogen from offshore wind: Investor perspective on the profitability of a hybrid system including for curtailment"
journal: "Applied Energy"
year: 2020
doi: "10.1016/j.apenergy.2020.114732"
topic: [offshore-wind, green-hydrogen, power-to-gas, curtailment, techno-economic-analysis, investor-npv]
paper_type: [modeling, TEA, scenario-analysis, simulation, hybrid]
main_contribution: [case-study-rigor, parameter-anchor, sensitivity-depth, engineering-feasibility, policy-relevance]
method_type: [custom-hourly-simulation, NPV, LCOE, LCOH, sensitivity-analysis]
journal_role: applied_flagship
ingest_depth: A_deep
subdomain_primary:
  - hydrogen-p2x
subdomain_secondary:
  - power-systems
  - energy-policy-economics
  - re-tech-resources
data_assets:
  main_pdf: false
  supplementary: false
  source_data: false
  data_statement: false
  code_statement: false
  code_repository: false
relevance_to_my_research: high
ingest_status: reviewed
address: c-000026
created: 2026-05-11
tags:
  - paper-analysis
  - L2
  - A-deep
---

# Hydrogen from offshore wind: Investor perspective on the profitability of a hybrid system including for curtailment

> Zotero: `4UG5EFDW` · DOI: 10.1016/j.apenergy.2020.114732 · Journal: Applied Energy (2020) · **L2 applied flagship**

## 1. Positioning

**One-sentence contribution**: Evidence: McDonagh et al. model a 504 MW Irish Sea OWF under electricity-only, H2-only, and hybrid PtG revenue cases, then compare investor interest by NPV.

**Applied-paper sub-type**: Evidence: techno-economic analysis plus hourly wind and price simulation for offshore wind to H2. Inference: high confidence, the value is investor-threshold framing, not a new algorithm.

**Primary value source(s)**: Evidence: The paper combines historical wind, simulated SMC, curtailment construction, 2030 costs, LCOE, LCOH, and NPV. Lesson: Report the H2 value at which PtG beats the baseline asset, not only LCOH.

## 2. Applied-strength table (11 dimensions)

| Dimension | Strength (1-5) | Evidence | Reusable Element | Comment |
|---|---:|---|---|---|
| Model structure | 4 | Evidence: Sec. 2 separates OWF output, SMC/load simulation, curtailment, set-point dispatch, and economics. | Modular OWF plus PtG TEA. | Portable to renewable-H2 assets. |
| System boundary | 3 | Evidence: Includes OWF, electrolysis, compression, storage, power revenue, H2 revenue, curtailment, O&M, CAPEX, and DECEX. | Asset-owner boundary. | Gap: no delivery logistics, tax, financing, or grid reinforcement. |
| Data source | 4 | Evidence: Uses historical wind, SMC, and load data, with appendix validation. | Hourly data spine. | Lesson: Anchor scenarios in measured series. |
| Parameter setting | 4 | Evidence: Tables 1 to 2 provide 2030 costs, O&M, discount rate, H2 value, HHV, and lifetime. | Parameter bank rows. | Label as 2030 European offshore-wind PtG. |
| Case design | 4 | Evidence: 504 MW Irish Sea OWF, 14.5 km from shore, 63 turbines of 8 MW, 110 m hub height. | Case-selection logic. | High-resource, near-shore, grid-constrained case is credible. |
| Scenario design | 4 | Evidence: Compares electricity-only, H2-only, and hybrid dispatch across H2 value and curtailment levels. | Baseline/alternative/hybrid triad. | Lesson: Keep incumbent investor option visible. |
| Sensitivity analysis | 4 | Evidence: Varies H2 value, wind CAPEX, H2 CAPEX, discount rate, lifetime, and efficiency. | LCOH plus NPV sensitivity. | Strong for ranking levers. |
| Uncertainty analysis | 2 | Evidence: Uses deterministic scenario sweeps, not distributions or Monte Carlo. | Missing-uncertainty audit. | Lesson: Add probability bands for publishable investment risk. |
| Results presentation | 4 | Evidence: Figures show NPV thresholds, PtG capacity, curtailment intensity, LCOH sensitivity, and NPV sensitivity. | Investor-threshold figures. | Applied-reader friendly. |
| Engineering feasibility | 4 | Evidence: Justifies PEM electrolysis, compression to 500 bar, 24 h storage, and onshore siting. | Component rationale. | Lesson: Pair each cost with a siting or operation reason. |
| Policy relevance | 3 | Evidence: Discusses incentives, diesel displacement, marginal abatement cost, and system benefits. | H2 credit framing. | Needs welfare accounting for a broader policy claim. |

**Top 3 strengths**:
1. Evidence: Key breakpoints include LCOH EUR3.77/kg H2 and hybrid parity around EUR4.25/kg H2 at 10% curtailment.
2. Evidence: Hour-level curtailment depth controls PtG use; annual curtailment percentage alone is weak.
3. Lesson: Reuse the electricity-only, H2-only, hybrid option triad.

**Top 3 weaknesses or gaps**:
1. Evidence: All hydrogen is assumed sellable at fixed producer value. Inference: high confidence, offtake depth is the largest gap.
2. Evidence: Financing, taxes, delivery cost, oxygen revenue, and grid reinforcement are outside the boundary.
3. Lesson: Separate producer H2 value, delivered H2 cost, and contracted demand.

## 3. Method blueprint

**Objective function**: Evidence: Compare project NPV across electricity-only, H2-only, and hybrid cases; LCOE and LCOH are diagnostics.

**Decision variables**: Evidence: Configuration, PtG capacity ratio, H2 value, curtailment level, and set-point price.

**Constraints**: Evidence: Hourly OWF output, SNSP-style curtailment, PtG capacity, fixed H2 sale value, 24 h storage, and efficiency.

**Inputs (data + parameters)**: Evidence: Historical wind, SMC, and load; 2030 costs; 6% discount rate; 25-year life; 39.4 kWh/kg H2 HHV; EUR3 to EUR5/kg H2 values.

**Outputs (decision + diagnostic metrics)**: Evidence: hourly revenue, LCOE, LCOH, NPV, break-even H2 value, curtailment thresholds, PtG response, and sensitivity ranking.

**System boundary**: Evidence: Inside: OWF, PEM electrolysis, compression, storage, power/H2 revenue, O&M, CAPEX, DECEX. Outside: delivery, taxes, financing, grid expansion, and competing H2 supply.

**Temporal resolution**: Evidence: Hourly model over 25 years; half-hourly SMC is averaged.

**Spatial resolution**: Evidence: One Irish Sea OWF case plus jurisdiction-level market, load, and curtailment context.

**Method novelty (Inference)**: Inference: high confidence, the method contribution is hybrid dispatch plus investor-threshold diagnosis, not mathematical optimization novelty.

**Transferable to Henry's work**: Lesson: Reuse the set-point rule, baseline NPV benchmark, and curtailment depth check.

## 4. Parameter & assumption table

| Parameter / Assumption | Value or range | Year / context | Source | Reusable for Henry? | Note |
|---|---|---|---|---|---|
| OWF capacity | 504 MW | 2030 Irish Sea case | Sec. 2.1.1 | yes | 63 turbines at 8 MW each. |
| Distance to shore | 14.5 km | Irish Sea case | Sec. 2.1.1 | yes | Near-shore case affects H2 cost. |
| OWF capacity factor | 47.5% | Losses included, before curtailment | Sec. 3.1 | yes | Useful offshore-wind H2 anchor. |
| Wind turbine CAPEX | EUR1,500,000/MW | 2030 base | Table 1 | yes | O&M 3%/yr; DECEX 10% final year. |
| Electrolysis plus compression CAPEX | EUR850,000/MW | 2030 onshore PtG | Table 1 | yes | O&M 3.2%/yr; 15% balance of plant. |
| Hydrogen storage | EUR6000/MW-hour | 24 h full-load storage | Table 1 | yes | Storage tied to PtG power. |
| Discount rate | 6% | 2030 low-risk project | Table 2 | yes | Sensitive economic input. |
| H2 value | EUR3 to EUR5/kg H2; base EUR4/kg H2 | Producer value | Table 2 | yes | May include incentive. |
| H2 HHV | 39.4 kWh/kg H2 | Model constant | Table 2 | yes | Diesel-equivalence input. |

**Parameters worth migrating into `wiki/banks/parameter-bank/`**: `offshore-wind-capex-2030.md`, `pem-electrolysis-compression-capex-2030.md`, `hydrogen-storage-power-hour-cost.md`, `green-h2-producer-value.md`, `offshore-wind-h2-lcoh.md`, `discount-rate-low-risk-energy-project.md`, `hydrogen-hhv.md`, `offshore-wind-capacity-factor.md`.

## 5. Case study design

**Case selected**: Evidence: A 504 MW offshore wind farm in the Irish Sea, 14.5 km from shore, 63 LEANWIND 8 MW turbines, 110 m hub height, modeled for 2030.

**Why this case**: Evidence: The authors choose a project under consideration in Europe, where near-shore high-resource conditions make PtG plausible. Inference: high confidence, the case is favorable but not purely stylized.

**Representativeness**: Evidence: The appendix frames the Irish market as high-wind, grid-managed, and limited-interconnection. Inference: medium confidence, transfer is strongest to constrained high-wind grids.

**Data realism**: Evidence: Historical wind, SMC, and load data support the hourly model. Gap: H2 demand is represented by fixed producer value, not a measured offtake profile.

**Generalizability (Inference)**: Inference: medium confidence, the workflow transfers if local hourly output, price/load, curtailment rule, and H2 value are rebuilt.

**Lesson for Henry's own case design**: Lesson: Pick cases where resource quality, grid constraint, and investor choice collide.

## 6. Sensitivity / uncertainty / robustness

**Sensitivity variables and ranges**:

| Variable | Range or case | Finding | Source |
|---|---|---|---|
| Hydrogen value | EUR3 to EUR5/kg H2 | Evidence: H2 value dominates NPV; EUR3/kg H2 fails. | Sec. 3.3 |
| Curtailment | 0 to 30% and thresholds | Evidence: at EUR4/kg H2, about 17% curtailment is needed for hybrid NPV parity. | Highlights, conclusion |
| H2 CAPEX | EUR850k/MW base; about 30% fall | Evidence: a 30% reduction can make hybrid match OWF-only at 10% curtailment. | Sec. 3.5 |
| Lifetime | 25 to 32 years | Evidence: LCOH falls from EUR3.77/kg H2 to about EUR3.5/kg H2. | Sec. 3.5 |
| PtG efficiency | 4.8 to 4.6 kWh/m3 | Evidence: LCOH falls to EUR3.61/kg H2 and NPV rises to EUR202M. | Sec. 3.5 |

**Most influential variable (Evidence)**: Evidence: Hydrogen value has the greatest effect on NPV; among endogenous variables, wind CAPEX, H2 CAPEX, and discount rate lead.

**Uncertainty analysis present**: Evidence: Partial. The paper uses deterministic sensitivity and scenario brackets, not probability distributions.

**Robustness checks present**: Evidence: Appendix validation checks market/load simulation and LCOE plausibility. Inference: medium confidence, market-structure robustness is still absent.

**Missing analyses (gaps)**: Evidence: No demand limit, offtake shape, debt structure, delivery logistics, taxes, or competitor H2 supply curve.

**Lesson for Henry's sensitivity design**: Lesson: Put H2 value, curtailment intensity, CAPEX, discount rate, lifetime, efficiency, and demand limit first.

## 7. Results & figures table

| Item | Shows | Argument function | Applied-typical or top-journal-typical? | Lesson for Henry |
|---|---|---|---|---|
| Fig. 1 | Evidence: OWF-only NPV declines with curtailment; H2-only NPV varies by H2 value. | Baseline and H2-only breakpoints. | Applied-typical | Put baseline and alternative on one axis. |
| Fig. 2 | Evidence: Hybrid NPV changes with PtG capacity, H2 value, and curtailment. | Tests option-value business case. | Applied-typical | Plot capacity ratio, not only optimum. |
| Fig. 3 | Evidence: Mean hourly curtailment intensity by total curtailment scenario. | Explains threshold mechanism. | Top-journal-typical potential | Use this as the mechanism figure. |
| Fig. 4 | Evidence: LCOH response from base EUR3.77/kg H2. | Identifies cost drivers. | Applied-typical | Pair with parameter-bank extraction. |
| Fig. 5 | Evidence: NPV response from base EUR117M at EUR4/kg H2. | Shows investor exposure. | Applied-typical | Pair cost and investor sensitivity. |
| Table 1 | Evidence: CAPEX, O&M, overhaul, water, storage cost. | Parameter spine. | Applied-typical | Make assumptions extractable. |
| Table 2 | Evidence: discount rate, H2 value, HHV, lifetime. | Economic base case. | Applied-typical | Put value assumptions beside physics. |

## 8. Comparison with top-journal style

**What makes this an applied paper (vs. Nature Energy / Joule)?** Evidence: The paper solves a project-level investor question for one offshore-wind-to-H2 case. Inference: high confidence, it is asset-specific and deterministic rather than field-level.

**Where is this paper already close to top-journal quality?** Evidence: Curtailment intensity explains why total curtailed energy can mislead PtG sizing. Inference: medium confidence, this can support a broader H2-curtailment rule.

**To upgrade this paper to top-journal target, the author would need to**:
- Lesson: Reframe from project profitability to a cross-market rule for bankable curtailment-to-H2 value.
- Lesson: Replace fixed H2 value with sectoral offtake curves for refinery, trucking, ammonia, ferry, or storage demand.
- Lesson: Compare offshore-wind H2 with onshore wind, solar import, grid-connected electrolysis, and fossil H2 with carbon pricing.
- Lesson: Add probabilistic CAPEX, power-price, curtailment, and H2-value uncertainty.
- Lesson: Compress the story into one mechanism figure linking curtailed-hour structure, price floor, PtG sizing, NPV, and policy credit.

**Upgrade lesson for Henry**: Lesson: Lift L2 hydrogen TEA by changing the decision rule, not by adding local parameter detail.

## 9. Direct value for Henry

**Citable background claims**: Evidence: LCOH is EUR3.77/kg H2 for the 2030 H2-only OWF case; hybrid profitability depends more on H2 value than curtailment recovery.

**Reusable methods / model components**: Evidence: Set-point dispatch converts power to H2 when SMC falls below H2-equivalent revenue and uses PtG for curtailed power.

**Reusable parameters or data**: Evidence: Tables 1 to 2 supply CAPEX, O&M, lifetime, discount rate, HHV, storage sizing, and H2 value assumptions.

**Case-study design lessons**: Lesson: Use a case where resource, grid constraint, and investor decision all matter; the 14.5 km near-shore Irish Sea case does that.

**Sensitivity-design lessons**: Lesson: Vary H2 value, curtailment intensity, discount rate, lifetime, CAPEX, efficiency, and demand limit; LCOH and NPV can move differently.

**Figure types worth borrowing**: Lesson: Borrow the threshold logic in Figs. 1 to 2 and the curtailment-intensity mechanism in Fig. 3.

**Future research questions inspired by this paper**: Lesson: Test demand-limited PtG sizing, policy credits, imported H2 competition, avoided grid cost, and stochastic prices.

## 10. KB outputs (mandatory)

### Technical Method Card

- **Method name**: Evidence: Hourly offshore-wind PtG investor-threshold model.
- **Applicable problem**: Lesson: Use when a renewable generator can sell electricity, convert to H2, or split output.
- **Inputs**: Evidence: hourly power, SMC, load, curtailment rule, OWF/PtG cost, storage, efficiency, H2 value, discount rate, lifetime.
- **Outputs**: Evidence: NPV, LCOE, LCOH, parity H2 value, curtailment threshold, PtG capacity response, sensitivity ranking.
- **Key assumptions**: Evidence: fixed H2 value, all H2 sold, same owner, constant efficiency, no taxes, no delivery station, no financing structure.
- **Advantages**: Inference: high confidence, the method makes H2 conversion compete against the incumbent electricity sale.
- **Limitations**: Evidence: no demand limit, stochastic uncertainty, detailed financing, delivered-H2 logistics, or competitor supply curve.
- **How to migrate into Henry's work**: Lesson: Implement set-point dispatch and NPV baseline; then add demand limits and uncertainty.

### Parameter Card

| Parameter | Value | Unit | Year | Source | Bank page candidate |
|---|---|---|---|---|---|
| OWF capacity | 504 | MW | 2030 | Sec. 2.1.1 | `offshore-wind-reference-project.md` |
| Distance to shore | 14.5 | km | 2030 | Sec. 2.1.1 | `offshore-wind-site-distance.md` |
| OWF capacity factor | 47.5 | % | 2030 | Sec. 3.1 | `offshore-wind-capacity-factor.md` |
| Wind turbine CAPEX | 1,500,000 | EUR/MW | 2030 | Table 1 | `offshore-wind-capex-2030.md` |
| Electrolysis plus compression CAPEX | 850,000 | EUR/MW | 2030 | Table 1 | `pem-electrolysis-compression-capex-2030.md` |
| Hydrogen storage | 6000 | EUR/MW-hour | 2030 | Table 1 | `hydrogen-storage-power-hour-cost.md` |
| Discount rate | 6 | % | 2030 | Table 2 | `discount-rate-low-risk-energy-project.md` |
| H2-only LCOH | 3.77 | EUR/kg H2 | 2030 | Sec. 3.2 | `offshore-wind-h2-lcoh.md` |
| Hybrid parity H2 value at 10% curtailment | 4.25 | EUR/kg H2 | 2030 | Sec. 3.3 | `green-h2-producer-value.md` |
| H2 HHV | 39.4 | kWh/kg H2 | constant | Table 2 | `hydrogen-hhv.md` |

### Case Study Card

- **Case**: Evidence: 504 MW Irish Sea OWF, 14.5 km from shore, 2030 operation, with onshore PEM electrolysis, compression, and 24 h storage.
- **Selection logic**: Evidence: near-shore, high-resource, Europe-led OWF deployment, and curtailment exposure.
- **Data realism**: Evidence: historical wind, market-price, and load data support hourly simulation; H2 demand is stylized through fixed producer value.
- **Generalizability**: Inference: medium confidence, transferable to constrained high-wind grids if local price, curtailment, and offtake data are rebuilt.
- **Transferability to Henry's projects**: Lesson: Use as an L2 benchmark for wind-solar-hydrogen TEA and investor-threshold writing.

### 5 Applied-Paper Writing Lessons

1. Lesson: Start with the investor decision, then make every method choice serve that decision.
2. Lesson: Keep the baseline asset visible; PtG must beat electricity-only NPV, not only look good alone.
3. Lesson: Build parameter tables that a later reader can migrate directly into banks.
4. Lesson: Explain curtailment with both annual loss and hour-level intensity.
5. Lesson: Separate producer H2 value, delivered H2 cost, and policy incentive.

### 5 Upgrade Notes (how to lift this kind of paper toward L1)

1. Lesson: Move from one project to a cross-market typology of when hydrogen captures curtailment value.
2. Lesson: Replace fixed H2 value with demand and offtake scenarios.
3. Lesson: Add imported renewable H2 and grid-connected electrolysis as competitors.
4. Lesson: Use uncertainty distributions for CAPEX, power price, curtailment, and policy support.
5. Lesson: Add a mechanism figure linking price floor, curtailed-hour structure, PtG capacity, and NPV parity.

### 5 Future Research Questions

1. Question: How does a demand-limited H2 offtake contract change optimal PtG capacity?
2. Question: Which curtailment frequency and depth combinations make PtG bankable across multiple grids?
3. Question: How would offshore-wind H2 compete with imported solar-derived H2?
4. Question: Can hybrid PtG reduce grid reinforcement or balancing costs enough to justify an incentive?
5. Question: How does stochastic power-price volatility change the H2 set-point dispatch rule?
