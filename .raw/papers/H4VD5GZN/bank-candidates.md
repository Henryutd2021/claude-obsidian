## Parameter rows (-> wiki/banks/parameter-bank/)

- wind-capex-2019.md | wind fixed capital investment | 1,300 | USD/kWe | 2019 current-cost case | Table 2 | reusable: yes | paired with 43% aggregate capacity factor
- solar-pv-capex-2019.md | solar PV fixed capital investment | 1,300 | USD/kWe | 2019 current-cost case | Table 2 | reusable: yes | single-axis tracking, 28% aggregate capacity factor
- gas-ccs-capex-2019.md | natural gas with 90% CCS fixed capital investment | 2,600 | USD/kWe | 2019 current-cost case | Table 2 | reusable: yes | dispatchable low-carbon proxy
- pem-electrolysis-capex-h2a.md | electrolysis facility fixed capital investment | 1,100 | USD/kWe | 2019 H2A-based case | Table 2 | reusable: yes | stack, BoP, and compressor combined
- battery-storage-capex-2019.md | battery storage fixed capital investment | 370 | USD/kWhe | 2019 Li-ion case | Table 2 | reusable: yes | energy-capacity basis
- pem-electrolysis-efficiency.md | electrolysis facility efficiency | 61 | % LHV | H2A-based case | Section 2.1 and Table 2 | reusable: yes | includes BoP and compressor
- pem-stack-efficiency.md | electrolyzer stack efficiency | 67.7 | % LHV | H2A PEM stack | Section 2.1 | reusable: yes | stack-only value
- battery-roundtrip-efficiency.md | battery round-trip efficiency | 90 | % | 2019 Li-ion case | Table 2 | reusable: yes | used in storage balance
- battery-self-discharge.md | battery self-discharge | 1 | % per month | 2019 Li-ion case | Section 2.1 | reusable: yes | additional battery assumption
- flexible-load-fraction-sweep.md | flexible load fraction | 0 to 1 in 0.01 steps | unitless | all modeled scenarios | Section 2.1 | reusable: yes | 101 cases plus endpoint-adjacent cases

## Sensitivity rows (-> wiki/banks/sensitivity-bank/)

- flexible-load-fraction-threshold.md | flexible load fraction | 0 to 1 | capacity expansion accelerates after roughly 0.2 to 0.3 flexible load fraction | Sections 3.1 and 4.3 | main scenario sweep
- technology-stack-flexibility.md | available technologies | Dispatch; Dispatch+Renew+Storage; Renew+Storage | more system flexibility reduces zero-marginal-cost surplus for electrolysis | Table 1 and Section 4.4 | scenario contrast
- demand-response-exclusion.md | demand response | included versus excluded | excluding demand response increases generation capacity, surplus generation, and system costs | Sections 3.3 and 4.4 | SI details referenced
- cost-reduction-robustness.md | future asset costs | current costs versus reduced-cost cases | authors report no substantial change in main conclusions | Section 4.5 and S.12 pointer | exact SI range not in extracted main text
- pgp-option.md | power-to-gas-to-power availability | absent versus available | PGP used only in Renew+Storage; average electricity cost falls about 10% and curtailed generation falls about 60% | Section 4.4 and S.18 pointer | useful for long-duration storage comparisons
- geography-transmission.md | spatial aggregation and transmission | CONUS copper plate versus smaller constrained regions discussed | smaller regions likely raise variability, capacity need, and surplus opportunity | Section 4.5 | limitation rather than direct sensitivity in main text

## Method rows (-> wiki/banks/method-bank/)

- annual-flexible-load-constraint.md | annual flexible-load constraint | when flexible demand can shift across hours or seasons | input: annual flexible energy; output: hourly electrolysis dispatch and capacity | Section 2.2 | core reusable formulation
- marginal-cost-attribution.md | MC_firm and MC_flex attribution | when firm and flexible loads share one optimized grid | input: average-cost derivative; output: load-specific marginal costs | Section 2.3 | separates capacity cost burden
- capacity-dispatch-lp.md | capacity and dispatch linear optimization | when testing least-cost grid architecture | inputs: costs, CFs, load; outputs: capacities and hourly dispatch | Sections 2.1 and 2.2 | transparent macro energy model
- demand-response-slack.md | high-cost demand response slack | when allowing rare firm-load curtailment | input: hourly firm load; output: peak capacity reduction and unserved fraction | Sections 2.1 and 3.3 | use cautiously in reliability studies
- merra2-top-resource-aggregation.md | top 25% resource-cell aggregation | when building smoothed national wind and solar profiles | input: MERRA-2 grid cells; output: area-weighted CF series | Section 2.1 | lower-variability resource case
- scenario-technology-ladder.md | Dispatch to Renew+Storage scenario ladder | when isolating flexibility mechanisms | input: technology inclusion matrix; output: comparable system cases | Table 1 | compact scenario design
- hour-month-availability-map.md | hour-by-month flexible-load capacity factor map | when checking temporal usability of surplus electricity | input: hourly dispatch; output: seasonal availability heatmap | Fig. 6 | converts annual result into operational constraint
