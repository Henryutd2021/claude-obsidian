#!/usr/bin/env python3
"""One-shot Phase 1 migration: add journal_role, ingest_depth, subdomain_primary,
subdomain_secondary fields to the 22 existing TPL paper analyses.

Idempotent: skips files that already have a journal_role line.
Run once; safe to re-run (will report 'already-has-fields' for all).
"""

import sys
from pathlib import Path

VAULT = Path("/Users/henry/Library/Mobile Documents/iCloud~md~obsidian/Documents/claude-obsidian")
PAPERS_DIR = VAULT / "wiki" / "papers"

# (slug-without-.md): (subdomain_primary, subdomain_secondary)
MAPPING = {
    "2022-NE-china-hta-clean-hydrogen":             (["hydrogen-p2x", "integrated-energy-systems"], ["energy-policy-economics"]),
    "2024-NE-h2-additionality-time-matching":       (["hydrogen-p2x", "energy-policy-economics"], ["power-systems", "lca-sustainability"]),
    "2023-N-china-pv-wind-3844-plants":             (["re-tech-resources", "integrated-energy-systems"], ["power-systems", "lca-sustainability"]),
    "2025-J-space-based-solar-europe":              (["re-tech-resources", "power-systems"], ["integrated-energy-systems"]),
    "2023-NC-endogenous-learning-green-h2-europe":  (["hydrogen-p2x", "integrated-energy-systems"], ["re-tech-resources"]),
    "2021-NE-kikstra-covid-energy-demand-scenarios":(["energy-policy-economics", "integrated-energy-systems"], ["lca-sustainability"]),
    "2015-N-china-fossil-cement-co2-revised":       (["lca-sustainability", "energy-policy-economics"], []),
    "2023-NCC-net-zero-investment-shifts-europe":   (["energy-policy-economics", "integrated-energy-systems"], ["lca-sustainability"]),
    "2020-J-data-center-load-migration-curtailment":(["power-systems", "ai-data-driven"], ["re-tech-resources", "integrated-energy-systems"]),
    "2023-NC-rooftop-pv-china-carbon":              (["re-tech-resources", "building-urban"], ["lca-sustainability"]),
    "2021-NE-national-wind-solar-growth-dynamics":  (["re-tech-resources", "energy-policy-economics"], []),
    "2024-OE-h2-economy-22pct-cost-reduction":      (["hydrogen-p2x", "integrated-energy-systems"], ["energy-policy-economics", "lca-sustainability"]),
    "2021-NCC-h2-efuels-potential-risks":           (["hydrogen-p2x", "energy-policy-economics"], ["lca-sustainability"]),
    "2022-NCC-residential-decarbonization-us":      (["building-urban"], ["energy-policy-economics", "lca-sustainability"]),
    "2022-N-solar-pv-supply-chain-cost-savings":    (["re-tech-resources", "energy-policy-economics"], []),
    "2022-NE-green-h2-probabilistic-feasibility":   (["hydrogen-p2x", "energy-policy-economics"], ["re-tech-resources"]),
    "2023-J-smr-industrial-process-heat-tea":       (["integrated-energy-systems", "power-systems"], ["energy-policy-economics"]),
    "2022-NE-flexible-nuclear-deep-decarb":         (["power-systems", "integrated-energy-systems"], ["energy-policy-economics"]),
    "2024-NE-flexible-geothermal-decarb-systems":   (["power-systems", "integrated-energy-systems"], ["re-tech-resources"]),
    "2025-NE-smr-policy-module-learning":           (["integrated-energy-systems", "energy-policy-economics"], ["power-systems"]),
    "2022-J-data-center-energy-estimates-review":   (["ai-data-driven", "energy-policy-economics"], ["lca-sustainability"]),
    "2026-NE-ai-data-centres-grid-interactive":     (["ai-data-driven", "power-systems"], ["integrated-energy-systems"]),
}


def yaml_list(items):
    """Render a YAML list as a block under the key (with leading newline) or [] if empty."""
    if not items:
        return " []"
    return "\n  - " + "\n  - ".join(items)


def build_insert(primary, secondary):
    """Build the 4-line block to insert."""
    lines = [
        "journal_role: top_journal_exemplar",
        "ingest_depth: A_deep",
        f"subdomain_primary:{yaml_list(primary)}",
        f"subdomain_secondary:{yaml_list(secondary)}",
    ]
    return "\n".join(lines)


def update_paper(path: Path, primary, secondary) -> str:
    """Return one of: 'updated', 'already-has-fields', 'no-anchor', 'no-frontmatter'."""
    text = path.read_text()
    if "journal_role:" in text:
        return "already-has-fields"

    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return "no-frontmatter"

    # find the closing --- of frontmatter
    end_idx = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end_idx = i
            break
    if end_idx is None:
        return "no-frontmatter"

    # find the method_type: line within frontmatter (anchor)
    anchor_idx = None
    for i in range(1, end_idx):
        if lines[i].startswith("method_type:"):
            anchor_idx = i
            break
    if anchor_idx is None:
        return "no-anchor"

    insert_block = build_insert(primary, secondary).split("\n")
    new_lines = lines[: anchor_idx + 1] + insert_block + lines[anchor_idx + 1 :]
    path.write_text("\n".join(new_lines))
    return "updated"


def main():
    results = {"updated": [], "already-has-fields": [], "no-anchor": [], "no-frontmatter": [], "not-found": []}
    for slug, (primary, secondary) in MAPPING.items():
        path = PAPERS_DIR / f"{slug}.md"
        if not path.exists():
            results["not-found"].append(slug)
            continue
        status = update_paper(path, primary, secondary)
        results[status].append(slug)

    for category, slugs in results.items():
        if slugs:
            print(f"{category}: {len(slugs)}")
            for s in slugs:
                print(f"  - {s}")

    if results["no-anchor"] or results["no-frontmatter"] or results["not-found"]:
        sys.exit(1)


if __name__ == "__main__":
    main()
