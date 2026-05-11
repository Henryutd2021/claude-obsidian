---
zotero_key: UELISBYS
title: "Mitigating Curtailment and Carbon Emissions through Load Migration between Data Centers"
journal: "Joule"
year: 2020
doi: "10.1016/j.joule.2020.08.001"
topic: [data-center-flexibility, renewable-curtailment, load-migration, demand-response, hourly-grid-emissions, abatement-cost, caiso, pjm]
paper_type: [modeling, scenario-analysis, data-driven, TEA, policy-analysis]
main_contribution: [system-boundary-expansion, counterintuitive-result, policy-relevance, sectoral-coverage]
method_type: [counterfactual-simulation, hourly-grid-emissions, data-center-load-migration, abatement-cost-model, LCA-boundary]
journal_role: top_journal_exemplar
ingest_depth: A_deep
subdomain_primary:
  - power-systems
  - ai-data-driven
subdomain_secondary:
  - re-tech-resources
  - integrated-energy-systems
data_assets:
  main_pdf: true
  supplementary: false
  source_data: true
  data_statement: true
  code_statement: true
  code_repository: true
relevance_to_my_research: medium
ingest_status: reviewed
address: c-000011
created: 2026-05-11
tags:
  - paper-analysis
---

# Mitigating Curtailment and Carbon Emissions through Load Migration between Data Centers

> Zotero: `UELISBYS` | DOI: 10.1016/j.joule.2020.08.001 | Journal: Joule (2020)

## 1. One-sentence contribution

Evidence: The paper models whether moving flexible data-center workloads from PJM to CAISO during CAISO curtailment hours can absorb excess VRE and cut emissions, using 2015-2019 curtailment, 2016-2019 hourly generation, server-utilization assumptions, facility costs, and embodied emissions. Inference: high confidence, the contribution is a demand-flexibility reframing of curtailment mitigation, where information moves instead of electricity or hydrogen. Lesson: When studying flexible demand, quantify both the avoided grid emissions and the utilization constraint that decides how much excess renewable electricity can actually be absorbed.

## 2. Archetype classification

Evidence: This is a modeling, scenario-analysis, data-driven TEA, and policy-analysis paper because it combines historical CAISO and PJM hourly grid data, a typical 10 MW IT-power data-center profile, server utilization scenarios from 65% to 90%, additional zero-carbon cloud capacity, embodied-emissions accounting, and net abatement-cost surfaces. Inference: high confidence, the paper's strongest archetype is "counterfactual demand migration" rather than conventional storage TEA. Lesson: For Henry's work on hydrogen and flexible loads, test a competing flexibility pathway with the same seriousness as a supply-side technology, including cost, emissions, operating window, and implementation barriers.

## 3. Real value sources

