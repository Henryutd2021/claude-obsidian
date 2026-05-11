---
zotero_key: XUGL6XPD
title: "Technoeconomic analysis of small modular reactors decarbonizing industrial process heat"
journal: "Joule"
year: 2023
doi: "10.1016/j.joule.2023.03.009"
topic: [small-modular-reactors, industrial-process-heat, industrial-decarbonization, techno-economic-analysis, wholesale-power-markets, united-states]
paper_type: [modeling, TEA, scenario-analysis, optimization, policy-analysis]
main_contribution: [system-boundary-expansion, counterintuitive-result, policy-relevance, mechanism-clarification, sectoral-coverage]
method_type: [MILP, Pyomo, CPLEX, price-taker-dispatch, scenario-sensitivity-analysis]
journal_role: top_journal_exemplar
ingest_depth: A_deep
subdomain_primary:
  - integrated-energy-systems
  - power-systems
subdomain_secondary:
  - energy-policy-economics
data_assets:
  main_pdf: true
  supplementary: true
  source_data: true
  data_statement: true
  code_statement: true
  code_repository: true
relevance_to_my_research: high
ingest_status: reviewed
address: c-000019
created: 2026-05-11
tags:
  - paper-analysis
---

# Technoeconomic analysis of small modular reactors decarbonizing industrial process heat

> Zotero: `XUGL6XPD` | DOI: 10.1016/j.joule.2023.03.009 | Journal: Joule (2023)

## 1. One-sentence contribution

Evidence: The paper builds a profit-maximizing MILP for five SMR designs at 421 natural-gas-fueled industrial facility processes in ERCOT and SPP, then shows that SMRs are not economic for heat alone at 2021 US gas prices but can serve 125 SPP facility processes when heat supply is paired with wholesale electricity revenue. Inference: high confidence, the contribution is a boundary expansion from "can an SMR supply process heat" to "which process, temperature, module size, fuel price, and power-market setting makes SMR heat economic." Lesson: For Henry's TEA work, make the headline depend on a decision boundary, not on a generic cost comparison.

## 2. Archetype classification

Evidence: This is a modeling, TEA, scenario-analysis, optimization, and policy-analysis paper because it combines process-level industrial demand data, five reactor archetypes, a mixed integer linear program, natural gas price thresholds, wholesale electricity price scenarios, carbon price cases, capital-cost sensitivity, and technology-operation constraints. Inference: high confidence, its closest archetype is emerging-technology threshold mapping for industrial decarbonization. Lesson: When evaluating a new decarbonization asset, compare heat-only economics against stacked-revenue economics so readers can see whether the asset fails or whether the business model is too narrow.

## 3. Real value sources

