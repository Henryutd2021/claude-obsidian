---
zotero_key: 52W57HP5
title: "Sources of data center energy estimates: A comprehensive review"
journal: "Joule"
year: 2022
doi: "10.1016/j.joule.2022.07.011"
topic: [data-center-energy, electricity-demand, energy-estimates, data-provenance, reproducibility, energy-policy]
paper_type: [review, data-driven, policy-analysis]
main_contribution: [data-novelty, policy-relevance, method-novelty]
method_type: [literature-review, source-provenance-mapping, methodological-classification, FAIR-data-audit]
journal_role: top_journal_exemplar
ingest_depth: A_deep
subdomain_primary:
  - ai-data-driven
  - energy-policy-economics
subdomain_secondary:
  - lca-sustainability
data_assets:
  main_pdf: true
  supplementary: false
  source_data: false
  data_statement: true
  code_statement: true
  code_repository: true
relevance_to_my_research: high
ingest_status: reviewed
address: c-000023
created: 2026-05-11
tags:
  - paper-analysis
---

# Sources of data center energy estimates: A comprehensive review

> Zotero: `52W57HP5` · DOI: 10.1016/j.joule.2022.07.011 · Journal: Joule (2022)

## 1. One-sentence contribution

Evidence: Mytton and Ashtine analyze 258 data-center energy estimates from 46 publications from 2007 to 2021 and trace 676 source links to show that reliability problems come less from one bad estimate than from weak source provenance, private market data, broken links, vague methods and future extrapolation. Lesson: When Henry estimates data-center, hydrogen or building loads, make the source audit part of the result rather than a hidden appendix.

## 2. Archetype classification

Evidence: This is a review plus data-provenance audit. The paper selects original publications that estimate use-stage electricity for a whole region or the world, extracts estimates and source categories, classifies methods as bottom-up, top-down or extrapolation, and turns the review into recommendations for end users, researchers and regulators. Inference: high confidence. Its Joule fit comes from making a messy evidence base decision-relevant for grid planners and policy users, not from adding a new energy-system optimization model. Lesson: A review can pass a top energy venue when it converts scattered estimates into a reliability framework with a concrete stakeholder action list.

## 3. Real value sources

| Dimension | Top driver? | Evidence | Inference | Lesson |
|---|---|---|---|---|
| Problem importance | Yes | Evidence: The Introduction connects data-center electricity uncertainty to public climate claims, West London grid-connection delays, Irish data-center demand and Danish demand projections. | Inference: high confidence, the paper frames estimate reliability as an infrastructure-planning problem, not a narrow literature-accounting problem. | Lesson: Tie estimate quality to decisions with physical lead times, such as grid upgrades or hydrogen infrastructure. |
| Problem novelty | Medium | Evidence: Earlier work had estimated data-center energy, but this paper asks whether the sources behind those estimates can be found, evaluated and reused. | Inference: high confidence, the freshness is in auditing the evidence chain behind estimates. | Lesson: If a topic is crowded, audit the inputs and provenance behind the headline numbers. |
| Method novelty | Medium | Evidence: The method maps 676 data-provenance traces across servers, storage, network, infrastructure and market categories. | Inference: high confidence, the method is a systematic coding exercise rather than a new quantitative model. | Lesson: Use a transparent coding grid when reviewing model assumptions across papers. |
| Data novelty | Yes | Evidence: The review extracts 258 estimates from 46 original publications and classifies source type, source access and reliability. | Inference: high confidence, the reusable asset is the structured source map, not only the narrative review. | Lesson: Build a table that future reviewers can inspect, rerun and extend. |
| System boundary | Yes | Evidence: Inclusion requires original calculations for whole-region or global use-stage data-center electricity, while cryptocurrency and network definitions are treated as boundary complications. | Inference: high confidence, boundary inconsistency is one of the paper's central mechanisms for conflicting results. | Lesson: Put system-boundary definitions before comparing cost or energy estimates. |
| Case-study design | Medium | Evidence: The paper uses global, USA, Europe, Germany, Sweden and China estimate coverage and policy examples from Ireland, Amsterdam and London. | Inference: medium confidence, the case examples are chosen to show why source reliability matters in real grid-planning settings. | Lesson: Pair a global evidence review with local policy cases that expose consequences. |
| Result impact | Yes | Evidence: The Summary reports 31% peer-reviewed sources, 38% reports, 43% reliance on IDC, 30% on Cisco, 11% broken web links and 10% insufficient detail. | Inference: high confidence, the result works because percentages turn a qualitative worry into an evidence-base diagnosis. | Lesson: Convert trust concerns into measurable audit categories. |
| Mechanism explanation | Yes | Evidence: Figures 6 and 7 trace how missing or private sources propagate through later cited estimates. | Inference: high confidence, the mechanism is citation-chain fragility and baseline reuse. | Lesson: Show how an error or opacity source travels, not only that it exists. |
| Comprehensiveness | Medium | Evidence: The title uses this term, and the paper spans 46 publications, 258 estimates and 676 source traces across multiple component categories. | Inference: high confidence, the breadth is across source provenance and estimate methods, not every data-center sustainability dimension. | Lesson: When using breadth claims, define the axes: publications, estimates, source traces and categories. |
| Policy / industry implication | Yes | Evidence: Recommendations target end users, researchers and policy makers, with disclosure requirements for data-center operators and equipment manufacturers. | Inference: high confidence, the paper turns a literature review into governance advice. | Lesson: End a review with stakeholder-specific rules rather than generic future work. |
| Writing / narrative | Yes | Evidence: The Introduction moves from IT growth to estimate variance, then to public confusion, grid planning, emissions and the review's source-provenance focus. | Inference: high confidence, the story narrows from social relevance to a precise review object. | Lesson: Use stakeholder confusion and grid constraints to motivate an evidence-audit paper. |
| Figure / table craft | Yes | Evidence: Figures 2, 4 and 5 show estimate ranges; Figures 6 and 7 show citation flows; Figure 9 turns recommendations into a workflow. | Inference: high confidence, the figures move from diagnosis to mechanism to remedy. | Lesson: A review figure set should include at least one mechanism diagram and one action workflow. |

