## Parameter rows (-> wiki/banks/parameter-bank/)

- ldv-hydrogen-demand.md | U.S. LDV hydrogen demand | 53.3 | billion kg H2/year | 2015 input data | Abstract, Fig. 5 | reusable: yes | Full LDV gasoline displacement benchmark.
- ldv-hydrogen-demand.md | Texas LDV hydrogen demand | 5.3 | billion kg H2/year | 2015 input data | Abstract, Fig. 5 | reusable: yes | State demand anchor for Texas H2 studies.
- ldv-hydrogen-demand.md | Texas Triangle LDV hydrogen demand | 3.9 | billion kg H2/year | 2015 input data | Abstract, Fig. 5 | reusable: yes | Demand cluster for H2 siting and delivery studies.
- fcev-ice-conversion.md | FCEV fuel economy | 67 | MPGe | Toyota Mirai basis | Section 3.1 | reusable: yes | Converts gasoline displacement to H2 demand.
- fcev-ice-conversion.md | ICE fuel economy | 25 | MPG | LDV baseline | Section 3.1 | reusable: yes | Baseline vehicle efficiency.
- fcev-ice-conversion.md | FCEV to ICE fuel-performance ratio | 2.5 | ratio | LDV demand model | Section 3.1 | reusable: yes | Main conversion from gasoline gallons to kg H2.
- electrolyzer-efficiency.md | electrolyzer system efficiency | 75 base; 60/75/90/100 sweep | percent | ERCOT and sensitivity cases | Sections 4.2-4.3 | reusable: yes | Core production sensitivity.
- hydrogen-compression-energy.md | compression energy context | 4.07 | kWh/kg H2 | 700 bar compression | Section 3.2 | reusable: yes | Check units before reuse because source text formatting is awkward.
- hydrogen-price-sweep.md | marginal hydrogen price sweep | 0-5 | USD/kg, 0.1 step | sensitivity case | Section 4.3 | reusable: yes | Price-response axis for dispatch.
- wind-h2-production-potential.md | wind-H2 production potential | 0.84 | billion kg H2/year | 2015 Texas wind, 75 percent efficiency, $4/kg H2 | Fig. 11 | reusable: yes | Covers about 22 percent of Texas Triangle LDV demand.
- ercot-h2-price-threshold.md | H2 production price threshold at $1/kg H2 | 21.6 | USD/MWh | 2015 ERCOT West hub | Fig. 14 | reusable: yes | Electricity price threshold for H2 dispatch.
- ercot-h2-price-threshold.md | H2 production price threshold at $4/kg H2 | 82.6 | USD/MWh | 2015 ERCOT West hub | Fig. 14 | reusable: yes | Electricity price threshold for H2 dispatch.
- electrolyzer-capex.md | centralized electrolyzer CAPEX proxy | 900 | USD/kW | order-of-magnitude capital-cost scale | Section 4.5 | reusable: maybe | Used for capital-cost illustration, not full LCOH.

## Sensitivity rows (-> wiki/banks/sensitivity-bank/)

- hydrogen-price-sensitivity.md | marginal hydrogen price | $0-5/kg, 0.1 step; $1 and $4 highlighted | production rises with price and levels off above $3/kg | Section 4.3, Figs. 11-12 | Revenue-side dispatch threshold.
- electrolyzer-efficiency-sensitivity.md | electrolyzer system efficiency | 60, 75, 90, 100 percent | higher efficiency raises threshold electricity price and improves low-price H2 production | Section 4.3, Fig. 15 | Technology-performance sweep.
- ercot-hub-price-sensitivity.md | ERCOT hub price location | Houston, North, South, West from 2011-2015 | West hub negative prices in 2011, 2012, and 2015 favor low-price H2 | Section 4.2, Table 2 | Locational market sensitivity.
- market-transfer-sensitivity.md | electricity market price series | ERCOT, SPP, MISO, PJM, NYISO, ISO-NE, CAISO | most markets favor early-morning H2 at $1/kg; CAISO daytime production is less attractive | Section 4.6, Figs. 18-19 | Cross-market transfer test.
- time-of-day-sensitivity.md | hour of day | 24 h profile | at $1/kg, production is favorable mainly at 1-6 a.m.; at $4/kg, production is economical through the day | Section 4.4, Fig. 13 | Dispatch timing rule.
- county-demand-validation.md | county-to-state aggregation | average deviation 1.32 percent, max 5.1 percent | demand model matches EIA state gasoline data closely | Section 4.1, Fig. 9 | Bottom-up demand validation.

## Method rows (-> wiki/banks/method-bank/)

- county-ldv-h2-demand.md | county-level LDV hydrogen demand estimation | when translating gasoline use into potential FCEV H2 demand | inputs: population, rurality, state gasoline, NHTS intensities, FCEV/ICE ratio; outputs: county and state H2 demand | Section 3.1 | Reusable demand-side module.
- wind-h2-price-threshold-lp.md | wind electricity allocation LP | when deciding whether renewable electricity should be sold or converted to H2 | inputs: wind output, electricity price, H2 price, conversion factor; outputs: grid sale, H2 production, revenue | Section 3.3, Eq. 8a-8d | Minimal dispatch model for screening.
- market-responsive-h2-sensitivity.md | cross-market price sensitivity | when testing whether a dispatch pattern travels across ISO/RTO markets | inputs: hourly price series and common wind profile; outputs: hourly H2 by market and price | Section 3.4 and 4.6 | Use with real regional renewable profiles in a deeper study.
- h2-demand-supply-comparison.md | demand-supply coverage comparison | when comparing renewable H2 production potential with transport demand | inputs: annual H2 production and demand cluster size; outputs: percent of demand served | Abstract, Section 4.3 | Useful for case-study positioning.
