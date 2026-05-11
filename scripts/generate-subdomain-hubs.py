#!/usr/bin/env python3
"""Generate the 8 wiki/subdomains/{slug}.md hub pages from L1 paper
frontmatter. Each hub gets:

- An auto-generated intro (hardcoded per-subdomain text, plus stats line)
- Auto-generated paper list grouped by year DESC
- Auto-generated outward bridges sorted by strength
- Placeholder sections for subdomain patterns and bank pages (Phase 3+)

Re-runnable: regenerates from current frontmatter. Hand edits to a hub
page are preserved only if you put them between
`<!-- HENRY-NOTE-START -->` and `<!-- HENRY-NOTE-END -->` markers, which
the generator splices through unchanged.
"""

import re
import sys
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path

VAULT = Path("/Users/henry/Library/Mobile Documents/iCloud~md~obsidian/Documents/claude-obsidian")
PAPERS = VAULT / "wiki" / "papers"
SUBDOMAINS_DIR = VAULT / "wiki" / "subdomains"

SUBDOMAIN_INTROS = {
    "integrated-energy-systems": (
        "Multi-vector energy system modeling (electricity + heat + gas + transport), "
        "techno-economic analysis (TEA), and system-level optimization. The catch-all "
        "subdomain for system-level work combining 3+ vectors. If a paper is system-level "
        "but really about one vector, prefer the more specific subdomain."
    ),
    "power-systems": (
        "Electricity systems, smart grid, RE-grid integration, microgrid, dispatch and "
        "market design, grid stability and reliability. Spans capacity expansion, unit "
        "commitment, OPF, market simulation, flexibility resources."
    ),
    "hydrogen-p2x": (
        "Hydrogen and Power-to-X systems, fuel cells, electrolyzers, hydrogen-based "
        "long-duration storage, ammonia, e-fuels. The most actively bridging subdomain "
        "in the lab: most H2 papers also feed power-systems or energy-policy-economics."
    ),
    "re-tech-resources": (
        "Solar, wind, and other RE technology and resource assessment. Capacity factor "
        "modeling, plant-level / site-level resource analysis, supply-chain costs of RE "
        "hardware. Cross-cuts with hydrogen-p2x (RE → H2) and power-systems (RE → grid)."
    ),
    "building-urban": (
        "Building energy efficiency, building decarbonization (residential and commercial), "
        "urban energy systems and district energy, heat pumps. Smallest subdomain in the "
        "current lab — only 2 L1 papers; deliberate L2 expansion target."
    ),
    "energy-policy-economics": (
        "Energy economics, policy, market design, socio-technical transitions, investment "
        "and finance. Often the secondary subdomain on papers whose primary contribution "
        "is technical but whose framing claims policy relevance."
    ),
    "lca-sustainability": (
        "Life-cycle assessment, carbon emissions inventory and accounting, environmental "
        "impact, sustainability assessment. Used as primary subdomain for inventory and "
        "LCA papers; as secondary when a technical paper makes carbon-mitigation claims."
    ),
    "ai-data-driven": (
        "Papers whose subject matter is AI / ML / data-driven methods *for* energy systems "
        "(not just papers that happen to use a neural network as a tool). Data center "
        "papers live here because the load source is AI/data infrastructure."
    ),
}

ORDER = list(SUBDOMAIN_INTROS.keys())  # canonical order


def parse_frontmatter(text: str) -> dict:
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return {}
    end_idx = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end_idx = i
            break
    if end_idx is None:
        return {}
    out = {}
    current_key = None
    list_buffer = None
    for raw in lines[1:end_idx]:
        line = raw.rstrip()
        m_item = re.match(r"^\s+-\s+(.+)$", line)
        if m_item and current_key is not None and list_buffer is not None:
            list_buffer.append(m_item.group(1).strip().strip('"').strip("'"))
            continue
        if current_key is not None and list_buffer is not None:
            out[current_key] = list_buffer
            current_key = None
            list_buffer = None
        m_kv = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", line)
        if m_kv:
            k = m_kv.group(1)
            v = m_kv.group(2).strip()
            if v == "" or v == "[]":
                current_key = k
                list_buffer = []
                if v == "[]":
                    out[k] = []
                    current_key = None
                    list_buffer = None
            elif v.startswith("[") and v.endswith("]"):
                items = [x.strip().strip('"').strip("'") for x in v[1:-1].split(",") if x.strip()]
                out[k] = items
            else:
                out[k] = v.strip().strip('"').strip("'")
    if current_key is not None and list_buffer is not None:
        out[current_key] = list_buffer
    return out


