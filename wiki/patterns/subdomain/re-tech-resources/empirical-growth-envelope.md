---
type: pattern
title: "Empirical growth envelope as feasibility ceiling"
created: 2026-05-11
updated: 2026-05-11
status: developing
supporting_papers_l1: 2
supporting_papers_l2: 0
pattern_category: subdomain
subdomain: re-tech-resources
tags:
  - pattern
  - subdomain
  - sd/re-tech-resources
  - sd/energy-policy-economics
---

# Empirical growth envelope as feasibility ceiling

> Subdomain pattern (`re-tech-resources`): use empirical growth history of past technologies as a feasibility ceiling for future deployment projections. The argument flips the burden of proof from "trust my projection" to "find a counter-example in the historical record".

## Pattern claim

L1 RE-deployment papers do not bet on a specific future trajectory; they construct an **envelope** of feasibility from observed historical growth (S-curves on past technologies, leader-country deployment rates, analog-technology distributions) and then test whether climate-target-implied trajectories fit inside that envelope.

This pattern is a structural inversion of conventional projection. Instead of:

> "Here is our scenario for solar PV; we project X GW/yr by 2030"

The argument becomes:

> "Here is the empirical envelope of historical growth. Climate-target-implied trajectories sit on / above / below this envelope. Trajectories above the envelope have no historical analog and need a defended exception."

The L1 corpus shows two complementary constructions:

1. **Logistic-fit on national experience** (Cherp 2021 NE): fit logistic S-curves to wind/solar deployment in 60 countries; identify "leader country" rates as the upper bound; check climate-target-implied rates against this bound. Only a handful of countries have ever hit the rates 1.5°C requires.
2. **Monte-Carlo from analog-tech distributions** (Odenweller 2022 NE): build a probability envelope from analog-technology growth distributions (Wright's-law-fit ensemble); even on the upper feasibility envelope, green hydrogen supply meets <1% of 2030 final energy in 1.5°C scenarios: the gap is structural.

Both constructions deliver the same rhetorical move: pre-empt reviewer pushback on optimistic projections by anchoring to observable historical reality.

## The recurring move (one-line)

When projecting RE deployment, construct an empirical envelope from historical analog technologies first; the contribution is the envelope, not the projection.

## Evidence (L1 papers supporting this pattern)

- [[2021-NE-national-wind-solar-growth-dynamics]]: Evidence: ex-post logistic fits to wind/solar deployment in 60 countries (1990-2020); leader-country growth rates as empirical ceiling. Lesson: when fitting growth curves, the unit of fitting (country, region, technology family) matters. Country-level fitting gives policy-relevant feasibility benchmarks because policy operates at country level.
- [[2022-NE-green-h2-probabilistic-feasibility]]: Evidence: Monte-Carlo feasibility envelope built on historical analog-technology growth distributions (Wright's-law-fit ensemble); even on upper envelope, green H2 supply meets <1% of 2030 final energy in 1.5°C scenarios. Lesson: by reporting envelopes (probability bands), not single-point projections, the paper makes its claim falsification-friendly: any future observation higher than the upper band would falsify it.

## Counter-evidence (papers that depart from the pattern)

- [[2024-OE-h2-economy-22pct-cost-reduction]]: Evidence: GCAM IAM produces 2050 H2 share trajectories from cost optimization, not empirical envelopes. Lesson: in full economy-wide IAM frameworks, empirical-envelope construction is replaced by economic optimization. Different rhetorical move.
- [[2023-N-china-pv-wind-3844-plants]]: Evidence: optimizes plant-by-plant from grid-parity geography; growth dynamics are not the contribution. Lesson: when the contribution lives elsewhere (plant resolution, grid-parity overlay), don't force in an empirical envelope.

## When this pattern works

- For papers projecting deployment over 10-30 year horizons where uncertainty in growth rate dominates.
- When climate-target literature has produced highly optimistic projections and the author wants to reframe feasibility as a falsifiable empirical claim.
- For technologies with enough historical-analog data to fit (PV, wind, electric vehicles, heat pumps).

## When this pattern fails or feels formulaic

- For genuinely novel technologies with no analog (fusion, space-based solar, some long-duration storage). The Cherp / Odenweller construction requires *analog technology data*: without it, the envelope is speculative.
- For full economy-wide models where deployment is endogenous to cost trajectories (different rhetorical pattern; see option-value-scenario-pairs).
- When the conclusion would be "feasibility is fine, no problem". The pattern's strength is its skeptical / pre-empting-criticism rhetoric; when there's no criticism to pre-empt, the pattern feels overbuilt.

## Transferable template (for Henry's drafts)

```
Section: "Feasibility envelope for {technology X}"

  Step 1: Identify analog technologies / past deployments.
    For X, what is the closest historical-growth analog?
    Wind→solar; solar→storage; storage→electrolyzer; ...

  Step 2: Fit growth curves on analog data.
    Either logistic per-country (Cherp style) or Wright's-law
    ensemble (Odenweller style).

  Step 3: Construct envelope - typically a probability band, with
    leader-country / upper-Wright as upper bound.

  Step 4: Overlay climate-target-implied trajectory for X.

  Step 5: Report:
    (a) Where the trajectory sits relative to the envelope
    (b) For trajectories above upper bound: name what's needed
        (no historical precedent => structural shift needed)
    (c) For trajectories near or below: feasibility supported.
```

For Henry's wind-solar-hydrogen TEA: the SMR build rate and the electrolyzer build rate are both candidates for empirical-envelope checking. SMR has limited analog (LWR build-out in 1970s-1980s, China's 2010s expansion); electrolyzer has Wright's-law-fit-able cost data and PV / wind analog patterns.

## Confidence

**Medium-high.** 2 L1 papers across the same journal (NE) but with different growth analytics (S-curves vs Monte-Carlo / Wright's law). A third independent paper applying the same framework to a different technology (e.g., heat pumps, electric vehicles) would push to high.

## Henry's stance

<!-- HENRY-NOTE-START -->
*For Henry's manuscripts: any deployment claim should be paired with empirical feasibility envelope. This is the single fastest way to upgrade Applied Energy-level deployment papers to NE-level.*
<!-- HENRY-NOTE-END -->

## Related patterns

- [[../../cross-cutting/methods-recurrent/option-value-scenario-pairs]]: different rhetorical move for projecting; envelope construction PRECEDES option-value scenarios in a paper
- [[../../cross-cutting/methods-recurrent/plant-vs-aggregate-resolution]]: the envelope-fit unit (country, plant, technology) is a resolution choice
- [[../../../bridges/energy-policy-economics--re-tech-resources]]

## Promoted from

`wiki/hot.md` cross-paper anchor `patterns/feasibility/empirical-growth-envelope` (2 supporting papers, 2026-05-11).