| Dimension | Top driver? | Evidence | Inference | Lesson |
|---|---|---|---|---|
| Problem importance | Yes | Evidence: The Introduction states that US industry emitted 1,522 million metric tons CO2-equiv per year in 2019, with fossil fuel combustion supplying 77% of industrial thermal energy and direct process-heat combustion causing roughly half of industrial emissions. | Inference: high confidence, the paper enters a central industrial-decarbonization bottleneck: high-temperature heat from 300 C to 850 C. | Lesson: Tie a technology assessment to a named emissions source, temperature band, and incumbent fuel before introducing the new asset. |
| Problem novelty | Yes | Evidence: The Introduction says prior SMR industrial studies either ignored economic viability or studied one remote facility, and that no prior work quantified broad SMR heat plus wholesale power market participation. | Inference: high confidence, the gap is a missing technoeconomic boundary rather than a missing reactor concept. | Lesson: Define the gap as the missing combination of scale, economics, and revenue channels. |
| Method novelty | Medium | Evidence: The paper designs a profit-maximizing MILP that chooses SMR type, module count, commitment state, heat output, electricity output, and dump heat per facility process. | Inference: medium confidence, the value is in applying standard optimization tools to a new process-level deployment problem. | Lesson: A useful TEA method can be familiar if the decision unit and constraints are newly aligned with the policy question. |
| Data novelty | Medium | Evidence: The model uses NREL process-heat demand for 423 processes at 200 facilities, then filters and batches them into 421 facility processes in ERCOT and SPP. | Inference: medium confidence, the data asset is process-temperature and process-demand matching, not a new survey. | Lesson: For heat decarbonization, collect demand quantity and heat quality together. Annual energy alone is not enough. |
| System boundary | Yes | Evidence: The boundary includes process heat revenues, SMR costs, thermal quantity, thermal quality, unit commitment, ramping, minimum load, and optional wholesale power-market revenue. | Inference: high confidence, the boundary is the reason the paper can explain why low-LCOH iPWRs are not always selected. | Lesson: Add the physical constraints that can reverse a simple LCOH ranking. |
| Case-study design | Yes | Evidence: The case covers Texas, Oklahoma, Kansas, Nebraska, and South Dakota, spanning ERCOT and SPP and 12 industries including refineries, ethyl alcohol, basic organic chemicals, and nitrogenous fertilizers. | Inference: high confidence, the two-region design makes electricity-market revenue variation visible while retaining process-level industrial detail. | Lesson: Pick cases where both the industrial load and the market context vary. |
| Result impact | Yes | Evidence: At 2021 US gas prices, no heat-only SMR deployments are viable, while heat plus power participation in SPP makes 125 facility processes economic, with 37.4 GWth of SMRs and 4.6 million metric tons CO2 avoided annually. | Inference: high confidence, the result is strong because it contains a negative baseline and a conditional positive case. | Lesson: Use a failed base case as a control if the stacked-revenue case is the real claim. |
| Mechanism explanation | Yes | Evidence: Figures 3 and 4 trace selection to thermal demand quantity and thermal quality, while Table 1 and Figure 5 show how wholesale market participation changes module counts and favored designs. | Inference: high confidence, the paper wins on mechanism tracing more than on a single national abatement number. | Lesson: After the headline, explain why the selected technology changes across demand scale, temperature, and market revenue. |
| Comprehensiveness | Medium | Evidence: The study spans five reactor designs, 421 facility processes, two electricity markets, multiple gas prices, two carbon prices, TES sensitivity, operational flexibility, thermal losses, and capital-cost increases. | Inference: high confidence, the breadth is across technology, process, market, and uncertainty axes, but not across all US regions or siting constraints. | Lesson: State the axes of breadth and the exclusions in the same section. |
| Policy / industry implication | Yes | Evidence: The Discussion says policy support such as carbon pricing and IRA nuclear credits could improve SMR heat economics, and identifies refineries, basic organic chemicals, petrochemicals, and ethyl alcohol as early case-study targets. | Inference: high confidence, the paper converts model output into deployment screening guidance. | Lesson: End a TEA with candidate industries and policy levers, not only with costs. |
| Writing / narrative | Medium | Evidence: The paper moves from industrial heat scale, to SMR attributes, to prior literature limits, to two research questions, then to a MILP design that matches those questions. | Inference: high confidence, the narrative is built around a funnel from emissions scale to missing economic test. | Lesson: Let the research questions mirror the two main revenue cases. |
| Figure / table craft | Yes | Evidence: Figures 1 to 7 move from demand landscape, to deployment stacks, LCOH mechanism, temperature constraint, power-market case, sensitivity, and model architecture. | Inference: high confidence, the visual sequence follows the full argument chain from opportunity to mechanism to robustness. | Lesson: Use figures to answer one objection at a time: where is demand, when does it pay, why that design, and what changes under sensitivity. |

**Top 3 value drivers**:
1. Evidence: Process-level thermal quantity and quality matching across 421 facility processes.
2. Evidence: Heat-only versus heat-plus-power revenue contrast under real ERCOT and SPP price histories.
3. Evidence: Mechanism explanation that shows why module size and outlet temperature beat simple LCOH ranking.

**What it does NOT win on**: Evidence: It does not perform site-specific nuclear siting, permitting, heat-transport design, safety review, waste analysis, or price-maker power-system feedback. The Discussion and Methods name these as limits.

**Most likely reason it cleared the top-tier bar**: Inference: high confidence, Joule fit comes from turning an emerging nuclear technology into a decision-grade industrial deployment screen with an explicit negative result at current US gas prices.

## 4. Research question & framing

Evidence: The paper asks two research questions: whether SMRs can achieve economic viability in decarbonizing industrial thermal demand, and how much joint participation in industrial heat and wholesale power markets changes SMR viability. Inference: high confidence, the framing treats SMR process heat as a conditional opportunity that depends on the industrial process, gas price, reactor design, and market revenue stack. Lesson: In Henry's green-hydrogen TEA, ask whether a technology fails under one revenue model but works under another, such as hydrogen production plus grid services, heat sales, or oxygen byproduct use.

## 5. Introduction structure (paragraph table)

