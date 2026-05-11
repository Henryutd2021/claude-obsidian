---
type: pattern
title: "Merit-order and end-use ranking for H2 / e-fuels"
created: 2026-05-11
updated: 2026-05-11
status: developing
supporting_papers_l1: 2
supporting_papers_l2: 0
pattern_category: subdomain
subdomain: hydrogen-p2x
tags:
  - pattern
  - subdomain
  - sd/hydrogen-p2x
  - sd/energy-policy-economics
---

# Merit-order and end-use ranking for H2 / e-fuels

> Subdomain pattern (`hydrogen-p2x`): the contribution of an L1 H2 / e-fuel paper often lives in producing an explicit ranking of end uses against a defensible scoring rule.

## Pattern claim

For hydrogen and e-fuels at the policy-relevant scale, the question "should we use H2 for X?" is contested across heating, ground transport, aviation, shipping, industrial heat, chemical feedstock, and seasonal power. L1 papers in this subdomain are not the ones that say "H2 is good"; they are the ones that **rank end uses against an explicit scoring rule** and let the bottom-of-rank uses be dropped.

Two distinct ranking rules appear:

1. **Efficiency-cost-MACC sorting** (Ueckerdt 2021 NCC): score each end use by (a) electricity-to-useful-energy efficiency (16-48% for e-fuel routes vs 60-90% for direct electrification), (b) levelized cost vs direct electrification alternative, (c) marginal abatement cost on the residual emissions. End uses where direct electrification is technically infeasible OR where MACC is uniquely low get H2; others should not.
2. **End-use exclusion ranking** (Wolfram 2024 OE): GCAM IAM run with each end use *excluded* one at a time. Rank end uses by the cost increase caused by exclusion. Shipping comes out #1 at 6.4% of 2050 H2 final-energy share.

Both rules deliver actionable hierarchies; both treat H2 as a finite resource to be rationed.

## The recurring move (one-line)

For a H2 / e-fuels paper, do not advocate H2 in general — produce a defensible ranking of end uses against an explicit scoring rule, and let the ranking carry the argument.

## Evidence (L1 papers supporting this pattern)

- [[2021-NCC-h2-efuels-potential-risks]] — Evidence: §Methods classifies end uses by efficiency-cost-MACC; explicit table of 16-48% electricity-to-useful efficiency for e-fuel routes vs 60-90% for direct electrification. Lesson: when you have a multi-dimensional scoring rule, present the dimensions in a single table, then let the reader see which end uses lose on every dimension.
- [[2024-OE-h2-economy-22pct-cost-reduction]] — Evidence: GCAM end-use exclusion paired scenarios with shipping at 6.4% final-energy share. Lesson: end-use exclusion scenarios produce a much more readable contribution than "what's the H2 share in 2050?" alone.

## Counter-evidence (papers that depart from the pattern)

- [[2022-NE-china-hta-clean-hydrogen]] — Evidence: TIMES-VEDA at process level; H2 is one option among many. The contribution lives in system-boundary expansion (cross-sectoral H2 modeling for China-2060), not in end-use ranking per se. Lesson: in a system-wide TEA, end-use ranking emerges implicitly through optimization but is not lifted into the headline.
- [[2024-NE-h2-additionality-time-matching]] — Evidence: the contribution is the additionality framework, not end-use ranking. Lesson: a paper can address a different H2 framing question entirely.

## When this pattern works

- For perspective / synthesis-style papers (NCC, OE) where the contribution is a ranking, not a single number.
- When the scoring rule itself is novel (efficiency-cost-MACC composite, exclusion-scenario ladder).
- When existing literature has named end uses but not ranked them rigorously.

## When this pattern fails or feels formulaic

- For deep system-coupled models (TIMES, GCAM full-economy) where end uses emerge from optimization. Lifting them out for ranking is artificial.
- When the scoring rule rewards what the author already wants to advocate (be careful with cherry-picked scoring).

## Transferable template (for Henry's drafts)

```
"We rank H2 / e-fuel end uses for region R, year Y, against scoring rule SR:
  - Dimension 1: {electricity-to-useful efficiency, %}
  - Dimension 2: {levelized cost vs direct-electrification alternative, $/MJ}
  - Dimension 3: {residual MACC, $/tCO2}

  End uses (sorted by composite score):
    Rank 1: {use_a} - eligible for H2 because {all alternatives infeasible}
    Rank 2: {use_b} - eligible if H2 cost falls below threshold T_b
    ...
    Last rank: {use_z} - not eligible; direct electrification wins on all dimensions"
```

For Henry's wind-solar-hydrogen system: the end-use question is critical when justifying *who buys the H2*. If a buyer's end use is below the merit threshold, the project is a candidate for stranded asset risk regardless of LCOH.

## Confidence

**Medium-high.** 2 L1 papers across different journals (NCC, OE) with consistent treatment. The two scoring rules are *complementary* (efficiency-cost-MACC is engineering-economic; exclusion-ranking is system-level), and a 3rd L1 paper combining both (perhaps from Joule or Nature Energy in 2025-2026) would push this to high.

## Henry's stance

<!-- HENRY-NOTE-START -->
<!-- For Henry's manuscripts: he should never propose "wind-solar-hydrogen for X" without checking X's rank in this merit-order. If X is shipping/aviation/industrial-heat, the merit-order argument helps. If X is light-duty transport or residential heating, the same merit-order argument hurts. -->
<!-- HENRY-NOTE-END -->

## Related patterns

- [[../../cross-cutting/methods-recurrent/option-value-scenario-pairs]] — exclusion-rankings are option-value pairs at the end-use level
- [[../../cross-cutting/archetype/firm-clean-flexible-baseload]] — both archetypes ration scarce clean energy in different ways
- [[../../../bridges/energy-policy-economics--hydrogen-p2x]]

## Promoted from

`wiki/hot.md` cross-paper anchor `patterns/hydrogen/merit-order-and-end-use-ranking` (2 supporting papers, 2026-05-11).
