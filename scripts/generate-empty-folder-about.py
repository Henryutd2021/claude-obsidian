#!/usr/bin/env python3
"""Generate `_about.md` navigation stubs in every currently-empty wiki
folder. Each stub explains: what the folder holds, why it's empty now,
what triggers it filling, and where the source-of-truth lives.

Idempotent: skips folders that already have an `_about.md`.

Filename choice: `_about.md` (not README.md) because the vault's
`.obsidian/app.json` has `README.md` in `userIgnoreFilters`: those
files would be invisible to Obsidian. Underscore prefix also sorts the
nav stub to the top of the folder listing.
"""

import re
from pathlib import Path

VAULT = Path("/Users/henry/Library/Mobile Documents/iCloud~md~obsidian/Documents/claude-obsidian")
WIKI = VAULT / "wiki"

# folder relative-to-wiki -> (title, purpose, fills_when, trigger, sot_link)
SPECS = {
    # ── banks ─────────────────────────────────────────────────────────
    "banks/parameter-bank": (
        "Parameter bank",
        "Parameter values (CAPEX, OPEX, capacity factors, efficiencies, lifetimes, discount rates, learning rates, carbon prices, etc.) extracted from L2-A ingests, supplemented by manual L3 entries. One `.md` per parameter category (e.g. `electrolyzer-capex.md`, `pv-capacity-factor.md`).",
        "When the first L2-A ingest produces a Parameter Card.",
        "An L2-A codex run finishes and the orchestrator merges `bank-candidates.md` parameter rows into this folder. Also: Henry manually adds rows from technical-support (L3) papers.",
        "[[_meta/routing-rules]] section L2-A row.",
    ),
    "banks/sensitivity-bank": (
        "Sensitivity bank",
        "Sensitivity-analysis design patterns extracted from L2-A ingests. One `.md` per scenario-design topic (e.g. `green-hydrogen-tea-sensitivity-variables.md`, `discount-rate-capex-sensitivity.md`).",
        "When the first L2-A ingest produces a Sensitivity row.",
        "Routing rules for L2-A include `wiki/banks/sensitivity-bank/*`.",
        "[[_meta/routing-rules]]",
    ),
    "banks/method-bank": (
        "Method bank",
        "Reusable model components and method recipes extracted from L2-A ingests. One `.md` per method (e.g. `milp-energy-systems.md`, `lcoh-calculation.md`).",
        "When the first L2-A ingest produces a Method Card.",
        "Routing rules for L2-A include `wiki/banks/method-bank/*`.",
        "[[_meta/routing-rules]]",
    ),

    # ── papers/L2 ────────────────────────────────────────────────────
    "papers/L2/_cross": (
        "L2 _cross folder",
        "L2 (`applied_flagship`) papers that span 3+ subdomains as primary. Rare in practice: usually a perspective / cross-disciplinary synthesis. Most L2 papers land in a single subdomain folder.",
        "When a Phase 2+ L2 ingest produces a paper with `len(subdomain_primary) >= 3` AND no subdomain is a clear dominant.",
        "`scripts/codex-ingest-paper-L2.sh <KEY> <ADDR> <SLUG> A_deep _cross`.",
        "[[_meta/subdomain-vocab]] (rules for cross-subdomain papers).",
    ),
    "papers/L2/integrated-energy-systems": (
        "L2 / integrated-energy-systems",
        "L2 papers whose `subdomain_primary[0] == integrated-energy-systems` (TEA, multi-energy, system-level optimization).",
        "When Henry picks an Applied Energy / AiAE / ECM / RSER / RE paper in this subdomain and runs the L2 ingest.",
        "`scripts/codex-ingest-paper-L2.sh <KEY> <ADDR> <SLUG> <DEPTH> integrated-energy-systems`.",
        "[[subdomains/integrated-energy-systems]].",
    ),
    "papers/L2/power-systems": (
        "L2 / power-systems",
        "L2 papers whose `subdomain_primary[0] == power-systems` (grid integration, microgrid, dispatch, markets).",
        "When Henry picks an Applied Energy / IEEE-TSG / RE / RSER paper in this subdomain and runs the L2 ingest.",
        "`scripts/codex-ingest-paper-L2.sh <KEY> <ADDR> <SLUG> <DEPTH> power-systems`.",
        "[[subdomains/power-systems]].",
    ),
    "papers/L2/hydrogen-p2x": (
        "L2 / hydrogen-p2x",
        "L2 papers whose `subdomain_primary[0] == hydrogen-p2x` (H2, P2X, fuel cells, electrolyzers, LDS).",
        "When Henry picks an Applied Energy / IJHE / J. Energy Storage paper in this subdomain and runs the L2 ingest.",
        "`scripts/codex-ingest-paper-L2.sh <KEY> <ADDR> <SLUG> <DEPTH> hydrogen-p2x`.",
        "[[subdomains/hydrogen-p2x]].",
    ),
    "papers/L2/re-tech-resources": (
        "L2 / re-tech-resources",
        "L2 papers whose `subdomain_primary[0] == re-tech-resources` (solar, wind, resource assessment).",
        "When Henry picks an RE / Solar Energy / Wind Energy paper in this subdomain and runs the L2 ingest.",
        "`scripts/codex-ingest-paper-L2.sh <KEY> <ADDR> <SLUG> <DEPTH> re-tech-resources`.",
        "[[subdomains/re-tech-resources]].",
    ),
    "papers/L2/building-urban": (
        "L2 / building-urban",
        "L2 papers whose `subdomain_primary[0] == building-urban` (building energy, building decarb, urban energy systems).",
        "When Henry picks an Energy & Buildings / Applied Thermal Eng. paper and runs the L2 ingest.",
        "`scripts/codex-ingest-paper-L2.sh <KEY> <ADDR> <SLUG> <DEPTH> building-urban`.",
        "[[subdomains/building-urban]].",
    ),
    "papers/L2/energy-policy-economics": (
        "L2 / energy-policy-economics",
        "L2 papers whose `subdomain_primary[0] == energy-policy-economics` (markets, transitions, finance).",
        "When Henry picks an Energy Policy / Energy Research & Social Science paper and runs the L2 ingest.",
        "`scripts/codex-ingest-paper-L2.sh <KEY> <ADDR> <SLUG> <DEPTH> energy-policy-economics`.",
        "[[subdomains/energy-policy-economics]].",
    ),
    "papers/L2/lca-sustainability": (
        "L2 / lca-sustainability",
        "L2 papers whose `subdomain_primary[0] == lca-sustainability` (LCA, emissions, sustainability assessment).",
        "When Henry picks an Applied Energy / J. Cleaner Production paper in this subdomain and runs the L2 ingest.",
        "`scripts/codex-ingest-paper-L2.sh <KEY> <ADDR> <SLUG> <DEPTH> lca-sustainability`.",
        "[[subdomains/lca-sustainability]].",
    ),
    "papers/L2/ai-data-driven": (
        "L2 / ai-data-driven",
        "L2 papers whose `subdomain_primary[0] == ai-data-driven` (papers *about* AI/ML/data-driven energy methods; data-center load papers).",
        "When Henry picks an Applied Energy / IEEE-TSG / AiAE paper in this subdomain and runs the L2 ingest.",
        "`scripts/codex-ingest-paper-L2.sh <KEY> <ADDR> <SLUG> <DEPTH> ai-data-driven`.",
        "[[subdomains/ai-data-driven]].",
    ),

    # ── patterns/cross-cutting (the 4 empty L1-only categories) ──────
    "patterns/cross-cutting/intro": (
        "patterns / cross-cutting / intro",
        "Patterns about Introduction architecture in top-tier energy papers (paragraph roles, gap-construction moves, headline-number placement).",
        "When a recurring Intro move is identified across 3+ L1 papers AND can be formalized as a transferable template.",
        "Sourced from §5 Introduction paragraph tables of the L1 papers. Currently captured at higher level in [[playbook/top-journal-craft/intro-template-energy-papers]]: split into per-pattern pages here when v0.2 of that playbook refines the moves.",
        "[[playbook/top-journal-craft/intro-template-energy-papers]].",
    ),
    "patterns/cross-cutting/figure": (
        "patterns / cross-cutting / figure",
        "Patterns about main-figure design in top-tier energy papers (mechanism-diagram-as-Fig-1, headline-number-home, sensitivity-figure rules, color-as-argument).",
        "When a recurring figure move is identified across 3+ L1 papers.",
        "Sourced from §10 figure argument-function tables. Currently captured at higher level in [[playbook/top-journal-craft/main-figure-design-rules]]; per-pattern splits land here later. **L2 contrast** (which figure styles signal applied-paper vs top-journal) will fill this folder after L2 pilots.",
        "[[playbook/top-journal-craft/main-figure-design-rules]].",
    ),
    "patterns/cross-cutting/discussion": (
        "patterns / cross-cutting / discussion",
        "Patterns about Discussion elevation in top-tier energy papers (how a result is lifted from engineering implication to system / policy implication).",
        "When a recurring Discussion move is identified across 3+ L1 papers. Pure L1 evidence (no L2) per the no-pollution rule.",
        "Sourced from §11 Discussion sections of L1 papers. Not yet drafted: will fill when a /wiki-query or fold synthesis surfaces a recurring move.",
        "[[../../../_meta/routing-rules]] no-pollution rule.",
    ),
    "patterns/cross-cutting/contribution": (
        "patterns / cross-cutting / contribution",
        "Patterns about contribution framing in top-tier energy papers (how contribution claims are constructed: system-boundary expansion, endogeneization, counterintuitive result, etc.).",
        "When a recurring contribution-framing move is identified across 3+ L1 papers.",
        "Currently captured at higher level in [[playbook/top-journal-craft/contribution-decision-tree]]; per-pattern pages here later. Pure L1 evidence (no L2).",
        "[[playbook/top-journal-craft/contribution-decision-tree]].",
    ),

    # ── patterns/subdomain (5 untouched subdomains) ──────────────────
    "patterns/subdomain/integrated-energy-systems": (
        "patterns / subdomain / integrated-energy-systems",
        "Patterns specific to multi-energy / TEA / system-optimization work.",
        "When 3+ L1+L2 papers in `integrated-energy-systems` share a recurring move.",
        "13 L1 papers currently in this subdomain (mostly via secondary). Candidate move: scenario-pair design at system-level (see [[../../cross-cutting/methods-recurrent/option-value-scenario-pairs]] for the cross-cutting form). Will split into per-pattern pages here when L2 lands and gives the subdomain-specific contrast.",
        "[[subdomains/integrated-energy-systems]].",
    ),
    "patterns/subdomain/power-systems": (
        "patterns / subdomain / power-systems",
        "Patterns specific to grid integration / dispatch / market work.",
        "When 3+ L1+L2 papers in `power-systems` share a recurring move.",
        "9 L1 papers currently in this subdomain. Candidate moves: flexibility parameter on firm-clean assets (see [[../../cross-cutting/archetype/firm-clean-flexible-baseload]]). Will split here when L2 lands.",
        "[[subdomains/power-systems]].",
    ),
    "patterns/subdomain/energy-policy-economics": (
        "patterns / subdomain / energy-policy-economics",
        "Patterns specific to policy / economics / market design / transitions work.",
        "When 3+ L1+L2 papers in `energy-policy-economics` share a recurring move.",
        "15 L1 papers currently in this subdomain (mostly via secondary). Candidate: meta-analysis-as-contribution patterns. Will fill when L2 lands.",
        "[[subdomains/energy-policy-economics]].",
    ),
    "patterns/subdomain/lca-sustainability": (
        "patterns / subdomain / lca-sustainability",
        "Patterns specific to LCA / emissions inventory / sustainability work.",
        "When 3+ L1+L2 papers in `lca-sustainability` share a recurring move.",
        "10 L1 papers currently in this subdomain (mostly via secondary). Candidate: inventory-correction-as-contribution. Will fill when L2 lands.",
        "[[subdomains/lca-sustainability]].",
    ),
    "patterns/subdomain/building-urban": (
        "patterns / subdomain / building-urban",
        "Patterns specific to building / urban energy work.",
        "When 3+ L1+L2 papers in `building-urban` share a recurring move.",
        "Smallest subdomain (2 L1 papers). Premature for pattern emergence at L1 alone; this folder fills only after several L2 ingests in `building-urban`.",
        "[[subdomains/building-urban]].",
    ),

    # ── patterns/bridges and comparisons ─────────────────────────────
    "patterns/bridges": (
        "patterns / bridges",
        "Patterns specific to a subdomain interface (e.g., what recurs at `hydrogen-p2x × power-systems`). Different from `wiki/bridges/` which holds the per-pair index page; this folder holds the *patterns* identified at those interfaces.",
        "When a bridge page in `wiki/bridges/` accumulates 3+ papers AND a recurring move is identifiable at the interface (not just inside either subdomain).",
        "Promoted from a `/wiki-query` or fold synthesis that surfaces a recurring interface move.",
        "[[bridges]] for the per-pair index pages.",
    ),
    "patterns/comparisons": (
        "patterns / comparisons",
        "**Top-vs-applied delta library.** The key piece for Henry's writing-level improvement. Each `.md` here captures one delta between an L1 paper and a comparable L2 paper on the same topic: framing diff, scope diff, narrative diff, figure-stack diff.",
        "After the first L2-A ingest pairs with an L1 paper on the same topic.",
        "Routing rules for L1 and L2-A both list `patterns/comparisons/*` as conditional update target.",
        "[[_meta/routing-rules]].",
    ),

    # ── playbook (3 empty subfolders + projects) ─────────────────────
    "playbook/applied-paper-craft": (
        "playbook / applied-paper-craft",
        "How to write Applied-Energy-grade papers: model rigor, system boundary, parameter justification, case-study justification, sensitivity design, engineering feasibility, results presentation.",
        "After L2 ingest accumulates enough that recurring applied-paper moves can be templated.",
        "Routing for L2-A ingest lists `playbook/applied-paper-craft/*` as a conditional update target.",
        "[[_meta/routing-rules]].",
    ),
    "playbook/upgrade-playbook": (
        "playbook / upgrade-playbook",
        "How to upgrade an L2-style paper to L1 framing: framing reshape, scope expansion, narrative compression, figure-stack reduction, Discussion elevation.",
        "After `patterns/comparisons/*` has 3+ pages so the upgrade moves can be generalized.",
        "Routing for L2-A ingest lists `playbook/upgrade-playbook/*` as conditional.",
        "[[_meta/routing-rules]].",
    ),
    "playbook/submission-tier-checklists": (
        "playbook / submission-tier-checklists",
        "Per-journal readiness checklists (Nature Energy, Joule, Nature Communications, Applied Energy, Advances in Applied Energy, ECM, etc.). Each `.md` lists what a manuscript needs to clear the target journal's bar.",
        "Phase 5 (~month 6). Requires both L1+L2 corpus + `patterns/comparisons/*` to be substantial.",
        "Manual drafting + cross-referencing patterns/comparisons.",
        "Plan section 14.",
    ),
    "projects": (
        "projects",
        "Henry's own manuscripts in progress. Each `.md` is one paper draft + working notes. The wiki's deepest output: Henry consults patterns/playbook/banks while drafting here.",
        "When Henry starts a new manuscript.",
        "Henry creates `wiki/projects/{slug}.md` manually. The /wiki-query skill reads from here when asking about Henry's current drafts.",
        "[[index]] for navigation.",
    ),
}


