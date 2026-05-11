---
name: wiki-query
description: "Answer questions using the Obsidian wiki vault. Reads hot cache first, then index, then relevant pages. Synthesizes answers with citations. Files good answers back as wiki pages. Supports quick, standard, and deep modes. Triggers on: what do you know about, query:, what is, explain, summarize, find in wiki, search the wiki, based on the wiki, wiki query quick, wiki query deep."
allowed-tools: Read Glob Grep
---

# wiki-query: Query the Wiki

The wiki has already done the synthesis work. Read strategically, answer precisely, and file good answers back so the knowledge compounds.

---

## Query Modes

Three depths. Choose based on the question complexity.

| Mode | Trigger | Reads | Token cost | Best for |
|------|---------|-------|------------|---------|
| **Quick** | `query quick: ...` or simple factual Q | hot.md + index.md only | ~1,500 | "What is X?", date lookups, quick facts |
| **Standard** | default (no flag) | hot.md + index + 3-5 pages | ~3,000 | Most questions |
| **Deep** | `query deep: ...` or "thorough", "comprehensive" | Full wiki + optional web | ~8,000+ | "Compare A vs B across everything", synthesis, gap analysis |

---

## Quick Mode

Use when the answer is likely in the hot cache or index summary.

1. Read `wiki/hot.md`. If it answers the question, respond immediately.
2. If not, read `wiki/index.md`. Scan descriptions for the answer.
3. If found in index summary, respond and do not open any pages.
4. If not found, say "Not in quick cache. Run as standard query?"

Do not open individual wiki pages in quick mode.

---

## Standard Query Workflow

1. **Read** `wiki/hot.md` first. It may already have the answer or directly relevant context.
2. **Read** `wiki/index.md` to find the most relevant pages (scan for titles and descriptions).
3. **Read** those pages. Follow wikilinks to depth-2 for key entities. No deeper.
4. **Synthesize** the answer in chat. Cite sources with wikilinks: `(Source: [[Page Name]])`.
5. **Offer to file** the answer: "This analysis seems worth keeping. Should I save it as `wiki/questions/answer-name.md`?"
6. If the question reveals a **gap**: say "I don't have enough on X. Want to find a source?"

---

## Deep Mode

Use for synthesis questions, comparisons, or "tell me everything about X."

1. Read `wiki/hot.md` and `wiki/index.md`.
2. Identify all relevant sections (concepts, entities, sources, comparisons).
3. Read every relevant page. No skipping.
4. If wiki coverage is thin, offer to supplement with web search.
5. Synthesize a comprehensive answer with full citations.
6. Always file the result back as a wiki page. Deep answers are too valuable to lose.

---

## Token Discipline

Read the minimum needed:

| Start with | Cost (approx) | When to stop |
|------------|---------------|--------------|
| hot.md | ~500 tokens | If it has the answer |
| index.md | ~1000 tokens | If you can identify 3-5 relevant pages |
| 3-5 wiki pages | ~300 tokens each | Usually sufficient |
| 10+ wiki pages | expensive | Only for synthesis across the entire wiki |

If hot.md has the answer, respond without reading further.

---

## Index Format Reference

The master index (`wiki/index.md`) looks like:

```markdown
## Domains
- [[Domain Name]]: description (N sources)

## Entities
- [[Entity Name]]: role (first: [[Source]])

## Concepts
- [[Concept Name]]: definition (status: developing)

## Sources
- [[Source Title]]: author, date, type

## Questions
- [[Question Title]]: answer summary
```

Scan the section headers first to determine which sections to read.

---

## Domain Sub-Index Format

Each domain folder has a `_index.md` for focused lookups:

```markdown
---
type: meta
title: "Entities Index"
updated: YYYY-MM-DD
---
# Entities

## People
- [[Person Name]]: role, org

## Organizations
- [[Org Name]]: what they do

## Products
- [[Product Name]]: category
```

Use sub-indexes when the question is scoped to one domain. Avoid reading the full master index for narrow queries.

---

## Filing Answers Back

Good answers compound into the wiki. Don't let insights disappear into chat history.

When filing an answer:

