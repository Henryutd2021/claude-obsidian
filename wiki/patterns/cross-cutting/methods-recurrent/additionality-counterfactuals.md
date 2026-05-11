---
type: pattern
title: "Additionality counterfactuals (compete vs non-compete)"
created: 2026-05-11
updated: 2026-05-11
status: developing
supporting_papers_l1: 2
supporting_papers_l2: 0
pattern_category: methods-recurrent
subdomain: ""
tags:
  - pattern
  - methods-recurrent
  - sd/hydrogen-p2x
  - sd/energy-policy-economics
---

# Additionality counterfactuals (compete vs non-compete)

> Methodology pattern: how hydrogen / clean-energy additionality is framed determines what answer the model returns on identical input data.

## Pattern claim

When the same grid-connected hydrogen production system is analyzed under different additionality framings, the policy conclusion flips. The disagreement is not about model accuracy; it is about which counterfactual is being scored. **The framing itself is the contribution.**

Two distinct counterfactual constructions appear in the L1 corpus:

- **Non-compete** (Zeyen 2023 NC, PyPSA-Eur-Sec with endogenous learning): new electrolyzer demand is accompanied by new renewable capacity that does not displace existing electricity demand. Emissions accounting treats this added capacity as "additional" by construction. Result: green H2 grows aggressively even at moderate carbon prices.
- **Compete** (Giovanniello 2024 NE, DOLPHYN capacity-expansion): new electrolyzer demand competes with existing demand for the same grid electrons. Without time-matching, the marginal electron is gas; with annual matching, it's still partially gas; only with hourly matching is the marginal electron clean. Result: phased policy (annual now, hourly post-2030) is least-cost.

The two papers reach **opposite policy recommendations** from this single framing choice.

## The recurring move (one-line)

State your additionality counterfactual explicitly in the methods section, then run the scenario both ways and report the delta as the contribution.

## Evidence (L1 papers supporting this pattern)

- [[2024-NE-h2-additionality-time-matching]] — Evidence: §Methods describes "compete" counterfactual via consequential emissions accounting in DOLPHYN. The paper explicitly diagnoses Zeyen 2023 NC as a "non-compete" framework in its Discussion. Lesson: name your counterfactual class and cite the prior literature it differs from.
- [[2023-NC-endogenous-learning-green-h2-europe]] — Evidence: §Methods, sector-coupling configuration where new electrolyzer demand pairs with new RE capacity within the optimization. Lesson: when a paper does not flag its additionality construction, downstream readers will (in 12 months, in print).

Reciprocal `> [!contradiction]` callouts already linked on both pages.

## Counter-evidence (papers that depart from the pattern)

- [[2022-NE-china-hta-clean-hydrogen]] — Evidence: TIMES-VEDA framework with system-boundary expansion, but additionality treatment is not the load-bearing argument; H2 is one of many options in a least-cost system. Inference (medium confidence): the additionality question would have mattered less because the system is China-wide and policy levers are large.
- [[2024-OE-h2-economy-22pct-cost-reduction]] — Evidence: GCAM IAM with H2 as an option, not a constrained additionality regime. The 22% cost-reduction headline is robust to additionality framing because IAM economy-wide.

## When this pattern works

- Policy-relevant venues (NE, NCC, OE, Joule) where the same dataset can produce headline-grabbing different answers depending on counterfactual choice.
- Regulatory contexts (EU RFNBO, US 45V) where explicit additionality language exists in the policy itself.
- System-level analyses with multiple producers of the same energy carrier.

## When this pattern fails or feels formulaic

- Field-level papers that need to clear "is hydrogen a thing" before they get to "what kind of hydrogen." A counterfactual taxonomy distracts from the bigger claim.
- Engineering / cost-of-production papers (LCOH-only) that do not engage with grid emissions at all.

## Transferable template (for Henry's drafts)

```
"We model X under two counterfactuals:
  (a) {compete construction} - electrons displaced from existing
      demand are sourced from {marginal generator class}.
  (b) {non-compete construction} - new clean capacity scales with
      new H2 demand, leaving existing demand untouched.
We report the delta {result_a - result_b} as the policy-relevant
quantity."
```

If a project doesn't fit this template, the project is probably not making an additionality contribution. That's fine — pick a different angle.

## Confidence

**Medium-high.** Two L1 papers in direct contradiction with rich reciprocal documentation. Adding any third paper with a third counterfactual (e.g., "consequential LCA additionality" from RFNBO compliance literature) would push this to high confidence.

## Henry's stance

<!-- HENRY-NOTE-START -->
<!-- Hand-edits in this block survive any regenerator. Useful note: for Henry's own SMR-DC paper, the equivalent counterfactual question is "does the data center load demand new SMR build, or shift existing demand?" — this is the directly analogous framing choice. -->
<!-- HENRY-NOTE-END -->

## Related patterns

- [[option-value-scenario-pairs]] — additionality pairs ARE one type of option-value pair
- [[plant-vs-aggregate-resolution]] — both papers above resolve at the bidding-zone / capacity-zone level, not plant level
- [[../../bridges/energy-policy-economics--hydrogen-p2x]]

## Promoted from

`wiki/hot.md` cross-paper anchor `patterns/methods/additionality-counterfactuals` (paper-10 gate cleared, 2026-05-11).
