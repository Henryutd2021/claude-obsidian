#!/usr/bin/env python3
"""Scan wiki/papers/L1/*.md (and wiki/papers/L2/**/*.md once it exists) and
emit:

  1. per-subdomain paper count (primary + secondary roles)
  2. pairwise bridge counts (papers listing both A and B in primary ∪ secondary)
  3. per-paper subdomain assignments (for spot-check)

Output: stdout JSON, plus a markdown summary at wiki/_meta/subdomain-bridge-stats.md
that the orchestrating session can read.
"""

import json
import re
import sys
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path

VAULT = Path("/Users/henry/Library/Mobile Documents/iCloud~md~obsidian/Documents/claude-obsidian")
PAPERS = VAULT / "wiki" / "papers"
OUT_MD = VAULT / "wiki" / "_meta" / "subdomain-bridge-stats.md"

SUBDOMAINS = [
    "integrated-energy-systems",
    "power-systems",
    "hydrogen-p2x",
    "re-tech-resources",
    "building-urban",
    "energy-policy-economics",
    "lca-sustainability",
    "ai-data-driven",
]


def parse_frontmatter(text: str) -> dict:
    """Return a dict with keys we care about. Handles list values in YAML block style."""
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
        # YAML list item: "  - value"
        m_item = re.match(r"^\s+-\s+(.+)$", line)
        if m_item and current_key is not None and list_buffer is not None:
            list_buffer.append(m_item.group(1).strip().strip('"').strip("'"))
            continue
        # closes a list
        if current_key is not None and list_buffer is not None:
            out[current_key] = list_buffer
            current_key = None
            list_buffer = None
        # scalar or new key
        m_kv = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", line)
        if m_kv:
            k = m_kv.group(1)
            v = m_kv.group(2).strip()
            if v == "" or v == "[]":
                # could be empty list or start of block list
                current_key = k
                list_buffer = []
                # if v == "[]" we keep buffer empty and let next line decide
                if v == "[]":
                    out[k] = []
                    current_key = None
                    list_buffer = None
            elif v.startswith("[") and v.endswith("]"):
                # inline list
                items = [x.strip().strip('"').strip("'") for x in v[1:-1].split(",") if x.strip()]
                out[k] = items
            else:
                out[k] = v.strip().strip('"').strip("'")
    # close trailing list
    if current_key is not None and list_buffer is not None:
        out[current_key] = list_buffer
    return out


def gather_papers():
    """Return list of dicts: {path, slug, primary, secondary, all, role, depth, year, journal}."""
    papers = []
    for path in sorted(PAPERS.rglob("*.md")):
        # skip non-paper files in L2 folder (e.g., README, .gitkeep that we might add later)
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
        all_sd = primary + secondary
        papers.append({
            "path": str(path.relative_to(VAULT)),
            "slug": path.stem,
            "role": fm.get("journal_role", ""),
            "depth": fm.get("ingest_depth", ""),
            "primary": primary,
            "secondary": secondary,
            "all": all_sd,
            "year": fm.get("year", ""),
            "journal": fm.get("journal", ""),
            "title": fm.get("title", ""),
            "address": fm.get("address", ""),
        })
    return papers


def main():
    papers = gather_papers()
    n = len(papers)

    # 1. per-subdomain counts
    by_sub_primary = defaultdict(list)
    by_sub_secondary = defaultdict(list)
    by_sub_any = defaultdict(list)
    for p in papers:
        for s in p["primary"]:
            by_sub_primary[s].append(p["slug"])
            by_sub_any[s].append(p["slug"])
        for s in p["secondary"]:
            by_sub_secondary[s].append(p["slug"])
            if p["slug"] not in by_sub_any[s]:
                by_sub_any[s].append(p["slug"])

    # 2. pairwise bridge counts
    pair_counts = Counter()
    pair_papers = defaultdict(list)
    for p in papers:
        sds = sorted(set(p["all"]))
        for a, b in combinations(sds, 2):
            pair = (a, b)
            pair_counts[pair] += 1
            pair_papers[pair].append(p["slug"])

    # JSON dump to stdout
    result = {
        "total_papers": n,
        "by_subdomain_primary_count": {s: len(by_sub_primary[s]) for s in SUBDOMAINS},
        "by_subdomain_any_count": {s: len(by_sub_any[s]) for s in SUBDOMAINS},
        "by_subdomain_papers": {s: by_sub_any[s] for s in SUBDOMAINS},
        "bridge_counts": {f"{a}--{b}": c for (a, b), c in sorted(pair_counts.items(), key=lambda kv: -kv[1])},
        "bridges_ready_for_stub_at_3plus": {
            f"{a}--{b}": pair_papers[(a, b)] for (a, b), c in pair_counts.items() if c >= 3
        },
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))

    # Markdown summary
    lines = []
    lines.append("---")
    lines.append("type: meta")
    lines.append('title: "Subdomain + bridge counts (auto-generated)"')
    lines.append("updated: 2026-05-11")
    lines.append("tags:")
    lines.append("  - meta")
    lines.append("  - auto-generated")
    lines.append("status: evergreen")
    lines.append("related:")
    lines.append('  - "[[subdomain-vocab]]"')
    lines.append('  - "[[../subdomains/integrated-energy-systems]]"')
    lines.append("---")
    lines.append("")
    lines.append("# Subdomain + bridge counts")
    lines.append("")
    lines.append(f"Auto-generated from `wiki/papers/**/*.md` frontmatter via `scripts/subdomain-bridge-stats.py`.")
    lines.append(f"Total papers scanned: **{n}**.")
    lines.append("")
    lines.append("## Papers per subdomain")
    lines.append("")
    lines.append("| Subdomain | Primary only | Any (primary or secondary) | Sample papers |")
    lines.append("|---|---|---|---|")
    for s in SUBDOMAINS:
        primary_n = len(by_sub_primary[s])
        any_n = len(by_sub_any[s])
        sample = ", ".join(f"`{x}`" for x in by_sub_any[s][:3])
        if len(by_sub_any[s]) > 3:
            sample += f", … (+{len(by_sub_any[s]) - 3} more)"
        lines.append(f"| `{s}` | {primary_n} | {any_n} | {sample} |")
    lines.append("")
    lines.append("## Pairwise bridge counts (sorted by strength)")
    lines.append("")
    lines.append("| Pair (A--B) | Papers spanning |")
    lines.append("|---|---|")
    for (a, b), c in sorted(pair_counts.items(), key=lambda kv: -kv[1]):
        lines.append(f"| `{a}--{b}` | {c} |")
    lines.append("")
    lines.append("## Bridges ready for stub (≥3 papers)")
    lines.append("")
    if not result["bridges_ready_for_stub_at_3plus"]:
        lines.append("None yet. Bridges emerge when 3+ papers span a pair.")
    else:
        for pair, slugs in sorted(result["bridges_ready_for_stub_at_3plus"].items(), key=lambda kv: -len(kv[1])):
            lines.append(f"### {pair}")
            lines.append(f"{len(slugs)} papers:")
            for s in slugs:
                lines.append(f"- `{s}`")
            lines.append("")

    OUT_MD.parent.mkdir(parents=True, exist_ok=True)
    OUT_MD.write_text("\n".join(lines))


if __name__ == "__main__":
    main()
