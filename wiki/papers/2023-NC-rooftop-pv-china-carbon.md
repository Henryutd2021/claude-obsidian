---
zotero_key: CRAKEP8V
title: "Carbon mitigation potential afforded by rooftop photovoltaic in China"
journal: "Nature Communications"
year: 2023
doi: "10.1038/s41467-023-38079-3"
topic: [rooftop-pv, distributed-pv, china, carbon-mitigation, geospatial-energy, urban-energy]
paper_type: [data-driven, scenario-analysis, policy-analysis]
main_contribution: [data-novelty, method-novelty, sectoral-coverage, policy-relevance]
method_type: [random-forest-regression, geospatial-assessment, k-means-clustering, carbon-mitigation-factor]
data_assets:
  main_pdf: true
  supplementary: false
  source_data: true
  data_statement: true
  code_statement: true
  code_repository: true
relevance_to_my_research: high
ingest_status: reviewed
address: c-000012
created: 2026-05-11
tags:
  - paper-analysis
---

# Carbon mitigation potential afforded by rooftop photovoltaic in China

> Zotero: `CRAKEP8V` · DOI: 10.1038/s41467-023-38079-3 · Journal: Nature Communications (2023)

## 1. One-sentence contribution

Evidence: This paper estimates 2020 rooftop photovoltaic carbon mitigation potential for 354 Chinese cities by combining a prior vectorized rooftop dataset, random-forest extrapolation, solar radiation, grid emission factors and clustering, then reports 65,962 km2 of rooftop area and about 4 billion tons of CO2 mitigation potential under its stated assumptions.

## 2. Archetype classification

Evidence: The archetype is data-driven geospatial assessment plus scenario analysis and policy analysis. The paper uses measured rooftop data for 86 cities, extrapolates the remaining 268 cities through random-forest regression, converts rooftop area into installed capacity, generation and avoided CO2, then tests 2030 changes under urban land expansion and power mix transformation scenarios.

Inference: Confidence high. It is not an optimization paper because it does not choose investments or dispatch. It is a potential-assessment paper that wins by converting a hard-to-observe physical stock, city rooftop area, into a national policy map.

## 3. Real value sources

