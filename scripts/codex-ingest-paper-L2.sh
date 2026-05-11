#!/usr/bin/env bash
# codex-ingest-paper-L2.sh — delegate a single L2 (applied flagship) paper ingest to codex-cli.
#
# Usage:
#   scripts/codex-ingest-paper-L2.sh <ZOTERO_KEY> <ADDRESS> <SLUG_HINT> <DEPTH> <PRIMARY_SUBDOMAIN>
#
# Args:
#   ZOTERO_KEY          8 uppercase alnum chars
#   ADDRESS             c-NNNNNN format (pre-allocated by orchestrating session)
#   SLUG_HINT           kebab-case slug, e.g. "ae-h2-grid-balancing"
#   DEPTH               A_deep | B_medium | C_light
#   PRIMARY_SUBDOMAIN   one of the 8 vocab slugs (decides L2/ subfolder placement);
#                       use "_cross" only if the paper genuinely spans 3+ subdomains
#
# Example:
#   scripts/codex-ingest-paper-L2.sh KEYABCD2 c-000026 ae-h2-grid-balancing A_deep hydrogen-p2x
#
# Notes:
#   - codex uses gpt-5.5 + xhigh from ~/.codex/config.toml.
#   - Address allocation is the orchestrating session's job.
#   - For L1 papers (Nature / NE / Joule / NC / NCC / OE / NSus etc.) use
#     scripts/codex-ingest-paper.sh instead.

set -euo pipefail

KEY="${1:-}"
ADDR="${2:-}"
SLUG_HINT="${3:-derive-from-title}"
DEPTH="${4:-}"
PRIMARY_SUBDOMAIN="${5:-}"

usage() {
  echo "usage: $0 <ZOTERO_KEY> <ADDRESS> <SLUG_HINT> <DEPTH:A_deep|B_medium|C_light> <PRIMARY_SUBDOMAIN>" >&2
  exit 2
}

if [ -z "$KEY" ] || [ -z "$ADDR" ] || [ -z "$DEPTH" ] || [ -z "$PRIMARY_SUBDOMAIN" ]; then
  usage
fi

if ! echo "$ADDR" | grep -Eq '^c-[0-9]{6}$'; then
  echo "ERR: address must match c-NNNNNN, got: $ADDR" >&2
  exit 2
fi

if ! echo "$KEY" | grep -Eq '^[A-Z0-9]{8}$'; then
  echo "ERR: zotero key must be 8 uppercase alnum chars, got: $KEY" >&2
  exit 2
fi

case "$DEPTH" in
  A_deep|B_medium|C_light) ;;
  *) echo "ERR: DEPTH must be A_deep|B_medium|C_light, got: $DEPTH" >&2; exit 2 ;;
esac

# subdomain slug whitelist
case "$PRIMARY_SUBDOMAIN" in
  integrated-energy-systems|power-systems|hydrogen-p2x|re-tech-resources|building-urban|energy-policy-economics|lca-sustainability|ai-data-driven|_cross) ;;
  *) echo "ERR: PRIMARY_SUBDOMAIN not in vocab. See wiki/_meta/subdomain-vocab.md. Got: $PRIMARY_SUBDOMAIN" >&2; exit 2 ;;
esac

# pick contract for the depth
case "$DEPTH" in
  A_deep)   CONTRACT="_templates/codex-ingest-contract-L2-A.md"; SUFFIX="A-deep" ;;
  B_medium) CONTRACT="_templates/codex-ingest-contract-L2-B.md"; SUFFIX="B-medium" ;;
  C_light)  CONTRACT="_templates/codex-ingest-contract-L2-C.md"; SUFFIX="C-light" ;;
esac

VAULT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PKG_DIR="$VAULT_ROOT/.raw/papers/$KEY"
mkdir -p "$PKG_DIR"

STDOUT_LOG="$PKG_DIR/codex-stdout.log"
STDERR_LOG="$PKG_DIR/codex-stderr.log"
RECEIPT="$PKG_DIR/codex-receipt.json"
PROMPT_FILE="$(mktemp -t codex-ingest-prompt-L2.XXXXXX)"
TODAY="$(date +%Y-%m-%d)"
NOW="$(date +%H:%M:%S)"

cleanup() {
  rm -f "$PROMPT_FILE"
}
trap cleanup EXIT