| Paragraph | Function | Core info | Writing move | Why it works | Lesson |
|---|---|---|---|---|---|
| P1 | Industrial heat bottleneck | Evidence: US industry emits 1,522 million metric tons CO2-equiv per year, fossil combustion supplies 77% of industrial thermal energy, and 300 C to 850 C processes are a hard-to-decarbonize target. | Starts with sector scale and temperature boundary. | It makes the paper about a measurable heat problem, not nuclear advocacy. | Lesson: Open with emissions, incumbent fuel, temperature range, and sectors. |
| P2 | SMR technology candidate | Evidence: SMRs and microreactors can be deployed modularly and can provide heat plus electricity like industrial cogeneration. | Introduces why SMRs might fit process heat. | It links modularity to facility-demand matching. | Lesson: Introduce the technology through the system feature your model will test. |
| P3 | Reactor design and sector fit | Evidence: iPWRs, iMSRs, SFRs, HTGRs, and PBR-HTGRs have outlet temperatures up to about 850 C after heat-transfer losses, matching petroleum refining, chemicals, plastics, and ethyl alcohol. | Narrows the candidate set and demand band. | It turns "nuclear" into a finite design space. | Lesson: Convert broad technology families into modeled archetypes early. |
| P4 | Prior literature map | Evidence: Prior studies found technical potential or single-site economics, while McMillan et al. ignored economic viability and Friedmann et al. focused on industries above SMR temperature limits. | Builds the literature gap through exclusions. | It shows the paper is not claiming nobody studied nuclear heat. | Lesson: Name what prior studies did measure before stating what they missed. |
| P5 | Gap paragraph | Evidence: Existing research does not quantify broad technoeconomic potential for more than a handful of remote facilities and does not include heat plus wholesale electricity participation. | States the missing decision boundary. | It prepares the two research questions directly. | Lesson: The gap paragraph should name the missing scale and missing revenue channel. |
| P6 | Study design preview | Evidence: The authors design a profit-maximizing MILP, analyze more than 300 grouped facility processes at 180 facilities in ERCOT and SPP states, and test five characteristic SMRs under heat-only and heat-plus-power cases. | Converts the gap into model, cases, and outputs. | It tells readers exactly how the paper will answer the gap. | Lesson: End the Introduction with model type, decision unit, geography, and scenario contrast. |

**Transferable Intro template extracted from this paper**: Evidence: The Intro uses "sector emissions and heat band -> technology attribute -> reactor designs -> prior limits -> gap as scale plus revenue channel -> model and case setup." Lesson: Use this structure for Henry's industrial hydrogen papers when the key issue is not the molecule itself but where, when, and under what revenue model it beats the incumbent.

## 6. Lit-gap & contribution construction

Evidence: The paper's gap is precise: previous work considered technical feasibility at broad scales or economics at isolated facilities, but did not quantify SMR technoeconomic potential across many facility processes or include joint heat and electricity-market participation. Inference: high confidence, the contribution is built as a missing deployment-screening layer between reactor feasibility and site-specific engineering. Lesson: For Henry's TEA papers, avoid saying "few studies exist" unless the missing axis is named. Use a formulation like "existing work lacks process-level economic screening under stacked revenue."

Evidence: The contribution construction also uses a useful contrast against McMillan et al. and Friedmann et al. McMillan et al. provides the technical-potential foundation, while Friedmann et al. motivates selecting the 300 C to 850 C range where SMRs can plausibly supply heat. Inference: medium confidence, the authors use prior literature as a boundary-setting tool rather than only as a citation count. Lesson: Use previous papers to justify the case window and excluded processes before presenting the model.

## 7. Method / model / design (adapt to archetype)

Evidence: The core model is a profit-maximizing MILP that optimizes, per industrial facility process, SMR type, module count, on/off state, thermal generation, electricity generation, and dump heat. It maximizes annualized net revenues, where costs include startup, variable, fixed, overnight capital cost, and capital recovery, while electricity revenues come from hourly LMPs when wholesale participation is allowed.

Evidence: The model enforces hourly heat demand quantity in MWhth and heat quality in C, unit commitment, ramping, minimum stable load, minimum turbine load, and a constraint that only one SMR type can be deployed at each facility process. It chooses from iPWR, iMSR, HTGR, PBR-HTGR, and microreactor parameter sets.

Evidence: The two-stage solve first runs every sixth hour of the year, 1,460 hours, to choose type and module count, then fixes the build decision and optimizes all 8,760 hours using a rolling 48-hour horizon with 24-hour look-ahead. The model is formulated in Pyomo and solved with IBM CPLEX.

Inference: high confidence, the method is designed to answer three reviewer concerns: simple LCOH misses module-size matching, industrial heat requires temperature matching, and wholesale market revenue can alter apparent heat economics. Lesson: If Henry uses MILP for hydrogen or industrial heat, make every constraint correspond to a reviewer objection: quantity, quality, temporal matching, revenue stack, and capacity limits.

## 8. Data & case-study design

