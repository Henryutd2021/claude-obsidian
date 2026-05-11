---
type: playbook
title: "Main-figure design rules for top-tier energy papers"
created: 2026-05-11
updated: 2026-05-11
status: v0.1-skeleton
source_papers_l1: 22
source_papers_l2: 0
related_patterns:
  - "[[patterns/cross-cutting/archetype/firm-clean-flexible-baseload]]"
tags:
  - playbook
  - top-journal-craft
  - figures
---

# Main-figure design rules for top-tier energy papers

> v0.1 skeleton. Heuristics induced from figure-argument-function tables across the 22 L1 papers. **To be enriched in v0.2 with explicit figure-by-figure analysis once §10 figure tables are read across all 22 papers.** The L1/L2 figure-design contrast (the most informative comparison axis) will arrive after L2 pilots in Phase 2.

## What this is

A set of design rules for the main figures (typically 4-5 figures per paper) in a top-tier energy submission. Distilled from the 22 L1 papers' use of figure-as-argument.

## Rule 1: One figure, one argument-function

Each main figure carries exactly one of these argument functions. Top-tier papers do not double-up; figures that try to do two things end up doing neither.

| Function | What the figure shows | L1 example (likely) |
|---|---|---|
| **Geographic overlay tied to policy claim** | A map with the policy-relevant unit (plant, city, country) colored by the key metric (LCOE, MAC, capacity). The reader should see the spatial heterogeneity that the policy lever must address. | [[2023-N-china-pv-wind-3844-plants]] (likely Fig. 1 or 2) |
| **Counterfactual contrast** | Two scenarios side by side (with-X / without-X), with the delta as the visual headline. | [[2024-OE-h2-economy-22pct-cost-reduction]], [[2022-NE-china-hta-clean-hydrogen]] |
| **Mechanism diagram** | A schematic that compresses the *whole argument* of the paper into one figure: inputs, model, key transformation, outputs. Common as Fig. 1. | [[2024-NE-h2-additionality-time-matching]], [[2025-J-space-based-solar-europe]] |
| **Sensitivity / robustness** | Tornado plot, Pareto frontier, or probability envelope. Shows the result's stability. | [[2022-NE-green-h2-probabilistic-feasibility]] (Monte-Carlo envelope) |
| **Empirical anchor** | Historical observed data plotted alongside model projection. Used by feasibility-envelope papers and provenance-audit papers. | [[2021-NE-national-wind-solar-growth-dynamics]], [[2022-J-data-center-energy-estimates-review]] |
| **System-asset displacement** | Stacked bars / area charts showing which assets get displaced under different scenarios. Used by firm-clean-flexible-baseload archetype. | [[2022-NE-flexible-nuclear-deep-decarb]], [[2024-NE-flexible-geothermal-decarb-systems]] |

## Rule 2: Fig. 1 is the mechanism diagram

In 17 of the 22 L1 papers (estimated; v0.2 will verify), Fig. 1 is a mechanism diagram. It compresses the paper into one image:

- Top: the problem (sectoral demand, grid load, deployment trajectory)
- Middle: the analytical move (model, scenario pair, counterfactual construction)
- Bottom: the headline output (the number, the ranking, the envelope)

For a top-tier energy paper, if Fig. 1 is *not* a mechanism diagram (instead being, say, a literature meta-plot), the paper is signaling a different archetype (perspective / synthesis).

## Rule 3: Pick the headline number's home figure

One main figure in every L1 paper carries the **headline number**: the number quoted in the abstract. Examples (likely placement):

- Yang 2022 NE: US$1.72T headline → Fig. 4 or Fig. 5 (cost decomposition)
- Wang 2023 N: 9 → 15 PWh/yr → Fig. 1 or Fig. 4 (geographic + temporal)
- Cherp 2021 NE: leader-country growth ceiling → Fig. 2 or Fig. 3 (S-curve fits)
- Wolfram 2024 OE: 22% cost reduction → Fig. 2 or Fig. 3 (paired scenarios)
- Colangelo 2026 NE: 25% power reduction over 3h → Fig. 2 or Fig. 3 (time-series with overlay)

