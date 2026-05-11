---
zotero_key: KRT75D4W
title: "Probabilistic feasibility space of scaling up green hydrogen supply"
journal: "Nature Energy"
year: 2022
doi: "10.1038/s41560-022-01097-4"
topic: [green-hydrogen, electrolysis-scale-up, technology-diffusion, policy-targets, europe, global-energy-transition]
paper_type: [modeling, scenario-analysis, policy-analysis]
main_contribution: [method-novelty, policy-relevance, counterintuitive-result]
method_type: [adapted-logistic-diffusion, Monte-Carlo-uncertainty, historical-analogue-benchmarking, demand-pull-scenario]
data_assets:
  main_pdf: true
  supplementary: false
  source_data: true
  data_statement: true
  code_statement: true
  code_repository: true
relevance_to_my_research: high
ingest_status: reviewed
address: c-000018
created: 2026-05-11
tags:
  - paper-analysis
---

# Probabilistic feasibility space of scaling up green hydrogen supply

> Zotero: `KRT75D4W` | DOI: 10.1038/s41560-022-01097-4 | Journal: Nature Energy (2022)

## 1. One-sentence contribution

Evidence: Odenweller et al. combine an adapted logistic technology-diffusion model with Monte Carlo uncertainty propagation, IEA electrolyser project data, wind and solar growth analogues, and emergency-deployment analogues to estimate when green hydrogen supply can plausibly reach material final-energy shares in the European Union and globally.

## 2. Archetype classification

Evidence: This is a modeling and scenario-analysis paper: the Methods state that the authors use a stochastic adaptation of a logistic diffusion model, sample initial capacity and annual growth rate, and impose a policy-backed demand pull for the European Union and global cases. Inference: confidence high. The archetype is "feasibility-space modeling for policy realism." It does not optimize a hydrogen system, compute a project-level LCOH, or propose an electrolyser technology. It tests whether public hydrogen targets are compatible with observed growth speeds of earlier technologies. Lesson: When Henry evaluates green-hydrogen pathways, add a deployment-feasibility axis beside cost, emissions, and resource quality.

## 3. Real value sources

