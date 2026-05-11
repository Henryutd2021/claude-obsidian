---
type: pattern
title: "Data-center load: shape, flexibility, and provenance"
created: 2026-05-11
updated: 2026-05-11
status: developing
supporting_papers_l1: 3
supporting_papers_l2: 0
pattern_category: subdomain
subdomain: ai-data-driven
tags:
  - pattern
  - subdomain
  - sd/ai-data-driven
  - sd/power-systems
---

# Data-center load: shape, flexibility, and provenance

> Subdomain pattern (`ai-data-driven`): a complete data-center energy paper needs three pillars: macroscale counterfactual on load shape, microscale field-trial on flexibility, and provenance audit of the input numbers being used.

## Pattern claim

The DC-load literature is fractured. Single-pillar papers get attacked on the missing pillars: "your counterfactual is wrong because your input estimates are wrong" (provenance pillar missing), "your scenario claims flexibility but no operational evidence" (field-trial pillar missing), "you measured one cluster but no system-level implications" (counterfactual pillar missing). L1-grade DC-load papers either cover all three pillars in one work or chain reference each other across the three pillars.

The three pillars and their L1 exemplars:

1. **Macroscale counterfactual / load-shape**: Zheng 2020 J: spatial load migration between US data centers absorbs wind/solar curtailment at near-zero marginal cost; counterfactual is "without migration, what happens to curtailment and emissions?"
2. **Microscale field-trial / flexibility**: Colangelo 2026 NE: 256-GPU Phoenix field trial, software workload orchestration cuts cluster power 25% for 3h while keeping QoS thresholds intact. The contribution is operational evidence, not modeling.
3. **Provenance audit / input quality**: Mytton & Ashtine 2022 J: review of 258 DC energy estimates across 46 publications and 676 source links; reliability is driven by provenance (private market data, broken links, vague methods, future extrapolation).

The three pillars stand in a specific argumentative order: provenance → counterfactual → field-trial. Provenance establishes which input numbers are trustworthy; counterfactual uses trustworthy inputs to claim a system-level outcome; field-trial provides operational evidence that the assumed flexibility is real.

## The recurring move (one-line)

A complete DC-load paper either does all three pillars itself, OR cites the work for the two pillars it doesn't do: never silently assumes them.

## Evidence (L1 papers supporting this pattern)

- [[2020-J-data-center-load-migration-curtailment]]: Evidence: spatial load migration between US DC sites absorbs curtailed renewables. Pillar: macroscale counterfactual. Lesson: counterfactual claims need an explicit "without migration" model, not just "we observed migration could happen".
- [[2026-NE-ai-data-centres-grid-interactive]]: Evidence: 256-GPU production cluster in Phoenix, 25% power cut for 3h with QoS intact. Pillar: field-trial flexibility. Lesson: field-trial evidence is the rarest currency in the DC-load literature; one well-documented field trial unlocks NE-grade venues.
- [[2022-J-data-center-energy-estimates-review]]: Evidence: provenance-audit meta-review tracing 676 source links. Pillar: provenance audit. Lesson: when the input estimates in your literature have unknown provenance, an audit is itself a primary contribution: and a paper without an audit but using poor-provenance inputs is at high reviewer risk.

## Counter-evidence (papers that depart from the pattern)

None yet in the L1 corpus. Any single-pillar DC paper that does not chain-reference the other two pillars would be a counter-example. Watch for Applied Energy / AiAE submissions in 2026 that focus only on one pillar.

## When this pattern works

- For any DC-load paper, period. The three pillars are necessary infrastructure for the argument to hold up.
- Especially when the paper makes claims about *future* DC load (where projection uncertainty dominates).

## When this pattern fails or feels formulaic

- For pure engineering papers about cooling systems, server efficiency, or chip-level energy where DC-load aggregation isn't the contribution. Single-pillar (e.g., experimental) is fine.

## Transferable template (for Henry's drafts)

```
For an SMR-DC paper that makes DC-load claims:

  Pillar 1 (provenance, must do or cite): which DC energy estimates
    am I using? What is each estimate's source? Quote Mytton 2022 J
    as the audit foundation. Annotate every load number with its
    provenance class (private market data, public reporting,
    extrapolated, modeled).

  Pillar 2 (counterfactual, must do): what does the SMR-DC pairing
    do for the grid versus grid-supplied-DC? Use a paired-scenario
    construction (with-SMR vs grid-supplied) and report system-level
    cost / emissions / curtailment-absorption deltas.

  Pillar 3 (field-trial / flexibility, must cite or scope-limit): if
    Henry's paper claims demand-side flexibility for the DC, cite
    Colangelo 2026 NE for operational evidence. If it doesn't claim
    flexibility, state that explicitly to avoid implicit assumption.
```

## Confidence

**High.** 3 L1 papers each clearly occupying one pillar, with reciprocal cross-references already documented in [[2020-J-data-center-load-migration-curtailment]] (cross-refs to Che 2025 J for threshold-based system TEA, Kikstra 2021 NE for demand-side framing, Giovanniello 2024 NE for hourly grid-emissions framing).

## Henry's stance

<!-- HENRY-NOTE-START -->
*Direct relevance to Henry's SMR-DC paper. The three pillars are a checklist - if Henry submits an SMR-DC paper to NE / Joule that lacks one of the pillars or fails to cite it, reviewers will flag immediately.*
<!-- HENRY-NOTE-END -->

## Related patterns

- [[../../cross-cutting/methods-recurrent/option-value-scenario-pairs]]: Zheng's with-migration / without-migration is an option-value pair
- [[../../cross-cutting/archetype/firm-clean-flexible-baseload]]: DC + SMR is a firm-clean + flexible-load combination
- [[../../../bridges/energy-policy-economics--integrated-energy-systems]]

## Promoted from

`wiki/hot.md` cross-paper anchor `patterns/data-center/load-shape-and-flexibility` (3 supporting papers, 2026-05-11).