**Top 3 value drivers**:
1. Evidence: Source-provenance data scale: 258 estimates, 46 publications and 676 source mappings.
2. Evidence: Reliability diagnosis: private IDC/Cisco dependence, broken links, insufficient references and weak method detail.
3. Evidence: Stakeholder translation: end-user checklist, researcher workflow and regulator disclosure agenda.

**What it does NOT win on**: Evidence: It does not create a new data-center electricity estimate, does not inspect every citation chain beyond the first source level, and does not verify all private commercial data. Inference: high confidence, the paper's value comes from evaluating estimate reliability rather than selecting one best estimate.

**Most likely reason it cleared the top-tier bar**: Inference: high confidence. Joule accepted the paper because it reframes data-center energy debate from "which TWh number is right" to "which estimates have inspectable sources, reusable methods and policy-grade data provenance."

## 4. Research question & framing

Evidence: The paper asks how reliable data-center energy estimates are when judged by the sources and data inputs used to calculate them. Evidence: The method restricts the review to English-language publications since 2007 that provide original calculations for whole-region or global use-stage electricity. Inference: high confidence, this framing is effective because it avoids ranking every estimate and instead asks whether the evidence chain is strong enough for reuse.

Lesson: For Henry's data-center or hydrogen-load papers, frame the research question around decision reliability: "Which input assumptions can be audited, reproduced and updated before a planner uses the result?"

## 5. Introduction structure (paragraph table)