| Dimension | Top driver? | Evidence | Inference | Lesson |
|---|---|---|---|---|
| Problem importance | Yes | Evidence: The Summary and Introduction frame VRE curtailment as rising with renewable penetration and name storage, transmission, pumped hydro, and hydrogen as existing responses with cost or siting limits. | Inference: high confidence, the paper enters a live grid-integration problem rather than a data-center-only problem. | Lesson: Start from the grid bottleneck, then introduce the computing asset only after the bottleneck is concrete. |
| Problem novelty | Yes | Evidence: The Introduction says the potential for load migration between data centers to use excess VRE and reduce GHG emissions had not been quantified. | Inference: high confidence, the gap is a quantified boundary gap across grid operations and computing workloads. | Lesson: A strong gap can be "no one has measured this cross-sector option", not only "no one has invented a new model". |
| Method novelty | Medium | Evidence: The paper links curtailment hours, hourly grid carbon intensity, server utilization, dynamic range, PUE, and data-center capacity into counterfactual baseline and migration scenarios. | Inference: medium confidence, the method value is in coupling existing datasets and assumptions, not in creating a new optimizer. | Lesson: Combine familiar modules across sectors when the research question is about coordination. |
| Data novelty | Medium | Evidence: The data stack includes CAISO 5-minute curtailment, CAISO generation, PJM Data Miner generation, data-center location and power estimates, and a typical data-center load profile. | Inference: medium confidence, the rare asset is the alignment of hourly grid and computing-capacity data. | Lesson: Treat time alignment as a data contribution when flexibility is the mechanism. |
| System boundary | Yes | Evidence: The model counts operational grid-emissions changes plus embodied emissions from added data-center capacity, and includes facility, electricity, and extra device costs. | Inference: high confidence, this boundary prevents "use curtailed power" from becoming a free-emissions story. | Lesson: Add embodied emissions when a flexibility option requires new physical capacity. |
| Case-study design | Yes | Evidence: CAISO supplies curtailment and lower-carbon excess VRE, while PJM supplies fossil-heavy baseline workloads and major data-center regions such as Northern Virginia. | Inference: high confidence, the case pair is chosen to maximize contrast in both power mix and computing demand. | Lesson: Pick paired regions where the mechanism is visible: one constrained renewable grid and one carbon-intensive workload source. |
| Result impact | Yes | Evidence: Figure 4 and the Summary report 113 to 239 KtCO2e per year reductions from existing CAISO data-center capacity in 2019, up to 62% curtailment absorption, and negative abatement cost. | Inference: high confidence, the result works because it gives a range, a utilization driver, and a cost sign. | Lesson: State a flexibility result as a feasible band rather than a single best-case point. |
| Mechanism explanation | Yes | Evidence: Figures 1 to 4 move from curtailment timing, to GHG-intensity gaps, to remaining server capacity, to emissions and cost surfaces. | Inference: high confidence, the paper succeeds by showing why the result occurs, not only that it occurs. | Lesson: Sequence figures so each one removes one uncertainty in the mechanism. |
| Comprehensiveness | Medium | Evidence: The paper covers 2015-2019 curtailment, 2016-2019 emissions intensity, server UR, PUE, DR, added capacity, embodied emissions, and abatement cost, while leaving software licensing and temporal deferral outside the model. | Inference: high confidence, the scope is broad across accounting layers but narrow in geography and workload classes. | Lesson: State what is inside the boundary and what is deferred, especially for cross-sector models. |
| Policy / industry implication | Yes | Evidence: Discussion calls for technology, policy, protocols, incentives, grid-operator communication, instantaneous generation/load/capacity data, and short-term VRE forecasting. | Inference: high confidence, the policy value lies in coordination architecture rather than one subsidy number. | Lesson: Translate model results into the institutions needed to make the control action real. |
| Writing / narrative | Medium | Evidence: The Introduction moves from curtailment, to limits of storage/transmission/hydrogen, to "moving bits, not watts", to quantified PJM-CAISO load migration. | Inference: high confidence, the rhetorical move makes data centers feel like a grid asset. | Lesson: Use a compact metaphor only after the physical constraint is already established. |
| Figure / table craft | Yes | Evidence: The main figures are a diagnostic time plot, a carbon-intensity comparison, a weekly load-profile illustration, and a two-panel emissions/cost contour result. | Inference: high confidence, the figures convert an abstract coordination idea into inspectable operating windows and thresholds. | Lesson: For a flexibility paper, combine time-series diagnostics with a final threshold surface. |

**Top 3 value drivers**:
1. Evidence: The paper reframes curtailment as a cross-sector load-migration opportunity, not only a storage or transmission problem.
2. Evidence: The result is quantified with hourly curtailment, hourly grid GHG intensity, server utilization, embodied emissions, and net abatement cost.
3. Evidence: The main result uses a surface over server UR and added data-center capacity, which exposes the point where added capacity stops helping.

**What it does NOT win on**: Evidence: The paper does not use confidential real data-center operations, does not model software licensing costs, does not optimize a live dispatch protocol, and does not evaluate temporal workload deferral.

**Most likely reason it cleared the top-tier bar**: Inference: high confidence, Joule accepted it because it turns an overlooked flexible-load asset into a quantified curtailment and emissions option, with a cost result that is bounded by embodied-emissions accounting.

## 4. Research question & framing