Evidence: The industrial demand data come from NREL process-level heat data for EPA GHGRP facilities in ERCOT and SPP states. The authors start from 200 facilities and 423 heat processes with 52.7 GWhth, then restrict to natural gas and similar gaseous fuels and combine same-temperature process demands at each facility into 164 SPP and 257 ERCOT facility processes.

Evidence: The case region includes Texas for ERCOT and Oklahoma, Kansas, Nebraska, and South Dakota for SPP. The dataset spans 12 industries, with large demand shares in petroleum refineries, petrochemicals, ethyl alcohol, nitrogenous fertilizers, and basic organic chemicals.

Evidence: Thermal demand profiles are disaggregated from annual to hourly using industry-specific profiles where available and constant demand otherwise. Wholesale electricity prices come from ERCOT day-ahead hub average prices and SPP hourly average LMPs. Natural gas reference prices include 2021 US prices near $4/MMBtu, pre-fracking US prices near $8/MMBtu, and 2021 EU prices at $16/MMBtu.

Inference: high confidence, ERCOT and SPP are not only geography choices. They are a paired test of process-heat demand and wholesale market value. Lesson: In Henry's TEA work, choose case regions that stress the model on both the asset side and the market side.

## 9. Results architecture

| Section | Main message | Evidence used | Role in argument | Why this order | Lesson |
|---|---|---|---|---|---|
| Result 1: heat-only deployment | SMRs do not achieve positive net revenues for any of the 421 studied facility processes at roughly $4/MMBtu 2021 US gas prices. | Evidence: Results report annualized costs of $5.88 million to $594.73 million and annualized revenues of $4.76 million to $534.05 million, with no positive net revenue at 2021 US gas prices. | Establishes the negative baseline. | The paper begins with the simplest business model before adding stacked revenue. | Lesson: Start with the incumbent comparison that readers expect, even if it fails. |
| Result 2: gas-price deployment stacks | At higher avoided gas prices, viability appears first in ERCOT at $6.56/MMBtu and SPP at $7.00/MMBtu, with much larger deployment at $16/MMBtu. | Evidence: At $8/MMBtu, ERCOT can serve 11% modeled demand with 29 PBR-HTGR modules and SPP can serve 2% with one PBR-HTGR module; at $16/MMBtu, ERCOT reaches 41% and SPP reaches 73%. | Converts no-viability into threshold logic. | It shows the condition under which heat-only economics improve. | Lesson: Use deployment stacks to turn a binary result into a policy-relevant threshold curve. |
| Result 3: design-selection mechanism | Thermal quantity and quality explain why PBR-HTGRs and microreactors often beat lower simple-LCOH iPWRs. | Evidence: Figure 3 compares LCOH curves with model results; Figure 4 shows viable modules by required temperature and reactor upper temperature. | Explains the mechanism behind the technology choice. | It prevents the threshold result from being a black box. | Lesson: After ranking technologies, explain the physical or operational cause of the rank. |
| Result 4: heat plus power markets | Wholesale market participation changes viability, especially in SPP, where 125 facility processes are viable at $4/MMBtu with 125 iMSR modules and 37.4 GWth. | Evidence: Table 1 and Figure 5 compare heat-only with heat plus power in ERCOT and SPP. | Answers the second research question. | It follows heat-only mechanics, so the added value of electricity revenue is visible. | Lesson: Present the stacked-revenue scenario after the base-case mechanism is understood. |
| Result 5: sensitivity | Results are robust to constant demand, reduced flexibility, TES, and transport loss in many cases, but sensitive to carbon price, market year, and capital-cost increases. | Evidence: Figure 6 and Table 5 report carbon prices of $51/mt CO2-equiv and $185/mt CO2-equiv, plus capital-cost increases of 10%, 50%, and 100%. | Tests uncertainty and policy levers. | It comes after core results so sensitivity has a reference point. | Lesson: Separate robustness checks from policy levers. They answer different questions. |

## 10. Figures & tables argument function