| Dimension | Top driver? | Evidence | Inference | Lesson |
|---|---|---|---|---|
| Problem importance | Yes | Evidence: China emitted more than 10 billion tons of carbon in 2020, and its power sector accounts for about half of energy-related carbon emissions. | Inference: Confidence high. The case is large enough that a city-level rooftop result can speak to national decarbonization planning. | Lesson: Justify a city-scale paper by tying the city units to a national emissions deadline. |
| Problem novelty | Medium | Evidence: Prior city case studies and national statistics approaches existed, but the paper identifies the lack of city-level rooftop area data for more than 300 prefecture-level cities. | Inference: Confidence high. The gap is not "RPV matters"; the gap is scalable rooftop measurement. | Lesson: Frame crowded PV topics around the missing measurable object. |
| Method novelty | Medium | Evidence: The paper uses random forest with road length, built-up area, population and night lights to extrapolate rooftop area from 86 measured cities to 268 unmeasured cities. | Inference: Confidence medium. Random forest is standard, but the value comes from using it as a national rooftop measurement bridge. | Lesson: A standard method can carry a paper if it unlocks a missing national-scale variable. |
| Data novelty | Yes | Evidence: The paper starts from a vectorized rooftop dataset covering 16% of China and reports a 10 km2 grid rooftop dataset for 354 cities. | Inference: Confidence high. The dataset is the paper's core asset. | Lesson: When the data asset is the contribution, state its spatial resolution, coverage and validation in the opening results. |
| System boundary | Medium | Evidence: The boundary covers rooftop area, solar radiation, regional grid emission factors, urban land expansion and power mix change, but not storage dispatch or full life cycle emissions. | Inference: Confidence high. The boundary is broad for potential assessment and narrow for system operation. | Lesson: State whether the boundary is technical potential, economic potential or operational integration. |
| Case-study design | Yes | Evidence: The study covers 354 Chinese cities, 88% of China's area in 2020, and excludes Hong Kong, Macau, Taiwan and Tibet because grid emission factors were unavailable. | Inference: Confidence high. The case design is national but honest about missing jurisdictions. | Lesson: A large case gains credibility when exclusions are named with the missing data reason. |
| Result impact | Yes | Evidence: The study reports 4 billion tons of 2020 mitigation potential, city values from 0.04 to 52 million tons, and most provinces having less than 1% of installed potential exploited. | Inference: Confidence high. The results create both a total national headline and city/province targeting logic. | Lesson: Pair a big national number with a ranked local action map. |
| Mechanism explanation | Medium | Evidence: K-means++ separates city clusters by rooftop area, solar radiation and grid emissions, and explains why dense southeastern cities dominate total mitigation while western cities have high radiation but less rooftop area. | Inference: Confidence high. The mechanism is geographic endowment rather than a causal technology model. | Lesson: Use clustering to explain heterogeneity only when each cluster axis has a physical interpretation. |
| Comprehensiveness | Medium | Evidence: The paper spans 354 cities, four location-condition clusters, two urban land scenarios and two grid-emission scenarios. | Inference: Confidence medium. It covers geography and 2030 scenario levers, but not economics, storage or hourly grid constraints. | Lesson: Claim breadth by naming covered axes and immediately naming omitted axes. |
| Policy / industry implication | Yes | Evidence: The paper ranks cities by mitigation volume and intensity, compares theoretical installed capacity with existing installed capacity, and compares potential generation with electricity consumption. | Inference: Confidence high. These outputs are designed for local-government and project-priority decisions. | Lesson: Convert technical potential into at least two decision views: top-down volume and bottom-up intensity. |
| Writing / narrative | Yes | Evidence: The Introduction moves from climate and China emissions to distributed PV, then to the rooftop-area measurement bottleneck, then to the paper's machine-learning bridge. | Inference: Confidence high. The narrative is a clean funnel from national target to missing physical variable. | Lesson: Put the data bottleneck before the method so the method appears necessary. |
| Figure / table craft | Yes | Evidence: Six main figures move from scope, inputs, validation, clustering, potential and regional action diagnosis, while Table 1 isolates 2030 scenario outcomes. | Inference: Confidence high. The figure sequence maps the whole pipeline rather than only showing final maps. | Lesson: Sequence figures as pipeline, validation, result, action. |

**Top 3 value drivers**:
1. Evidence: National city-level rooftop area estimation across 354 Chinese cities.
2. Evidence: A headline carbon mitigation estimate linked to local prioritization.
3. Evidence: Validation and heterogeneity explanation through random forest and clustering.

**What it does NOT win on**:

Evidence: It does not win on economic feasibility, hourly integration, storage dispatch or life-cycle assessment. The Methods state that facility construction, transportation and recycling are outside the carbon calculation, and the Discussion names flexibility and cost assessment as future work.

**Most likely reason it cleared the top-tier bar**:

Inference: Confidence high. Nature Communications likely accepted it because the paper turns a national rooftop-data bottleneck into a reusable geospatial assessment pipeline, then ties the result to China's 2030 carbon-peak context with city-level maps rather than a single national total.

## 4. Research question & framing

Evidence: The research question is: how much CO2 mitigation could China's city-level rooftop photovoltaic resources deliver in 2020 and 2030, once rooftop area is estimated nationally and combined with solar resource and grid emission factors?

Inference: Confidence high. The framing is a "measurement bottleneck to policy map" structure. The authors do not ask whether rooftop PV is cheaper than alternatives. They ask where the hidden rooftop stock is and how its mitigation potential varies by city.

Lesson: For Henry's building-energy and distributed-energy papers, make the first research question about the missing measurable stock, then make the second question about what that stock changes in decarbonization planning.

## 5. Introduction structure (paragraph table)