def render_about(folder: str, title: str, purpose: str, fills_when: str, trigger: str, sot: str) -> str:
    lines = []
    lines.append("---")
    lines.append("type: folder-about")
    lines.append(f'title: "About: {title}"')
    lines.append("updated: 2026-05-11")
    lines.append("tags:")
    lines.append("  - meta")
    lines.append("  - folder-about")
    lines.append("status: living")
    lines.append("---")
    lines.append("")
    lines.append(f"# About: `{folder}/`")
    lines.append("")
    lines.append(f"_This folder is currently empty. This `_about.md` explains why and what triggers it filling._")
    lines.append("")
    lines.append("## Purpose")
    lines.append("")
    lines.append(purpose)
    lines.append("")
    lines.append("## When it fills")
    lines.append("")
    lines.append(fills_when)
    lines.append("")
    lines.append("## Trigger")
    lines.append("")
    lines.append(trigger)
    lines.append("")
    lines.append("## Source of truth")
    lines.append("")
    lines.append(sot)
    lines.append("")
    return "\n".join(lines)


def main():
    written, skipped = [], []
    for rel, (title, purpose, fills_when, trigger, sot) in SPECS.items():
        folder = WIKI / rel
        folder.mkdir(parents=True, exist_ok=True)
        out = folder / "_about.md"
        if out.exists():
            skipped.append(str(out.relative_to(VAULT)))
            continue
        out.write_text(render_about(rel, title, purpose, fills_when, trigger, sot))
        written.append(str(out.relative_to(VAULT)))

    print(f"Wrote {len(written)} _about.md stubs:")
    for w in written:
        print(f"  + {w}")
    if skipped:
        print(f"\nSkipped {len(skipped)} (already exists):")
        for s in skipped:
            print(f"  - {s}")


if __name__ == "__main__":
    main()