| Item | Shows | Proves | Role | Why in main text | Design lesson |
|---|---|---|---|---|---|
| Fig. 1 | 2015 industrial thermal demand in ERCOT and SPP by temperature band and fuel type. | Evidence: Demand is large, fuel-based, and distributed across heat quality bands. | Opportunity landscape. | It justifies the chosen heat band and regions. | Lesson: Open results with the demand map that makes the model necessary. |
| Fig. 2 | Economically viable SMR deployment stacks in SPP and ERCOT for heat-only cases across gas prices. | Evidence: No deployment at $4/MMBtu and increasing module count at higher avoided gas costs. | Heat-only threshold curve. | It is the first direct answer to research question 1. | Lesson: Deployment-stack figures make thresholds more useful than single breakeven points. |
| Fig. 3 | Generalized LCOH curves versus optimized SMR selections. | Evidence: Average demand and module-size matching explain many selections. | Mechanism diagnostic. | It explains why the MILP result differs from simple LCOH. | Lesson: Pair model output with a simplified comparator to expose the value of the model. |
| Fig. 4 | Economically viable modules by required temperature range. | Evidence: High-temperature demands restrict technology choice, and HTGRs only become viable at high gas prices. | Thermal-quality diagnostic. | It answers why outlet temperature matters. | Lesson: For heat TEA, show temperature as a first-class axis. |
| Fig. 5 | Deployment stacks for heat plus power markets and comparison against heat-only. | Evidence: Wholesale revenue greatly expands SPP viability and changes the dominant SMR type toward iMSR. | Stacked-revenue result. | It answers research question 2 visually. | Lesson: When a revenue stack changes the conclusion, show base and expanded cases side by side. |
| Fig. 6 | Sensitivities across carbon price, operation, TES, thermal loss, and capital cost. | Evidence: Carbon price shifts the supply curve left, while 50% to 100% capital-cost increases shift deployment right. | Robustness and policy screen. | It concentrates many uncertainty tests into one figure. | Lesson: Use a grid of sensitivity panels when the reader needs to see which uncertainties matter most. |
| Fig. 7 | Diagram of a single SMR module system with heat output, electricity generation, and dump heat. | Evidence: The model separates reactor output, process heat, electricity, and heat losses. | Model architecture. | It makes the MILP variables physically interpretable. | Lesson: Include a system-flow diagram for optimization models with coupled energy outputs. |
| Table 1 | Economic viability at $4, $8, and $16/MMBtu in ERCOT and SPP for heat-only and heat plus power cases. | Evidence: The table reports process count, demand share, module count, and GWth capacity. | Numeric anchor for headline results. | It gives exact values behind Figures 2 and 5. | Lesson: Pair deployment curves with a compact table at policy-relevant price points. |
| Table 2 | Descriptive statistics for SPP, ERCOT, and the 50-process sensitivity set. | Evidence: It reports process counts, demand, emissions, industries, and temperature distributions. | Case-study audit. | It lets readers inspect whether the sample matches the claim. | Lesson: Add a sample-characterization table when facility heterogeneity drives results. |
| Table 3 | SMR parameters including temperature, capacity, ramp rate, costs, O&M, and fuel costs. | Evidence: It defines the reactor archetypes used in the MILP. | Technology input audit. | It makes reactor comparisons traceable. | Lesson: Put cost and performance assumptions in one table so readers can challenge them directly. |
| Table 4 | Day-ahead market electricity price statistics for ERCOT and SPP years. | Evidence: It shows 2021 SPP and 2020 ERCOT price distributions used in base market scenarios. | Market-data audit. | It supports the stacked-revenue scenario. | Lesson: Report price distributions, not only chosen years, when market revenue drives results. |
| Table 5 | Sensitivity descriptions and rationales. | Evidence: It maps each sensitivity to its uncertainty source. | Robustness design. | It explains why each sensitivity exists before readers see the effect. | Lesson: Give every sensitivity a rationale, not only a parameter value. |

## 11. Discussion & Conclusion

Evidence: The Discussion elevates the results from "SMRs can sometimes beat gas" to three deployment rules: process-heat quantity matching, heat quality matching, and wholesale market participation decide viability. It also states that refineries, basic organic chemicals, petrochemicals, and ethyl alcohol facilities are initial case-study targets.

Evidence: The Discussion names policy and market implications. At 2021 EU gas prices and heat plus power participation, 60% of modeled thermal demand could be better served by more than 300 SMR modules. At a $51/mt CO2-equiv carbon price, SMRs could decarbonize 65% of industrial CO2 emissions in SPP.

Evidence: Limitations are substantive: nuclear waste, decommissioning, site layout, heat-transfer infrastructure, historical price uncertainty, speculative SMR capital costs, and the price-taker assumption for wholesale markets. Inference: high confidence, the Discussion is strongest when it converts the TEA into screening criteria and weakest when it scales nationally through proportional extrapolation. Lesson: In Henry's papers, separate "deployment screen" conclusions from "national potential" extrapolations and mark the latter as rough.

## 12. Argument chain (compressed)