| Paragraph | Function | Core info | Writing move | Why it works | Lesson |
|---|---|---|---|---|---|
| P1 | National stake and technology relevance | China exceeded 10 billion tons of carbon emissions in 2020, the power sector is about half of energy-related emissions, cumulative PV capacity reached 253 GW in 2020, and distributed PV share rose from 13% in 2016 to 31% in 2020. | Moves from climate to China to power-sector PV to distributed PV. | It makes rooftop PV a national mitigation lever rather than a niche urban feature. | Lesson: Open with policy target, emitting sector and technology diffusion in one chain. |
| P2 | Gap paragraph | City-level RPV potential is needed, but single-city studies do not transfer across more than 300 cities, national statistics are too aggregated, and rooftop delineation is the main error source. | Defines a data-resolution gap, not just a literature-volume gap. | It makes the missing object precise: city-level rooftop area at national scale. | Lesson: The gap paragraph should name the missing variable, the unit of analysis and the failed workaround. |
| P3 | Method and contribution preview | Urban information acquisition and artificial intelligence create an opening; the paper uses multisource geospatial data and machine-learning regression to quantify 354 cities, cluster geographic heterogeneity and assess 2030 scenarios. | Converts the gap into a pipeline and previews the result layers. | The contribution reads as a sequence of deliverables: data, potential, heterogeneity, future scenarios, exploitation status. | Lesson: End the Intro with deliverables in the same order as the Results. |

**Transferable Intro template extracted from this paper**:

Evidence: The template is "national target and sector stake -> technology deployment trend -> data-resolution bottleneck -> method that measures the missing stock -> policy-relevant maps and scenarios." Lesson: Use this template when a paper's strength is converting a hidden physical asset into a planning dataset.

## 6. Lit-gap & contribution construction

Evidence: The gap construction uses three comparisons. First, single-city PV studies cannot guide more than 300 Chinese cities with different geography and socioeconomic conditions. Second, national statistics such as floor area and land use are aggregated and limit city-level accuracy. Third, detailed high-resolution rooftop mapping is expensive and unavailable for most cities.

Inference: Confidence high. The contribution is built as a scale-up of measurement, not as a new PV concept. The prior work is not dismissed. Each prior approach is assigned a scale limit or data-resolution limit.

Lesson: When writing a top-tier assessment paper, avoid claiming that prior work is wrong. Say which prior approach is valid at one scale but fails at the scale needed by the policy question.

## 7. Method / model / design (adapt to archetype)

Evidence: The design has five linked blocks. The authors use a previous vectorized rooftop area dataset for 86 cities, divide the study area into 1,045,022 cells of 10 km2 each, build random-forest rooftop-area regression from road length, built-up area, population and night-light intensity, validate on 18 cities from six geographic regions, and convert rooftop area into installed capacity, generation and mitigation.

Evidence: The power and mitigation calculations assume 35% rooftop availability, 20% PV panel conversion efficiency, 80% overall PV system efficiency, 200 W rated power per unit panel area, and horizontal fixed panels. The mitigation factor is based on combined marginal grid emission factors with operating-margin and build-margin weights of 0.75 and 0.25.

Evidence: The scenario layer uses two urban land expansion scenarios, 9% and 14% rooftop-area growth from 2020 to 2030, and two power mix transformation scenarios, STEPS at a 10% emission-factor decline and APS at a 30% decline from 2020 to 2030.

Inference: Confidence medium. The strongest design choice is the validation layer because the paper does not ask readers to trust national extrapolation without ground-truth city checks. The weakest design choice is treating 35% rooftop availability as a national average when local roof shape, shading and ownership could vary sharply.

Lesson: In a geospatial extrapolation paper, put validation before the headline potential. It protects the result from becoming only a map-making exercise.

## 8. Data & case-study design

Evidence: The study covers 354 Chinese cities and excludes Hong Kong, Macau, Taiwan and Tibet because regional grid baseline emission factors were unavailable. It uses vectorized rooftop data, OpenStreetMap roads, ESRI 10 m land cover, WorldPop 100 m population, EOG 500 m nighttime lights, high-resolution solar radiation for China and regional grid emission factors.

Evidence: The validation dataset selects three representative cities in each of six geographic regions, for 18 validation cities. At the 10 km2 cell level, mean absolute error is 0.06 km2, most cells fall within -0.05 to 0.05 km2 error, city-level cumulative error is -26 km2 over 2641 km2 of rooftop area, and city relative error does not exceed plus or minus 20%.

Inference: Confidence high. The case study is strong because the city set matches the policy unit. Prefecture-level cities are not only computational units. They are also plausible local planning units.

Lesson: Match the spatial unit to the decision maker. City-level data supports city-level deployment policy better than national or provincial totals.

## 9. Results architecture