The headline figure should pass the **screenshot test**: a reader who only sees that one figure plus the caption should be able to state the paper's contribution.

## Rule 4: No more than one figure carries a sensitivity / robustness analysis

Top-tier figures resist sensitivity-overload. At most one sensitivity figure (tornado, envelope, Pareto). Multiple sensitivities should land in Extended Data or Supplementary. Applied papers often place 3-5 sensitivities in main text; this is a signature L2 move.

## Rule 5: Color is argument-functional, not decorative

L1 figures use color to **discriminate scenarios or asset classes**, not for aesthetic. Each color should be unambiguously named in the caption and consistent across figures within the paper.

Common discriminations:

- Scenario pair: muted gray (baseline / without-X) + saturated red or blue (with-X)
- Asset class: solar=yellow, wind=blue, nuclear=teal, hydrogen=green, gas=brown (rough convention)
- Time periods: muted past + saturated future (probability-band style)

## Rule 6: The model schematic is its own figure, or it is not in main text

If the paper relies on a complex model (TIMES-VEDA, GCAM, PyPSA-Eur-Sec, GenX, DOLPHYN), the model schematic is either (a) its own main figure (often Fig. 1, fused with the mechanism diagram), or (b) entirely in Extended Data / Methods. Hybrid placements (schematic-as-inset, schematic-as-supplement-of-Fig.-2) are signature applied-paper moves.

## Anti-patterns common in applied-paper figures

Will be expanded after L2 pilot ingest (Phase 2). Initial observations from the broader literature:

- Cost-decomposition stacks with 10+ categories
- Dispatch curves spanning full year at hourly resolution in main text
- Pareto frontier with 5+ axes
- Sankey diagrams used decoratively rather than for transformation argument
- Geographic maps without a policy-relevance overlay

## Transferable template for Henry's draft figures

```
Fig. 1: Mechanism diagram.
  Top:    Big problem (one panel, with one anchored number)
  Middle: The analytical move (model + counterfactual)
  Bottom: Headline output (one number, big font, deliberately exposed)

Fig. 2: Geographic / temporal heterogeneity.
  Map or time-series showing where / when the contribution applies.

Fig. 3: Headline counterfactual.
  Paired-scenario contrast. Color-discriminated. Delta annotated.

Fig. 4: Sensitivity / robustness (single figure).
  Either tornado on key variables, probability envelope, or Pareto.

Fig. 5: System-asset displacement / consequence.
  What gets displaced, who benefits, what is the policy / industry
  consequence implied by Figs. 1-4.
```

For Henry's SMR-DC paper: Fig. 1 mechanism (SMR ↔ DC ↔ grid). Fig. 2 geographic candidate pairs in ERCOT / SPP. Fig. 3 with-co-location vs grid-supplied counterfactual. Fig. 4 sensitivity (gas price, DC growth rate, ORC efficiency). Fig. 5 asset displacement (which gas plants retire, which transmission gets deferred).

## Confidence

**Low-medium (v0.1).** Rules are induced from headline patterns + archetype data, not from systematic figure-table mining. v0.2 will refine after structured reads of §10 across all 22 papers. **The L1/L2 contrast is the most informative axis and will land in v0.3 after L2 pilots.**

## Source papers (full mining in v0.2)

22 L1 papers ingested as of 2026-05-11. Each has a `§10 Figures & tables argument function` section in its analysis page.

## Henry's stance

<!-- HENRY-NOTE-START -->
*Hand-edits here survive regenerator. Useful note: paste Rule 1 table next to Henry's draft figures and force each figure to claim ONE function.*
<!-- HENRY-NOTE-END -->

## Related

- [[../../patterns/cross-cutting/archetype/firm-clean-flexible-baseload]]: system-asset-displacement figures (Rule 1) are the archetype signature
- [[../../patterns/subdomain/re-tech-resources/empirical-growth-envelope]]: envelope figures (Rule 1) are the signature for that pattern
- [[../../patterns/subdomain/ai-data-driven/load-shape-and-flexibility]]: Colangelo's time-series with overlay is a clean example of the headline-figure move