```text
Industrial heat is a large fossil-fuel emissions source
  -> 300 C to 850 C process heat is hard to decarbonize with many alternatives
  -> SMRs can provide high-quality heat and electricity, but broad economics are unknown
  -> Prior studies miss either process-level economics or heat plus power revenue
  -> Build a MILP for five SMR designs at 421 facility processes in ERCOT and SPP
  -> Heat-only SMRs fail at 2021 US gas prices
  -> Higher gas prices create deployment stacks, especially at $16/MMBtu
  -> Thermal quantity and thermal quality explain reactor choice
  -> Wholesale power participation unlocks SPP viability at current gas prices
  -> Capital cost, carbon price, and market year decide whether the opportunity survives
  -> SMRs are best treated as targeted industrial decarbonization options, not universal heat replacements
```

**Weakest link**: Inference: high confidence, the price-taker wholesale market assumption is the weakest link because large SMR electricity sales would reduce prices, especially in SPP where 139 TWhe annual sales are reported at $8/MMBtu.

**Strongest link**: Evidence: The strongest link is the mechanism chain from Figure 3 and Figure 4: facility demand quantity and temperature requirement explain why module selection differs from simple LCOH.

## 13. Writing strategy extracted

Evidence: The paper uses a controlled sequence of negative result, threshold curve, mechanism diagnosis, revenue-stack reversal, and sensitivity. Inference: high confidence, this sequence is persuasive because it first disappoints the easy narrative and then shows the precise condition under which the technology returns.

Lesson: For Henry's TEA manuscripts, avoid opening the Results with a best-case deployment number. Start with the base-case economics, then add the mechanism and policy lever that changes the outcome.

Evidence: The title is direct and method-labeled: "Technoeconomic analysis of small modular reactors decarbonizing industrial process heat." Inference: medium confidence, the title works because it names technology, application, and method without adding a policy slogan. Lesson: When the paper's value is in system screening, put the asset and use case in the title.

Evidence: The paper's Context & Scale box states the reader-level takeaway in plain units: over 400 processes, no viability at 2021 US gas prices for heat alone, about 6 GW unlocked by doubling gas prices, and over 120 processes under heat plus power. Lesson: Build an abstract-side summary that gives scale, negative result, threshold, and conditional opportunity.

## 14. Research-design strategy extracted

Evidence: The design uses a per-facility-process decision unit, not a national average heat demand. It then adds reactor type, module count, hourly operation, temperature feasibility, and market participation. Inference: high confidence, this decision unit is the main reason the paper can identify ethyl alcohol, refineries, and chemicals as different opportunities.

Lesson: For hydrogen or industrial heat TEA, choose the decision unit at the level where technology selection changes. National averages are too coarse if module size, temperature, or temporal operation decide economics.

Evidence: The authors include a simplified LCOH comparator and then show why the MILP selection diverges. Lesson: When using an optimizer, include a simple benchmark that readers understand, then show exactly where the benchmark fails.

Evidence: The sensitivity set is reduced to 50 randomly selected facility processes due to compute constraints and then compared through Table 2 descriptive statistics. Inference: medium confidence, this is a practical compromise but depends on the representativeness of the subset. Lesson: If using a subset for robustness, publish a table comparing the subset to the full case population.

## 15. Critical analysis

Evidence: The price-taker assumption is openly limited. The Results state that at $8/MMBtu in SPP, SMRs could sell 139 TWhe annually, and that this quantity would lower electricity prices and violate the price-taker assumption. Inference: high confidence, this means the largest stacked-revenue result should be read as upper-bound potential, not likely deployment.

Evidence: SMR cost assumptions use FOAK costs and omit interest during construction, while capital-cost sensitivities show that 50% and 100% increases shift deployment stacks right by roughly $4/MMBtu and $8/MMBtu. Inference: high confidence, cost uncertainty can change whether current-gas-price deployment exists. Lesson: In Henry's emerging-technology TEA, do not hide cost uncertainty in one base scenario. Make cost escalation a front-page sensitivity.

Evidence: The study does not model site layout, heat-transfer networks, nuclear setback distances, permitting, waste management, or facility-specific integration with industrial partners. Inference: high confidence, the results are best used for screening which industries and sites deserve deeper engineering study. Lesson: Do not blindly copy the broad-screen design if the research question requires buildable project design.

Evidence: The national extrapolation scales regional findings to MISO, PJM, and CAISO using proportional demand assumptions. Inference: medium confidence, this is useful for scale intuition but weaker than the process-level ERCOT and SPP analysis. Lesson: Label extrapolations as rough and keep the central claim anchored to modeled regions.

## 16. Transfer to my own work

Evidence: The paper is directly aligned with Henry's energy-system optimization, industrial decarbonization, energy policy and cost analysis, and green-hydrogen TEA interests because it studies process heat, revenue stacking, hourly market participation, and technology-selection thresholds.

