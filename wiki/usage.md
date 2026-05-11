---
type: meta
title: "How to Use the Top Paper Lab"
updated: 2026-05-11
tags:
  - meta
  - usage
  - how-to
status: living
related:
  - "[[index]]"
  - "[[hot]]"
  - "[[log]]"
---

# How to Use the Top Paper Lab

Navigation: [[index]] · [[hot]] · [[log]] · [[Wiki Map]]

A practical user manual for this vault. Read once. Bookmark. Come back to a section when you need it.

The vault is a Karpathy-style LLM Wiki specialized for reverse-engineering top-tier energy papers (NE / Joule / NC / NCC / NSus / OE / N) and compounding the analyses into a personal high-impact writing playbook. See [[index]] for what is currently in the lab. See [[hot]] for what changed most recently.

---

## 1. The 7 things you can do

| # | What | Trigger | When to use |
|---|---|---|---|
| 1 | Ingest a paper | `/wiki-ingest <zotero-key or path>` | After you add a paper to the `Top Paper Lab` Zotero collection. Produces an 18-section analysis under `papers/`. |
| 2 | Talk to the lab | `/wiki-query <question>` | Writing strategy, research design, journal positioning, archetype matching, cross-paper synthesis. |
| 3 | Save useful answers | `/save` | After a Q&A produces a result worth keeping (template, decision tree, checklist). Files it into `playbook/`. |
| 4 | Visual maps | `/canvas` | When pattern clusters get dense and prose tables stop helping. |
| 5 | Fill gaps | `/autoresearch <topic>` | When `scripts/boundary-score.py` shows a pattern area with <2 supporting papers. |
| 6 | Health check | `/wiki-lint` | Every 5-10 ingests. Catches banned-words, contradictions, orphan patterns, dead links, weak lessons. |
| 7 | Roll up the log | `/wiki-fold` | When `log.md` hits the next 2^k boundary (k=3 → 8 entries, k=4 → 16, k=5 → 32). Promotes durable claims to named pattern pages. |

---

## 2. How to talk to the lab (the main use)

The single highest-value operation is `/wiki-query`. It reads `hot.md` → `index.md` → `papers.base` → drills into 3-5 relevant `papers/` and `patterns/` pages → answers with file-cited evidence. Good answers get saved back into `playbook/` so the knowledge compounds.

### Three depth modes

| Mode | Trigger | Reads | Cost | Use for |
|---|---|---|---|---|
| Quick | `query quick: ...` or simple factual Q | `hot.md` + `index.md` only | ~1.5k tokens | Date lookups, "what is X", quick facts |
| Standard | default | hot + index + 3-5 pages | ~3k tokens | Most questions |
| Deep | `query deep: ...` or "thorough" | Full wiki, optionally + web | ~8k+ tokens | "Compare X across everything", synthesis, gap analysis |

Pick the depth based on the question. A simple "did the lab cover X?" is quick. "Draft my Intro P3 paragraph from lab evidence" is deep.

### Question patterns that work

**Writing strategy**:
```
/wiki-query "对比 lab 里 4 篇 H2 论文的 Intro 第一段，哪种开篇最值得我借鉴？"
/wiki-query "Lab 里所有 China-case 论文都怎么解释为什么选 China 而不是其他国家？"
/wiki-query "Nature Energy vs Joule 在 Discussion 段落处理 limitations 时有什么差别？"
```

**Research design**:
```
/wiki-query "我要做城市级建筑减碳 TEA，Berrill 2022 的 108-pathway 框架适合吗？"
/wiki-query "Lab 里所有 firm clean baseload 论文（Duan, Ricks）的 system boundary 怎么画？给我对比表。"
/wiki-query "如果我的核心结果对小时电价敏感，IAM 还是 capacity expansion 更合适？给 lab 证据。"
```

**Journal positioning**:
```
/wiki-query "我的稿件是 emerging-tech TEA + threshold mapping，应该投 Joule 还是 Nature Energy？基于 lab 证据。"
/wiki-query "Nature Climate Change 喜欢的 system boundary 是什么？给 Berrill/Ueckerdt 对比。"
```

**Targeted synthesis**:
```
/wiki-query "对比 Vanatta 2023 J 和 Vanatta 2025 NE 的方法演进，告诉我从单期 MILP 到多期 endogenous learning 的 5 个关键建模决策"
/wiki-query "基于 lab 22 篇证据，写一段 SMR-DC-waste-heat 论文的 P5 gap paragraph 草稿，标 Evidence: 给每个论据"
```