| Dimension | Top driver? | Evidence | Inference | Lesson |
|---|---|---|---|---|
| Problem importance | Yes | Evidence: The Introduction states that global electrolysis capacity was about 600 MW in 2021 and must grow 6,000 to 8,000-fold from 2021 to 2050 for Paris-compatible climate-neutrality scenarios. | Inference: confidence high. The paper turns green hydrogen from a cost debate into a supply-scale timing problem. | Lesson: In Henry's hydrogen work, quantify the scale-up multiple before discussing cost optimism. |
| Problem novelty | Yes | Evidence: The Introduction states that no prior study had analyzed possible expansion pathways of green hydrogen from electrolysis, a technology in its infancy. | Inference: confidence high. The gap is not "hydrogen is understudied"; it is "supply ramp-up feasibility is missing despite heavy demand-side debate." | Lesson: Frame gaps around a missing feasibility axis, not around a broad topic shortage. |
| Method novelty | Yes | Evidence: The paper replaces a fixed logistic asymptote with a time-dependent demand pull and propagates uncertain initial capacity and growth rates through 10,000 Monte Carlo samples. | Inference: confidence high. The method value comes from matching an emerging hydrogen market where demand, infrastructure, and supply co-develop. | Lesson: Modify standard diffusion models only where the system boundary requires it, then explain the modified term in one conceptual figure. |
| Data novelty | Medium | Evidence: The data combine the IEA Hydrogen Projects Database, market research on 49 large 2022 to 2023 projects, BP wind and solar capacity data, and a curated set of emergency-deployment analogues. | Inference: confidence medium. The individual datasets are not rare, but the analogue pairing creates the comparison value. | Lesson: A data contribution can come from disciplined pairing of public datasets to answer one feasibility question. |
| System boundary | Yes | Evidence: The model includes electrolysis capacity, policy and market demand pull, investor anticipation, European Union targets, global targets, and final-energy-share translation. | Inference: confidence high. The boundary is broader than electrolyser manufacturing but narrower than full hydrogen supply chains. | Lesson: State what the model includes and what it leaves outside before readers infer too much from capacity numbers. |
| Case-study design | Yes | Evidence: The main cases are the European Union and global scale, with European Union demand pull tied to 6 GW in 2024, 100 GW in 2030, and 500 GW in 2050, and global demand pull tied to 254 GW in 2030 and 3,600 GW in 2050. | Inference: confidence high. The European Union case gives policy specificity and the global case tests scale. | Lesson: Pair a policy-rich region with a global case when a result needs both institutional and planetary relevance. |
| Result impact | Yes | Evidence: The abstract reports that green hydrogen likely, with probability at least 75%, supplies less than 1% of final energy until 2030 in the European Union and 2035 globally under wind and solar-like growth. | Inference: confidence high. The result punctures target-driven optimism without rejecting green hydrogen. | Lesson: Make the headline a probability plus threshold plus date, not a vague feasibility claim. |
| Mechanism explanation | Yes | Evidence: The Discussion explains that exponential expansion has a flat beginning, so high growth rates still take time to become material market shares. | Inference: confidence high. The mechanism is timing physics of S-curves, not just low starting capacity. | Lesson: Explain why a result happens in a simple growth-mechanism sentence that a policy reader can reuse. |
| Comprehensiveness | No | Evidence: The limitations exclude other green-hydrogen bottlenecks, hydrogen trade, competitiveness-driven demand-pull feedbacks, and grey or blue hydrogen. | Inference: confidence high. The paper succeeds by narrowing the feasibility question rather than spanning the full hydrogen economy. | Lesson: Do not claim full-system coverage when the power of the paper comes from isolating one bottleneck. |
| Policy / industry implication | Yes | Evidence: The Discussion argues that policymakers must accelerate the full green-hydrogen supply chain while safeguarding against limited availability through electrification and efficiency alternatives. | Inference: confidence high. The paper gives a two-handed policy message: accelerate and hedge. | Lesson: For risky transition technologies, end with a portfolio rule, not a single-policy endorsement. |
| Writing / narrative | Yes | Evidence: The Introduction moves from hydrogen's role, to supply scarcity, to electrolysis scale-up, to a stated method and contrast between conventional and emergency growth. | Inference: confidence high. The narrative keeps demand-side enthusiasm visible while changing the evaluative lens to supply feasibility. | Lesson: Let the opening acknowledge why a technology is attractive, then ask whether the required physical expansion can occur in time. |
| Figure / table craft | Yes | Evidence: Fig. 1 shows project announcements, Fig. 2 defines the three uncertainty parameters, Fig. 3 parameterizes distributions, Fig. 4 and Fig. 5 show feasibility spaces, and Fig. 6 compares breakthrough-year and capacity distributions. | Inference: confidence high. The figure order teaches the model before asking readers to trust the probability surface. | Lesson: Sequence figures as data input, model logic, parameter distributions, result space, then decision comparison. |

**Top 3 value drivers**:
1. Evidence: The paper converts green-hydrogen optimism into a probabilistic deployment-feasibility question.
2. Evidence: The adapted logistic model adds a time-varying demand pull, matching hydrogen's co-development problem across supply, demand, and infrastructure.
3. Evidence: The wind and solar analogue versus emergency-deployment analogue contrast turns policy urgency into a modeled growth-rate range.

**What it does NOT win on**:

Evidence: It does not estimate project LCOH, optimize renewable siting, model hourly power-system operation, or include hydrogen trade. Inference: confidence high. Its value comes from a high-level growth-feasibility lens with enough structure to challenge policy targets.

**Most likely reason it cleared the top-tier bar**:

Inference: confidence high. It cleared the Nature Energy bar because it made a popular policy technology look quantitatively scarce in the near term, tied the result to observed growth analogues, and gave policymakers a practical hedge: accelerate green hydrogen where needed while protecting against overreliance.

## 4. Research question & framing

Evidence: The paper asks whether electrolysis capacity can scale fast enough to make green hydrogen available at material levels in the European Union and globally, under growth rates comparable to wind and solar and under faster emergency-like growth. Evidence: It frames the answer as a probabilistic feasibility space, not as a deterministic forecast. Inference: confidence high. The framing is stronger than a normal scenario study because it makes uncertainty the object of the paper rather than a sensitivity appendix. Lesson: For Henry's wind-solar-hydrogen work, phrase the research question as "what deployment space remains feasible under empirically grounded growth analogues?"

## 5. Introduction structure (paragraph table)