| ¶ | Function | Core info | Writing move | Why it works | Lesson |
|---|---|---|---|---|---|
| P1 | Object definition | Evidence: Data centers are secure environments for servers, network switches and storage, ranging from cabinets to hyperscale warehouses. | Starts with a plain system definition. | It gives non-specialist Joule readers the physical object before the controversy. | Lesson: Define the engineered object before giving statistics. |
| P2 | Growth context | Evidence: Server instances rose 647%, storage capacity 2,500% and network traffic 1,000% over the previous decade; hyperscale sites were growing. | Establishes demand pressure without yet claiming energy growth. | It separates IT-service growth from energy-use growth. | Lesson: Keep service-demand growth and electricity growth as separate variables. |
| P3 | Estimate conflict | Evidence: One side reports plateauing data-center energy near 205 TWh by 2018 and 209.6 TWh by 2023, while others project up to 51% of global electricity demand by 2030. | Places extreme estimates side by side. | It creates the puzzle without deciding which number is correct. | Lesson: Show the range before explaining why the range exists. |
| P4 | Public-action consequence | Evidence: The paper notes claims about deleting photos or chat messages as climate action and warns that decoupling would make such actions weak. | Moves from technical estimates to public behavior. | It shows that bad estimates distort everyday climate advice. | Lesson: Include a human consequence when a modeling dispute looks abstract. |
| P5 | Grid-planning consequence | Evidence: The Introduction cites West London housing delays, Ireland's data-center electricity growth from 1.2 TWh in 2015 to 3.0 TWh in 2020, and Denmark's 15% projection for 2030. | Converts estimate variance into infrastructure planning risk. | It makes the question relevant to grid operators and policy makers. | Lesson: Link load estimates to grid-connection lead times. |
| P6 | Emissions consequence | Evidence: The paper cites IT's share of global greenhouse gas emissions as 1.8% to 2.8%, possibly 3.9%, then says reliability of estimates must be understood. | Connects electricity estimates to emissions accounting. | It expands the stakes beyond local grid congestion. | Lesson: Put emissions relevance after the demand-planning relevance. |
| P7 | Study object and period | Evidence: The authors analyze original data-center energy estimates published from 2007 to 2021, starting near the public-cloud era and the Brown et al. report. | Defines the review window historically. | It justifies why the review starts at 2007. | Lesson: Anchor a review period to a technological regime shift. |
| P8 | Scope boundary | Evidence: The paper focuses on use-stage electricity, not embodied emissions or water consumption. | Narrows the field after showing broader sustainability relevance. | It prevents the paper from becoming a general sustainability review. | Lesson: State excluded impact categories before reviewers ask. |
| P9 | Gap paragraph | Evidence: The final Introduction paragraph says the review examines source provenance and data inputs because they determine reliability, then previews methods, data-quality findings and recommendations. | Turns the gap into a source-audit task. | It makes the contribution operational: trace sources, classify methods and advise users. | Lesson: The gap paragraph should name the exact audit object, not just say previous estimates differ. |

**Transferable Intro template extracted from this paper**:

Evidence: The Introduction follows a nine-step ladder: define the system, show service growth, show conflicting estimates, show public confusion, show infrastructure risk, show emissions relevance, define the review period, narrow the scope and state the source-provenance gap. Lesson: Use this ladder for data-center, hydrogen or building-energy papers where the field has many inconsistent estimates.

## 6. Lit-gap & contribution construction

Evidence: The literature gap is not "no one has studied data-center energy." The gap is that many published estimates cannot be compared or trusted because their input sources are private, broken, insufficiently specified or methodologically incompatible. Evidence: The paper explicitly avoids criticizing individual estimates and instead studies common methodological problems.

Inference: high confidence. This gap construction is strong because it turns prior literature abundance into the reason for the new paper. More estimates make the field harder to use, so the paper justifies a review that audits provenance and reliability.

Lesson: When Henry's topic has many TEA or load estimates, do not claim scarcity. Claim that existing numbers are not decision-ready because boundaries, sources, scenarios or uncertainty treatments differ.

## 7. Method / model / design (adapt to archetype)

Evidence: This is N/A for an experimental controls frame because the paper is a review and source-audit article. The design uses a literature search with data-center keywords, includes English-language publications since 2007, and selects publications only if they offer original whole-region or global use-stage electricity calculations with methods and sources.

Evidence: The authors extract estimate geography, estimate year and scenario into Table S2; classify key data or analysis sources by component category into Table S1; group source information for statistical analysis and visualization in Table S3; and code source access categories such as existing link, not found, broken link, not specified and private/commercial.

Inference: high confidence. The method is a reproducibility audit layered on a review. It treats each estimate as a claim whose credibility depends on traceable input data, method detail, source access and boundary compatibility. Lesson: For Henry's own review-style papers, build the extraction table before the narrative so every recommendation can point back to a coded field.

## 8. Data & case-study design

Evidence: The review includes 46 publications, 258 estimates and 676 provenance traces. Evidence: Scope covers global, USA, Europe, Germany, Sweden and China estimates, with 179 global estimates, 24 USA estimates and 19 Europe estimates. Evidence: Use-stage electricity is the focal metric and all calculations are converted to annual TWh.

Inference: high confidence. The "case study" is the data-center energy-estimate literature itself, while Ireland, Amsterdam and London serve as policy-facing examples of why estimate reliability matters. Lesson: In Henry's work, separate the empirical corpus from the policy examples. The corpus proves the pattern; the examples prove why the pattern matters.

