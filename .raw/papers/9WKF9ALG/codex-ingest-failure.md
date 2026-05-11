# Codex Ingest Failure

Zotero key: `9WKF9ALG`
Address requested: `c-000031`
Requested ingest depth: `B_medium`
Requested primary subdomain: `hydrogen-p2x`

Blocker: wrong journal tier for the L2-B contract.

Evidence: Zotero resolves the item as `ACS Sustainable Chemistry & Engineering`, while `wiki/_meta/journal-role-vocab.md` does not list that journal under `applied_flagship`. Per `_templates/codex-ingest-contract-L2-B.md`, a non-`applied_flagship` paper must abort before a wiki page is written.

See: `.raw/papers/9WKF9ALG/wrong-tier.md`