| Para | Function | Core info | Writing move | Why it works | Lesson |
|---|---|---|---|---|---|
| P1 | Stakes and technology role | Evidence: Green hydrogen and e-fuels can reduce emissions where direct electrification is infeasible and avoid biofuel sustainability concerns. | Evidence: Starts from the policy reason for caring about hydrogen, including energy crisis and net-zero scenarios. | Inference: confidence high. It invites hydrogen supporters into the paper before challenging them. | Lesson: Begin with the strongest case for the technology you later constrain. |
| P2 | Gap paragraph | Evidence: Debate has focused on demand applications, while supply availability is equally critical, and no study had analyzed electrolysis expansion pathways. | Evidence: Narrows from hydrogen demand to the missing supply-ramp question. | Inference: confidence high. This is the gap paragraph because it names the missing analysis directly. | Lesson: State the missing axis as "supply availability," not as a generic modeling gap. |
| P3 | Scale shock | Evidence: Electrolysis capacity was about 600 MW globally in 2021 and needs to grow 6,000 to 8,000-fold by 2050; 80% of added capacity announced by 2023 lacked FID. | Evidence: Uses one starting stock, one growth multiple, and one project-risk statistic. | Inference: confidence high. This paragraph makes the feasibility problem concrete enough to justify a growth model. | Lesson: Use three numbers to turn a broad transition problem into a modelable bottleneck. |
| P4 | Contribution preview | Evidence: The authors combine an S-shaped logistic diffusion model with probabilistic parameterization from wind and solar growth, then contrast with unconventional growth rates. | Evidence: Gives method, source of parameters, main result class, and policy contrast in one paragraph. | Inference: confidence high. The contribution preview makes the paper's logic visible before the Results. | Lesson: End the Introduction with method plus answer type, not only with a list of tasks. |

**Transferable Intro template extracted from this paper**:

Evidence: The Introduction follows this sequence: technology promise, overlooked feasibility axis, numeric scale shock, method and result preview. Lesson: For Henry's green-hydrogen TEA or optimization papers, use this template when the paper needs to challenge a policy target while remaining constructive.

## 6. Lit-gap & contribution construction

Evidence: The paper constructs the literature gap by separating hydrogen-demand research from hydrogen-supply availability, then links supply availability to technology-diffusion literature on growth patterns and pace. Evidence: It cites prior feasibility analyses for renewables and fossil phase-out, then states that electrolysis expansion pathways had not been analyzed. Inference: confidence high. This is a bridge gap: it imports a mature method family from technology diffusion into a hydrogen supply question. Lesson: When Henry sees a saturated topic, search for a mature method from an adjacent literature that has not been applied to the exact bottleneck.

Evidence: The contribution is also positioned between two modeling approaches in long-term projections. One fits growth models with the asymptote as a free parameter, while the other imposes an ex ante target. Inference: confidence high. The authors use this debate to justify the adapted demand-pull logistic model as a middle path. Lesson: A strong method section can start by reconciling two existing modeling logics before introducing the new equation.

## 7. Method / model / design (adapt to archetype)

Evidence: The method uses a stochastic adaptation of the logistic diffusion model for electrolysis capacity in the European Union and globally. It samples two uncertain parameters: initial electrolysis capacity in 2023 and annual emergence growth rate. Evidence: The initial capacity distribution uses IEA Hydrogen Projects Database projects plus market research, a lower truncation from operational and under-construction projects, and a post-truncation mean equivalent to realizing 30% of feasibility-study projects. Evidence: The conventional growth case fits seven-year exponential growth rates for wind and solar power from 1995 to 2010. Evidence: The emergency-deployment case fits logistic curves to 11 historical technologies, excluding COVID vaccinations as an outlier.

Evidence: The model replaces the fixed logistic asymptote with a time-dependent demand pull, parameterized by policy targets, announcements, and climate-neutrality scenarios. The European Union demand pull uses 6 GW in 2024, 100 GW in 2030, and 500 GW in 2050; the global demand pull uses 254 GW in 2030 and 3,600 GW in 2050. Evidence: Demand-pull anticipation is set to five years by default and tested at zero years, ten years, and full anticipation. Inference: confidence high. The core design is not a detailed hydrogen-sector model. It is a probability engine for asking whether capacity can catch a moving demand target. Lesson: When modeling immature technologies, separate growth-speed uncertainty from market-size uncertainty and propagate both.

N/A for this archetype: experimental controls are not relevant because the paper is a modeling and scenario-analysis study. Evidence: Robustness instead comes from growth analogue choices, Gompertz comparison, demand-pull anticipation sensitivity, and project-announcement validation.

## 8. Data & case-study design

Evidence: The case design covers the European Union and the global system. The European Union case is policy-rich because REPowerEU and the EU Hydrogen Strategy define near-term and long-term demand-pull points. The global case tests whether a technology with tiny starting capacity can plausibly serve climate-neutrality pathways at planetary scale. Inference: confidence high. The region pair is not arbitrary; one side gives policy specificity, the other gives scale stress.

