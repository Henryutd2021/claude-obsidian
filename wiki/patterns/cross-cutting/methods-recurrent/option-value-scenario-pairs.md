---
type: pattern
title: "Option-value scenario pairs (with-X / without-X)"
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

# Option-value scenario pairs (with-X / without-X)

> Methodology pattern: quantify the option value of a technology, policy lever, or methodological choice by running paired scenarios that differ only in whether the option is available. The delta IS the headline number.

## Pattern claim

L1 energy modeling papers convert qualitative "is technology X worth pursuing?" questions into hard-number contributions by running with-X and without-X scenarios over identical input data and identical solver setup. The headline becomes a percent reduction / increase / cost saving attributable cleanly to the option.

The recurring construction:

```
Scenario A: all baseline assumptions, option X available
Scenario B: all baseline assumptions, option X disabled
Headline: (objective_B - objective_A) / objective_B = N%
```

This sidesteps the "compared to what?" critique that haunts single-scenario optimization papers and produces a directly policy-quotable number.

## The recurring move (one-line)

When you have an optimization model, do not report a single optimal scenario; report the delta against a comparable counterfactual where the option of interest is removed.

## Evidence (L1 papers supporting this pattern)

- [[2024-OE-h2-economy-22pct-cost-reduction]] — Evidence: GCAM with-H2 vs without-H2 paired runs across 3-9% H2 share scenarios; headline is "15-22% mitigation cost reduction". Also runs end-use exclusion paired scenarios (shipping in/out, etc.) to rank end uses by option value. Lesson: a *family* of paired scenarios produces both a headline number and a ranking.
- [[2022-NE-china-hta-clean-hydrogen]] — Evidence: ZERO-H (H2 available) vs ZERO-NH (H2 disabled) scenarios in TIMES-VEDA; headline is "US$1.72T avoided cumulative investment, 0.13% of GDP". Lesson: pick a single dollar (or percent) number as the headline; reviewers and journalists will use that one.
- [[2023-NC-endogenous-learning-green-h2-europe]] — Evidence: endogenous-learning-on vs endogenous-learning-off paired runs in PyPSA-Eur-Sec. Lesson: option value can be a *methodological* choice (learning treatment), not just a technology — and still produce a headline delta.
- [[2024-NE-h2-additionality-time-matching]] — Evidence: additionality-on vs additionality-off, plus annual-matching vs hourly-matching, in DOLPHYN. Lesson: stacking paired scenarios across a *policy design grid* converts a policy debate into a quantified trade-off curve.

## Counter-evidence (papers that depart from the pattern)

- [[2021-NE-national-wind-solar-growth-dynamics]] — Evidence: empirical fit, not a scenario-pair paper. The contribution is "this is the historical envelope"; there's no counterfactual to run. Lesson: when the data is observational, the option-value pattern doesn't apply — find a different headline construction.
- [[2015-N-china-fossil-cement-co2-revised]] — Evidence: data-correction, not modeling. The contribution is "estimates are 14% lower than IPCC default"; the counterfactual is "what the world believed before".

These counter-examples show option-value pairs need *a decision the analyst can flip in code*. Observational and data-correction papers use different headline-construction patterns.

## When this pattern works

- Any optimization / IAM / capacity-expansion paper with at least one configurable lever.
- Policy-relevant venues (NE, OE, Joule, NCC) where a single-number headline is critical for reach.
- Cases where the option-value of an early-stage technology or policy is contested.

## When this pattern fails or feels formulaic

- When the "without X" world is implausible (e.g., "without electricity altogether") and the comparison feels rigged. Pair the option only against realistic alternatives.
- When the model has many strongly-coupled options and disabling one cascades into 10 others. Then pair pieces by piece, not the whole vs whole.
- When the deltas are tiny (<2%) and noise-dominated.

## Transferable template (for Henry's drafts)

```
Section: "Quantifying the option value of {X}"

  We run two scenario families:
    1. {Baseline-with-X}: {one-line description}
    2. {Baseline-without-X}: identical to (1) except X is forced to
       zero capacity / zero deployment / disabled-in-the-formulation.

  Headline metric: {cost} or {emissions} or {feasibility-cap}
    delta = (metric_without - metric_with) / metric_without

  Reporting: report delta as a single number AND as a function of
  the key driver variable (carbon price, year, region) to give the
  reader a sensitivity ladder.
```

For Henry's wind-solar-hydrogen TEA: run with-co-located-electrolyzer vs without; with-grid-import vs island; with-LCOH-based-pricing vs commodity-H2-import.

## Confidence

**High.** 4 L1 papers across 4 different journals (NE, OE, NC) — option-value pairing is widely transferable across modeling traditions (IAM, TIMES, PyPSA-Eur-Sec, capacity-expansion).

## Henry's stance

<!-- HENRY-NOTE-START -->
<!-- For SMR-DC: the obvious option-value pair is "with-SMR-co-located vs grid-supplied-DC". The non-obvious option-value pair is "with-waste-heat-ORC vs heat-discarded" — that one is probably the real headline number. -->
<!-- HENRY-NOTE-END -->

## Related patterns

- [[additionality-counterfactuals]] — additionality framings are a specific class of option-value pair
- [[plant-vs-aggregate-resolution]] — resolution choices interact with option-value framing
- [[cost-multi-unit-reporting]] (figure pattern, see [[../figure/cost-multi-unit-reporting]] once promoted)

## Promoted from

`wiki/hot.md` cross-paper anchor `patterns/methods/option-value-scenario-pairs` (4 supporting papers, 2026-05-11).
