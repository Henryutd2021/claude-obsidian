---
type: meta
title: "Journal-role controlled vocabulary"
updated: 2026-05-11
tags:
  - meta
  - vocab
status: evergreen
related:
  - "[[subdomain-vocab]]"
  - "[[depth-policy]]"
  - "[[routing-rules]]"
---

# journal_role — controlled vocabulary

The `journal_role` frontmatter field on every paper-analysis page takes one of these four values. **Roles are functional, not a quality hierarchy.** L1 teaches cross-domain craft (problem framing, contribution, top-journal narrative). L2 teaches subdomain-specific technical rigor (model, parameters, case studies, sensitivity). The two are read together by Henry, never substituted.

## Values

| Slug | What it covers |
|---|---|
| `top_journal_exemplar` | Top-tier multi-disciplinary or flagship energy journals where field-level papers are published. |
| `applied_flagship` | Applied/technical flagship journals where rigorous engineering and TEA work is published. |
| `technical_support` | Niche / technical journals used as parameter / formula / data sources. **Manual entry only — not on the codex automated track.** |
| `comparison_control` | Papers explicitly held as a baseline for top-vs-applied comparisons (rare). |

## Journal → role mapping (lock list)

### top_journal_exemplar
- Nature
- Nature Energy
- Joule
- Nature Communications
- Nature Climate Change
- Nature Sustainability
- One Earth
- Energy & Environmental Science
- Science
- Science Advances
- PNAS
- Cell Reports Physical Science *(borderline; map to top tier unless content is clearly applied)*
- iScience *(borderline; same rule)*

### applied_flagship
- Applied Energy
- Advances in Applied Energy
- Energy Conversion and Management
- Renewable & Sustainable Energy Reviews
- Renewable Energy
- Energy & Buildings
- Energy
- Energy Policy
- Energy Research & Social Science
- Energy Strategy Reviews
- Sustainable Production and Consumption
- Sustainable Energy Technologies and Assessments
- Sustainable Energy & Fuels *(if technical methods)*

### technical_support (manual-only)
- International Journal of Hydrogen Energy
- Journal of Energy Storage
- Applied Thermal Engineering
- Solar Energy
- Wind Energy
- Wind Engineering
- Journal of Power Sources
- Journal of Cleaner Production *(LCA-heavy)*
- IEEE Transactions on Smart Grid
- IEEE Transactions on Power Systems
- IEEE Transactions on Sustainable Energy
- Electric Power Systems Research
- Smart Grid

### comparison_control
- Reserved. Use only when a specific paper is explicitly held against an L1 paper for comparison purposes in `wiki/patterns/comparisons/`.

## Rules

1. **Role is set per paper, not per journal in absolute.** A Cell Reports Physical Science paper that is clearly engineering can be `applied_flagship`; one that is clearly cross-domain framing can be `top_journal_exemplar`. The journal column above is the **default**; Henry can override per-paper with a one-line `journal_role_note:` in the page.
2. **`technical_support` is manual-only.** No codex contract generates `technical_support` pages. Technical-support papers contribute as rows in `wiki/banks/*` pages with a Zotero citation; no paper-analysis page exists.
3. **Promotion path** (L2 → L1): an L2-A paper cited 3+ times across pattern pages auto-flags for L1 re-ingest under the full 18-section template. The address persists; the page is rewritten under `wiki/papers/L1/{slug}.md` and removed from `wiki/papers/L2/{primary}/`.
4. **No L1-pollution rule** (lint-enforced): pattern pages in `patterns/cross-cutting/{intro,figure,discussion,archetype,contribution}/` and `playbook/top-journal-craft/` must NOT cite L2 papers as **primary** evidence. L2 appears in `patterns/comparisons/` and `patterns/cross-cutting/methods-recurrent/` as supplementary / contrast evidence.

## When the lock list needs to change

If Henry adds a paper from a journal not listed here, append it to the relevant section above and bump `updated:` in this file's frontmatter. The journal-role-vocab file is the single source of truth for what counts as L1 vs L2.