Evidence: Data sources include IEA Hydrogen Projects Database electrolysis projects, own market research for 49 projects of at least 50 MW starting in 2022 or 2023, BP wind and solar capacity data, INNOPATHS European final-energy scenarios, IEA NZE global final-energy data, IPCC scenario explorer data, and historical analogues for emergency deployment. Lesson: For Henry's own H2 papers, use a data table that groups evidence by model role: initial condition, growth analogue, demand pull, validation, and final-energy translation.

## 9. Results architecture

| Section | Main message | Evidence used | Role in argument | Why this order | Lesson |
|---|---|---|---|---|---|
| Three uncertain parameters | Evidence: Initial capacity, emergence growth rate, and demand pull define the feasibility space. | Evidence: Fig. 1 project announcements, Fig. 2 conceptual model, Fig. 3 distributions, Table 1 parameters. | Inference: confidence high. This section teaches the variables before any result claim. | Inference: confidence high. Readers need to see why uncertainty is structural, not optional. | Lesson: Define the uncertainty architecture before showing probability outputs. |
| Reconciling projection approaches | Evidence: Free-asymptote models risk bias from recent slowdowns; ex ante target models assume an existing market. | Evidence: Literature contrast plus adapted logistic model explanation. | Inference: confidence high. It defends the model choice against both modeling camps. | Inference: confidence high. The defense appears before the main feasibility result to reduce method pushback. | Lesson: Place method positioning before the headline figure when the model form itself carries the contribution. |
| Conventional growth results | Evidence: Under wind and solar-like growth, EU 2024 and 2030 targets and the global 2030 target are outside or far beyond modeled distributions. | Evidence: Fig. 4, Extended Data Figs. 4 and 5, and Fig. 6 capacity distributions. | Inference: confidence high. This is the main scarcity and uncertainty result. | Inference: confidence high. It tests the default optimistic analogue first. | Lesson: Start with the benchmark the audience already trusts before introducing extreme cases. |
| Emergency deployment results | Evidence: Unconventional growth rates have a mean of 126% per year and can raise the EU 2030 target probability to 49%, compared with 0.2% under conventional growth. | Evidence: Fig. 5 and Fig. 6. | Inference: confidence high. This transforms the paper from pessimism into conditional policy design. | Inference: confidence high. The second result answers "what would it take?" | Lesson: After a sobering result, include a conditional escape route with explicit policy requirements. |
| Discussion | Evidence: Policymakers face a twofold problem: accelerate the supply chain and hedge against limited availability. | Evidence: Discussion and limitations. | Inference: confidence high. The policy result is risk management under asymmetric downside. | Inference: confidence high. It generalizes the result without claiming the model covers all hydrogen constraints. | Lesson: Close with a risk-management rule tied to the uncertainty structure. |

## 10. Figures & tables argument function

| Item | Shows | Proves | Role | Why in main text | Design lesson |
|---|---|---|---|---|---|
| Fig. 1 | Evidence: Historical electrolysis projects and future announcements by region, country, and project status. | Evidence: Many announced projects are not backed by FID, including 80% of added capacity announced to come online by 2023. | Inference: confidence high. It justifies uncertainty in the 2023 starting point. | Inference: confidence high. The model needs a visual data basis before distributions. | Lesson: Use the first figure to convert a messy project pipeline into a model input. |
| Fig. 2 | Evidence: Initial capacity, emergence growth rate, demand-pull magnitude, and demand-pull anticipation. | Evidence: The probability space follows from uncertain parameters propagated through Monte Carlo simulation. | Inference: confidence high. It is the conceptual spine of the model. | Inference: confidence high. Readers need the mechanism before seeing density maps. | Lesson: Draw the modified model logic, not only the equations. |
| Fig. 3 | Evidence: Truncated normal distributions for 2023 initial capacity and conventional emergence growth rates. | Evidence: Wind and solar 1995 to 2010 growth rates provide the conventional analogue distribution. | Inference: confidence high. It makes the parameterization auditable. | Inference: confidence high. Without this figure, Fig. 4 would look like a black-box forecast. | Lesson: Show probability inputs as figures when the output is probabilistic. |
| Fig. 4 | Evidence: Probabilistic feasibility space under wind and solar-like growth for the European Union and globally. | Evidence: Short-term targets are out of reach and long-term capacity remains uncertain under conventional growth. | Inference: confidence high. This is the central result figure. | Inference: confidence high. It combines model output, targets, example paths, and density. | Lesson: Put the headline feasibility result into a single figure with both trajectory and uncertainty density. |
| Fig. 5 | Evidence: Emergency-deployment analogues and resulting feasibility spaces. | Evidence: Unconventional growth can accelerate breakthrough and reduce long-term uncertainty. | Inference: confidence high. It introduces the policy-effort counterfactual. | Inference: confidence high. It answers whether the default scarcity result is destiny or policy-contingent. | Lesson: When a result is sobering, include a second figure that quantifies the conditions for improvement. |
| Fig. 6 | Evidence: Breakthrough-year and electrolysis-capacity distributions in 2030 and 2040 for both growth cases. | Evidence: Conventional growth likely gives less than 1% EU final energy by 2030, while emergency growth expands the distribution. | Inference: confidence high. It translates capacity paths into decision-facing timing and final-energy shares. | Inference: confidence high. The main text needs a compact comparison figure after the two scenario families. | Lesson: End the figure sequence with a direct comparison of policy-relevant metrics. |
| Table 1 | Evidence: Parameter values for initial capacity, emergence growth rate, demand-pull magnitude, and demand-pull anticipation. | Evidence: It gives EU and global minima, means, IQRs, targets, and assumptions. | Inference: confidence high. It is the model audit table. | Inference: confidence high. Nature Energy readers need a compact map of assumptions. | Lesson: Put all scenario inputs into one table before readers search the Methods. |

