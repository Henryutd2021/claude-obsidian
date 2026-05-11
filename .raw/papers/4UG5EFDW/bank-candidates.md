## Parameter rows (to wiki/banks/parameter-bank/)

- offshore-wind-reference-project.md | OWF capacity | 504 | MW | 2030 Irish Sea case | Sec. 2.1.1 | reusable: yes | 63 turbines at 8 MW each
- offshore-wind-site-distance.md | distance to shore | 14.5 | km | 2030 Irish Sea case | Sec. 2.1.1 and conclusion | reusable: yes | near-shore case affects H2 cost
- offshore-wind-capacity-factor.md | capacity factor before curtailment | 47.5 | percent | 2030 case, losses included | Sec. 3.1 | reusable: yes | offshore-wind H2 case anchor
- offshore-wind-capex-2030.md | wind turbine CAPEX | 1500000 | EUR/MW | 2030 base | Table 1 | reusable: yes | O&M 3% of CAPEX per year
- pem-electrolysis-compression-capex-2030.md | electrolysis and compression CAPEX | 850000 | EUR/MW | 2030 onshore PtG | Table 1 | reusable: yes | includes 15% balance of plant assumption
- hydrogen-storage-power-hour-cost.md | hydrogen storage cost | 6000 | EUR/MW-hour | 24 h full-load storage | Table 1 | reusable: yes | storage expressed against PtG power capacity
- discount-rate-low-risk-energy-project.md | discount rate | 6 | percent | 2030 low-risk project | Table 2 | reusable: yes | sensitive economic assumption
- offshore-wind-h2-lcoh.md | H2-only LCOH | 3.77 | EUR/kg H2 | 2030 base case | Sec. 3.2 | reusable: yes | full OWF output converted to H2
- green-h2-producer-value.md | hybrid parity H2 value at 10% curtailment | 4.25 | EUR/kg H2 | 2030 hybrid case | Sec. 3.3 | reusable: yes | producer value including possible incentive
- hydrogen-hhv.md | hydrogen HHV | 39.4 | kWh/kg H2 | model constant | Table 2 | reusable: yes | used for value and diesel-equivalence calculations

## Sensitivity rows (to wiki/banks/sensitivity-bank/)

- offshore-wind-h2-investor-sensitivity.md | hydrogen value | EUR3 to EUR5/kg H2 | NPV depends more on H2 value than curtailment; no hybrid case at EUR3/kg H2 | Sec. 3.3, Figs. 1 to 2 | producer value includes possible incentive
- offshore-wind-h2-investor-sensitivity.md | curtailment | 0 to 30% and threshold cases | at EUR4/kg H2, about 17% curtailment required for hybrid NPV to exceed OWF-only | Highlights and conclusion | total percentage must be paired with hourly intensity
- offshore-wind-h2-cost-sensitivity.md | hydrogen CAPEX | EUR850k/MW base to about EUR600k/MW parity | about 30% cost reduction required for hybrid to match OWF-only at 10% curtailment | Sec. 3.5 and conclusion | central bank row
- offshore-wind-h2-cost-sensitivity.md | project lifetime | 25 to 32 years | LCOH falls from EUR3.77/kg H2 to about EUR3.5/kg H2 | Sec. 3.5 | includes added refurbishment/O&M
- offshore-wind-h2-cost-sensitivity.md | PtG efficiency | 4.8 to 4.6 kWh/m3 | LCOH falls to EUR3.61/kg H2 and NPV rises to EUR202M | Sec. 3.5 | compressed-H2 efficiency case

## Method rows (to wiki/banks/method-bank/)

- hybrid-renewable-h2-set-point-dispatch.md | H2 set-point dispatch | use when a renewable generator can choose electricity sale or H2 production by hourly market value | inputs: hourly power, SMC, H2 value, efficiency; outputs: electricity/H2 revenue | Sec. 2.2.4 | converts H2 value into a price floor
- curtailment-frequency-depth-model.md | curtailment intensity audit | use when annual curtailment is not enough to size PtG | inputs: hourly curtailment events; outputs: total curtailed share and event-depth distribution | Sec. 3.4, Fig. 3 | prevents overvaluing small scattered curtailment
- investor-npv-baseline-comparison.md | baseline NPV benchmark | use when hybrid asset must beat incumbent project | inputs: CAPEX, O&M, revenue streams, discount rate; outputs: NPV parity | Sec. 3.1 to 3.3 | investor decision rule
- offshore-wind-p2g-lcoh-npv-tea.md | paired LCOH and NPV sensitivity | use when cost metric and investor metric can diverge | inputs: cost parameters, H2 value, lifetime, discount rate; outputs: LCOH and NPV sensitivity | Sec. 3.5 | separates producer economics from system-value story
