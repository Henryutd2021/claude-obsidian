#!/usr/bin/env python3
"""One-shot Phase 1 migration: extend top_paper_lab_manifest.csv schema with
6 new columns and backfill the 22 already-ingested rows.

New columns:
- journal_role            (all 142 rows: top_journal_exemplar)
- ingest_depth            (22 rows: A_deep; others: blank)
- subdomain_primary       (22 rows: ";"-joined; others: blank)
- subdomain_secondary     (22 rows: ";"-joined; others: blank)
- use_tags                (all rows: blank)
- notes                   (all rows: blank)

Also creates l2_candidate_manifest.csv staging file with the same schema
plus journal_role default empty (Henry fills per row when adding L2 candidates).

Idempotent: if all new columns already present, exits with status 'no-op'.
"""

import csv
import sys
from pathlib import Path

VAULT = Path("/Users/henry/Library/Mobile Documents/iCloud~md~obsidian/Documents/claude-obsidian")
MANIFEST = VAULT / ".raw" / "zotero_manifest" / "top_paper_lab_manifest.csv"
L2_MANIFEST = VAULT / ".raw" / "zotero_manifest" / "l2_candidate_manifest.csv"

# zotero_key -> (primary, secondary) mirrored from migrate-v2-frontmatter.py
# (single source of truth lives in subdomain assignments; keep in sync)
INGESTED = {
    "PIQKGJNB": (["hydrogen-p2x", "integrated-energy-systems"], ["energy-policy-economics"]),
    "8IMLJZAH": (["hydrogen-p2x", "energy-policy-economics"], ["power-systems", "lca-sustainability"]),
    "T5W8LVA9": (["re-tech-resources", "integrated-energy-systems"], ["power-systems", "lca-sustainability"]),
    "M9HYZCZE": (["re-tech-resources", "power-systems"], ["integrated-energy-systems"]),
    "T3YPX6LR": (["hydrogen-p2x", "integrated-energy-systems"], ["re-tech-resources"]),
    "QDU6TZYF": (["energy-policy-economics", "integrated-energy-systems"], ["lca-sustainability"]),
    "H998SFTH": (["lca-sustainability", "energy-policy-economics"], []),
    "A4EZAC5U": (["energy-policy-economics", "integrated-energy-systems"], ["lca-sustainability"]),
    "UELISBYS": (["power-systems", "ai-data-driven"], ["re-tech-resources", "integrated-energy-systems"]),
    "CRAKEP8V": (["re-tech-resources", "building-urban"], ["lca-sustainability"]),
    "L8UI4RX3": (["re-tech-resources", "energy-policy-economics"], []),
    "73CKKQFI": (["hydrogen-p2x", "integrated-energy-systems"], ["energy-policy-economics", "lca-sustainability"]),
    "UIWZD5EE": (["hydrogen-p2x", "energy-policy-economics"], ["lca-sustainability"]),
    "VMSZ42JG": (["building-urban"], ["energy-policy-economics", "lca-sustainability"]),
    "B6LNILBU": (["re-tech-resources", "energy-policy-economics"], []),
    "KRT75D4W": (["hydrogen-p2x", "energy-policy-economics"], ["re-tech-resources"]),
    "XUGL6XPD": (["integrated-energy-systems", "power-systems"], ["energy-policy-economics"]),
    "SYZJZS6F": (["power-systems", "integrated-energy-systems"], ["energy-policy-economics"]),
    "5CAVXPE9": (["power-systems", "integrated-energy-systems"], ["re-tech-resources"]),
    "SYGLCEMJ": (["integrated-energy-systems", "energy-policy-economics"], ["power-systems"]),
    "52W57HP5": (["ai-data-driven", "energy-policy-economics"], ["lca-sustainability"]),
    "KWNBZ8FA": (["ai-data-driven", "power-systems"], ["integrated-energy-systems"]),
}

NEW_COLS = ["journal_role", "ingest_depth", "subdomain_primary", "subdomain_secondary", "use_tags", "notes"]


def extend_main_manifest():
    rows = list(csv.reader(MANIFEST.open()))
    if not rows:
        print("ERROR: main manifest empty")
        sys.exit(1)

    header = rows[0]
    if all(c in header for c in NEW_COLS):
        print(f"main manifest: no-op (all {len(NEW_COLS)} columns already present)")
        return 0

    # extend header
    new_header = header + [c for c in NEW_COLS if c not in header]

    # extend each data row
    new_rows = [new_header]
    backfilled = 0
    for row in rows[1:]:
        # pad row to header length first
        row = row + [""] * (len(header) - len(row))
        zkey = row[0].strip() if row else ""
        new_vals = {
            "journal_role": "top_journal_exemplar",
            "ingest_depth": "",
            "subdomain_primary": "",
            "subdomain_secondary": "",
            "use_tags": "",
            "notes": "",
        }
        if zkey in INGESTED:
            primary, secondary = INGESTED[zkey]
            new_vals["ingest_depth"] = "A_deep"
            new_vals["subdomain_primary"] = ";".join(primary)
            new_vals["subdomain_secondary"] = ";".join(secondary)
            backfilled += 1
        appended = [new_vals[c] for c in NEW_COLS if c not in header]
        new_rows.append(row + appended)

    with MANIFEST.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerows(new_rows)

    print(f"main manifest: extended schema by {len(new_header) - len(header)} cols")
    print(f"main manifest: backfilled {backfilled} ingested rows with depth + subdomain")
    return backfilled


def create_l2_staging():
    if L2_MANIFEST.exists():
        print(f"L2 staging: already exists at {L2_MANIFEST.name}, skipping")
        return
    # Same schema as main; journal_role defaults to applied_flagship
    header = ["zotero_key", "title", "authors", "journal", "year", "doi",
              "zotero_pdf_attached", "zotero_si_attached", "da_extracted", "ca_extracted",
              "external_repo", "priority", "ingest_status", "review_status",
              "journal_role", "ingest_depth", "subdomain_primary", "subdomain_secondary",
              "use_tags", "notes"]
    with L2_MANIFEST.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
    print(f"L2 staging: created {L2_MANIFEST.name} with {len(header)} cols")


def main():
    extend_main_manifest()
    create_l2_staging()


if __name__ == "__main__":
    main()