Extended Data figures:

| Item | Function | Lesson |
|---|---|---|
| Extended Data Fig. 1 | Evidence: Historical wind and solar capacities and seven-year growth rates. | Lesson: Put analogue derivation in Extended Data when the main figure only needs the fitted distribution. |
| Extended Data Fig. 2 | Evidence: Growth-rate distributions under varying interval lengths. | Lesson: Test whether a chosen time slice drives the result. |
| Extended Data Fig. 3 | Evidence: Adapted logistic versus Gompertz comparison. | Lesson: Use an alternative growth model to show which conclusions depend on model form. |
| Extended Data Fig. 4 | Evidence: Demand-pull anticipation sensitivity for conventional growth. | Lesson: Stress-test policy foresight assumptions. |
| Extended Data Fig. 5 | Evidence: Project announcements exceed the median conventional-growth path. | Lesson: Validate against announced pipeline while treating announcements as uncertain. |
| Extended Data Fig. 6 | Evidence: Demand-pull anticipation sensitivity for emergency growth. | Lesson: Check whether the escape route depends on full investor foresight. |
| Extended Data Fig. 7 | Evidence: Five-year capacity and final-energy-share distributions from 2025 to 2050. | Lesson: Provide time-slice diagnostics for readers who care about policy milestones. |
| Extended Data Fig. 8 | Evidence: Comparison with IAM scenarios, IEA, IRENA, Hydrogen Europe, and Hydrogen Council. | Lesson: Compare the paper's feasibility space with scenario-community expectations. |

## 11. Discussion & Conclusion

Evidence: The Discussion elevates the result from a capacity forecast to a coordination-risk argument. It says short-term scarcity creates a supply, demand, and infrastructure coordination problem, while long-term uncertainty can deter investors through a second-mover advantage. Evidence: The paper argues that relying on large-scale green-hydrogen availability is risky because disappointment can cause fossil lock-in, but accelerated supply-chain policy could turn uncertain supply, insufficient demand, and incomplete infrastructure into a positive feedback mechanism.

Inference: confidence high. The Discussion is effective because it does not simply repeat Fig. 4 and Fig. 5. It translates the probability space into asymmetric policy risk: overbuilding alternatives is reversible, but waiting for hydrogen and then discovering scarcity may be hard to fix. Lesson: For Henry's manuscripts, convert model uncertainty into a decision asymmetry, then recommend a hedge.

Evidence: Limitations are handled in the Methods rather than hidden: the paper excludes other green-hydrogen supply-chain bottlenecks, hydrogen trade, feedback from green-hydrogen competitiveness to demand pull, exogenous long-term demand-pull uncertainty, and fossil hydrogen pathways. Lesson: Place limitations near the model details when they change interpretation of the output.

## 12. Argument chain (compressed)