```yaml
---
type: question
title: "Short descriptive title"
question: "The exact query as asked."
answer_quality: solid
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [question, <domain>]
related:
  - "[[Page referenced in answer]]"
sources:
  - "[[wiki/sources/relevant-source.md]]"
status: developing
---
```

Then write the answer as the page body. Include citations. Link every mentioned concept or entity.

After filing, add an entry to `wiki/index.md` under Questions and append to `wiki/log.md`.

---

## Gap Handling

If the question cannot be answered from the wiki:

1. Say clearly: "I don't have enough in the wiki to answer this well."
2. Identify the specific gap: "I have nothing on [subtopic]."
3. Suggest: "Want to find a source on this? I can help you search or process one."
4. Do not fabricate. Do not answer from training data if the question is about the specific domain in this wiki.

---

## TPL Mode: Top Paper Lab v2 layer-aware routing

**Trigger**: vault has `wiki/_meta/journal-role-vocab.md`, `wiki/papers/L1/`, and `wiki/papers/L2/`. When triggered, this mode REPLACES the generic Standard / Deep workflows for any question scoped to top-tier energy paper writing, methodology, parameters, contribution framing, journal fit, or Henry's own manuscripts.

```bash
if [ -f wiki/_meta/journal-role-vocab.md ] && [ -d wiki/papers/L1 ] && [ -d wiki/papers/L2 ]; then
  TPL_V2=1
else
  TPL_V2=0
fi
```

If `TPL_V2=0`, fall through to the generic Standard / Deep workflows above.

### Out-of-scope guard (run first)

TPL covers: renewable energy integration · wind-solar-hydrogen integrated systems · green hydrogen TEA · energy system optimization · building energy + emission reduction · energy policy and cost analysis. **For any question outside this scope, do not consult the wiki. Say so and stop.** Reading L1/L2 pages on unrelated topics adds noise and wastes tokens.

### Question classification (decides which layer to read)

Classify the question into one of five intents. Each intent has its own evidence path.

| Intent | Examples | Layer to read | Entry points |
|---|---|---|---|
| **A. Writing craft** (Intro, title, abstract, figure narrative, Discussion elevation, contribution framing, archetype) | "How do top-tier Intros open?", "What's a Joule-grade contribution claim?", "What does a Nature Energy figure 1 do?" | L1 only | `playbook/top-journal-craft/*` → `patterns/cross-cutting/{intro,figure,discussion,archetype,contribution}/*` → relevant `papers/L1/*` |
| **B. Methods / parameters / technical depth** | "What electrolyzer CAPEX should I use?", "How is LCOH typically decomposed?", "How are sensitivity tables structured?", "What's a typical case-study justification for an EU+UK study?" | banks + L2 (+ L1 contrast if useful) | `banks/{parameter,sensitivity,method}-bank/*` → `patterns/subdomain/{slug}/*` → `papers/L2/{slug}/*` |
| **C. Comparison / delta** (top-vs-applied; same topic at two layers) | "What does Joule do that AE doesn't?", "What's missing from an applied paper that would make it Joule-tier?" | both layers via comparisons | `patterns/comparisons/*` → both `papers/L1/*` and `papers/L2/*/*` |
| **D. Subdomain-scoped** (everything we know about hydrogen / power systems / etc.) | "Summarize TPL's hydrogen-p2x evidence", "What buildings papers do I have?" | both layers, scoped | `subdomains/{slug}.md` hub → drill into `papers/L1/*` and `papers/L2/{slug}/*` |
| **E. Cross-subdomain / bridge** (interface between two subdomains) | "What do papers say at the H2 + power-systems interface?" | both layers via bridge | `bridges/{A}--{B}.md` (if exists, 3+ paper gate) → fall back to filtering both hubs |

If a question is mixed (most are): start with the *highest-priority* intent (writing craft beats methods if both apply), then surface the other intent's evidence in a separate section of the answer.

### Read order (replaces generic Standard workflow when TPL_V2=1)

```
hot.md  →  index.md  →  classify intent  →  entry point per the table above
                                          →  drill down to specific paper pages
                                          →  synthesize with explicit citations
```

Token discipline: even in deep mode, the L1 corpus alone is 22 papers × ~25 KB ≈ 550 KB. Always pre-filter via:

1. `subdomains/{slug}.md` hubs (1-3 KB each, list relevant papers)
2. `papers.base` Bases queries (the views are pre-built: All / L1 / L2-deep / By subdomain / By archetype / High-relevance / Upgrade candidates / Drafts)
3. `index.md`

…and only THEN open specific paper pages.

### Using `papers.base` for filtered retrieval

`wiki/papers.base` exposes 10 views. Typical query → view mapping:

| Question | View to consult |
|---|---|
| "What L1 papers do we have on hydrogen?" | "By subdomain" filtered to `hydrogen-p2x` |
| "Which L2 papers were deep-analyzed?" | "L2-deep" |
| "Which papers spoke to relevance for my SMR-DC manuscript?" | "High-relevance" |
| "Which papers are candidates for L2→L1 promotion?" | "Upgrade candidates" |
| "What archetypes are dominant in my corpus?" | "By archetype" |

Read the Base file once; remember its filter definitions for the session.

### Frontmatter-aware filtering when paper pages aren't open

When the question is "do we have any paper on X?" and you have not opened any paper page yet, prefer grepping frontmatter over reading full pages:

```bash
grep -l "subdomain_primary:" wiki/papers/L1/*.md wiki/papers/L2/**/*.md | \
  xargs grep -l "hydrogen-p2x"
```

Then open only the 3-5 most-promising pages.

### Citation discipline in answers

Every assertion in the answer must carry **one** of these in the same sentence or the same paragraph:

- **`Evidence:`** : directly supported by a paper page section / figure / table you read. Cite as `(Source: [[year-journal-slug]] §K)`.
- **`Inference:`** : reasonable interpretation from the wiki, not directly stated. Mark confidence (high / medium / low).
- **`Lesson:`** : transferable insight for Henry's writing. Must say *what to do* concretely.

If the answer cannot be tagged, do not promote it from chat to a `playbook/` page.

### Anti-fluff rule (re-stated)

These words may appear ONLY with a same-sentence concrete justification: `innovative · important · rigorous · comprehensive · novel · significant · high-impact · seminal · well-written · clear · elegant · groundbreaking`. To use any of them, specify *innovative in what aspect*, *important for what audience*, *rigorous in which methodological choice*, *comprehensive across which axis*. If the concrete claim is not available, drop the word.

### Filing valuable answers back

When a TPL answer surfaces a synthesis (e.g., "compare Intros across these 5 L1 papers"), file it under the right layer:

| Answer shape | Target file |
|---|---|
| Generalizable top-journal writing rule (with L1-only evidence) | `wiki/playbook/top-journal-craft/{slug}.md` |
| Methods / parameter rule (with L2 evidence, optionally L1 contrast) | `wiki/playbook/applied-paper-craft/{slug}.md` or `wiki/banks/{relevant-bank}/{slug}.md` |
| Top-vs-applied delta | `wiki/patterns/comparisons/{slug}.md` |
| Subdomain-specific pattern | `wiki/patterns/subdomain/{slug}/{topic}.md` |
| Bridge pattern (3+ papers across two subdomains) | `wiki/patterns/bridges/{A}--{B}/{topic}.md` |
| Specific manuscript advice | `wiki/projects/{manuscript-slug}/notes/{slug}.md` |

After filing, update `wiki/index.md`, append to `wiki/log.md`, refresh `wiki/hot.md` if it changes the recent-context picture. The PostToolUse hook auto-stages but does not commit.

### Synthesis gate

Until the lab has 10 L1 paper analyses ingested, **do not** materialize new pattern pages from a query. Pattern pages emerge bottom-up at the first `/wiki-fold` (log size 8). Until then, file syntheses under `playbook/` (when L1-only) or as new `_about.md`-style stubs.

After paper 10, pattern materialization from queries is allowed; cross-check the no-pollution rule (L1-only pattern paths must not cite L2 as primary evidence).

### Cross-project consult

If this skill is invoked from outside the TPL vault (cross-project consult), follow CLAUDE.md "Cross-project access" section: read `wiki/hot.md` → `wiki/index.md` → relevant subdomain hub → drill. Cite specific paper-analysis pages with absolute paths under `/Users/henry/Library/Mobile Documents/iCloud~md~obsidian/Documents/claude-obsidian/`.