| Section | Main message | Evidence used | Role in argument | Why this order | Lesson |
|---|---|---|---|---|---|
| Study area and city representations | The paper defines the data pipeline and assumptions before showing potential. | Evidence: 86 measured cities, 268 extrapolated cities, 354 cities total, 35% availability, 20% panel efficiency and 80% system efficiency. | Establishes boundary and inputs. | Readers need the assessment unit before trusting maps. | Lesson: Put scope and assumptions before headline results. |
| Extrapolation and validation of rooftop area | Random forest can estimate rooftop area nationally with explicit validation. | Evidence: 1,045,022 cells, four explanatory variables, 10-fold cross-validation, validation on 18 cities, MAE of 0.06 km2 per 10 km2 cell and city relative error within plus or minus 20%. | Defends the data asset. | The mitigation result depends on rooftop area, so validation must precede potential. | Lesson: Validate the proxy variable before using it in carbon accounting. |
| Assessment of current RPV carbon mitigation potential | China's city-level RPV potential is large and spatially uneven. | Evidence: 4 billion tons in 2020, 0.04 to 52 million tons by city, 89% of potential in Clusters 1-3 in southeastern regions. | Provides headline and heterogeneity. | After validation, the paper can state the national and city results. | Lesson: Always report total, range and spatial concentration. |
| Assessment of future RPV carbon mitigation potential | 2030 potential depends on rooftop growth versus grid decarbonization. | Evidence: 5937 to 9235 km2 rooftop area growth, 416 to 646 GW added installed capacity potential, STEPS range 3730 to 3901 MT CO2 and APS range 2901 to 3034 MT CO2. | Adds policy-clock relevance. | The 2030 target makes the 2020 map forward-looking. | Lesson: Use scenarios to test whether the headline survives policy-driven changes. |
| Exploitation of RPV carbon mitigation potential | The paper translates theory into deployment priority. | Evidence: Volume and intensity quartiles, 73% of provinces and municipalities below 1% installed potential, 80% with potential generation above half of local electricity consumption. | Turns assessment into action diagnosis. | The last result answers "where next" after "how much." | Lesson: End with deployment triage, not only potential. |

## 10. Figures & tables argument function

| Item | Shows | Proves | Role | Why in main text | Design lesson |
|---|---|---|---|---|---|
| Fig. 1 | Study area, rooftop data scope, solar radiation, grid emission data and extrapolation from 86 to 268 cities. | Evidence: The paper has national scope and named data layers. | Scope figure. | It anchors the whole paper geographically. | Lesson: Use the first figure to show both case boundary and data boundary. |
| Fig. 2 | Regression input data: grid cells, vectorized rooftop polygons, roads, land cover, population and night lights. | Evidence: The explanatory variables are visible and interpretable. | Data-engineering figure. | It makes a machine-learning model readable to non-ML readers. | Lesson: Show proxies spatially before showing model metrics. |
| Fig. 3 | Correlations, prediction errors and random-forest performance. | Evidence: Correlations are 0.75, 0.83, 0.52 and 0.69 for road length, built-up area, population and night lights; validation MAE is 0.06 km2; R2 is 0.83. | Validation figure. | It defends the extrapolated rooftop map. | Lesson: Put validation in the main text when the input asset drives the whole paper. |
| Fig. 4 | K-means++ clustering of 354 cities by rooftop area, solar radiation and grid emissions. | Evidence: Four clusters differ across physical and power-system location conditions. | Mechanism figure. | It explains why potential is spatially uneven. | Lesson: Use clusters to convert a map into named mechanism groups. |
| Fig. 5 | Installed capacity, generation and carbon mitigation potential for 354 cities and clusters in 2020. | Evidence: Cluster 1 contributes 29% of total mitigation potential while Cluster 4 contributes 11%. | Headline result figure. | It reports the core potential at city and cluster levels. | Lesson: Pair city maps with aggregated cluster bars so readers can see pattern and total. |
| Fig. 6 | Regional deployment diagnosis by mitigation volume, intensity, installed gap, electricity demand and emissions comparison. | Evidence: It compares theory with current installation, consumption and emissions. | Action-priority figure. | It translates potential into where deployment pressure is highest. | Lesson: A final figure should answer "what should planners do with this map?" |
| Table 1 | 2030 mitigation under urban land expansion and grid-emission scenarios. | Evidence: STEPS gives 3730 to 3901 MT CO2, while APS gives 2901 to 3034 MT CO2. | Scenario table. | It isolates the effect of power mix transformation and rooftop growth without overloading Fig. 6. | Lesson: Use a compact table when the message is a small scenario matrix. |