```text
Big problem: green hydrogen is needed for hard-to-electrify sectors.
  -> Specific gap: supply availability and electrolysis expansion pathways were not yet analyzed.
  -> Research question: can electrolysis scale fast enough under empirical growth analogues?
  -> Method / data: adapted logistic diffusion model, Monte Carlo uncertainty, IEA project data, wind and solar growth, emergency analogues, policy-backed demand pull.
  -> Core result 1: under wind and solar-like growth, green hydrogen remains below 1% of final energy until 2030 in the European Union and 2035 globally with probability at least 75%.
  -> Core result 2: breakthrough timing is uncertain, with conventional median breakthrough around 2040 in the European Union and 2045 globally.
  -> Mechanism: exponential growth begins flat, and hydrogen must ramp supply, demand, and infrastructure together.
  -> Robustness: Gompertz comparison and demand-pull anticipation sensitivities retain short-term scarcity and long-term uncertainty.
  -> Broader implication: policy must accelerate green hydrogen while hedging with direct electrification and efficiency.
```

**Weakest link**: Evidence: The demand pull is exogenous and assumes continuous policy support, future competitiveness, and long-term market volumes. Inference: confidence high. If demand fails to materialize or if hydrogen imports dominate the European Union case, capacity-share interpretation changes.

**Strongest link**: Evidence: The same scarcity conclusion appears under wind and solar-like growth, Gompertz comparison, and demand-pull anticipation sensitivity. Inference: confidence high. The near-term scarcity result is less fragile than the exact 2040 to 2050 capacity distribution.

## 13. Writing strategy extracted

Evidence: The paper's writing strategy is to support a contrarian result with a friendly premise. It begins by agreeing that green hydrogen is useful for sectors where electrification is infeasible, then argues that usefulness does not imply near-term availability. Lesson: When challenging a popular transition pathway, start by granting the strongest legitimate use case before narrowing to the feasibility bottleneck.

Evidence: The abstract uses the sequence "attractive replacement," "scaling is critical and challenging," "even if electrolysis grows as fast as wind and solar," then "scarce in the short term and uncertain in the long term." Inference: confidence high. This phrasing makes the paper feel like a risk audit rather than an anti-hydrogen argument. Lesson: Use concessive structure: "even if the favorable analogue holds, the bottleneck remains."

Evidence: The Results use named contrasts: conventional growth versus emergency deployment, short-term scarcity versus long-term uncertainty, supply versus demand pull. Lesson: Give readers binary conceptual handles, then fill them with numbers.

## 14. Research-design strategy extracted

Evidence: The research design uses historical analogues as empirical guardrails: wind and solar for fast energy-technology growth, and wartime, nuclear, rail, internet-host, smartphone, and e-bike examples for emergency-like growth. Inference: confidence high. The design avoids pure speculation by asking what has actually scaled quickly before. Lesson: For Henry's technology-feasibility work, build an analogue library and make each analogue's role explicit.

Evidence: The model separates initial capacity uncertainty from growth-rate uncertainty and demand-pull uncertainty. Inference: confidence high. This separation gives reviewers specific places to contest assumptions without rejecting the whole model. Lesson: Decompose uncertainty into named parameters so robustness checks map to reviewer concerns.

Evidence: The paper translates electrolysis capacity into final-energy shares using 60% overall efficiency, 5,000 full-load hours, and final-energy demand scenarios. Lesson: Translate technical capacity into system-share metrics when the audience cares about climate contribution, not only installed GW.

## 15. Critical analysis

Evidence: The authors state that the results are conditional probabilities contingent on assumed demand pull from policies and markets. Inference: confidence high. The word "probability" can mislead if readers treat it as an absolute real-world probability. Lesson: In Henry's probabilistic papers, repeat the conditioning statement near any policy-facing probability.

Evidence: The model focuses on electrolysis capacity and excludes other supply-chain bottlenecks such as direct air capture for e-fuels. Inference: confidence high. This means the paper may still be optimistic about usable e-fuel supply even if electrolysis capacity scales. Lesson: Do not infer delivered fuel availability from electrolyser capacity without adding downstream bottlenecks.

Evidence: The European Union final-energy-share calculation excludes imports from other world regions. Inference: confidence medium. For a trade-heavy hydrogen future, European domestic capacity may understate availability but still matters for security and policy autonomy. Lesson: For Henry's regional H2 studies, include at least one import sensitivity.

Evidence: The emergency-deployment analogues are heterogeneous and mostly non-energy technologies. Inference: confidence medium. They are useful as a policy ambition ceiling, but they do not prove that electrolyser supply chains can behave like smartphones or wartime aircraft. Lesson: Treat extreme analogues as "what policy intensity might require," not as a forecast.

## 16. Transfer to my own work

Evidence: The paper directly fits Henry's scope because it links green hydrogen, renewable energy integration, electrolysis scale-up, energy policy, uncertainty, and system-level feasibility. Lesson: Add a "deployment feasibility" module to any green-hydrogen TEA that currently reports only LCOH and emissions.