def gather_papers():
    papers = []
    for path in sorted(PAPERS.rglob("*.md")):
        if path.name.startswith("."):
            continue
        try:
            text = path.read_text()
        except Exception:
            continue
        fm = parse_frontmatter(text)
        if "journal_role" not in fm:
            continue
        primary = fm.get("subdomain_primary") or []
        secondary = fm.get("subdomain_secondary") or []
        if isinstance(primary, str):
            primary = []
        if isinstance(secondary, str):
            secondary = []
        papers.append({
            "slug": path.stem,
            "role": fm.get("journal_role", ""),
            "depth": fm.get("ingest_depth", ""),
            "primary": primary,
            "secondary": secondary,
            "all": primary + secondary,
            "year": fm.get("year", ""),
            "journal": fm.get("journal", ""),
            "title": fm.get("title", ""),
            "address": fm.get("address", ""),
            "rel_path": str(path.relative_to(VAULT)),
        })
    return papers


def bridge_counts(papers):
    counts = Counter()
    pair_papers = defaultdict(list)
    for p in papers:
        sds = sorted(set(p["all"]))
        for a, b in combinations(sds, 2):
            counts[(a, b)] += 1
            pair_papers[(a, b)].append(p["slug"])
    return counts, pair_papers


def preserve_henry_note(existing_text: str) -> str:
    """If a hub page already has a Henry-note block, return it. Else empty string."""
    if not existing_text:
        return ""
    m = re.search(
        r"<!--\s*HENRY-NOTE-START\s*-->(.*?)<!--\s*HENRY-NOTE-END\s*-->",
        existing_text,
        flags=re.DOTALL,
    )
    if m:
        return m.group(0)
    return ""