Lesson: For wind-solar-hydrogen studies, copy the boundary logic: compare hydrogen production under a single-product business model against a stacked model that includes grid services, heat integration, oxygen use, curtailment absorption, or fuel-switching value.

Lesson: For green-hydrogen TEA, adopt the "quantity plus quality" frame from process heat. Hydrogen demand is not just kg H2/year. It also has purity, pressure, delivery timing, offtake reliability, and temperature-coupling requirements.

Lesson: For data-center or industrial-load optimization, use a paired-market design similar to ERCOT versus SPP. A flexible asset's value can depend more on local price distributions than on average annual energy cost.

Lesson: For policy-cost analysis, report deployment stacks at recognized price points. This paper's $4, $8, and $16/MMBtu gas anchors make the result easier to interpret than an abstract breakeven curve alone.

## 17. KB outputs (mandatory)

### 5 Permanent Notes (atomic, evergreen, with `Evidence:` from this paper)

1. Emerging clean-heat assets should be tested against both heat-only and stacked-revenue cases before concluding that they are uneconomic. Evidence: At 2021 US gas prices, no heat-only SMR deployment is viable, but SPP heat plus power participation makes 125 facility processes viable with 37.4 GWth. Lesson: Always include at least one revenue-stack sensitivity when the asset can sell more than one product.
2. Heat decarbonization TEA needs both thermal quantity and thermal quality. Evidence: Figure 3 links SMR selection to average demand and module utilization, while Figure 4 shows that high-temperature demands restrict feasible reactor types. Lesson: Put demand magnitude and temperature in the same input table and figure set.
3. A simple LCOH ranking can mislead when module size and utilization drive economics. Evidence: The iPWR has the lowest simplified LCOH at 100% capacity factor, but PBR-HTGRs and microreactors are often selected because they better match facility demand. Lesson: Use LCOH as a comparator, not as the final decision rule.
4. Wholesale electricity revenue can reverse industrial heat economics, but only if market-price feedback is bounded. Evidence: The paper reports SPP iMSR viability at $4/MMBtu with heat plus power, but also warns that 139 TWhe of sales at $8/MMBtu would violate the price-taker assumption. Lesson: Treat large price-taker revenue as an upper-bound screen and add price-feedback analysis before project claims.
5. Facility-process batching is a defensible first screen, but it is not a site design. Evidence: The authors combine same-temperature process demands at facilities and state that spatial layout, infrastructure, and sub-process optimization need future industrial-partner case studies. Lesson: Use broad screening to pick targets, then switch to facility-specific engineering before claiming deployability.

### 5 Writing Lessons

1. Evidence: The Results begin with a negative heat-only result before showing threshold and market-participation cases. Lesson: Let the paper earn the positive case by first stating the baseline failure.
2. Evidence: The Introduction's gap paragraph names both missing scale and missing revenue channel. Lesson: Write gaps as "existing studies miss X under Y boundary" rather than as a broad absence claim.
3. Evidence: Figures 2 and 5 use deployment stacks across avoided gas costs. Lesson: Use stack curves when the policy question is "how much deployment unlocks at this price."
4. Evidence: The Discussion names target industries and required future case-study work. Lesson: End TEA papers with a short screening-to-deployment handoff.
5. Evidence: Table 5 gives each sensitivity a rationale. Lesson: Write sensitivities as reviewer questions, not as a parameter appendix.

### 5 Research-Design Lessons

1. Evidence: The model's decision unit is the facility process, not the region. Lesson: Choose the smallest unit where the technology decision can change.
2. Evidence: The model constrains both heat demand and heat temperature. Lesson: Add quality constraints when substituting one energy carrier for another.
3. Evidence: The authors run a simplified LCOH comparator beside the MILP outputs. Lesson: Include a transparent baseline model to make optimizer value visible.
4. Evidence: The two market scenarios isolate heat revenue from heat plus wholesale electricity revenue. Lesson: Design scenarios so each one tests one business-model assumption.
5. Evidence: Capital cost increases of 50% and 100% materially reduce viability. Lesson: Stress emerging-technology economics with cost increases, not only optimistic cost declines.

### 5 Future Research Questions

