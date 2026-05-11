#!/usr/bin/env python3
"""Generate wiki/bridges/{A--B}.md stub pages for every subdomain pair with
3+ papers spanning it (per subdomain_primary ∪ subdomain_secondary). Re-runs
safely; preserves hand-edits inside HENRY-NOTE blocks.

Pairs below 3 stay implicit (visible only in subdomain hub bridge tables).
"""

import re
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path

VAULT = Path("/Users/henry/Library/Mobile Documents/iCloud~md~obsidian/Documents/claude-obsidian")
PAPERS = VAULT / "wiki" / "papers"
BRIDGES_DIR = VAULT / "wiki" / "bridges"

GATE = 3  # bridge emergence gate


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
            "address": fm.get("address", ""),
        })
    return papers


def preserve_henry_note(existing_text: str) -> str:
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


def render_bridge(a: str, b: str, supporting: list, all_papers: list) -> str:
    """Render bridge page for pair (a, b) with the list of papers spanning it.

    `supporting` are paper dicts containing both a and b in their `all` set.
    """
    pair = "--".join(sorted([a, b]))
    title_pair = f"{a} ↔ {b}"
    out_path = BRIDGES_DIR / f"{pair}.md"

    supporting_sorted = sorted(supporting, key=lambda p: (-int(p["year"] or 0), p["journal"], p["slug"]))

    lines = []
    lines.append("---")
    lines.append("type: bridge")
    lines.append(f'title: "{pair}"')
    lines.append("updated: 2026-05-11")
    lines.append("tags:")
    lines.append("  - bridge")
    lines.append(f"  - sd/{a}")
    lines.append(f"  - sd/{b}")
    lines.append("status: living")
    lines.append("related:")
    lines.append(f'  - "[[../subdomains/{a}]]"')
    lines.append(f'  - "[[../subdomains/{b}]]"')
    lines.append('  - "[[../_meta/subdomain-bridge-stats]]"')
    lines.append("---")
    lines.append("")
    lines.append(f"# Bridge: {title_pair}")
    lines.append("")
    lines.append(f"> Cross-subdomain bridge page. Emerges when 3+ papers span both `{a}` and `{b}` "
                 f"in `subdomain_primary ∪ subdomain_secondary`. Auto-regenerable from frontmatter via "
                 f"`scripts/generate-bridges.py`. Hand-edits inside `HENRY-NOTE` blocks are preserved.")
    lines.append("")
    lines.append("## Why this interface matters")
    lines.append("")
    existing = out_path.read_text() if out_path.exists() else ""
    henry_block = preserve_henry_note(existing) or (
        "<!-- HENRY-NOTE-START -->\n"
        f"*This block is for Henry's hand-edits. The auto-generator preserves whatever is between the START and END markers. "
        f"Write one short paragraph on why papers at the {a} × {b} interface tend to produce strong contributions, "
        f"what kinds of claims live here, and what reviewer pushback this interface attracts.*\n"
        "<!-- HENRY-NOTE-END -->"
    )
    lines.append(henry_block)
    lines.append("")

    lines.append("## Papers spanning this pair")
    lines.append("")
    lines.append(f"**Count**: {len(supporting_sorted)}")
    lines.append("")
    lines.append(f"| Year | Journal | Paper | Address | Role: {a} | Role: {b} |")
    lines.append("|---|---|---|---|---|---|")
    for p in supporting_sorted:
        role_a = "primary" if a in p["primary"] else ("secondary" if a in p["secondary"] else "—")
        role_b = "primary" if b in p["primary"] else ("secondary" if b in p["secondary"] else "—")
        lines.append(f"| {p['year']} | {p['journal']} | [[{p['slug']}|{p['slug']}]] | `{p['address']}` | {role_a} | {role_b} |")
    lines.append("")

    # L1 / L2 split
    l1 = [p for p in supporting_sorted if p["role"] == "top_journal_exemplar"]
    l2 = [p for p in supporting_sorted if p["role"] == "applied_flagship"]
    lines.append(f"L1: {len(l1)} · L2: {len(l2)}")
    lines.append("")

    lines.append("## Shared methods / problems / claims (placeholder)")
    lines.append("")
    lines.append("Phase 3 onward. Extract from supporting papers:")
    lines.append("")
    lines.append("- What problems live at this interface (not in either subdomain alone)?")
    lines.append("- What methods recur across these papers (e.g., counterfactual, sector-coupled optimization, additionality, plant-level resolution)?")
    lines.append(f"- What does `{a}` learn from `{b}`, and vice versa?")
    lines.append("- Exemplar papers that *succeed* at the interface (often the most impactful).")
    lines.append("")

    lines.append("## L2 evidence")
    lines.append("")
    if l2:
        lines.append(f"{len(l2)} L2 papers participate. See the table above.")
    else:
        lines.append("None yet. Will populate once L2 pilots (Phase 2 next step) and beyond fill `wiki/papers/L2/`.")
    lines.append("")

    return "\n".join(lines) + "\n"


def main():
    papers = gather_papers()

    pair_papers = defaultdict(list)
    for p in papers:
        sds = sorted(set(p["all"]))
        for a, b in combinations(sds, 2):
            pair_papers[(a, b)].append(p)

    BRIDGES_DIR.mkdir(parents=True, exist_ok=True)
    written = []
    for (a, b), supporting in sorted(pair_papers.items(), key=lambda kv: -len(kv[1])):
        if len(supporting) < GATE:
            continue
        content = render_bridge(a, b, supporting, papers)
        out_path = BRIDGES_DIR / f"{'--'.join(sorted([a, b]))}.md"
        out_path.write_text(content)
        written.append((out_path.name, len(supporting)))

    print(f"Generated {len(written)} bridge stubs at wiki/bridges/ (gate: {GATE}+ papers):")
    for name, n in written:
        print(f"  - {name}  ({n} papers)")


if __name__ == "__main__":
    main()