## 9. Results architecture

| Section | Main message | Evidence used | Role in argument | Why this order | Lesson |
|---|---|---|---|---|---|
| Review methodology | Define eligible evidence and audit categories. | Evidence: Figure 1, Table 1 and Tables S1 to S3 specify inclusion, source categories and availability codes. | Sets the audit rules. | The reader must trust the review before accepting the reliability critique. | Lesson: Put the review protocol before the shocking percentages. |
| Findings: bringing estimates together | Published estimates span wide TWh ranges and become more dispersed for future years. | Evidence: Figures 2 and 5 show 2010, 2020 and 2030 ranges, excluding five estimates above 2,000 TWh for display. | Establishes the variance problem. | It motivates a method and source-quality explanation. | Lesson: Use range visuals to make inconsistency visible before explaining causes. |
| Key data sources | Source types and availability are weak. | Evidence: Figure 3 reports 31% peer-reviewed sources, 38% reports, 11% broken links and 10% not specified. | Turns concern into measured diagnosis. | It answers why readers should distrust simple estimate reuse. | Lesson: Quantify provenance weakness with auditable categories. |
| Methodological classifications | Bottom-up, top-down and extrapolation approaches have different assumptions and failure modes. | Evidence: Table 2 compares inputs, assumptions, limitations and examples. | Builds the taxonomy for interpreting estimates. | Method differences explain range and projection risk. | Lesson: Give readers a method taxonomy they can apply outside the paper. |
| Questioning assumptions and comparison limits | Extrapolation can carry old assumptions through citation chains. | Evidence: Figure 6 tracks Corcoran and Andrae, Andrae and Edler, and The Shift Project. | Shows mechanism of error propagation. | It follows the taxonomy with a concrete citation-flow case. | Lesson: Trace assumptions across papers when later work reuses a baseline. |
| Data quality and technological change | Private data, link rot, hyperscale change, cryptocurrency and efficiency shifts make old estimates fragile. | Evidence: Figure 7, IDC 43%, Cisco 30%, hyperscale share above 40% of 2020 server installed base, Bitcoin energy ranges on 15 July 2022. | Explains why data-center estimates decay quickly. | It moves from literature coding to technology dynamics. | Lesson: Add updateability and technology-change tests to energy-demand models. |
| Recommendations and conclusions | Three stakeholder groups need different reliability rules. | Evidence: Figure 8 gives end-user questions; Figure 9 gives a researcher workflow; policy section discusses disclosure. | Converts review into action. | It closes with user-specific implementation. | Lesson: End a review by assigning actions to user groups. |

## 10. Figures & tables argument function

| Item | Shows | Proves | Role | Why in main text | Design lesson |
|---|---|---|---|---|---|
| Fig. 1 | Evidence: Inclusion flow for original, regional or global, sourced, use-stage energy estimates. | Evidence: The review corpus is filtered by method transparency and scope. | Protocol figure. | It makes eligibility rules inspectable. | Lesson: Use a flowchart when review inclusion depends on multiple exclusion gates. |
| Fig. 2 | Evidence: Global data-center energy estimate ranges for 2010, 2020 and 2030 in TWh. | Evidence: Estimates vary by orders of magnitude for future years. | Problem visualization. | It lets readers see why one headline number is unsafe. | Lesson: Put the uncertainty spread early. |
| Fig. 3 | Evidence: Source-type and missing-source breakdown for grouped key sources. | Evidence: Many sources are reports, private, broken or not specified. | Main evidence audit. | It turns source quality into a visual result. | Lesson: Color missing or weak sources distinctly. |
| Fig. 4 | Evidence: Estimate ranges grouped by methodological classification. | Evidence: Method family helps explain estimate spread. | Taxonomy-result bridge. | It links method classification to numerical dispersion. | Lesson: Group estimates by method before comparing values. |
| Fig. 5 | Evidence: Global estimates from 2010 to 2030 with and without method grouping. | Evidence: Future projections widen, especially under extrapolation. | Projection-risk figure. | It supports the warning against long-range extrapolation. | Lesson: Show how uncertainty changes over the forecast horizon. |
| Fig. 6 | Evidence: Citation flow from Corcoran and Andrae to Andrae and Edler to The Shift Project, with missing sources. | Evidence: A weak assumption can travel through later publications. | Mechanism figure. | It explains how unreliable estimates gain influence. | Lesson: Use a citation-flow figure when the mechanism is inherited opacity. |
| Fig. 7 | Evidence: Citation flow among Malmodin and Lunden, Shehabi et al. and Van Heddeghem et al. with IDC dependencies. | Evidence: Seemingly independent estimates can share hidden private data roots. | Dependency figure. | It shows correlation among evidence sources. | Lesson: Audit shared inputs before treating estimates as independent. |
| Fig. 8 | Evidence: Three end-user questions on source age, estimate basis and source/calculation availability. | Evidence: The review can be converted into a checklist. | Translation figure. | It serves journalists and non-expert users. | Lesson: Make one figure a reader-facing decision tool. |
| Fig. 9 | Evidence: Recommended methodology flow from system boundary through source validation and rerun. | Evidence: The authors offer a corrective research workflow. | Method playbook figure. | It makes the paper useful beyond diagnosis. | Lesson: Turn recommendations into a process diagram. |
| Table 1 | Evidence: Availability classifications: existing link, not found, broken link, not specified and private/commercial. | Evidence: Source availability is coded consistently. | Coding schema. | It legitimizes the source-quality percentages. | Lesson: Define audit labels in the main text, not only the SI. |
| Table 2 | Evidence: Bottom-up, top-down and extrapolation inputs, assumptions, limitations and examples. | Evidence: Method families differ in data needs and future-projection risk. | Method taxonomy. | It teaches readers how to classify estimates. | Lesson: Use tables for method comparison when the paper is a review. |