1. Evidence: The paper uses a price-taker market assumption and notes it can break under large SMR electricity sales. Inference: high confidence. How would SMR industrial heat deployment change in a price-maker power-system model with endogenous electricity prices?
2. Evidence: The paper omits detailed facility layout, heat-transfer network design, and nuclear setback constraints. Inference: high confidence. Which refinery or ethyl alcohol facility clusters remain viable after site-specific heat-transport and permitting constraints?
3. Evidence: The paper treats SMR cost increases uniformly across reactor types. Inference: medium confidence. How would reactor-specific cost uncertainty alter the ranking of iMSR, PBR-HTGR, microreactor, HTGR, and iPWR options?
4. Evidence: The paper compares SMRs against natural gas but not against co-optimized electrification, hydrogen, biomass, geothermal, or solar thermal options in the same MILP. Inference: high confidence. Which industrial heat technologies win under a shared facility-process optimization boundary?
5. Evidence: The paper points to IRA production and investment tax credits as policy supports. Inference: medium confidence. How would explicit tax credits, carbon prices, and clean heat contracts interact with wholesale market participation in SMR economics?

## 18. Final summary

**Top 3 lessons**:
1. Evidence: SMRs fail for heat-only service at 2021 US gas prices. Lesson: A credible TEA can lead with a negative result if the threshold and mechanism are then explained.
2. Evidence: Thermal quantity and quality drive reactor choice. Lesson: Treat energy quality as a model constraint, not a narrative detail.
3. Evidence: Wholesale power-market revenue changes SPP viability. Lesson: Test stacked business models when an asset can serve more than one market.

**Top 3 to transfer**:
1. Lesson: Use deployment stacks at recognizable price points in Henry's hydrogen and industrial heat papers.
2. Lesson: Pair optimizer outputs with a simple benchmark such as LCOH or levelized hydrogen cost.
3. Lesson: Define the decision unit at the facility, process, or load level where technology choice changes.

**Top 3 to NOT blindly copy**:
1. Evidence: Price-taker wholesale revenue can overstate deployment at high SMR electricity sales. Lesson: Do not claim market-scale viability without price-feedback modeling.
2. Evidence: The national extrapolation is proportional rather than process-modeled. Lesson: Do not treat scaled potential as equally strong as modeled potential.
3. Evidence: Facility siting and heat-transfer design are deferred. Lesson: Do not use broad TEA screening as project engineering evidence.

**One-line takeaway** (the core research skill this paper teaches): Lesson: Build TEA around the boundary conditions that decide technology selection: demand quantity, energy quality, revenue stack, market feedback, and cost uncertainty.

## Pass-2 follow-up (deferred)

Evidence: Pass 1 used the main PDF text, embedded supplemental pages, Zotero metadata, and the availability statement. Lesson: A later pass should inspect the Zenodo code/data package and supplemental equations in detail only if a methods or sensitivity pattern page needs this paper as evidence.

## Cross-references

- Zotero parent key: `XUGL6XPD`
- Main PDF attachment key: `YJSFW7YP`
- Stub files: [[.raw/papers/XUGL6XPD/metadata.json|metadata.json]], [[.raw/papers/XUGL6XPD/zotero-attachments|zotero-attachments]], [[.raw/papers/XUGL6XPD/data-availability|data-availability]], [[.raw/papers/XUGL6XPD/code-availability|code-availability]], [[.raw/papers/XUGL6XPD/repository-links|repository-links]], [[.raw/papers/XUGL6XPD/article-page|article-page]], [[.raw/papers/XUGL6XPD/asset-status|asset-status]]
- Related papers in this lab: [[papers/2025-J-space-based-solar-europe|Che et al. 2025, Joule]] (same journal, emerging-technology threshold TEA, and advanced nuclear comparator); [[papers/2020-J-data-center-load-migration-curtailment|Zheng et al. 2020, Joule]] (same journal and flexible demand or market-value framing); [[papers/2022-NE-china-hta-clean-hydrogen|Yang et al. 2022, Nature Energy]] (hard-to-abate industrial decarbonization and TEA); [[papers/2021-NCC-h2-efuels-potential-risks|Ueckerdt et al. 2021, Nature Climate Change]] (industrial heat alternatives and fuel merit-order reasoning); [[papers/2024-NE-h2-additionality-time-matching|Giovanniello et al. 2024, Nature Energy]] (ERCOT-linked policy TEA with hourly market and emissions boundaries).
- Pattern pages it will inform after paper 10: [[patterns/methods/stacked-revenue-tea]], [[patterns/figures/deployment-stack-curves]], [[patterns/methods/energy-quality-constraints]], [[patterns/discussion/screening-to-case-study-handoff]]
- Playbook pages it will inform after paper 20: [[playbook/tea/revenue-stack-scenarios]], [[playbook/figures/threshold-curve-design]], [[playbook/methods/facility-level-decision-units]]
- Contradiction scan: Inference: medium confidence, no substantive contradiction with existing paper pages was found. The closest tension is with hydrogen-focused papers that position hydrogen as a hard-to-abate option, but this paper evaluates SMRs as a competing heat source rather than disputing those hydrogen results.