Evidence: The paper asks whether migrating data-processing workloads from fossil-heavy PJM to renewable-heavy CAISO during CAISO excess VRE hours can reduce curtailment, lower GHG emissions, and do so at no or negative cost. Evidence: The counterfactual baseline keeps workloads in typical PJM-served data centers, while the migration scenario first uses underutilized existing CAISO-served capacity and then adds zero-carbon cloud data centers for remaining excess VRE. Inference: high confidence, the research question is framed as "how much flexible computing demand is already latent in the system" rather than "how much new storage should be built". Lesson: In Henry's TEA work, include a demand-side counterfactual before treating storage or hydrogen as the default sink for curtailment.

## 5. Introduction structure (paragraph table)

| Paragraph | Function | Core info | Writing move | Why it works | Lesson |
|---|---|---|---|---|---|
| P1 | Energy transition opening | Evidence: The first paragraph says VRE such as solar PV and wind is growing under policy targets, including EU 2030 renewables and California's 2030 RPS. | Starts with macro transition pressure. | It makes curtailment a consequence of success in renewable deployment. | Lesson: Open a flexibility paper by showing the transition has created the operating problem. |
| P2 | Existing solution limits | Evidence: The second paragraph defines curtailment, lists Europe, America, and Asia, then reviews storage, transmission, and pumped hydro limits. | Narrows to bottleneck and incumbent fixes. | It prevents the paper from seeming like it invented concern about curtailment. | Lesson: Name competing solutions before introducing your alternative. |
| P3 | Material-product detour | Evidence: The third paragraph notes hydrogen from electrolysis can use excess VRE but faces logistics and handling costs, then proposes information as a transportable product. | Uses contrast between molecules and information. | It creates the "moving bits" bridge without dismissing hydrogen. | Lesson: Use an adjacent option, such as hydrogen, to show why your option solves a different bottleneck. |
| P4 | Data centers as flexible load | Evidence: The fourth paragraph reviews zero-carbon cloud, geographic load balancing, automated operations, flexible workloads, underutilized capacity, and non-coincident workload peaks. | Establishes technical feasibility. | It gives enough computing-domain evidence for energy readers to accept the mechanism. | Lesson: Before modeling a new asset class, prove it has controllability, unused capacity, and timing fit. |
| P5 | Gap paragraph | Evidence: The fifth paragraph says fiber networks are cheaper than transmission, data demand is growing, and the potential for load migration to use excess VRE and cut GHG emissions has not been quantified. | Combines economics, scale, and the missing measurement. | It makes the gap measurable and sector-crossing. | Lesson: The gap paragraph should end with the exact missing quantitative link. |
| P6 | Study design setup | Evidence: The final Introduction paragraph chooses CAISO and PJM, names CAISO curtailment and PJM thermal generation, and says the analysis uses historical hourly curtailment plus a typical data-center energy profile. | Converts the gap into a paired-region experiment. | It immediately tells the reader what the model will compare. | Lesson: End the Introduction with data, regions, and counterfactual structure, not a broad promise. |

**Transferable Intro template extracted from this paper**: Evidence: The paper uses the sequence "transition creates bottleneck -> incumbent fixes have limits -> adjacent sector has latent flexibility -> no one quantified the cross-sector mechanism -> paired case study tests it". Lesson: For Henry's hydrogen papers, use this structure when comparing electrolyzers against other flexible loads.

## 6. Lit-gap & contribution construction

Evidence: The literature gap is built from four bodies: VRE curtailment and storage/transmission limits, hydrogen as a curtailment sink, zero-carbon or green data-center operation, and geographic load balancing. Evidence: The contribution is stated as quantifying load migration between data centers for curtailment and GHG mitigation with CAISO and PJM as the test pair. Inference: high confidence, the paper's contribution construction depends on moving a known data-center practice from cost or renewable matching into grid-curtailment mitigation. Lesson: When adapting a method from another field, make the contribution a boundary shift with explicit input and output variables.

Evidence: The paper also uses a "negative comparison" against hydrogen and transmission: it does not claim those options are wrong, but it says they have logistics, handling, cost, siting, or infrastructure barriers. Inference: medium confidence, this is why the computing pathway feels credible to energy readers. Lesson: Use competing options as boundary markers, not as straw targets.

## 7. Method / model / design (adapt to archetype)