### Question patterns that don't work well

- Topics outside Henry's research scope (renewable integration · wind-solar-hydrogen · green-H2 TEA · energy system optimization · building decarb · energy policy). The lab will say so.
- Vague questions ("what's good in the lab?"). Ask about a specific decision you're facing.
- Questions answerable directly from a single paper that you can just read. Save the lab for cross-paper synthesis.

---

## 3. Compounding workflow (the unique value)

This vault gets more useful per ingest. The compounding loop:

```
Ingest paper → cross-paper anchors auto-detected
            → hot.md tracks emerging clusters (≥2 papers each)
            → at paper 10+: pattern pages stub out for clusters
            → at paper 20+: distill playbook pages from patterns
            → /wiki-query draws on patterns + playbook for advice
            → save valuable Q&A back → loop
```

Operationally:

1. **Ingest 5-6 papers** in one go (batch ingest via parallel codex jobs). Each batch ~12 min wall-clock.
2. **Read the new hot.md** after each batch. New cross-paper anchors are listed there.
3. **Ask the lab a question** the new batch made answerable. Save useful answers.
4. **Run `/wiki-lint`** after every 5-10 ingests. Catches drift.
5. **Run `/wiki-fold`** when log hits 8 / 16 / 32 entries. Creates a fold page. Promote durable claims from the fold into named pattern pages.

---

## 4. When you start your own manuscript

The lab's final purpose: support `wiki/projects/{your-paper}/`.

| Step | Tool |
|---|---|
| Create `wiki/projects/{slug}/` | Plain folder. Put working drafts, figure scripts, notes inside. |
| "Which archetype fits my paper?" | `/wiki-query` |
| Load the target venue's structural fingerprint | `research-blueprint <Journal>` (ARS skill) |
| Outline + evidence map | `/ars-outline` |
| Full pipeline draft | `/ars-full` or `academic-pipeline` |
| Find CNS-series citations for prose | `nature-citation` |
| Submission-grade figures | `nature-figure` (asks Python or R first) |
| Polish prose to Nature register | `nature-polishing` |
| Draft Data Availability + repository plan | `nature-data` |
| Pre-submission review with 5 reviewer personas | `academic-paper-reviewer` |
| Handle reviewer comments | `nature-response` + `/ars-revision-coach` |
| Build a journal-club PPT | `nature-paper2ppt` |

At every step, `/wiki-query` can pull evidence from the 22 (and growing) analyzed papers.

---

## 5. Ingest deeper than the default

The default ingest is **L0+L1** (PDF + DA/CA verbatim). 80-90% of writing-playbook value. ~1.0x effort.

If a pattern page or project page needs more, opt in:

| Tier | What it adds | When to trigger |
|---|---|---|
| L0 | PDF only | Always (default) |
| L1 | + DA/CA verbatim | Always (default, cheap) |
| L2 | + SI methods / SI tables | When a pattern page needs SI-only equations or sensitivity-table density |
| L3 | + data / code repository inspection | When you are about to reuse the modeling technique in your own `projects/` |

L2/L3 are opt-in, named-by-paper, and produce extra stubs (`si-methods-notes.md`, `code-walkthrough.md`) alongside the 7 default stubs. They never copy binaries into the vault: Zotero storage stays source of truth.

---

## 6. Mandatory discipline (constraints from [[../CLAUDE|CLAUDE.md]])

When the lab writes anything substantive, it must tag with one of three labels:

- **Evidence**: directly supported by paper text / figure / table / SI / DA / CA / referenced repo. Cite section, figure number, page.
- **Inference**: derived interpretation, not literally stated. Mark confidence high / medium / low.
- **Lesson**: transferable insight for Henry's own research or writing. State *what to do* concretely.

Banned words (used only with same-paragraph concrete justification):

`innovative · important · rigorous · comprehensive · novel · significant · high-impact · seminal · well-written · clear · elegant · groundbreaking`

No em dashes (U+2014). No double-hyphen as punctuation. Periods, commas, colons, parentheses, single hyphens only.

Style: short, direct. Tables for cross-paper data. Prose for argumentation. No trailing summaries.

---

## 7. Cross-project consult

To consult the lab from a different Claude Code project, add this to that project's `CLAUDE.md`:

```markdown
## Top Paper Lab consult

Path: /Users/henry/Library/Mobile Documents/iCloud~md~obsidian/Documents/claude-obsidian/

When the question is about top-tier energy-paper writing strategy, contribution framing, or journal fit:

1. Read wiki/hot.md (recent context).
2. Read wiki/index.md.
3. Search wiki/papers/ and wiki/patterns/ for relevant pages.
4. Cite specific paper-analysis pages.

Do NOT consult for anything outside renewable energy / wind-solar-hydrogen / TEA / energy-system-optimization / building decarbonization scope.
```

---

## 8. Read this if something looks wrong

- **`/wiki-ingest` fails on PDF resolution** → check whether Zotero desktop is running. Zotero MCP needs it open.
- **Codex Zotero MCP cancelled** → codex falls back to local Zotero SQLite + storage cache. `fulltext_source: main-pdf` if successful; `fulltext_source: unknown` if both fallbacks fail (rare, e.g. UIWZD5EE which had no PDF attachment).
- **Address counter drift** → run `./scripts/allocate-address.sh --rebuild` (rebuilds from max observed page address in vault).
- **Empty `pattern/` page or single-paper "premature pattern"** → wait for the second supporting paper. Don't stub.
- **`wiki-fold` says no changes** → log hasn't reached the next 2^k boundary.

---

## 9. What this vault is NOT

- NOT a general second-brain or note-taking app. Use Apple Notes for groceries.
- NOT for non-energy research questions. The lab will refuse those.
- NOT a Zotero replacement. Zotero is the bibliographic + binary source of truth; this vault only stores analysis text.
- NOT for storing PDFs / SI / source-data. `.raw/papers/` is text-only stubs (~5-10 KB per paper). `.gitignore` catches accidental binary drops.
- NOT a CI/CD or coding project. The 4 DragonScale scripts (`allocate-address.sh`, `tiling-check.py`, `boundary-score.py`, `wiki-fold` via skill) are the only active machinery.

---

## 10. The 30-second mental model

```
You add papers to Zotero "Top Paper Lab" collection.
You /wiki-ingest them (default: PDF + DA/CA, 8-12 min/paper via codex).
You /wiki-query for writing or research-design advice.
You save useful Q&A with /save.
Patterns emerge at paper 10+; playbook entries crystallize at paper 20+.
When you start writing your own paper, you go to wiki/projects/,
and the 22+ analyses become your evidence base + writing coach.
```

That is the entire loop.

---

## Skills directly relevant (cheat sheet)

| Skill | One-line purpose |
|---|---|
| `/wiki-ingest` | Add a paper analysis |
| `/wiki-query` | Ask the lab anything in scope |
| `/wiki-lint` | Health-check |
| `/wiki-fold` | Roll up `log.md` to a `folds/` page |
| `/save` | File a useful Q&A as playbook page |
| `/canvas` | Visual relationship map |
| `/autoresearch` | Fill an under-covered pattern area |
| `/defuddle` | Clean a publisher landing page before snapshot |
| `obsidian-bases` | Author Bases dashboards over `papers/` |
| `obsidian-markdown` | Wikilink / callout / frontmatter discipline |
| `pre-review-brief` | Per-paper deep-analysis core (ARS) |
| `research-blueprint` | Venue structural fingerprint (ARS) |
| `academic-paper-reviewer` | Multi-persona simulated review (ARS) |
| `ars-lit-review` | Cross-paper annotated bibliography (ARS) |
| `academic-paper` | Henry's own drafting pipeline (ARS) |
| `academic-pipeline` | End-to-end: research → publish (ARS) |
| `deep-research` | Topic exploration beyond Zotero (ARS) |
| `nature-citation` | Strict CNS-series citation expansion |
| `nature-figure` | Submission-grade figure production |
| `nature-polishing` | Nature-leaning English polish |
| `nature-response` | Reviewer response letter |
| `nature-data` | Data Availability + repo planning |
| `nature-paper2ppt` | Journal-club PPT from a paper |

---

## Constants you may need

- Lab counter: see `.vault-meta/address-counter.txt`
- Lab manifest: `.raw/zotero_manifest/top_paper_lab_manifest.csv` (142 papers; 22 reviewed as of 2026-05-11)
- Codex contract: `_templates/codex-ingest-contract.md`
- Codex wrapper: `scripts/codex-ingest-paper.sh <KEY> <ADDR> [SLUG]`
- TPL constitution: [[../CLAUDE|CLAUDE.md]]
- Pre-fork archive: [[_meta/old-index|wiki/_meta/]]
