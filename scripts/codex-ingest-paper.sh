#!/usr/bin/env bash
# codex-ingest-paper.sh — delegate a single TPL paper ingest to codex-cli.
#
# Usage:
#   scripts/codex-ingest-paper.sh <ZOTERO_KEY> <ADDRESS> [SLUG_HINT]
#
# Example:
#   scripts/codex-ingest-paper.sh 8IMLJZAH c-000004 nature-energy-h2-additionality
#
# Notes:
#   - macOS ships bash 3.2, which does not parse $(cat <<EOF ... EOF) reliably.
#     We use a temp file via mktemp + stdin piping instead.
#   - codex picks up gpt-5.5 + xhigh from ~/.codex/config.toml by default.
#   - Address allocation is the orchestrating session's job; do NOT call
#     scripts/allocate-address.sh from here.

set -euo pipefail

KEY="${1:-}"
ADDR="${2:-}"
SLUG_HINT="${3:-derive-from-title}"

if [ -z "$KEY" ] || [ -z "$ADDR" ]; then
  echo "usage: $0 <ZOTERO_KEY> <ADDRESS> [SLUG_HINT]" >&2
  exit 2
fi

if ! echo "$ADDR" | grep -Eq '^c-[0-9]{6}$'; then
  echo "ERR: address must match c-NNNNNN, got: $ADDR" >&2
  exit 2
fi

if ! echo "$KEY" | grep -Eq '^[A-Z0-9]{8}$'; then
  echo "ERR: zotero key must be 8 uppercase alnum chars, got: $KEY" >&2
  exit 2
fi

VAULT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PKG_DIR="$VAULT_ROOT/.raw/papers/$KEY"
mkdir -p "$PKG_DIR"

STDOUT_LOG="$PKG_DIR/codex-stdout.log"
STDERR_LOG="$PKG_DIR/codex-stderr.log"
RECEIPT="$PKG_DIR/codex-receipt.json"
PROMPT_FILE="$(mktemp -t codex-ingest-prompt.XXXXXX)"
TODAY="$(date +%Y-%m-%d)"
NOW="$(date +%H:%M:%S)"

cleanup() {
  rm -f "$PROMPT_FILE"
}
trap cleanup EXIT

cat > "$PROMPT_FILE" <<EOF
You are running as a TPL ingest agent. Read the contract first, then proceed.

Inputs:
- Zotero key: $KEY
- Pre-allocated page address: $ADDR
- Slug hint: $SLUG_HINT
- Vault root (already your -C): $VAULT_ROOT
- Today's date: $TODAY

Read in this order before writing anything:
1. _templates/codex-ingest-contract.md  (the rules)
2. CLAUDE.md                            (TPL constitution + scope + style)
3. _templates/paper-analysis.md         (the 18-section template you fill in)
4. .raw/papers/$KEY/pre-extraction.md   (optional; if present, use as a starter but verify)

Then:
- Resolve the paper via Zotero MCP. Watch out for the Peer Review File trap (per the contract).
- Compose wiki/papers/{year}-{journal-short}-{slug}.md
- Write the 7 stub files in .raw/papers/$KEY/
- Print the JSON receipt to stdout. Single object. No markdown fences.

Self-check before printing the receipt:
- frontmatter complete and address exactly == $ADDR
- 18 sections present
- banned-word scan clean (or justified in-paragraph)
- no em dashes; no double-hyphen as punctuation
- 5 + 5 + 5 + 5 KB outputs

If anything blocks completion, write .raw/papers/$KEY/codex-ingest-failure.md instead of a partial wiki page, and print a receipt with wiki_page=null.
EOF

echo "[$NOW] codex exec starting for $KEY (address $ADDR)" >&2

# codex exec reads the prompt from stdin when - is passed and no positional prompt is set.
codex exec \
  -C "$VAULT_ROOT" \
  -s workspace-write \
  --skip-git-repo-check \
  - < "$PROMPT_FILE" \
  > "$STDOUT_LOG" 2> "$STDERR_LOG"

RC=$?

# Extract the JSON receipt from stdout. The contract requires codex to print
# a single JSON object at the end; the object may span multiple lines, so we
# use Python regex + json.loads rather than line-based jq scanning.
if command -v python3 >/dev/null 2>&1 && [ -s "$STDOUT_LOG" ]; then
  python3 - <<PY 2>/dev/null
import json, re, sys
content = open("$STDOUT_LOG").read()
# Find every balanced { ... } substring (greedy, multiline). Walk from the end
# so the very last receipt JSON wins if codex prints anything earlier.
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
echo "[$DONE] codex exec finished for $KEY (rc=$RC)" >&2
echo "  stdout:  $STDOUT_LOG"
echo "  stderr:  $STDERR_LOG"
echo "  receipt: $RECEIPT"
exit $RC