Evidence: The model has two scenarios. In the baseline scenario, workloads are processed by typical PJM-served data centers. In the migration scenario, workloads are migrated to CAISO-served data centers during excess VRE hours, first using remaining existing capacity and then adding zero-carbon cloud capacity if needed. Evidence: Remaining capacity is determined by the hourly load of a typical data center and a maximum allowed server UR ranging from 65% to 90%. Evidence: The model includes a 3-hour CAISO-PJM time difference, assumes similar data-center scale and energy-use characteristics, and assumes advanced automation can enable migration.

Evidence: The emissions module multiplies absorbed excess VRE by the difference between PJM generation GHG intensity and CAISO excess-VRE GHG intensity, then subtracts embodied emissions from added data-center capacity. Evidence: CAISO excess VRE intensity is treated as a solar/wind weighted value, while PJM intensity is based on hourly fuel generation and U.S.-specific life-cycle factors. Evidence: Added data-center embodied emissions are estimated from non-operational emissions and U.S. grid intensities, and facility/electricity/additional costs feed the abatement-cost calculation.

N/A for experimental controls for this archetype. Evidence: This is a counterfactual modeling paper, not a laboratory experiment with treatment and control samples. Lesson: For modeling work, the control is the baseline scenario, so define it as carefully as an experimental control.

## 8. Data & case-study design

Evidence: CAISO is selected because it has rising curtailment, detailed curtailment reporting, and a lower-carbon excess VRE profile. Evidence: PJM is selected because it is a large ISO with thermal-heavy generation and major data-center demand, including Northern Virginia. Evidence: The paper reports CAISO curtailment grew from 188 GWh in 2015 to 965 GWh in 2019, with solar PV making up 90% of cumulative curtailment and first plus second quarters making up 69%.

Evidence: The data-center side uses 288 data centers in the CAISO region by the end of 2019, an average annual total power consumption of 9.92 MW per California colocation site from 26 data points, and a standardized data center with 10 MW critical IT power, 21 MW total peak power, and about 114 GWh annual electricity consumption. Evidence: Efficiency parameters include dynamic range and PUE, with a linear non-server energy-use model reporting R2 = 0.988.

Inference: high confidence, the case design is intentionally asymmetric: CAISO supplies curtailment and PJM supplies carbon-intensive movable work. Lesson: For cross-region flexibility studies, the paired case should make the value of shifting visible in both timing and emissions.

## 9. Results architecture

| Section | Main message | Evidence used | Role in argument | Why this order | Lesson |
|---|---|---|---|---|---|
| Historical Curtailment of CAISO | Evidence: CAISO curtailment rose from 188 GWh in 2015 to 965 GWh in 2019, with solar-driven daytime concentration emerging by 2017-2019. | Evidence: Fig. 1 uses daily and hourly solar, wind, and total curtailment. | Establishes the temporal resource to absorb. | The reader first sees the size and timing of the wasted energy. | Lesson: Start results with the flexibility opportunity, not the final cost number. |
| Hourly GHG Intensity | Evidence: During CAISO excess generation hours, average CAISO excess intensity was 41 kgCO2e/MWh and PJM intensity was 476 kgCO2e/MWh during 2016-2019. | Evidence: Fig. 2 compares hourly life-cycle intensities. | Proves migrated work has a carbon gradient. | It shows that using curtailment also changes emissions. | Lesson: For load shifting, show the marginal or hourly carbon contrast before claiming abatement. |
| Data-center absorption capacity | Evidence: Existing CAISO data centers can absorb excess VRE depending on underutilized capacity and maximum server UR from 65% to 90%. | Evidence: Fig. 3 illustrates baseline versus migration energy profiles for a typical week. | Converts curtailment into feasible computing load. | It links the grid opportunity to operational server constraints. | Lesson: Show the physical load-shape change before the aggregate benefit. |
| GHG and abatement cost | Evidence: Existing capacity alone can absorb 29% to 62% of 2019 CAISO excess VRE, cut 113 to 239 KtCO2e, and yield -$242/tCO2e; added capacity can raise reductions to 247 KtCO2e. | Evidence: Fig. 4A and Fig. 4B report emissions and cost surfaces. | Delivers the decision result. | The final surface integrates all prior assumptions. | Lesson: Use a 2D threshold surface when two controllable levers jointly determine feasibility. |
| Discussion and implementation | Evidence: The Discussion calls for protocols, incentives, data sharing, short-term VRE forecasts, latency management, interruptible workloads, and confidentiality safeguards. | Evidence: Discussion paragraphs after Fig. 4. | Moves from modeled potential to adoption gates. | It avoids presenting the result as automatically deployable. | Lesson: Close a model paper with the institutional infrastructure required by the mechanism. |