Extended Data figures: N/A for this article format. Evidence: The article text references Supplementary Figs. 1-4 rather than Extended Data figures.

## 11. Discussion & Conclusion

Evidence: The Discussion elevates the 4 BT result into four policy messages: use building rooftops because land for PV installation is limited, prioritize dense southeastern cities for early RPV deployment, treat sparsely populated northwestern cities as better suited to centralized PV, and target highly industrialized coal-dependent cities for distributed PV as part of power-system transformation.

Evidence: The limitations are explicit. The main result estimates theoretical maximum mitigation potential, uses a national 35% rooftop-availability factor, omits life-cycle stages outside power generation, does not model detailed economic feasibility, and calls for future work on flexibility, storage, renewable complementarity, higher-resolution training data and costs.

Inference: Confidence high. The Discussion is stronger on spatial targeting than on system integration. It knows that rooftop PV creates grid-flexibility questions but leaves those for future studies.

Lesson: End a potential-assessment paper by naming the exact next model layer needed. Here that layer is flexibility plus storage plus cost.

## 12. Argument chain (compressed)

```text
China needs power-sector decarbonization by 2030 and 2060.
  -> Distributed PV is growing, but national city-level rooftop potential is hard to measure.
  -> Existing single-city and statistics-based studies cannot provide transferable city-level rooftop area.
  -> Use measured rooftop data from 86 cities plus multisource geospatial proxies and random forest.
  -> Validate extrapolation on 18 cities from six regions.
  -> Convert rooftop area into installed capacity, generation and avoided CO2 using stated PV and grid assumptions.
  -> Cluster cities by rooftop area, solar radiation and grid emissions.
  -> Report 4 BT 2020 potential and persistent 3-4 BT scale in 2030 scenarios.
  -> Compare theoretical potential with current installation, electricity demand and emissions.
  -> Recommend targeted city and provincial RPV deployment.
```

**Weakest link**:
Inference: Confidence high. The weakest link is the move from theoretical potential to deployable mitigation because rooftop ownership, grid hosting capacity, storage, hourly profile, permitting and economics are not modeled.

**Strongest link**:
Evidence: The strongest link is rooftop-area extrapolation and validation. The paper reports measured data for 86 cities, 18 validation cities, MAE of 0.06 km2 per cell and city relative error within plus or minus 20%.

## 13. Writing strategy extracted

Evidence: The title names object, outcome and geography in 9 words: rooftop photovoltaic, carbon mitigation and China. The abstract follows a compact structure: stakes, measurement challenge, method, 2020 headline, 2030 persistence, adoption gap and practice relevance.

Inference: Confidence high. The paper's best writing move is to make the hidden physical stock, rooftop area, the protagonist. The PV technology is familiar, but the national rooftop dataset is not.

Lesson: For Henry's papers, name the hidden asset in the title or first sentence when the technology itself is familiar. Do not make the title about "assessment" if the object can be named.

Lesson: Use a final abstract sentence that states how the dataset changes practice. Here the action target is "targeted RPV development in China."

## 14. Research-design strategy extracted

Evidence: The research design follows a defensible ladder: source data, extrapolation, validation, carbon conversion, clustering, future scenario, deployment diagnosis. Each ladder step has a figure or table.

Inference: Confidence high. The ladder works because each step answers a reviewer objection in order. Is the rooftop area known? If not, how is it estimated? Is the estimate validated? Does it matter for CO2? Where should deployment occur?

Lesson: Build assessment papers as objection ladders. Each main figure should remove one possible objection before the next claim appears.

Lesson: Separate technical potential from deployment status. This paper first reports theoretical mitigation, then shows that most cities have exploited less than 1% of potential.

## 15. Critical analysis

Evidence: The carbon estimate is operational-stage mitigation only. The Methods state that construction, transportation and recycling are not considered because life-cycle emissions are smaller than prevented operational emissions.

Evidence: The rooftop availability factor is 35% nationally, even though the Discussion says city-level availability can vary due to orientation, slope, obstacles and other factors.