## 11. Discussion & Conclusion

Evidence: The Discussion-style sections do not merely repeat the source-audit results. They elevate them into three stakeholder-specific recommendation sets: end users should ask about source age, estimate basis and source availability; researchers should define boundaries, parameterize models, publish code and assess source reliability; regulators should consider disclosure requirements for equipment lifecycle, energy use and grid mix.

Evidence: The Conclusion states that data-center energy demand has become a mainstream environmental issue, but many calculations cannot be reliably reproduced and extrapolation-based claims should be used cautiously. Inference: high confidence. The conclusion works because it changes the user's default action from "pick the newest TWh number" to "inspect provenance, method and boundary before reuse." Lesson: In Henry's conclusions, end with a changed decision rule for the reader.

## 12. Argument chain (compressed)

```text
Big problem
  -> Data centers matter for digital services, grid planning and emissions accounting
  -> Published energy estimates vary widely and shape public and policy decisions
  -> Existing debate focuses too much on headline values
  -> Review question: can the sources and inputs behind estimates be trusted and reused?
  -> Method: select original regional/global use-stage electricity estimates since 2007
  -> Data: extract 258 estimates from 46 publications and code 676 source traces
  -> Core result 1: many sources are reports, private data, broken links or vague citations
  -> Core result 2: bottom-up, top-down and extrapolation methods have incompatible assumptions
  -> Mechanism: weak assumptions and hidden data roots propagate through citation chains
  -> Robustness posture: publish tables and Figshare code for the review's own calculations
  -> Broader implication: users and regulators need provenance rules before using data-center energy estimates
```

**Weakest link**: Evidence: The review analyzes first-level sources and does not trace every citation chain to the original data source. Inference: high confidence, deeper backward tracing could reveal more hidden dependencies but would require much larger source retrieval work.

**Strongest link**: Evidence: The paper combines estimate extraction, source availability coding, method classification and citation-flow figures. Inference: high confidence, this makes the reliability critique hard to dismiss as a general complaint.

## 13. Writing strategy extracted

Evidence: The title names the object, "sources of data center energy estimates," rather than leading with a broad digital-sustainability claim. Evidence: The Summary gives the corpus size and main percentages before the recommendations. Inference: high confidence, the writing strategy is to sell the review as an audit of evidence infrastructure.

Lesson: For Henry's review or TEA-method papers, lead with the decision object and the audit unit. Use sentences like: "We analyze X estimates and Y sources to assess whether Z policy conclusion is reusable." Avoid leading with generic decarbonization language.

Evidence: The paper uses concrete examples of West London, Ireland and Denmark before the methods. Inference: high confidence, those examples keep the review grounded in grid planning. Lesson: Use two or three policy cases to show why a literature-method problem affects physical infrastructure.

## 14. Research-design strategy extracted

Evidence: The review's design has four separable layers: inclusion rules, estimate extraction, source-provenance coding and stakeholder recommendations. Inference: high confidence, this layered design prevents the paper from becoming a narrative review with unsupported advice.