## 10. Figures & tables argument function

| Item | Shows | Proves | Role | Why in main text | Design lesson |
|---|---|---|---|---|---|
| Graphical Abstract | Evidence: A workload is shifted from a fossil-heavy grid to a renewable-heavy grid during curtailment. | Inference: high confidence, the paper's whole mechanism is geographic load migration as demand response. | Entry-point mechanism. | It makes a cross-sector idea legible before equations. | Lesson: Use a graphical abstract when the mechanism crosses domains. |
| Fig. 1 | Evidence: CAISO solar and wind curtailment by day, and solar, wind, and total curtailment by day and hour for 2015-2019. | Evidence: Curtailment is growing and becoming daytime solar-linked. | Problem diagnosis. | The entire paper needs an hourly excess-energy target. | Lesson: Show the time pattern that your flexibility asset must match. |
| Fig. 2 | Evidence: Hourly life-cycle GHG intensity of PJM and CAISO for 2016-2019, with CAISO shown during curtailment periods. | Evidence: PJM workloads moved during CAISO excess hours face a large emissions-intensity contrast. | Carbon mechanism. | It justifies treating load migration as emissions mitigation, not only curtailment absorption. | Lesson: Pair flexibility timing with carbon intensity timing. |
| Fig. 3 | Evidence: A typical data-center weekly energy profile changes from baseline to migration under a 65% maximum server UR example. | Evidence: Underutilized server capacity can absorb added work during excess VRE hours. | Operational feasibility illustration. | It bridges abstract curtailment to data-center operations. | Lesson: Include one intuitive operational example before presenting contour results. |
| Fig. 4 | Evidence: Net GHG emissions reduction and net abatement cost vary by maximum server UR and added data-center capacity in 2019. | Evidence: Existing capacity can reduce 113 to 239 KtCO2e, and excessive added capacity can reduce the benefit because embodied emissions and costs rise. | Main decision figure. | It shows feasible, profitable, break-even, and overbuild regions in one place. | Lesson: Let the main figure reveal the stopping rule, not only the optimum. |
| Table S1 to S5 | Evidence: Supplementary tables contain emission factors, data-center specifications, DR/PUE assumptions, cost breakdowns, and nomenclature. | Inference: medium confidence, the SI carries reproducibility detail for the cost and emissions model. | Methods support. | Main text stays readable while assumptions remain traceable. | Lesson: Keep the article's narrative compact and push parameter inventory to SI. |

## 11. Discussion & Conclusion

Evidence: The Discussion first re-states the grid problem, then reports that existing CAISO-served data-center capacity can absorb up to 62% of excess VRE and reduce up to 239 KtCO2e in 2019 at -$242/tCO2e, provided server UR improves. Evidence: It then says added data centers could absorb up to 79% cumulative excess VRE and reduce up to 247 KtCO2e while keeping negative abatement cost. Evidence: The paper also notes an 80% or higher absorption target does not make economic sense under any maximum server UR because net abatement cost turns positive.

Evidence: The Discussion elevates the result to institutional needs: real-time workload-migration protocols, incentives, communication between grid operators and data centers, instantaneous generation/load/capacity data, short-term VRE forecasts, latency management, interruptible workloads, storage for checkpoint-restart, and confidentiality safeguards. Inference: high confidence, the paper's conclusion is a "coordination stack" rather than a pure technology-availability claim. Lesson: When a result depends on coordination, make the adoption architecture part of the conclusion.

## 12. Argument chain (compressed)

