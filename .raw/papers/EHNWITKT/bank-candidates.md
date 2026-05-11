## Parameter rows (-> wiki/banks/parameter-bank/)

- floating-offshore-wind-capex.md | floating offshore wind CAPEX | 4.532 / 2.354 / 1.533 | M EUR/MW | 2020 / 2030 / 2050 | Table 4 | reusable: yes | Cost trajectory for floating offshore wind in offshore H2 TEA.
- pem-electrolyzer-capex.md | electrolyzer CAPEX | 700 / 395 / 175 | k EUR/MW | 2020 / 2030 / 2050 | Table 4 | reusable: yes | PEMEL cost trajectory used in H2 production model.
- hydrogen-storage-capex.md | hydrogen storage CAPEX | 439 / 397 / 325 | EUR/kg | 2020 / 2030 / 2050 | Table 4 | reusable: yes | Storage cost for H2 system sizing.
- pem-fuel-cell-capex.md | fuel cell CAPEX | 1600 / 425 / 340 | k EUR/MW | 2020 / 2030 / 2050 | Table 4 | reusable: yes | Useful for P2P or imbalance mitigation cases.
- offshore-transmission-loss.md | electrical transmission loss | 3.5 | percent | offshore electrical export | Section 3.1 | reusable: yes | Constant loss assumption for offshore cable export.
- compressor-specific-energy.md | compressor specific energy | 1 | kWh/kg H2 | compression from 30 to 100 bar | Section 3.1 | reusable: yes | Adds auxiliary load to electrolyzer H2 balance.
- project-finance-assumptions.md | discount rate | 7 | percent | 25-year project | Section 4.2 | reusable: yes | TEA finance baseline.
- project-finance-assumptions.md | loan structure | 20 percent down, 80 percent loan, 5 percent interest, 20-year duration | mixed | economic case | Section 4.2 | reusable: yes | Project-finance structure for NPV and LCOH.
- hydrogen-price-sweep.md | hydrogen sale price sweep | 2-10 | EUR/kg, step 2 | sensitivity case | Section 4 | reusable: yes | Profitability sweep.
- offshore-wind-h2-lcoh.md | onshore electrolyzer LCOH | 5.84 / 3.42 / 2.57 | EUR/kg | 2020 / 2030 / 2050, 50 km site | Abstract and Conclusions | reusable: yes | Benchmark for grid-connected onshore electrolysis.
- offshore-wind-h2-lcoh.md | offshore electrolyzer LCOH | 8.98 / 4.37 / 2.68 | EUR/kg | 2020 / 2030 / 2050, 50 km site | Abstract and Conclusions | reusable: yes | Benchmark for offshore electrolysis with pipeline export.

## Sensitivity rows (-> wiki/banks/sensitivity-bank/)

- hydrogen-price-sensitivity.md | hydrogen sale price | 2 to 10 EUR/kg, step 2 | higher H2 price increases profitability and shifts onshore electrolyzer sizing from 5 percent to 100 percent at 4 EUR/kg | Section 4 and Table 6 | Use as revenue-side sweep.
- cost-year-sensitivity.md | scenario year | 2020 / 2030 / 2050 | LCOH falls sharply from 2020 to 2030 and more slowly by 2050 | Fig. 1 and Conclusions | Technology learning axis.
- electrolyzer-sizing-sensitivity.md | electrolyzer nominal power ratio | 5 to 100 percent of wind farm power | offshore optimum mostly 90-95 percent; onshore optimum 5 percent at 2 EUR/kg and 100 percent at 4 EUR/kg | Table 6 | Co-sizing rule.
- offshore-distance-sensitivity.md | distance from shore | 25 km and 50 km | 50 km site improves conventional wind and offshore electrolyzer economics because wind resource offsets transport cost | Fig. 1 and Fig. 3 | Siting axis.
- fuel-cell-flexibility-sensitivity.md | fuel-cell ratio / operation | tested ratios, optimum 5 percent | fuel-cell operation is rarely profitable because H2-to-electricity value is low except during extreme price and imbalance events | Section 5.2 | Treat fuel cell as optional flexibility.

## Method rows (-> wiki/banks/method-bank/)

- offshore-wind-h2-hourly-tea.md | component-resolved offshore wind to H2 TEA | when comparing electron export, molecule export, and grid-connected electrolysis | inputs: wind, prices, regulation costs, component cost tables; outputs: LCOH, NPV, IRR, sizing | Sections 3-5 | Core method candidate.
- day-ahead-real-time-milp.md | two-stage day-ahead and real-time MILP | when market bids and real-time imbalances affect dispatch value | inputs: forecasts, actual production, price, imbalance cost; outputs: bids, H2 production, grid sales, regulation cost | Section 3.2.1 | Reusable dispatch structure.
- vmd-cnn-forecasting.md | VMD plus CNN day-ahead forecasting | when hourly renewable output and electricity price forecasts feed dispatch | inputs: 64 h history; outputs: 24 h forecast with 12 h bid gap | Section 3.3 | Forecast preprocessor for market-coupled TEA.
- boundary-comparison-electron-vs-molecule.md | offshore electrolyzer versus onshore electrolyzer boundary comparison | when testing cable export against pipeline H2 export and grid flexibility | inputs: distance, cable/pipeline cost, grid price, H2 price; outputs: system ranking | Sections 1, 3, and 5 | Transferable framing method.
- lcoh-npv-irr-triad.md | LCOH plus NPV plus IRR reporting | when levelized cost alone hides investor outcome | inputs: discounted CAPEX, OPEX, revenues, loan terms; outputs: LCOH, NPV, IRR | Sections 3.4 and 5 | Reporting method for applied TEA.