Lesson: For Henry's work, build reviews as reusable datasets. Minimum table columns should include system boundary, geography, year, method family, input source, source availability, code/data access and whether the estimate is historical or projected.

Evidence: The authors publish calculation and visualization code on Figshare. Inference: high confidence, this is aligned with their own transparency argument. Lesson: If a paper criticizes weak reproducibility, the paper's own extraction table and plotting code must be deposited.

## 15. Critical analysis

Evidence: The review is limited to English-language publications and records non-English sources only when cited by included English sources. Inference: medium confidence, this may understate regional data-center energy-estimate practices in China, Germany or other non-English policy contexts. Lesson: Do not copy this language boundary blindly for a global review unless the exclusion is justified and sensitivity checked.

Evidence: The authors only analyze the first level of sources cited by included papers. Inference: high confidence, source-chain opacity may be deeper than reported because a first-level accessible paper can still depend on unavailable market data further downstream. Lesson: If Henry studies source inheritance, add a second-level tracing sample for the most-cited estimates.

Evidence: The paper states that it does not aim to identify which estimate is more accurate. Inference: high confidence, this protects the review from overclaiming but leaves practitioners without a ranked current estimate. Lesson: Pair a provenance audit with a "use with confidence" tier only when the data support it.

Evidence: The code repository is on Figshare, but the Zotero item lacks attached supplementary and source-data files. Inference: medium confidence, the lab has enough for L0+L1 analysis but would need a later L2/L3 pass to inspect the supplemental tables and code. Lesson: For a method-transfer pass, inspect the Figshare package before reusing the coding schema.

## 16. Transfer to my own work

Evidence: The paper is high relevance to Henry's scope because data-center load growth affects renewable integration, hourly grid emissions, energy-system planning and future demand scenarios. Inference: high confidence, its strongest transfer is not the data-center estimate itself, but the reliability rules for any input series used in TEA or optimization.

Lesson: For a green-hydrogen TEA, audit electricity-price, electrolyzer-cost, capacity-factor and grid-emission inputs the same way this paper audits data-center estimates: source type, year, availability, boundary and method. Lesson: For energy-system optimization, classify demand forecasts as bottom-up, top-down or extrapolation before mixing them in scenarios. Lesson: For building-energy or data-center decarbonization, keep load-growth estimates and energy-intensity assumptions separate so efficiency claims do not hide activity growth.

## 17. KB outputs (mandatory)

### 5 Permanent Notes (atomic, evergreen, with `Evidence:` from this paper)

1. Data-center energy estimates should not be compared unless their system boundaries and source provenance are visible. Evidence: The paper shows incompatible inclusion choices such as internal networks, Bitcoin mining and component categories across estimates. Lesson: Build a boundary table before comparing TWh values.
2. Extrapolation is a fragile method for long-range data-center demand forecasts because it imports baseline errors and assumes stable demand-energy relationships. Evidence: Figure 5 shows wider future ranges and Figure 6 traces inherited assumptions through later publications. Lesson: Treat extrapolated 2030 or 2040 load estimates as scenario stress tests, not as forecasts.
3. Private market data can make multiple estimates look independent while sharing the same hidden root. Evidence: IDC appears in 43% of publications and Figure 7 shows IDC dependencies across cited papers. Lesson: Check common source roots before using several estimates as an uncertainty range.
4. Link rot and vague citation detail directly weaken energy-estimate reproducibility. Evidence: The review reports 11% broken links and 10% sources with insufficient detail to locate. Lesson: Archive web sources and record document IDs, dates and versions.
5. A review can produce policy value by assigning different rules to different users. Evidence: The paper gives separate recommendations for end users, researchers and policy makers/regulators. Lesson: End review papers with stakeholder-specific checklists.

### 5 Writing Lessons

1. Lesson: Start a review with a visible decision failure, such as grid delays or public misinformation, before presenting the coding protocol.
2. Lesson: Put the corpus size in the Summary so readers know the evidence base: publications, estimates and source traces.
3. Lesson: Use method-family labels as the organizing language throughout the paper, not just in one table.
4. Lesson: Use citation-flow figures when the core mechanism is inherited assumptions or shared hidden data.
5. Lesson: Make recommendations operational by phrasing them as questions, workflow steps or disclosure requirements.