```text
VRE growth creates curtailment
  -> storage, transmission, pumped hydro, and hydrogen each face cost or logistics limits
  -> information can move more cheaply than electricity or molecules
  -> data centers have geographic flexibility and underused server capacity
  -> CAISO has excess VRE and PJM has carbon-intensive workloads
  -> hourly counterfactual migration can absorb CAISO excess VRE
  -> emissions fall when PJM load is replaced by CAISO excess VRE processing
  -> costs stay negative until added data-center capacity overbuilds the opportunity
  -> implementation requires protocols, incentives, forecasts, and data sharing
```

**Weakest link**: Evidence: The paper lacks confidential real-world data-center workload and power profiles, so it relies on a typical profile and simplified workload compatibility assumptions. Inference: high confidence, this is the main reviewer pressure point because the result depends on underutilized capacity and movable jobs.

**Strongest link**: Evidence: The paper aligns the CAISO curtailment time series with PJM and CAISO hourly GHG intensity and server-capacity constraints. Inference: high confidence, the time-resolved mechanism is stronger than a static annual comparison. Lesson: The strongest part of a flexibility paper is the aligned-hour logic.

## 13. Writing strategy extracted

Evidence: The paper's central phrase is effectively "moving bits, not watts", but the paper earns that phrase by first discussing curtailment, storage, hydrogen, transmission, data-center automation, and unused capacity. Inference: high confidence, the phrase works because it condenses an already-supported mechanism. Lesson: Use memorable language only after the evidence has narrowed the reader to that idea.

Evidence: The authors avoid overclaiming by reporting ranges over maximum server UR and added capacity, then naming the 80% absorption threshold as economically unattractive. Inference: high confidence, the stopping rule gives credibility to the negative-cost result. Lesson: In Henry's writing, include the "do not overbuild past this point" result whenever an option looks cheap.

Evidence: The Results are organized as problem data, carbon data, capacity logic, and cost/emissions integration. Inference: high confidence, this order makes a cross-sector model readable to both energy and computing audiences. Lesson: For mixed-audience papers, order results by reader questions rather than by model modules.

## 14. Research-design strategy extracted

Evidence: The research design uses a counterfactual baseline and migration scenario with the same workload service but different location and timing. Lesson: For Henry's flexible hydrogen and data-center studies, keep the service output constant so the comparison isolates the flexibility mechanism.

Evidence: The model starts with existing capacity before adding new zero-carbon cloud capacity. Inference: high confidence, this separates a low-capex operating strategy from infrastructure expansion. Lesson: Always test "use existing slack better" before proposing new assets.

Evidence: The paper counts embodied emissions only for additional data-center capacity, and this causes GHG reductions to peak before 80% absorption. Lesson: Add embodied-emissions terms where they can change the optimal capacity, not just as an appendix footnote.

Evidence: The paper does not model software licensing because public data are lacking. Inference: medium confidence, the authors chose transparency over a weak placeholder assumption. Lesson: When a cost category lacks data, state the exclusion and explain the direction of bias.

## 15. Critical analysis

Evidence: The paper uses a simulated typical data-center weekly load profile and extrapolates it to a full year, while noting seasonal variation is not considered. Inference: high confidence, this can bias remaining capacity estimates if cooling loads or workload patterns correlate with curtailment seasons. Lesson: Do not reuse one representative week for annual flexibility unless the seasonal sensitivity is tested.

Evidence: The authors state there is no complete transparent database of U.S. data-center capacity, and power-consumption data are scarce. Inference: high confidence, the CAISO capacity estimate is directionally useful but not a site-level deployment plan. Lesson: Treat facility-count data as a screening layer, then validate with operator or interconnection data before making siting claims.

Evidence: The model assumes migration between similar-scale data centers with typical energy-use characteristics and excludes software licensing costs. Inference: high confidence, the result is best read as technical-economic potential under coordination, not as a ready market offer. Lesson: In Henry's own papers, separate "potential" scenarios from "deployable under current market rules" scenarios.

Evidence: The paper focuses on spatial workload migration and says temporal deferral is not evaluated. Inference: medium confidence, the combined spatial-temporal control problem could change the utilization and curtailment absorption bands. Lesson: A follow-up study should compare shifting across regions, deferring in time, and hybrid scheduling under the same emissions metric.

## 16. Transfer to my own work