def render_hub(slug: str, papers: list, counts: Counter, pair_papers: dict) -> str:
    intro = SUBDOMAIN_INTROS[slug]

    # papers in this subdomain (any role)
    in_sd = [p for p in papers if slug in p["all"]]
    primary_only = [p for p in in_sd if slug in p["primary"]]
    secondary_only = [p for p in in_sd if slug not in p["primary"]]

    in_sd_sorted = sorted(in_sd, key=lambda p: (-int(p["year"] or 0), p["journal"], p["slug"]))

    # bridges out of this subdomain
    out_bridges = []
    for (a, b), c in counts.items():
        if slug == a:
            other = b
        elif slug == b:
            other = a
        else:
            continue
        out_bridges.append((other, c))
    out_bridges.sort(key=lambda x: -x[1])

    lines = []
    lines.append("---")
    lines.append("type: subdomain-hub")
    lines.append(f'title: "{slug}"')
    lines.append("updated: 2026-05-11")
    lines.append("tags:")
    lines.append("  - subdomain-hub")
    lines.append(f"  - sd/{slug}")
    lines.append("status: living")
    lines.append("related:")
    lines.append('  - "[[index]]"')
    lines.append('  - "[[../_meta/subdomain-vocab]]"')
    lines.append('  - "[[../_meta/subdomain-bridge-stats]]"')
    lines.append("---")
    lines.append("")
    lines.append(f"# {slug}")
    lines.append("")
    lines.append(f"> Subdomain hub. Auto-regenerable from frontmatter via `scripts/generate-subdomain-hubs.py`. Hand-edits inside `HENRY-NOTE` blocks are preserved.")
    lines.append("")
    lines.append("## What this subdomain covers")
    lines.append("")
    lines.append(intro)
    lines.append("")

    # Henry-note section
    existing = (SUBDOMAINS_DIR / f"{slug}.md").read_text() if (SUBDOMAINS_DIR / f"{slug}.md").exists() else ""
    henry_block = preserve_henry_note(existing) or (
        "<!-- HENRY-NOTE-START -->\n"
        "*This block is for Henry's hand-edits. The auto-generator preserves whatever is between the START and END markers. "
        "Use it to record stance, key questions for this subdomain, watchlist papers, or \"how does this map to my current project?\" notes.*\n"
        "<!-- HENRY-NOTE-END -->"
    )
    lines.append("## Henry's stance and key questions")
    lines.append("")
    lines.append(henry_block)
    lines.append("")

    lines.append("## Papers in this subdomain")
    lines.append("")
    lines.append(f"Total: **{len(in_sd)}** ({len(primary_only)} primary, {len(secondary_only)} secondary-only).")
    lines.append("")

    # L1 group
    lines.append("### L1 (top-journal exemplars)")
    lines.append("")
    l1 = [p for p in in_sd_sorted if p["role"] == "top_journal_exemplar"]
    if not l1:
        lines.append("None yet.")
    else:
        lines.append("| Year | Journal | Paper | Address | Role here |")
        lines.append("|---|---|---|---|---|")
        for p in l1:
            role_here = "primary" if slug in p["primary"] else "bridge"
            lines.append(f"| {p['year']} | {p['journal']} | [[{p['slug']}|{p['slug']}]] | `{p['address']}` | {role_here} |")
    lines.append("")

    # L2 group
    lines.append("### L2 (applied flagships)")
    lines.append("")
    l2 = [p for p in in_sd_sorted if p["role"] == "applied_flagship"]
    if not l2:
        lines.append("None yet. Phase 2 pilot will land here once Henry triggers the L2 ingest.")
    else:
        lines.append("| Year | Journal | Depth | Paper | Address | Role here |")
        lines.append("|---|---|---|---|---|---|")
        for p in l2:
            role_here = "primary" if slug in p["primary"] else "bridge"
            lines.append(f"| {p['year']} | {p['journal']} | {p['depth']} | [[{p['slug']}|{p['slug']}]] | `{p['address']}` | {role_here} |")
    lines.append("")

    lines.append("## Outward connections (bridges)")
    lines.append("")
    if not out_bridges:
        lines.append("None yet.")
    else:
        lines.append("Ranked by number of papers spanning the pair (`subdomain_primary ∪ subdomain_secondary`). Bridge pages auto-emerge at 3+ papers; see [[bridges]].")
        lines.append("")
        lines.append("| Bridge to | Papers | Bridge page |")
        lines.append("|---|---|---|")
        for other, c in out_bridges:
            pair_slug = "--".join(sorted([slug, other]))
            link = f"[[bridges/{pair_slug}]]" if c >= 3 else f"`bridges/{pair_slug}` (premature)"
            lines.append(f"| `{other}` | {c} | {link} |")
    lines.append("")

    lines.append("## Subdomain-specific patterns")
    lines.append("")
    lines.append(f"Patterns under `wiki/patterns/subdomain/{slug}/`. Emerge once 3+ papers in this subdomain genuinely inform a pattern.")
    lines.append("")
    lines.append("- *No patterns drafted yet — Phase 3 onward.*")
    lines.append("")

    lines.append("## Subdomain-specific banks")
    lines.append("")
    lines.append(f"Bank rows scoped to this subdomain across [[banks/parameter-bank]], [[banks/sensitivity-bank]], [[banks/method-bank]]. Filled primarily by L2-A ingests.")
    lines.append("")
    lines.append("- *No bank rows yet — Phase 3 bootstrap.*")
    lines.append("")

    lines.append("## Comparisons (top-vs-applied delta library)")
    lines.append("")
    lines.append(f"Once L2 papers in this subdomain are ingested, the comparison library at [[patterns/comparisons]] will host the L1-vs-L2 delta analyses that touch `{slug}`.")
    lines.append("")
    lines.append("- *No comparisons yet — Phase 3 onward.*")
    lines.append("")

    return "\n".join(lines) + "\n"


def main():
    papers = gather_papers()
    counts, pair_papers = bridge_counts(papers)

    SUBDOMAINS_DIR.mkdir(parents=True, exist_ok=True)
    written = []
    for slug in ORDER:
        out = SUBDOMAINS_DIR / f"{slug}.md"
        content = render_hub(slug, papers, counts, pair_papers)
        out.write_text(content)
        written.append(out.name)

    print(f"Generated {len(written)} hubs at wiki/subdomains/:")
    for w in written:
        print(f"  - {w}")


if __name__ == "__main__":
    main()
