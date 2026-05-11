---
type: meta
title: "Ingest routing rules (which downstream pages get updated per role/depth)"
updated: 2026-05-11
tags:
  - meta
  - vocab
  - policy
status: evergreen
related:
  - "[[journal-role-vocab]]"
  - "[[depth-policy]]"
  - "[[subdomain-vocab]]"
---

# Ingest routing rules

When a paper is ingested, the codex contract is **aware of which downstream pages it should update** based on `(journal_role, ingest_depth)`. The contract receipt records the actual `pages_updated[]` array; `/wiki-lint` audits routing.

## Routing matrix

| Source | Always updates | Conditionally updates |
|---|---|---|
| **L1-A** (`top_journal_exemplar, A_deep`) | `papers/L1/{slug}.md` <br> `subdomains/{primary[0]}.md` (paper list) <br> `subdomains/{primary[1]}.md` if present <br> `log.md` <br> `hot.md` <br> `index.md` (Papers ingested) <br> `papers.base` (auto via Bases) | `patterns/cross-cutting/{intro,figure,discussion,archetype,contribution}/*` (if a recurring pattern is reinforced) <br> `patterns/cross-cutting/methods-recurrent/*` (if methodology is shared) <br> `patterns/comparisons/*` (if a comparable L2 exists for the same topic) <br> `playbook/top-journal-craft/*` <br> `bridges/{A}--{B}.md` (if 3+ papers span the pair) |
| **L2-A** (`applied_flagship, A_deep`) | `papers/L2/{primary[0]}/{slug}.md` <br> `subdomains/{primary[0]}.md` <br> `subdomains/{primary[1]}.md` if present <br> `banks/parameter-bank/*` (Parameter Card → bank rows) <br> `banks/sensitivity-bank/*` (Sensitivity section → bank rows) <br> `banks/method-bank/*` (Method Card → bank rows) <br> `log.md` <br> `hot.md` <br> `index.md` <br> `papers.base` | `patterns/subdomain/{primary[0]}/*` (subdomain-specific patterns) <br> `patterns/cross-cutting/methods-recurrent/*` (shared methodology) <br> `patterns/comparisons/*` (top-vs-applied delta) <br> `playbook/applied-paper-craft/*` <br> `playbook/upgrade-playbook/*` <br> `bridges/{A}--{B}.md` (if 3+ papers span the pair) <br> `banks/case-study-bank/*`, `banks/figure-bank/*`, `banks/results-bank/*` (Phase 4 — once the banks exist) |
| **L2-B** (`applied_flagship, B_medium`) | `papers/L2/{primary[0]}/{slug}.md` <br> `log.md` | `banks/parameter-bank/*` (if a novel parameter is extracted) <br> `subdomains/{primary[0]}.md` paper list only |
| **L2-C** (`applied_flagship, C_light`) | `papers/L2/{primary[0]}/{slug}.md` (small card) <br> `log.md` | citation index only |
| **Manual L3 entry** (`technical_support`) | `banks/{relevant-bank}/*` (Henry adds the row manually) <br> Zotero tag `tpl:role/technical_support` | none — no paper-analysis page generated |
| **Comparison promotion** (`comparison_control`) | `patterns/comparisons/{slug}.md` | none — reserved use |

## Receipt schema addition

The codex contract receipt (`.raw/papers/{KEY}/codex-receipt.json`) must include:

```json
{
  "pages_updated": [
    "wiki/papers/L2/hydrogen-p2x/2024-AE-example.md",
    "wiki/subdomains/hydrogen-p2x.md",
    "wiki/banks/parameter-bank/electrolyzer-capex.md",
    "wiki/banks/method-bank/lcoh-calculation.md"
  ],
  "pages_skipped": [
    {
      "path": "wiki/banks/sensitivity-bank/*",
      "reason": "paper did not include explicit sensitivity table"
    }
  ]
}
```

`/wiki-lint` cross-checks `pages_updated[]` against the routing matrix above and flags missing required-pages.

## Bridge emergence trigger

After every ingest, the codex contract (or post-ingest hook) recomputes bridge participation:

1. For the new paper, enumerate every pair `(A, B)` from `subdomain_primary ∪ subdomain_secondary`.
2. For each pair, count papers in the lab listing both A and B.
3. If count == 3 and `wiki/bridges/{A}--{B}.md` does not exist, create a stub via `_templates/bridge-page.md` and notify in `log.md`.
4. If count > 3 and the bridge page exists, just append the new paper to its supporting-papers list.

## No-pollution rule (lint)

L1-only patterns must NOT cite L2 as primary evidence:
- `patterns/cross-cutting/intro/*`
- `patterns/cross-cutting/figure/*`
- `patterns/cross-cutting/discussion/*`
- `patterns/cross-cutting/archetype/*`
- `patterns/cross-cutting/contribution/*`
- `playbook/top-journal-craft/*`

L2 papers may appear in:
- `patterns/cross-cutting/methods-recurrent/*` (as supplementary, marked)
- `patterns/comparisons/*` (as the contrast case)
- `patterns/subdomain/{slug}/*` (as primary or supplementary)
- `patterns/bridges/{A}--{B}/*` (as primary or supplementary)
- `playbook/applied-paper-craft/*`, `playbook/upgrade-playbook/*`, `playbook/submission-tier-checklists/*`
