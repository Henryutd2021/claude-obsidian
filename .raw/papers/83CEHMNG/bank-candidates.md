# Bank Candidates

## Parameter rows (-> wiki/banks/parameter-bank/)

- pv-hydrogen-sardinia-yield.md | PV specific yield | 1,577 | kWh/kWp/yr | Carbonia, south-west Sardinia, 2024 case | Section 2.1 | reusable: yes | Mediterranean solar-H2 case anchor.
- pem-electrolyzer-specific-power.md | PEM electrolyzer specific power consumption | 58 | kWh/kgH2 | 5 MW PEM, Table 1 | Table 1 | reusable: yes | Core LCoH input.
- pem-electrolyzer-capex-5mw.md | PEM electrolyzer CAPEX | 1,260 | EUR/kW | Provider quote, 5 MW, 2024 case | Section 3.1, Table 3 | reusable: yes | Includes water softener, cooling, auxiliaries, delivery, installation, commissioning.
- utility-pv-capex-mediterranean.md | PV plant CAPEX | 760 | EUR/kW | Provider quote, 12.5 MWp, 2024 case | Section 3.1 | reusable: yes | Includes arrays, inverter, auxiliaries, installation, civil works, fence, permits.
- hydrogen-compression-energy-450bar.md | H2 compression energy | 1.7 | kWh/kgH2 | Compression to 450 bar for heavy-duty FCEV refueling | Section 2.2 | reusable: yes | About 500 MWh/yr supplied by PV plant.
- hydrogen-valley-capex-sardinia.md | Total project CAPEX | 20.3094 | M EUR | Sardinia PV-H2 base case | Table 4 | reusable: yes | Land, PV, battery, electrolyzer, O2 compression, H2 compression, H2 storage.
- hydrogen-valley-opex-sardinia.md | Total annual OPEX | 520,424 | EUR/yr | First operating year | Table 5 | reusable: yes | Conclusion rounds this to about 526,000 EUR/yr.
- oxygen-byproduct-price.md | Oxygen by-product price | 150 | EUR/t | 2024 base price | Section 3.3 | reusable: yes | Revenue-side LCoH sensitivity.
- pv-export-price-italy-arera.md | Electricity export price | 125.06 | EUR/MWh | Italian ARERA value, 2024 base | Section 3.3 | reusable: yes | Revenue for PV overproduction.
- h2-bus-consumption-cost.md | H2 bus fuel consumption | 0.10 | kg/km | Urban bus comparison | Table 6 | reusable: yes | Converts H2 output to fleet service demand.
- h2-bus-capex.md | H2 bus initial investment | 650,000 | EUR/bus | Urban bus comparison | Table 6 | reusable: yes | Paper also notes 580,000 to 720,000 EUR range.

## Sensitivity rows (-> wiki/banks/sensitivity-bank/)

- h2-capex-lcoh-sensitivity.md | Component CAPEX | plus/minus 20% | PV and electrolyzer CAPEX changes have low LCoH impact; other components nearly negligible | Section 4.2, Fig. 11 | Deterministic sweep.
- oxygen-price-lcoh-sensitivity.md | Oxygen price | 150 EUR/t base, 50% lower, zero | 50% lower oxygen price raises LCoH to 3.23 EUR/kg; zero oxygen revenue raises it to 3.48 EUR/kg | Section 4.2, Fig. 12 | Revenue-side effect.
- electricity-export-lcoh-sensitivity.md | Electricity export price | 125.06 EUR/MWh base, 62.5 EUR/MWh half-price | Half export price raises LCoH to 3.27 EUR/kg | Section 4.2, Fig. 12 | Revenue-side effect.
- h2-selling-price-investor-sensitivity.md | H2 selling price | 5 EUR/kg, 8 EUR/kg, break-even >5.25 EUR/kg | 5 EUR/kg gives NPV -0.89 M EUR and IRR 7.48%; 8 EUR/kg gives NPV 8.84 M EUR, IRR 12.80%, payback 13 years | Section 4.1, Fig. 7, Fig. 13 | Main investor-risk variable.
- capex-grant-h2-parity-sensitivity.md | Public CAPEX funding | 100% CAPEX support with H2 at 2 EUR/kg | NPV about 8.45 M EUR and theoretical LCoH 0.84 EUR/kg without by-product revenue | Section 4.1, Fig. 8 | Subsidy scenario.
- electricity-procurement-lcoh-sensitivity.md | Electricity supply route | Self-produced PV versus PPA/grid at 200 EUR/MWh | PPA/grid case raises LCoH to 7.23 EUR/kg or 6.72 EUR/kg with oxygen revenue | Section 4.1, Fig. 10 | Benchmark against self-produced PV.

## Method rows (-> wiki/banks/method-bank/)

- lcoh-plus-investor-metrics.md | Dual LCoH and cash-flow TEA | Use when a project needs both literature-comparable cost and investor feasibility | Inputs: CAPEX, OPEX, finance, production, revenues; outputs: LCoH, NPV, IRR, payback | Section 2.3 | Strong template for Henry's H2 TEA.
- revenue-adjusted-lcoh.md | LCoH with by-product and export revenue subtraction | Use when electrolyzer projects sell oxygen or excess renewable power | Inputs: by-product prices, export price, discounted revenue; output: net LCoH | Equation 1, Section 4.1 | Keep gross and net LCoH separate.
- h2-bus-specific-transport-cost.md | Bus STC comparison | Use when H2 is evaluated as a transport service, not only kg fuel | Inputs: bus CAPEX, maintenance, fuel cost, mileage, lifetime, discount rate; output: EUR/km STC | Section 4.3, Equation 4 | Useful for mobility end-use comparison.
- provider-quote-plus-literature-scaling.md | Mixed CAPEX estimation protocol | Use when main equipment has vendor quotes and smaller equipment uses scaled literature costs | Inputs: quote values, literature costs, scaling factors; outputs: component CAPEX table | Section 3.1 | Transparent applied-paper costing pattern.
- deterministic-market-sensitivity-stack.md | Market-facing deterministic sensitivity | Use when product price and by-product revenue dominate project finance | Inputs: H2 price, oxygen price, export price, CAPEX variations; outputs: LCoH, NPV, IRR shifts | Section 4.2 | Add probabilistic layer for higher-tier work.