Evidence: The paper is medium relevance to Henry's research scope because it is not hydrogen TEA directly, but it is highly relevant to renewable integration, flexible demand, hourly emissions, curtailment sinks, and data-center decarbonization. Inference: high confidence, its biggest transfer value is as a competing-flexibility benchmark for hydrogen and battery storage papers.

Lesson: In a green-hydrogen TEA, add a competing curtailment-sink scenario where flexible data centers, thermal loads, or industrial demand absorb the same excess VRE before assuming electrolyzers get the full resource. Lesson: In energy-system optimization, represent digital loads as movable demand with latency and utilization constraints, not as fixed annual consumption. Lesson: In policy-cost analysis, include communication protocols and incentive design when the modeled action requires two sectors to coordinate in real time.

Evidence: The paper's DA/CA statement links datasets and code to Mendeley Data. Lesson: For Henry's own studies, use a single public DOI for data and code when possible, then make the availability statement short and direct.

## 17. KB outputs (mandatory)

### 5 Permanent Notes (atomic, evergreen, with `Evidence:` from this paper)

1. Flexible computing demand can act as a curtailment sink when excess renewable hours align with underused server capacity. Evidence: The paper models CAISO excess VRE hours and reports existing CAISO-served data centers could absorb 29% to 62% of 2019 excess VRE depending on maximum server UR. Lesson: When modeling demand flexibility, quantify the unused-capacity window before estimating emissions benefits.
2. Moving information can be a substitute for moving electricity when transmission is costly and workloads are geographically portable. Evidence: The Introduction contrasts transmission expansion and hydrogen logistics with data transfer and geographic load balancing. Lesson: In cross-sector energy papers, identify what physical product or service actually needs to move.
3. Emissions benefits from new flexible-load infrastructure can peak before total curtailment absorption is maximized. Evidence: Figure 4 shows net GHG reduction peaks around 68% to 75% absorption when maximum server UR exceeds 85%, and above 80% absorption added capacity no longer improves reductions. Lesson: Report the emissions-optimal scale, not just the maximum utilization of curtailed energy.
4. Existing capacity can change the economics of a curtailment solution. Evidence: Without additional data-center capacity, the existing-capacity migration case has a net abatement cost of -$242/tCO2e in 2019, driven by lower electricity cost. Lesson: Separate operational reallocation from new-build expansion in TEA scenarios.
5. Implementation barriers for cross-sector flexibility are institutional as much as technical. Evidence: The Discussion calls for protocols, incentives, grid-operator communication, forecasting, latency management, and confidentiality safeguards. Lesson: End flexible-load papers with the coordination requirements implied by the model.

### 5 Writing Lessons

1. Lesson: Use "incumbent solution limits" before introducing a surprising alternative. Evidence: The Introduction covers storage, transmission, pumped hydro, and hydrogen before data-center load migration.
2. Lesson: Make the gap a missing quantitative link across sectors. Evidence: The gap says load migration's potential to use excess VRE and reduce GHG emissions had not been quantified.
3. Lesson: Use one memorable phrase only after the mechanism is grounded. Evidence: The "moving bits, not watts" line follows discussion of over-generated electricity, data-center flexibility, and network economics.
4. Lesson: Put the main result in a two-lever surface when the decision depends on both operations and new capacity. Evidence: Figure 4 varies maximum server UR and additional data-center capacity.
5. Lesson: State the stopping rule in the Discussion. Evidence: The paper says absorbing more than 80% of excess VRE does not make economic sense under any maximum server UR.

### 5 Research-Design Lessons

1. Lesson: Pair regions so each side supplies one necessary contrast. Evidence: CAISO supplies curtailment and low-carbon excess VRE, while PJM supplies carbon-intensive baseline workloads.
2. Lesson: Use hourly alignment when studying flexibility. Evidence: The paper combines hourly CAISO curtailment, hourly CAISO/PJM generation intensity, and hourly data-center load profiles.
3. Lesson: Model existing slack before adding new assets. Evidence: The migration scenario first uses existing CAISO data-center capacity, then adds zero-carbon cloud capacity only after existing capacity is exhausted.
4. Lesson: Include embodied emissions when added capacity changes the optimum. Evidence: Added data-center embodied emissions cause net GHG reductions to peak before full curtailment absorption.
5. Lesson: Track omitted costs explicitly. Evidence: The paper excludes software licensing costs due to lack of public information and flags data-center cost uncertainty as a limitation.

