---
type: pattern
title: "Plant vs aggregate resolution as contribution"
created: 2026-05-11
updated: 2026-05-11
status: developing
supporting_papers_l1: 4
supporting_papers_l2: 0
pattern_category: methods-recurrent
subdomain: ""
tags:
  - pattern
  - methods-recurrent
---

# Plant vs aggregate resolution as contribution

> Methodology pattern: in top-tier energy modeling papers, the spatial / unit resolution choice is itself the contribution, not a methodological detail.

## Pattern claim

L1 energy modeling papers explicitly justify their resolution choice along one of four levels and lift the resolution itself into the contribution claim. Higher resolution is not automatically better; the contribution is making a defensible resolution choice that matches the policy question being asked.

The L1 corpus shows four resolution archetypes:

1. **Plant level (3,000-4,000 entities)**: Wang 2023 N — 3,844 individual utility-scale PV / wind plants in China, optimized in geography.
2. **City level (300-400 entities)**: Zhang 2023 NC — 354 Chinese cities, rooftop-PV potential mapped to retail-grid-parity geography.
3. **Process / facility level (500-1000 entities)**: Yang 2022 NE — 780+ technology processes in TIMES-VEDA spanning all sectors.
4. **Country level (50-100 entities)**: Cherp 2021 NE — 60 countries fitted with logistic growth curves on observed wind / solar deployment.

Each paper makes the resolution itself the headline:

- Wang: plant-level enables grid-parity diagnosis at point-of-generation
- Zhang: city-level enables retail-tariff arbitrage assessment
- Yang: process-level enables sector-coupling claims that aggregate models cannot make
- Cherp: country-level matches the unit of climate policy and growth feasibility

## The recurring move (one-line)

Pick the resolution that maps 1:1 to the policy lever you're testing, and make the resolution-to-lever match a primary claim.

## Evidence (L1 papers supporting this pattern)

- [[2023-N-china-pv-wind-3844-plants]] — Evidence: Methods section enumerates the 3,844-plant database and lifts plant-level resolution into the abstract. Lesson: when the policy lever (project-level investment) operates at point-of-generation, model at point-of-generation.
- [[2023-NC-rooftop-pv-china-carbon]] — Evidence: 354-city resolution mapped to retail-tariff geography. Lesson: pick the resolution that matches the *price signal* the actor faces (retail tariff is city-level, wholesale is plant / node level).
- [[2022-NE-china-hta-clean-hydrogen]] — Evidence: 780+ TIMES-VEDA processes span hard-to-abate sectors that aggregate models cannot resolve. Lesson: for sector-coupling claims, resolution must be process-level, not aggregate.
- [[2021-NE-national-wind-solar-growth-dynamics]] — Evidence: 60-country logistic fits anchored to climate policy units. Lesson: when the question is "is this rate feasible at policy unit X", model at policy unit X — not above, not below.

## Counter-evidence (papers that depart from the pattern)

- [[2022-NE-flexible-nuclear-deep-decarb]] — Evidence: 42 country-level regions, hourly resolution. Inference (high): country-level chosen because the question is system-level (deep-decarb portfolio), not facility-level. The contribution lives in the *temporal* resolution (hourly), not the spatial.
- [[2025-J-space-based-solar-europe]] — Evidence: PyPSA-Eur at standard bidding-zone resolution. Inference (medium): the contribution lives in the technology threshold mapping (cost + availability), not the spatial resolution choice.

These counter-examples show that *not every paper makes resolution-itself the headline*. They make a different choice (temporal resolution, threshold mapping) and shift the contribution there.

## When this pattern works

- When the policy lever / decision-maker operates at a specific unit (plant, city, facility, country) and aggregate models cannot resolve that unit's heterogeneity.
- When the dataset is plant-by-plant / city-by-city available and the *novelty of the dataset* is part of the contribution.
- When a reviewer might say "but couldn't you do this with country averages?" — make the resolution choice load-bearing.

## When this pattern fails or feels formulaic

- When the system-level dynamics dominate (sector-coupling, dispatch, market-design) and finer resolution adds noise without adding answer.
- When data quality at the finer resolution is suspect (provenance issues, missing fields). Wang 2023 N can do plant-level because the Chinese plant database is unusually complete; in regions where the database is weak, plant-level becomes a liability.

## Transferable template (for Henry's drafts)

```
Step 1: name the policy lever (carbon tax, investment subsidy, RFNBO,
        capacity payment, dispatch priority...)
Step 2: name the unit at which the lever operates (project, facility,
        bidding zone, country, region, sector...)
Step 3: model AT THAT UNIT and lift the resolution-to-lever match
        into the contribution claim. Do not let resolution become
        "we modeled at this level" - make it "we modeled at THIS level
        because that's the level at which the policy actually bites".
```

For Henry's SMR-DC paper: the policy lever is the data center developer's siting choice + the SMR developer's deployment choice. Both operate at *facility-pair* level. The contribution should resolve at facility-pair, not zone.

## Confidence

**High.** 4 L1 papers across 3 journals (NE, N, NC) with consistent treatment of resolution-as-contribution.

## Henry's stance

<!-- HENRY-NOTE-START -->
<!-- For the SMR-DC waste-heat-ORC paper: model at facility-pair (SMR ↔ DC). Look for the 100-200 candidate sites in the ERCOT / SPP geographies where Vanatta 2023 J already did the SMR side. -->
<!-- HENRY-NOTE-END -->

## Related patterns

- [[national-vs-continental-case]] — case-geography choice; related but orthogonal (one is spatial unit, the other is geographic scope)
- [[option-value-scenario-pairs]] — pairs scenarios at a fixed resolution
- [[../../bridges/integrated-energy-systems--power-systems]]

## Promoted from

`wiki/hot.md` cross-paper anchor `patterns/methods/plant-vs-aggregate-resolution` (4 supporting papers, 2026-05-11).