Evidence: The 2030 scenario uses two drivers, urban land expansion and power mix transformation. It does not fully consider all factors that may change future potential.

Inference: Confidence high. A reviewer could push on whether theoretical rooftop potential translates into feasible urban deployment under distribution-grid limits, building ownership, roof condition and local load matching.

Lesson: Do not copy the single national rooftop-availability factor when writing a city-level deployment paper. If the claim is deployable capacity, add local roof quality, load match, grid hosting capacity and policy constraints.

## 16. Transfer to my own work

Evidence: The paper aligns with Henry's scope because it connects distributed solar, urban infrastructure, carbon mitigation, city-level planning and China energy policy.

Lesson: For wind-solar-hydrogen or green-hydrogen TEA, use this paper as a design model for creating a missing spatial input. Example: estimate city-level rooftop PV surplus as an input to distributed electrolysis siting rather than treating renewable supply as a provincial average.

Lesson: For building-energy decarbonization, copy the city-level stock logic. The paper makes rooftops measurable at planning scale; a building-energy paper could make retrofit surface, HVAC stock or flexible-load potential measurable at the same scale.

Inference: Confidence medium. The most valuable transfer is not the exact random-forest model. It is the paper's habit of converting a national policy target into a city-ranked asset map.

## 17. KB outputs (mandatory)

### 5 Permanent Notes (atomic, evergreen, with `Evidence:` from this paper)

1. City-level rooftop PV potential becomes policy-relevant when rooftop area, solar resource and grid emission factors are joined at the same spatial unit. Evidence: The paper estimates 65,962 km2 rooftop area and 4 BT CO2 mitigation potential for 354 Chinese cities in 2020. Lesson: Align physical asset, resource and emissions data before ranking locations.
2. A familiar technology can support a top-tier paper when the missing asset stock is newly measured at national planning scale. Evidence: The paper uses measured rooftop data from 86 cities and random-forest extrapolation to estimate 268 additional cities. Lesson: Make the hidden stock the contribution when the technology is already mature.
3. Validation must appear before carbon-accounting claims when the carbon result depends on a predicted spatial variable. Evidence: The validation set has 18 cities, cell-level MAE of 0.06 km2 and city relative error within plus or minus 20%. Lesson: Defend the input map before monetizing or carbonizing it.
4. Rooftop PV mitigation value declines as the grid becomes cleaner, even if rooftop area grows. Evidence: In 2030, STEPS gives 3730 to 3901 MT CO2, while APS gives 2901 to 3034 MT CO2 despite rooftop-area growth. Lesson: Report both resource growth and counterfactual grid decarbonization.
5. Technical potential needs a deployment-gap figure to become actionable. Evidence: The paper reports that 73% of provinces and municipalities had developed less than 1% of installed potential. Lesson: After estimating potential, compare it with current deployment.

### 5 Writing Lessons

1. Evidence: The title names outcome, asset and geography. Lesson: Use "carbon outcome + physical asset + case" when the paper is an assessment.
2. Evidence: The abstract gives the data bottleneck before the method. Lesson: State why the method is needed before naming the method.
3. Evidence: The gap paragraph contrasts single-city studies, national-statistics proxies and high-cost remote-sensing mapping. Lesson: Build the gap from failed scale transitions.
4. Evidence: The Results start with study-area representations before validation and potential. Lesson: Do not open geospatial papers with the final map before readers know the data boundary.
5. Evidence: The final Results section compares potential with installation, demand and emissions. Lesson: End with decision diagnostics rather than restating total potential.

### 5 Research-Design Lessons

1. Evidence: The model uses four interpretable urban proxies: road length, built-up area, population and night lights. Lesson: Prefer proxies that reviewers can physically link to the predicted asset.
2. Evidence: The paper validates on three cities in each of six geographic regions. Lesson: Validation samples should represent spatial heterogeneity, not only random holdouts.
3. Evidence: The paper separates 2020 current potential from 2030 scenario potential. Lesson: Keep baseline measurement and policy-clock projection in different result blocks.
4. Evidence: The clustering axes are rooftop area, solar radiation and grid emissions. Lesson: Choose clustering variables that map directly to mechanism, not only statistical separation.
5. Evidence: The paper states assumptions for rooftop availability, panel efficiency, system efficiency and rated power. Lesson: Put conversion assumptions near the first result that uses them.

