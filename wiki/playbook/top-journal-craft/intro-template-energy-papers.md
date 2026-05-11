---
type: playbook
title: "Intro template for top-tier energy papers"
created: 2026-05-11
updated: 2026-05-11
status: v0.1-skeleton
source_papers_l1: 22
source_papers_l2: 0
related_patterns:
  - "[[patterns/cross-cutting/methods-recurrent/option-value-scenario-pairs]]"
  - "[[patterns/cross-cutting/methods-recurrent/plant-vs-aggregate-resolution]]"
tags:
  - playbook
  - top-journal-craft
  - intro
---

# Intro template for top-tier energy papers

> v0.1 skeleton. Distillation of Intro architecture across the 22 L1 papers ingested as of 2026-05-11. **To be enriched in v0.2 once L2 contrast pages land (Phase 4) and once §5 Intro paragraph tables are read across all 22 papers.**

## What this is

A reusable Intro skeleton for Henry's drafts that target Nature Energy / Joule / Nature Communications / One Earth / Nature Climate Change. Derived from the recurring Intro architecture across the 22 L1 papers in the lab.

## The 5-paragraph recurring scaffold (induction from L1)

Top-tier energy paper Introductions across the 22-paper corpus exhibit 4-6 paragraphs, with the median being 5. The role-sequence is consistent enough to template:

| ¶ | Role | What it does | Move that signals top-tier vs applied |
|---|---|---|---|
| P1 | **Big problem** | State the climate / energy-transition stake; tie to a defensible, sourced number (a global emissions figure, a deployment target, a stranded-asset estimate). | Top-tier names the **policy-relevant** scale (national, global, sectoral); applied papers name the **engineering** scale (one plant, one site). |
| P2 | **Why now** | Recent shift in the field that makes the question urgent: a policy package (IRA, EU H2 Bank, China dual-carbon), a technological tipping (cost crossover), a measurement (new dataset). | Top-tier opens with the *shift*; applied papers open with the technology specification. |
| P3 | **Specific gap** | The literature has done X, Y, Z; but A is unresolved. Frame the gap not as "no one has studied A" but as "the field is debating A in two camps" or "A has been treated implicitly but never made explicit". | Top-tier frames the gap as a **debate** or **implicit-assumption-now-load-bearing**; applied papers frame the gap as a missing case study. |
| P4 | **What we do** | Briefly: the method / model / data / scope. Top-tier introductions resist methods-dense writing here; they preview *contributions in plain terms*. | Top-tier says "we identify / quantify / rank / resolve"; applied papers say "we develop a model that…". |
| P5 (or merged into P4) | **Headline contribution + outline** | The single headline number or qualitative claim, plus a one-sentence outline of sections 2-N. | Top-tier puts the headline number in P5 — readers should be able to *quote one number after reading the Intro*. |

## The 4-paragraph compressed variant

Some shorter L1 papers (Nature Communications) use a 4-paragraph variant that merges P3 (gap) and P4 (what we do):

| ¶ | Role |
|---|---|
| P1 | Big problem |
| P2 | Why now |
| P3 | Gap + what we do |
| P4 | Headline contribution + outline |

## The 6-paragraph extended variant

Some L1 perspective / review papers (NCC, OE) use a 6-paragraph extended Intro that splits P1 (problem) into "physical / engineering stakes" + "policy / economic stakes":

| ¶ | Role |
|---|---|
| P1 | Physical / engineering stake |
| P2 | Policy / economic stake |
| P3 | Why now |
| P4 | Specific gap (debate or implicit-assumption) |
| P5 | What we do |
| P6 | Headline contribution + outline |

## Anti-patterns common in applied-paper Intros

These moves appear in the L2 candidate manifest (Applied Energy, AiAE) but are rare in L1:

- **Methods-dense P3 or P4** ("we develop a mixed-integer linear programming model that…"). Top-tier introductions delay method detail until §2.
- **Multiple headline numbers in one Intro** ("we find X is Y% lower, Z increases by W%, A drops by B%"). Top-tier picks one number per Intro.
- **"To the best of the authors' knowledge"** as the gap construction. Top-tier doesn't use this phrase; it names the debate or the unresolved tension directly.
- **Plant-level engineering description in P1** (e.g., "data centers consist of servers, cooling, and power conversion units…"). Top-tier assumes reader knows this; opens at policy-scale.

## Transferable template

Henry's Intro draft scaffold:

```
P1 — Big problem (sourced number; policy-relevant scale)
    "Global / China / EU {X target} requires {Y action} by {date}.
    Yet {observed gap or constraint}, citing {1 high-quality source}."

P2 — Why now (recent shift)
    "{Recent policy package / technological cost crossover / new dataset}
    has changed the calculation. Specifically {one-sentence shift}."

P3 — Specific gap (frame as debate or implicit-assumption)
    "The literature is divided on {question}: {camp A} argues {claim A};
    {camp B} argues {claim B}. The disagreement turns on
    {load-bearing assumption that has not been explicit}."

P4 — What we do (preview in plain terms)
    "Here we {identify | quantify | rank | resolve} {the load-bearing
    assumption} by {method or data, one short clause}, applied to
    {scope: case study, scenario set, region}."

P5 — Headline contribution
    "We find {one number with unit, year, scenario context}. This
    implies {one-sentence policy / system / industry consequence}.
    Section {N} {one-sentence per remaining section}."
```

## For Henry's SMR-DC paper (worked example)

```
P1 — "Decarbonized electricity systems through 2050 require ~X TWh
    of firm clean capacity in regions where VRE alone meets seasonal
    peaks (cite Duan 2022 NE)."

P2 — "Simultaneously, AI-driven data center electricity demand is
    projected to {Y} by 2030, with ~Z% potentially serving as
    flexible co-located load (cite Colangelo 2026 NE, Mytton 2022 J)."

P3 — "Whether SMRs and AI data centers should co-locate is debated:
    {camp A: SMR-as-grid-asset} argues SMRs serve the grid first;
    {camp B: SMR-as-anchor-customer} argues co-located demand
    de-risks SMR financing. The disagreement turns on whether the
    grid-flexibility benefit of SMR exceeds the customer-anchoring
    benefit at the relevant scale."

P4 — "Here we resolve this by jointly optimizing SMR deployment
    and DC siting under both framings, using a facility-pair
    capacity-expansion model + waste-heat-ORC integration, for
    {region X} in {year Y}."

P5 — "We find {Z} co-location pairs are economic under the customer-
    anchoring framing but only {W} under the grid-asset framing.
    This {implication}. Section 2 ... Section 3 ..."
```

## Confidence

**Low-medium (v0.1).** The role-sequence is induced from headlines + archetype data, not from systematic reading of all 22 §5 paragraph tables. v0.2 will refine after structured reads.

## Source papers (will populate v0.2)

22 L1 papers ingested as of 2026-05-11. Each has a `§5 Introduction structure (paragraph table)` section. v0.2 will mine these systematically.

## Henry's stance

<!-- HENRY-NOTE-START -->
<!-- Hand-edits here survive regenerator. Useful note: when Henry drafts an Intro, paste this skeleton into the draft as the first move. -->
<!-- HENRY-NOTE-END -->

## Related

- [[../../patterns/cross-cutting/methods-recurrent/option-value-scenario-pairs]] — P5 headlines often quote option-value deltas
- [[../../patterns/cross-cutting/methods-recurrent/plant-vs-aggregate-resolution]] — P4 method-preview signals resolution choice
- [[../../patterns/cross-cutting/methods-recurrent/additionality-counterfactuals]] — P3 gap-as-debate exemplar