cat > "$PROMPT_FILE" <<EOF
You are running as a TPL L2 ingest agent ($SUFFIX). Read the contract first, then proceed.

Inputs:
- Zotero key: $KEY
- Pre-allocated page address: $ADDR
- Slug hint: $SLUG_HINT
- Depth: $DEPTH ($SUFFIX)
- Primary subdomain (decides folder placement): $PRIMARY_SUBDOMAIN
- Output folder: wiki/papers/L2/$PRIMARY_SUBDOMAIN/
- Vault root (already your -C): $VAULT_ROOT
- Today's date: $TODAY

Read in this order before writing anything:
1. $CONTRACT                                                   (the rules for this depth)
2. CLAUDE.md                                                    (TPL constitution + scope + style)
3. wiki/_meta/journal-role-vocab.md                             (confirm this paper is applied_flagship)
4. wiki/_meta/subdomain-vocab.md                                (8 subdomain definitions)
5. wiki/_meta/depth-policy.md                                   (A/B/C selection criteria — confirm $DEPTH fit)
6. wiki/_meta/routing-rules.md                                  (which pages get updated)
7. _templates/paper-analysis-L2-${SUFFIX%%-*}.md                (the matching template)
8. .raw/papers/$KEY/pre-extraction.md                           (optional starter, if present)

Then:
- Confirm: is this paper really applied_flagship? If not, abort with .raw/papers/$KEY/wrong-tier.md (per contract).
- Resolve the paper via Zotero MCP (handle Peer Review File trap if applicable).
- Compose wiki/papers/L2/$PRIMARY_SUBDOMAIN/{year}-{journal-short}-{slug}.md per the template.
- Write the stub files per contract (7 stubs at A_deep, 5 at B_medium, 3 at C_light).
- For A_deep and (if relevant) B_medium: write .raw/papers/$KEY/bank-candidates.md listing parameter / sensitivity / method rows to be merged into wiki/banks/* by the orchestrating session.
- Print the JSON receipt to stdout. Single object. No markdown fences.

Self-check before printing the receipt:
- frontmatter complete: journal_role=applied_flagship, ingest_depth=$DEPTH, subdomain_primary[0] starts with "$PRIMARY_SUBDOMAIN", address exactly == $ADDR
- section count matches template (10 for A_deep, 6 for B_medium, ~3 paragraphs for C_light)
- page size in target band: A_deep 12-18 KB, B_medium 4-6 KB, C_light < 500 bytes (body, excluding frontmatter)
- banned-word scan clean
- no em dashes; no double-hyphen as punctuation
- bank-candidates.md present (A_deep) or absent-with-reason (B_medium, C_light)

If anything blocks completion, write .raw/papers/$KEY/codex-ingest-failure.md and print a receipt with wiki_page=null.
EOF

echo "[$NOW] codex exec L2-$SUFFIX starting for $KEY (address $ADDR, subdomain $PRIMARY_SUBDOMAIN)" >&2

codex exec \
  -C "$VAULT_ROOT" \
  -s workspace-write \
  --skip-git-repo-check \
  - < "$PROMPT_FILE" \
  > "$STDOUT_LOG" 2> "$STDERR_LOG"

RC=$?

# Extract JSON receipt from stdout (last valid JSON object containing zotero_key wins).
if command -v python3 >/dev/null 2>&1 && [ -s "$STDOUT_LOG" ]; then
  python3 - <<PY 2>/dev/null
import json, re, sys
content = open("$STDOUT_LOG").read()
matches = re.findall(r'\{[\s\S]*?\}', content)
for m in reversed(matches):
    try:
        d = json.loads(m)
        if 'zotero_key' in d:
            with open("$RECEIPT", 'w') as f:
                json.dump(d, f, indent=2)
            sys.exit(0)
    except Exception:
        continue
PY
fi

if [ ! -s "$RECEIPT" ]; then
  echo "WARN: could not extract JSON receipt from $STDOUT_LOG; raw stdout preserved." >&2
fi

DONE="$(date +%H:%M:%S)"
echo "[$DONE] codex exec L2-$SUFFIX finished for $KEY (rc=$RC)" >&2
echo "  stdout:  $STDOUT_LOG"
echo "  stderr:  $STDERR_LOG"
echo "  receipt: $RECEIPT"
exit $RC