Evidence: The paper uses wind and solar historical growth rates as the reference case for electrolysis. Lesson: For wind-solar-hydrogen integrated systems, benchmark hydrogen buildout against local renewable buildout rates, not only against electrolyser cost decline.

Evidence: The paper's demand-pull concept combines policy targets, regulation, market opportunities, competitiveness, and investor anticipation. Lesson: When Henry models policy incentives, represent investor foresight as a scenario lever rather than assuming targets instantly become bankable demand.

Evidence: The Discussion warns that overreliance on hydrogen can delay direct electrification and energy efficiency. Lesson: In project recommendations, separate "hydrogen where electrification is infeasible" from "hydrogen as a general backstop."

## 17. KB outputs (mandatory)

### 5 Permanent Notes (atomic, evergreen, with `Evidence:` from this paper)

1. Green hydrogen can be policy-critical and still near-term scarce. Evidence: The abstract reports that under wind and solar-like growth, green hydrogen likely, with probability at least 75%, supplies less than 1% of final energy until 2030 in the European Union and 2035 globally. Lesson: In Henry's papers, never move from "needed" to "available" without a scale-up check.
2. A 600 MW starting stock makes even high growth look slow in final-energy terms. Evidence: The Introduction states global electrolysis capacity was about 600 MW in 2021 and must grow 6,000 to 8,000-fold by 2050 for Paris-compatible scenarios. Lesson: Report starting capacity and required growth multiple together.
3. Hydrogen has a three-sided scale-up problem. Evidence: The paper states that green-hydrogen supply, demand, and infrastructure must ramp up in parallel, unlike wind and solar power entering an existing electricity market. Lesson: Model supply, demand, and infrastructure as coupled constraints whenever possible.
4. Demand pull should be modeled as both magnitude and anticipation. Evidence: Fig. 2 distinguishes demand-pull magnitude from demand-pull anticipation, and the Methods test zero, five, ten, and full anticipation cases. Lesson: Turn investor foresight into an explicit scenario axis.
5. Extreme policy effort changes probabilities, not certainty. Evidence: Under emergency-like growth, achieving the EU 2030 target rises to 49% probability versus 0.2% under conventional growth, while the global 850 GW IEA NZE requirement remains unlikely at 18%. Lesson: Present emergency-policy pathways as probability shifts, not guaranteed rescue cases.

### 5 Writing Lessons

1. Evidence: The Introduction begins with hydrogen's strongest use case before testing scale-up feasibility. Lesson: Start a critical paper by granting the technology's best argument.
2. Evidence: The abstract uses "even if electrolysis capacity grows as fast as wind and solar power" before reporting scarcity. Lesson: Use an "even if" clause to make a skeptical result harder to dismiss.
3. Evidence: Fig. 2 explains the model variables before equations dominate the Methods. Lesson: Give readers a conceptual figure before mathematical detail.
4. Evidence: The paper names two result regimes, conventional growth and emergency deployment. Lesson: Use memorable scenario names that encode the causal contrast.
5. Evidence: The Discussion ends with acceleration plus safeguards against limited availability. Lesson: Close policy modeling papers with a paired action rule, not a single slogan.

### 5 Research-Design Lessons

1. Evidence: The model propagates uncertainty in initial capacity and emergence growth rate through 10,000 Monte Carlo samples. Lesson: Use stochastic propagation when the argument is about feasibility space, not point prediction.
2. Evidence: The conventional growth distribution uses the fastest wind and solar seven-year growth windows from 1995 to 2010. Lesson: Choose analogues that are generous enough to make negative results credible.
3. Evidence: The emergency case uses historical non-energy and energy examples that reached very high growth rates. Lesson: Add an upper-bound analogue family to distinguish "hard under normal policy" from "possible under mobilization."
4. Evidence: Extended Data Fig. 3 compares the adapted logistic model with a Gompertz model. Lesson: Test the core conclusion against an alternative curve form.
5. Evidence: Extended Data Fig. 5 compares modeled conventional percentiles with project announcements. Lesson: Validate model outputs against the announced pipeline, while treating announcements as uncertain evidence.

### 5 Future Research Questions

1. Inference: confidence high. How would domestic European scarcity estimates change when hydrogen imports and export-region renewable constraints are modeled endogenously?
2. Inference: confidence high. Which policy instruments create demand-pull anticipation strong enough to move projects from feasibility study to FID?
3. Inference: confidence medium. How do electrolyser manufacturing capacity, critical minerals, water constraints, and grid-connection queues alter the feasibility space beyond installed electrolysis capacity?
4. Inference: confidence medium. Can a wind-solar-hydrogen optimization model include a diffusion-rate constraint so that cost-optimal capacity additions remain historically plausible?
5. Inference: confidence medium. How should blue hydrogen be represented as a transition bridge without creating fossil lock-in that slows green-hydrogen scale-up?