### 5 Future Research Questions

1. How would real hyperscale data-center hourly workload and cooling profiles change the 29% to 62% existing-capacity absorption estimate?
2. What market design would pay data centers for absorbing curtailment while protecting service-level agreements and user latency?
3. How does spatial load migration compare with temporal workload deferral, electrolytic hydrogen, batteries, and thermal demand response under a shared hourly emissions metric?
4. What happens if CAISO imports, marginal emissions, or nodal congestion replace the paper's average life-cycle intensity method?
5. Can carbon-aware AI training and inference loads provide a larger flexible-load pool than the generic workload profile used in the 2020 study?

## 18. Final summary

**Top 3 lessons**:
1. Evidence: The paper shows a curtailment sink can be a movable service demand, not only a physical storage asset. Lesson: Include demand-side alternatives in curtailment TEA.
2. Evidence: Figure 4 shows that the best economic and emissions region is bounded by server UR and added capacity. Lesson: Use threshold surfaces for flexible-load design.
3. Evidence: The Discussion names protocols, incentives, forecasts, latency, and confidentiality as adoption gates. Lesson: Treat coordination infrastructure as part of the research object.

**Top 3 to transfer**:
1. Lesson: For hydrogen work, compare electrolyzers against other curtailment sinks using the same hourly resource and emissions data.
2. Lesson: For data-center-energy studies, model load as dispatchable within latency and utilization constraints.
3. Lesson: For TEA, separate existing-capacity operation from new infrastructure and include embodied emissions when adding assets.

**Top 3 to NOT blindly copy**:
1. Evidence: The paper uses one typical weekly data-center energy profile extended to a year. Lesson: Do not copy this without seasonal validation.
2. Evidence: The paper assumes similar-scale data centers and advanced automation for migration. Lesson: Do not treat potential as deployment readiness.
3. Evidence: Software licensing costs are excluded. Lesson: Do not claim full business economics unless software and operational contracts are included.

**One-line takeaway**: Evidence: Zheng et al. 2020 teaches that flexible demand can be evaluated like storage only when timing, capacity slack, carbon intensity, embodied emissions, and coordination rules are all visible.

## Pass-2 follow-up (deferred)

Deferred: Re-read the paper after 10 TPL ingests to mine less obvious lessons on cross-sector metaphors, negative-cost claims, Figure 4 threshold design, and how the limitations section protects a potential study from overdeployment claims.

## Cross-references

- Zotero parent key: `UELISBYS`
- Main PDF attachment key: `2LS5AM2J`
- Stub files: [[.raw/papers/UELISBYS/metadata.json|metadata]], [[.raw/papers/UELISBYS/zotero-attachments.md|zotero-attachments]], [[.raw/papers/UELISBYS/data-availability.md|data-availability]], [[.raw/papers/UELISBYS/code-availability.md|code-availability]], [[.raw/papers/UELISBYS/repository-links.md|repository-links]], [[.raw/papers/UELISBYS/article-page.md|article-page]], [[.raw/papers/UELISBYS/asset-status.md|asset-status]]
- Related papers in this lab: [[2025-J-space-based-solar-europe]] shares Joule and threshold-based system TEA; [[2021-NE-kikstra-covid-energy-demand-scenarios]] shares demand-side load-change framing; [[2024-NE-h2-additionality-time-matching]] shares hourly grid-emissions and flexible hydrogen-policy relevance.
- Pattern pages it will inform after paper 10: [[patterns/value-source/demand-flexibility-as-storage]], [[patterns/figures/threshold-surface-main-result]], [[patterns/methods/counterfactual-load-migration]], [[patterns/discussion/implementation-barrier-ladder]]
- Playbook pages it will inform after paper 20: [[playbook/intro/bottleneck-to-flexibility-alternative]], [[playbook/figures/show-thresholds-not-only-points]], [[playbook/methods/include-embodied-emissions-boundary]]