### 5 Future Research Questions

1. Inference: Confidence high. How would city-level RPV mitigation potential change if distribution-grid hosting capacity and feeder constraints were included?
2. Inference: Confidence high. Which Chinese cities keep high rooftop PV value when hourly load matching, storage and curtailment are modeled?
3. Inference: Confidence medium. How would rooftop PV surplus support distributed green hydrogen production in industrial parks or dense urban load centers?
4. Inference: Confidence medium. What happens to the 35% rooftop availability assumption when roof ownership, roof age, shading and structural quality are measured city by city?
5. Inference: Confidence medium. Can the same rooftop-stock pipeline estimate building retrofit, heat-pump or flexible-load potential across Chinese cities?

## 18. Final summary

**Top 3 lessons**:
1. Evidence: The paper makes the hidden rooftop stock measurable at national city scale. Lesson: Convert missing physical assets into planning datasets.
2. Evidence: The paper validates rooftop extrapolation before stating mitigation potential. Lesson: Put validation before headline carbon claims.
3. Evidence: The paper turns 4 BT technical potential into city and province priority views. Lesson: End potential papers with deployment triage.

**Top 3 to transfer**:
1. Evidence: The pipeline moves from proxy data to asset stock to mitigation. Lesson: Use the same chain for city-level renewable integration inputs.
2. Evidence: The 2030 scenarios pair urban land expansion with grid decarbonization. Lesson: Pair resource growth with counterfactual emissions decline in TEA and policy studies.
3. Evidence: The figure sequence is scope, input, validation, mechanism, result and action. Lesson: Use figure order as an argument ladder.

**Top 3 to NOT blindly copy**:
1. Evidence: The study uses a national 35% rooftop availability factor. Lesson: Do not use one national factor for deployable city capacity without local constraints.
2. Evidence: The study excludes life-cycle stages outside power generation. Lesson: Do not generalize operational avoided CO2 to full LCA claims.
3. Evidence: The study does not model storage dispatch or hourly flexibility. Lesson: Do not use technical RPV potential as evidence of grid-integrated deliverable energy.

**One-line takeaway** (the core research skill this paper teaches):

Lesson: Make a hidden physical stock visible at the decision-maker's spatial scale, validate it, then convert it into policy-ranked outcomes.

## Pass-2 follow-up (deferred)

Deferred. Re-examine after more TPL papers are ingested for subtle lessons about geospatial proxy selection, validation figure placement, city-ranking rhetoric and how Nature Communications papers convert data assets into policy action maps.

## Cross-references

- Zotero parent key: `CRAKEP8V`
- Main PDF attachment key: `RV2YFDSR`
- Stub files: [[.raw/papers/CRAKEP8V/metadata.json|metadata]], [[.raw/papers/CRAKEP8V/zotero-attachments.md|zotero-attachments]], [[.raw/papers/CRAKEP8V/data-availability.md|data-availability]], [[.raw/papers/CRAKEP8V/code-availability.md|code-availability]], [[.raw/papers/CRAKEP8V/repository-links.md|repository-links]], [[.raw/papers/CRAKEP8V/article-page.md|article-page]], [[.raw/papers/CRAKEP8V/asset-status.md|asset-status]]
- Related papers in this lab: [[2023-N-china-pv-wind-3844-plants|Wang et al. 2023, Nature]] (China PV and geospatial renewable planning, utility-scale contrast), [[2022-NE-china-hta-clean-hydrogen|Yang et al. 2022, Nature Energy]] (China carbon-neutrality policy clock), [[2023-NC-endogenous-learning-green-h2-europe|Zeyen et al. 2023, Nature Communications]] (same journal and model-based energy transition assessment).
- Pattern pages it will inform after paper 10: [[patterns/methods/geospatial-proxy-to-energy-potential]], [[patterns/figures/validation-before-headline-map]], [[patterns/cases/china-city-scale-energy-policy]], [[patterns/contributions/data-asset-as-contribution]]
- Playbook pages it will inform after paper 20: [[playbook/intro-data-bottleneck-template]], [[playbook/figure-order-as-objection-ladder]], [[playbook/case-study-spatial-unit-choice]]
