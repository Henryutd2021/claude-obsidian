---
type: playbook
title: "Contribution decision tree (archetype → claim type)"
created: 2026-05-11
updated: 2026-05-11
status: v0.1-skeleton
source_papers_l1: 22
source_papers_l2: 0
related_patterns:
  - "[[patterns/cross-cutting/archetype/firm-clean-flexible-baseload]]"
  - "[[patterns/cross-cutting/methods-recurrent/option-value-scenario-pairs]]"
  - "[[patterns/cross-cutting/methods-recurrent/plant-vs-aggregate-resolution]]"
tags:
  - playbook
  - top-journal-craft
  - contribution
---

# Contribution decision tree (archetype → claim type)

> v0.1. A decision tree for picking what *kind* of contribution Henry's manuscript should claim, derived from the archetype distribution across the 22 L1 papers. To be refined as the corpus grows.

## What this is

Henry asks: "I have a result. What kind of contribution should I claim for a top-tier energy submission?" This page maps the path from the analysis the work has actually done to the contribution language that will resonate with NE / Joule / NC / OE / NCC editors and reviewers.

## The 8 archetype contribution classes (induced from 22 L1 papers)

| Class | What it claims | L1 exemplars | Method signature | Headline construction |
|---|---|---|---|---|
| **System-boundary expansion** | Existing analyses missed an important slice of the system; we add it. | [[2022-NE-china-hta-clean-hydrogen]] (cross-sector H2 in China to 2060), [[2022-NE-flexible-nuclear-deep-decarb]] (nuclear-flexibility in deep-decarb) | TIMES, GCAM, capacity-expansion with new technology / sector activated | Single dollar / percent: "US$X avoided" |
| **Methodological endogeneization** | A treatment that's been exogenous in prior work is made endogenous here. | [[2023-NC-endogenous-learning-green-h2-europe]] (endogenous learning curves), [[2025-NE-smr-policy-module-learning]] (endogenous policy + factory learning) | Modify objective / constraints to make X internal | "When X is treated endogenously, deployment is N% higher / lower" |
| **Counterintuitive result** | A policy that the field expects to be effective turns out not to be (or vice versa). | [[2024-NE-h2-additionality-time-matching]] (additionality framework choice flips conclusions), [[2022-NE-green-h2-probabilistic-feasibility]] (even upper feasibility envelope, H2 falls short of 1.5°C target) | Paired counterfactual + careful framing | "Against [field expectation], we find [opposite]" |
| **Plant / city / process resolution** | Resolve at a unit the field has previously studied at aggregate. | [[2023-N-china-pv-wind-3844-plants]] (3,844 plants), [[2023-NC-rooftop-pv-china-carbon]] (354 cities), [[2022-NE-china-hta-clean-hydrogen]] (780+ processes) | New database / dataset, optimization at unit level | "At unit level, we find heterogeneity / opportunity / cost X" |
| **Data correction / inventory revision** | The numbers the field has been using are wrong. | [[2015-N-china-fossil-cement-co2-revised]] (Chinese CO2 14% lower than IPCC default), [[2022-J-data-center-energy-estimates-review]] (provenance audit of 258 estimates) | Bottom-up recomputation, source verification | "We revise X by N%, with implication Y for prior claims" |
| **Meta-analysis / synthesis** | Existing literature is fragmented; we synthesize and reveal pattern. | [[2023-NCC-net-zero-investment-shifts-europe]] (meta-analysis of 21 scenarios) | Harmonization of multiple datasets / models | "Across the literature, X is the common finding; the spread is N×" |
| **Empirical feasibility envelope** | Project a feasibility ceiling from historical analog growth. | [[2021-NE-national-wind-solar-growth-dynamics]] (60-country logistic fits), [[2022-NE-green-h2-probabilistic-feasibility]] (Monte-Carlo from analog distributions) | S-curve fit, Wright's law fit, probability bands | "Even on the upper envelope, X falls short of climate-target rate Y" |
| **Field-trial / operational evidence** | Operational data on a system the literature has only modeled. | [[2026-NE-ai-data-centres-grid-interactive]] (256-GPU Phoenix field trial) | Production-system instrumentation + counterfactual | "We demonstrate X under operational conditions, with magnitude Y" |

## The decision tree