## 18. Final summary

**Top 3 lessons**:
1. Evidence: The paper's main result is a probability-bounded scarcity claim, not a single forecast. Lesson: Use probability, threshold, geography, and date in one sentence for feasibility headlines.
2. Evidence: The method modifies logistic diffusion with increasing demand pull. Lesson: Adapt standard models to the market structure of the technology, then show the adaptation graphically.
3. Evidence: The Discussion recommends both acceleration and hedging. Lesson: Treat uncertain hydrogen availability as a risk-management problem.

**Top 3 to transfer**:
1. Evidence: Initial capacity and growth-rate uncertainty are modeled separately. Lesson: Use named uncertainty parameters in Henry's H2 scale-up studies.
2. Evidence: Wind and solar growth provide the conventional analogue. Lesson: Benchmark electrolyser buildout against historical renewable deployment speeds.
3. Evidence: Final-energy-share translation uses efficiency, full-load hours, and demand scenarios. Lesson: Convert GW of hydrogen assets into final-energy contribution.

**Top 3 to NOT blindly copy**:
1. Evidence: The European Union final-energy-share calculation excludes imports. Lesson: Do not use the domestic-only framing for a trade-focused study.
2. Evidence: The demand pull is exogenous and policy-contingent. Lesson: Do not treat policy targets as realized demand without a bankability mechanism.
3. Evidence: Emergency analogues are heterogeneous. Lesson: Do not claim electrolyser deployment can copy non-energy technologies without supply-chain evidence.

**One-line takeaway**: Evidence: Odenweller et al. show that green hydrogen's climate value depends on deployment timing as much as cost. Lesson: In hydrogen research, always audit whether the technology can arrive before the system locks into alternatives.

## Pass-2 follow-up (deferred)

Deferred prompt: `/wiki-query "Pass-2 follow-up on [[2022-NE-green-h2-probabilistic-feasibility]]: implicit lessons not yet captured for research-design thinking, writing strategy, result-curation logic, and figure-curation logic."`

## Cross-references

- Zotero parent key: `KRT75D4W`
- Main PDF attachment key: `C24TPL5Q`
- Paper package stubs: [[../../.raw/papers/KRT75D4W/metadata.json|metadata]], [[../../.raw/papers/KRT75D4W/zotero-attachments|zotero-attachments]], [[../../.raw/papers/KRT75D4W/data-availability|data-availability]], [[../../.raw/papers/KRT75D4W/code-availability|code-availability]], [[../../.raw/papers/KRT75D4W/repository-links|repository-links]], [[../../.raw/papers/KRT75D4W/article-page|article-page]], [[../../.raw/papers/KRT75D4W/asset-status|asset-status]]
- Related papers in this lab: [[2021-NE-national-wind-solar-growth-dynamics|Cherp et al. 2021, Nature Energy]] (direct citation and shared logistic/Gompertz growth-curve family); [[2023-NC-endogenous-learning-green-h2-europe|Zeyen et al. 2023, Nature Communications]] (European green-hydrogen scale-up, but with sector-coupled optimization and learning); [[2024-NE-h2-additionality-time-matching|Giovanniello et al. 2024, Nature Energy]] (green-hydrogen policy design under grid and investment constraints); [[2022-NE-china-hta-clean-hydrogen|Yang et al. 2022, Nature Energy]] (hydrogen as hard-to-abate-sector decarbonization lever).
- Pattern pages it will inform after paper 10: `patterns/methods/technology-diffusion-feasibility`, `patterns/figures/probabilistic-feasibility-space`, `patterns/policy/accelerate-and-hedge`, `patterns/hydrogen/scale-up-bottlenecks`
- Playbook pages it will inform after paper 20: `playbook/intro-scale-shock-template`, `playbook/probabilistic-policy-headlines`, `playbook/hydrogen-feasibility-checklist`

> [!note] Method-family link with [[2021-NE-national-wind-solar-growth-dynamics|Cherp et al. 2021]]
> Evidence: Odenweller et al. cite Cherp et al. 2021 as ref. 28 and use the wind and solar growth-curve literature as a methodological base. Inference: confidence high. Odenweller shifts the question from whether wind and solar growth can meet climate targets to whether green-hydrogen electrolysis can scale fast enough to support targets that assume hydrogen availability.
