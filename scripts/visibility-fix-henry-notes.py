#!/usr/bin/env python3
"""One-shot fix: convert HENRY-NOTE blocks from HTML-comment-only content
to italics. HTML comments don't render in Obsidian's reading mode, which
made these blocks look empty.

Transformation:

    <!-- HENRY-NOTE-START -->
    <!-- some hand-written note -->
    <!-- HENRY-NOTE-END -->

becomes:

    <!-- HENRY-NOTE-START -->
    *some hand-written note*
    <!-- HENRY-NOTE-END -->

The START/END markers stay so any future regenerator can still identify
and preserve the editable region.

Idempotent: skips blocks whose body is already non-comment text.
"""

import re
import sys
from pathlib import Path

VAULT = Path("/Users/henry/Library/Mobile Documents/iCloud~md~obsidian/Documents/claude-obsidian")

# files to scan: 7 patterns + 3 playbook + L2 templates (which have similar placeholders)
import glob
TARGETS = [
    "wiki/patterns/cross-cutting/methods-recurrent/additionality-counterfactuals.md",
    "wiki/patterns/cross-cutting/methods-recurrent/option-value-scenario-pairs.md",
    "wiki/patterns/cross-cutting/methods-recurrent/plant-vs-aggregate-resolution.md",
    "wiki/patterns/cross-cutting/archetype/firm-clean-flexible-baseload.md",
    "wiki/patterns/subdomain/hydrogen-p2x/merit-order-and-end-use-ranking.md",
    "wiki/patterns/subdomain/ai-data-driven/load-shape-and-flexibility.md",
    "wiki/patterns/subdomain/re-tech-resources/empirical-growth-envelope.md",
    "wiki/playbook/top-journal-craft/intro-template-energy-papers.md",
    "wiki/playbook/top-journal-craft/main-figure-design-rules.md",
    "wiki/playbook/top-journal-craft/contribution-decision-tree.md",
]
# add all subdomain hubs and bridge pages dynamically
for hub in sorted(glob.glob(str((Path("/Users/henry/Library/Mobile Documents/iCloud~md~obsidian/Documents/claude-obsidian") / "wiki/subdomains/*.md")))):
    rel = str(Path(hub).relative_to(Path("/Users/henry/Library/Mobile Documents/iCloud~md~obsidian/Documents/claude-obsidian")))
    if rel not in TARGETS:
        TARGETS.append(rel)
for br in sorted(glob.glob(str((Path("/Users/henry/Library/Mobile Documents/iCloud~md~obsidian/Documents/claude-obsidian") / "wiki/bridges/*.md")))):
    rel = str(Path(br).relative_to(Path("/Users/henry/Library/Mobile Documents/iCloud~md~obsidian/Documents/claude-obsidian")))
    if rel not in TARGETS:
        TARGETS.append(rel)

BLOCK_RE = re.compile(
    r"(<!--\s*HENRY-NOTE-START\s*-->)\s*\n"
    r"(.+?)\n"
    r"(<!--\s*HENRY-NOTE-END\s*-->)",
    re.DOTALL,
)

INNER_COMMENT_RE = re.compile(r"^\s*<!--\s*(.+?)\s*-->\s*$", re.DOTALL)


def fix_file(path: Path) -> str:
    text = path.read_text()

    def repl(m: re.Match) -> str:
        start, body, end = m.group(1), m.group(2), m.group(3)
        # if body is already visible text (not just an HTML comment), leave alone
        inner = INNER_COMMENT_RE.match(body)
        if not inner:
            return m.group(0)  # already non-comment
        visible = inner.group(1).strip()
        # convert to italics (use single * which Obsidian renders as italic)
        return f"{start}\n*{visible}*\n{end}"

    new_text, n = BLOCK_RE.subn(repl, text)
    if n == 0:
        return "no-block-found"
    if new_text == text:
        return "already-visible"
    path.write_text(new_text)
    return f"converted-{n}-block(s)"


def main():
    results = []
    for rel in TARGETS:
        path = VAULT / rel
        if not path.exists():
            results.append((rel, "not-found"))
            continue
        status = fix_file(path)
        results.append((rel, status))

    for rel, status in results:
        print(f"{status:25}  {rel}")


if __name__ == "__main__":
    main()