```
START: I have a result. What kind of paper is it?

Q1: Is the result OBSERVATIONAL (a measurement, field-trial, historical data) or MODELING (an optimization or simulation)?

  → OBSERVATIONAL:
    Q1a: Does the observation overturn a number the field has used?
      → YES: Data correction / inventory revision (Liu 2015 N, Mytton 2022 J)
      → NO:
        Q1b: Is it an envelope from historical growth?
          → YES: Empirical feasibility envelope (Cherp 2021 NE)
          → NO: Field-trial / operational evidence (Colangelo 2026 NE)

  → MODELING:
    Q2: Does the model add a technology / sector / region the field has analyzed without?
      → YES: System-boundary expansion (Yang 2022 NE, Duan 2022 NE)
      → NO:
        Q3: Does the model treat a previously-exogenous element endogenously?
          → YES: Methodological endogeneization (Zeyen 2023 NC, Vanatta 2025 NE)
          → NO:
            Q4: Does the model resolve at a unit (plant, city, process) the field has not?
              → YES: Plant / city / process resolution (Wang 2023 N, Zhang 2023 NC)
              → NO:
                Q5: Is the result counterintuitive to the field's prior consensus?
                  → YES: Counterintuitive result (Giovanniello 2024 NE, Odenweller 2022 NE)
                  → NO:
                    Q6: Is the contribution synthesis across prior models?
                      → YES: Meta-analysis / synthesis (Klaaßen 2023 NCC)
                      → NO: STOP. The contribution may not be top-tier strong.
                             Consider what's missing: counterfactual sharpness?
                             Bigger system boundary? Newer data? Reframe and retry.
```

## How to use it for Henry's drafts

1. Start with the *result* of the analysis Henry has actually done.
2. Walk the tree to identify which contribution class the result fits.
3. Use the row from the table above to determine: (a) the method signature reviewers will expect, (b) the headline construction (single number, contrast claim, envelope), (c) the L1 exemplars to cite as architectural ancestors.
4. If the result fits no class cleanly, the manuscript is either (a) early: go back to analysis and sharpen the counterfactual / resolution / endogeneization, or (b) a different class not in the 22-paper corpus yet: promising but riskier, and the Intro must work harder to establish what *kind* of contribution it is.

## For Henry's SMR-DC paper (worked example)

Walking the tree:

- Q1: MODELING.
- Q2: Does it add a technology / sector? **Yes: SMR + DC co-location with waste-heat-ORC is a system Configuration the field has not coupled. → SYSTEM-BOUNDARY EXPANSION.**
- Q3: Does it endogenize something? **Secondarily yes: DC siting + SMR deployment as coupled decisions is endogeneization of what's typically two separate problems. → secondary METHODOLOGICAL ENDOGENEIZATION.**
- Q4: Does it resolve at a new unit? **Yes: facility-pair (SMR ↔ DC pair) resolution. → tertiary PLANT / PROCESS RESOLUTION.**

So the SMR-DC paper has primary contribution = system-boundary expansion, secondary = endogeneization, tertiary = resolution. The Intro and abstract should lead with the system-boundary claim ("we are the first to jointly optimize SMR + DC + ORC at facility-pair resolution"), with the endogeneization and resolution as second-tier supporting claims.

## Confidence

**Medium.** The 8 archetype classes are induced from the 22-paper corpus and from `hot.md` archetype tags. As more L1 papers ingest, classes will be refined. The L2 contrast (which contribution classes the applied flagships favor) lands in v0.2.

## Source papers

22 L1 papers, archetype-tagged. Run `python3 scripts/subdomain-bridge-stats.py` to refresh the stats and re-induce classes if needed.

## Henry's stance

<!-- HENRY-NOTE-START -->
*Hand-edits here survive any regenerator. When drafting, paste the decision tree into the draft notes and force a single primary class. Avoid making "we did 4 things" claims - reviewers want one contribution.*
<!-- HENRY-NOTE-END -->

## Related

- [[../../patterns/cross-cutting/methods-recurrent/option-value-scenario-pairs]]: the standard headline construction for system-boundary expansion + counterintuitive results
- [[../../patterns/cross-cutting/methods-recurrent/plant-vs-aggregate-resolution]]: the methodological signature for plant / city / process resolution
- [[../../patterns/cross-cutting/archetype/firm-clean-flexible-baseload]]: a system-boundary-expansion archetype with specific structure
- [[intro-template-energy-papers]]: companion playbook on Intro architecture
