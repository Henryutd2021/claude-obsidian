---
type: meta
title: "Ingest depth policy (A_deep / B_medium / C_light)"
updated: 2026-05-11
tags:
  - meta
  - vocab
  - policy
status: evergreen
related:
  - "[[journal-role-vocab]]"
  - "[[subdomain-vocab]]"
---

# ingest_depth — A_deep / B_medium / C_light

The `ingest_depth` frontmatter field is **orthogonal** to `journal_role`. It controls *how thoroughly* a paper is analyzed, independent of which corpus it belongs to.

## Values

| Depth | Template | Page size | Approx codex cost |
|---|---|---|---|
| `A_deep` | Full L1 18-section OR L2-A 10-section | 12-35 KB | ~$2.5-5 |
| `B_medium` | L2-B one-page summary | 4-6 KB | ~$1 |
| `C_light` | L2-C citation marker | <500 B | ~$0.1 |

## Selection rules by `journal_role`

### L1 (top_journal_exemplar)
**Always `A_deep`.** L1 papers are why the lab exists. No B or C tier for L1.

### L2 (applied_flagship)

Choose depth at ingest time based on three signals. If 2+ "yes" → `A_deep`. If 1 "yes" → `B_medium`. If 0 → `C_light`.

| Signal | Yes if |
|---|---|
| Direct method reuse | Paper's model, formulation, or case design is something Henry plans to adapt for `wiki/projects/` within 6 months |
| Parameter / case anchor | Paper is the canonical source for a specific parameter (electrolyzer CAPEX in region X, COP curve for type Y) or a canonical case-study justification |
| Subdomain coverage need | Paper's subdomain has <5 ingested L2 papers and Henry wants the bench filled |

**Default if uncertain**: `B_medium`. Easy to promote later via re-ingest; hard to justify a $2.5 deep dive that lands on a B-grade paper.

### L3 (technical_support)
**Manual entry only — no automated depth tier.** Technical-support papers contribute as rows in `wiki/banks/*` pages with the Zotero citation. No paper-analysis page is created. If a technical-support paper becomes important enough to warrant a full page, promote it to L2 by changing its `journal_role` and re-ingesting at B_medium or A_deep.

## Promotion / demotion

- **Promote L2-C → L2-B** if the paper later gets cited 2+ times across pattern pages.
- **Promote L2-B → L2-A** if Henry decides to migrate the paper's method or case to a `wiki/projects/` manuscript.
- **Promote L2-A → L1** if the paper is cited 3+ times across `patterns/cross-cutting/*` AND its archetype is judged transferable to a Joule/NE submission. Trigger the `/wiki-ingest` skill with the L1 contract; the page is rewritten under `wiki/papers/L1/{slug}.md`. Address persists.
- **Demote L1 → L2-A** is rare. Only if a paper turns out to be far less significant than initially thought (e.g., later retraction or controversy makes its framing unreliable). Move to `wiki/papers/L2/{primary-subdomain}/`. Address persists.

## Codex contract routing

| `(journal_role, ingest_depth)` | Contract | Script |
|---|---|---|
| `top_journal_exemplar, A_deep` | `_templates/codex-ingest-contract-L1.md` | `scripts/codex-ingest-paper.sh` (existing) |
| `applied_flagship, A_deep` | `_templates/codex-ingest-contract-L2-A.md` | `scripts/codex-ingest-paper-L2.sh A_deep` |
| `applied_flagship, B_medium` | `_templates/codex-ingest-contract-L2-B.md` | `scripts/codex-ingest-paper-L2.sh B_medium` |
| `applied_flagship, C_light` | `_templates/codex-ingest-contract-L2-C.md` | `scripts/codex-ingest-paper-L2.sh C_light` |
| `technical_support, *` | (no contract — manual bank row only) | n/a |
| `comparison_control, *` | reserved | n/a |

## Routing of downstream updates

See `wiki/_meta/routing-rules.md` for the table of which pages get updated when a paper of each `(role, depth)` is ingested.