### 5 Research-Design Lessons

1. Lesson: Extract estimate year, geography, scenario and units before judging reliability, because mismatched values can appear contradictory when they are not.
2. Lesson: Code source availability as a variable, not as a footnote, so link rot and private data become analyzable outcomes.
3. Lesson: Separate historical estimates from projections because measured data, short-term projections and long-term extrapolations carry different risks.
4. Lesson: Treat source age as part of model validity in fast-changing technology systems.
5. Lesson: Deposit the review's extraction tables and plotting code when the paper argues for transparency.

### 5 Future Research Questions

1. How would the reliability ranking change if every high-citation estimate were traced beyond first-level sources to original data roots?
2. Which national statistical agencies now publish metered data-center electricity consumption, and how do those data compare with bottom-up estimates?
3. How should AI training and inference loads be classified inside data-center energy boundaries after 2022?
4. Can data-center demand scenarios be integrated into power-system models with uncertainty classes for source provenance and method family?
5. What minimum disclosure standard should regulators require from hyperscale operators for grid planning, hourly emissions and load forecasting?

## 18. Final summary

**Top 3 lessons**:
1. Evidence: Estimate spread is not only a numerical uncertainty problem; it is a source-provenance and boundary problem.
2. Evidence: Extrapolation-based estimates become weak when old correlations between data traffic, compute activity and electricity are carried forward without retesting.
3. Evidence: Review papers can be action-oriented when they translate the audit into checklists for users, workflows for researchers and disclosure rules for regulators.

**Top 3 to transfer**:
1. Lesson: Add a source-provenance audit table to Henry's data-center, hydrogen-load or building-energy reviews.
2. Lesson: Classify each forecast input by method family before using it in TEA or optimization scenarios.
3. Lesson: Make figure architecture move from range, to source quality, to mechanism, to action workflow.

**Top 3 to NOT blindly copy**:
1. Evidence: The review uses English-language inclusion only. Lesson: Do not copy this boundary for regional or China-facing work without a language sensitivity note.
2. Evidence: The review stops at first-level source tracing. Lesson: Do not claim full source genealogy unless deeper citation-chain tracing is performed.
3. Evidence: The review avoids selecting the most accurate estimate. Lesson: Do not leave practitioners without a usable estimate tier if the goal is operational planning.

**One-line takeaway**: The most transferable research skill is to turn a messy estimate literature into a provenance-coded decision framework before using its numbers in policy, TEA or optimization.

---

## Pass-2 follow-up (deferred)

Deferred. Re-examine after more data-center and demand-side papers are ingested to mine subtler lessons about source-age thresholds, method-family naming, stakeholder-specific recommendation figures and how Joule review papers convert reproducibility critique into policy action.

## Cross-references

- Zotero parent key: `52W57HP5`
- Main PDF attachment key: `Q6LYUHSZ`
- Raw stubs: [[.raw/papers/52W57HP5/metadata.json|metadata]], [[.raw/papers/52W57HP5/zotero-attachments|zotero-attachments]], [[.raw/papers/52W57HP5/data-availability|data-availability]], [[.raw/papers/52W57HP5/code-availability|code-availability]], [[.raw/papers/52W57HP5/repository-links|repository-links]], [[.raw/papers/52W57HP5/article-page|article-page]], [[.raw/papers/52W57HP5/asset-status|asset-status]]
- Related papers in this lab: [[2020-J-data-center-load-migration-curtailment|Zheng et al. 2020, Joule]] shares data-center energy and grid-planning relevance; [[2025-J-space-based-solar-europe|Che et al. 2025, Joule]] shares Joule and system-cost estimate interpretation; [[2021-NE-kikstra-covid-energy-demand-scenarios|Kikstra et al. 2021, Nature Energy]] shares demand-scenario reliability; [[2022-NCC-residential-decarbonization-us|Wilson et al. 2022, Nature Climate Change]] shares demand-side decarbonization and grid-planning context.
- Pattern pages it will inform after paper 10: [[patterns/methods/source-provenance-audits]], [[patterns/figures/citation-flow-mechanisms]], [[patterns/data-center/load-forecast-reliability]], [[patterns/reviews/stakeholder-recommendation-architecture]]
- Playbook pages it will inform after paper 20: [[playbook/review-paper-source-audit-template]], [[playbook/forecast-input-reliability-checklist]], [[playbook/data-center-demand-scenario-rules]]
