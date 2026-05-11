---
type: meta
title: "Operation Log"
updated: 2026-05-11
tags:
  - meta
  - log
status: evergreen
related:
  - "[[index]]"
  - "[[hot]]"
---

# Operation Log

Navigation: [[index]] | [[hot]] | [[usage|How to use this vault]]

Append-only. New entries go at the TOP. Never edit past entries.

Entry format: `## [YYYY-MM-DD] operation | Title`

Parse recent entries: `grep "^## \[" wiki/log.md | head -10`

---

## [2026-05-11] ingest | Colangelo et al. 2026, Nature Energy, AI data centres as grid-interactive assets (via codex, batch 4)

- Zotero: `KWNBZ8FA`
- Analysis: [[papers/2026-NE-ai-data-centres-grid-interactive]] (address `c-000024`, 30.2KB)
- Receipt: all checks pass. `fulltext_source: main-pdf` via OneDrive Zotero backup SQLite (active /Users/henry/Zotero/zotero.sqlite was empty for this key).
- Key insight: **first field-trial paper in the lab** — Phoenix 256-GPU production AI cluster shows software workload orchestration can cut cluster power 25% for 3 hours during grid peaks with QoS intact. Empirically settles a question that 3 of our modeling papers (Zheng 2020 J, Berrill 2022 NCC, Kikstra 2021 NE) had to assume.
- Cross-cluster: pairs with Zheng 2020 J (UELISBYS) as the "DC as grid asset" empirical complement to Zheng's macroscale counterfactual.

## [2026-05-11] ingest | Mytton & Ashtine 2022, Joule, data center energy estimates review (via codex, batch 4)

- Zotero: `52W57HP5`; main PDF `Q6LYUHSZ`
- Analysis: [[papers/2022-J-data-center-energy-estimates-review]] (address `c-000023`, 35KB)
- Receipt: all checks pass. `fulltext_source: main-pdf` via local Zotero SQLite + storage cache fallback.
- Key insight: 258 DC energy estimates from 46 publications 2007-2021, 676 source links audited. Reliability problems come from provenance (private market data, broken links, vague methods, future extrapolation), not from one bad number. **Methodology gate for any DC-load paper in the lab**: a paper that doesn't audit its DC load inputs will get reviewer-killed.
- Lesson archetype: provenance-audit as primary contribution — same archetype as Liu 2015 N (emissions inventory correction) but applied to estimates rather than measurements.

## [2026-05-11] ingest | Vanatta, Stewart & Craig 2025, Nature Energy, SMR policy + module learning (via codex, batch 4)

- Zotero: `SYGLCEMJ`
- Analysis: [[papers/2025-NE-smr-policy-module-learning]] (address `c-000022`, 37.5KB)
- Receipt: all checks pass. `fulltext_source: main-pdf` via local Zotero SQLite + storage cache fallback.
- Key insight: profit-max deployment of 4 SMR designs at 925 US industrial facilities 2030-2050. Deployment gated by delivered gas price, FOAK capex escalation, factory learning rate, carbon tax, ITC — direct early subsidies have weak effect compared to learning + carbon price.
- Cross-cluster: **same Michigan group (Vanatta + Craig) as 2023 J SMR-industrial-heat paper** (XUGL6XPD, address c-000019). The two together form a methodologically-sequential pair (single-period MILP → multi-period deployment with endogenous learning). Critical pair for understanding SMR economics in industrial heat contexts.

## [2026-05-11] ingest | Vanatta et al. 2023, Joule, SMR industrial process heat TEA (via codex, batch 4)

- Zotero: `XUGL6XPD`
- Analysis: [[papers/2023-J-smr-industrial-process-heat-tea]] (address `c-000019`, 40.1KB)
- Receipt: all checks pass. `fulltext_source: main-pdf` via local Zotero SQLite + storage cache fallback.
- Key insight: profit-maximizing MILP over 5 SMR designs × 421 natural-gas industrial processes in ERCOT/SPP. SMRs **not economic for heat alone** at 2021 gas prices, but serve 125 SPP processes when heat is paired with wholesale electricity revenue. This is the dual-product (heat + power) framework Henry needs for the SMR + DC + ORC paper.
- Cross-cluster: **direct framework archetype for Henry's planned SMR-DC-waste-heat paper**. Pair with SYGLCEMJ (same group, follow-up paper) and 5CAVXPE9 (flexible geothermal, same firm-clean-flexible archetype).

## [2026-05-11] ingest | Ricks et al. 2024, Nature Energy, flexible geothermal in decarbonized systems (via codex, batch 4)

- Zotero: `5CAVXPE9`; main PDF `MD6GQT4Q`
- Analysis: [[papers/2024-NE-flexible-geothermal-decarb-systems]] (address `c-000021`, 41.4KB)
- Receipt: all checks pass. `fulltext_source: main-pdf` via Zotero indexed full-text cache.
- Key insight: GenX capacity-expansion with flexible vs inflexible EGS, 11-zone Western Interconnection 2045. **EGS flexibility changes system value far more than EGS LCOE**. The paper's strongest move: scale transition from prior plant-level (price-taker) work to system-level (capacity-expansion) deployment.
- Cross-cluster: forms a "firm-clean-flexible baseload" cluster with Duan 2022 NE (flexible nuclear). Same archetype: "when does firm-flexible enter the least-cost system, and what does it displace?" Both answer "beyond ~80% emissions cuts; displaces storage, transmission, wind/solar."

## [2026-05-11] ingest | Duan et al. 2022, Nature Energy, flexible nuclear in deep-decarb electricity (via codex, batch 4)

- Zotero: `SYZJZS6F`
- Analysis: [[papers/2022-NE-flexible-nuclear-deep-decarb]] (address `c-000020`, 35.1KB)
- Receipt: all checks pass. `fulltext_source: main-pdf` via local Zotero SQLite + storage cache fallback.
- Key insight: Macro Energy Model, 42 country-level regions, hourly LP. Flexible nuclear + thermal energy storage is excluded under moderate emissions cuts; enters least-cost portfolios **beyond ~80% emissions reduction**, especially where wind resources are weak and low-cost grid-flexibility substitutes are absent.
- Cross-cluster: foundational paper for the firm-clean-flexible cluster. Pairs with Ricks 2024 NE (EGS) as the same archetype applied to a different firm clean technology. Strong global-vs-regional contrast: Duan covers 42 regions globally; Ricks does 11-zone Western US deep-dive.

## [2026-05-11] ingest | Odenweller et al. 2022, Nature Energy, probabilistic green H2 feasibility (via codex, batch 3)

- Zotero: `KRT75D4W`
- Analysis: [[papers/2022-NE-green-h2-probabilistic-feasibility]] (address `c-000018`, 40KB)
- Receipt: all checks pass. `fulltext_source: main-pdf` via local Zotero SQLite + storage fallback (Zotero MCP cancelled).
- Key insight: Monte-Carlo feasibility envelope using Wright's-law-fit ensembles over analog technologies (wind, solar, batteries) shows green H2 stays below 1% of EU final energy until 2030 and 1% globally until 2035 with ≥75% probability under "wind-and-solar-like" growth. Headline pattern: probability + threshold + date is more useful than a single feasibility point estimate.
- Cross-cluster: pairs with Cherp 2021 NE (growth-curve fitting), strengthens the empirical-feasibility-envelope pattern. Same first-author Ueckerdt overlap with Ueckerdt et al. 2021 NCC (same batch).

## [2026-05-11] ingest | Helveston, He & Davidson 2022, Nature, solar PV supply chain cost savings (via codex, batch 3)

- Zotero: `B6LNILBU`
- Analysis: [[papers/2022-N-solar-pv-supply-chain-cost-savings]] (address `c-000017`, 39.9KB)
- Receipt: all checks pass. `fulltext_source: main-pdf` via local Zotero SQLite + storage cache.
- Key insight: globalized PV module markets saved installers US$67 billion cumulatively 2008-2020 (China $36B + US $24B + Germany $7B); nationalizing supply chains would cost the deployment debt the world cannot afford. Archetype: counterfactual-cost-savings on the supply chain itself, not on the technology.
- Cross-cluster: novel archetype in the lab — first paper centering supply-chain geography rather than technology cost. Loose link to Wang 2023 N (plant-level optimization) via PV economics; conceptual link to Liu 2015 N (data-correction archetype) via "what gets counted shapes policy".

## [2026-05-11] ingest | Berrill et al. 2022, Nature Climate Change, US residential decarbonization (via codex, batch 3)

- Zotero: `VMSZ42JG`; main PDF `UDF7CJ47`
- Analysis: [[papers/2022-NCC-residential-decarbonization-us]] (address `c-000016`, 35KB)
- Receipt: all checks pass. `fulltext_source: main-pdf` via Zotero storage cache.
- Key insight: 108-pathway national stock-level scenario frame (3 housing-stock × 4 new-housing × 3 renovation × 3 supply paths, 2020-2060) reaches 91% emissions reduction by 2050 only when renovation + new-build efficiency + electrification + sufficiency (smaller homes, multifamily growth) + clean grid combine. **First building-energy paper in the lab** (directly in Henry's scope).
- Cross-cluster: opens patterns/buildings/ subfolder candidate; pairs with Kikstra 2021 NE on demand-side framing (residential energy can be the demand lever).

## [2026-05-11] ingest | Ueckerdt et al. 2021, Nature Climate Change, H2 e-fuels potential and risks (via codex, batch 3)

- Zotero: `UIWZD5EE`
- Analysis: [[papers/2021-NCC-h2-efuels-potential-risks]] (address `c-000015`, 36KB)
- Receipt: all checks pass except `fulltext_source: unknown` — Zotero had no PDF attachment for this key; codex fell back to the Nature article page + ResearchGate author preprint. Deviation documented. Analysis quality is intact (18 sections, 5/5/5/5, banned-word check passed, three-label discipline applied).
- Key insight: e-fuel routes deliver 16-48% electricity-to-useful-energy efficiency (2-10x more renewable electricity than direct electrification); 2050 MACC of EUR20-270/tCO2 only after deep scale-up. The merit-order argument forces a sorting rule on policy: ration e-fuels to sectors inaccessible to direct electrification.
- Cross-cluster: anchors the option-value-with-discipline pattern. Strong link to Wolfram 2024 OE (same batch, same H2-option-value frame but global IAM vs perspective-synthesis). Strong link to Zeyen 2023 NC (endogenous learning) and Giovanniello 2024 NE (additionality framework).
- **Follow-up**: a PDF attachment for `UIWZD5EE` should be added to Zotero so a Pass-2 can verify the analysis against the actual main-PDF text (same situation as the original M9HYZCZE issue).

## [2026-05-11] ingest | Wolfram et al. 2024, One Earth, H2 economy 22% cost reduction (via codex, batch 3)

- Zotero: `73CKKQFI`; main PDF `8GFTMJCS`
- Analysis: [[papers/2024-OE-h2-economy-22pct-cost-reduction]] (address `c-000014`, 38KB)
- Receipt: all checks pass. `fulltext_source: main-pdf` via local Zotero SQLite + storage cache.
- Key insight: **first One Earth paper in the lab**. GCAM scenario pairs (with-H2 vs no-H2, full option set vs end-use exclusions) demonstrate that hydrogen at only 3-9% of 2050 final energy can yield 15-22% mitigation-cost reduction — its value is option value, not adoption share. International shipping is the highest-value end use (~6.4% cost reduction alone).
- Cross-cluster: directly informs an option-value-scenario-pair pattern with Yang 2022 NE (China TIMES-VEDA), Zeyen 2023 NC (endogenous learning, sector-coupled), and Giovanniello 2024 NE (additionality). Strong methodological contrast: global IAM breadth (Wolfram) vs national sector detail (Yang) vs European sector-coupled optimization (Zeyen) vs grid-emissions accounting (Giovanniello).

## [2026-05-11] ingest | Cherp et al. 2021, Nature Energy, national wind/solar growth dynamics (via codex, batch 2)

- Zotero: `L8UI4RX3`; main PDF `SBU9QH66` per receipt
- Analysis: [[papers/2021-NE-national-wind-solar-growth-dynamics]] (address `c-000013`, 39KB)
- Composed by `codex exec` (gpt-5.5 + xhigh) per contract V2 (which now requires `## Cross-references`).
- Receipt: all checks pass. `fulltext_source: main-pdf` via local Zotero SQLite + storage fallback.
- Key insight: ex-post growth-curve fitting on 60-country data sets empirical ceilings for renewable deployment. The "leader country" framing converts feasibility from prescriptive to historical, sidestepping the technology-vs-policy debate.
- Codex autodetected anchor with Wang 2023 N (paper 3) on national wind/solar deployment at scale.

## [2026-05-11] ingest | Zhang et al. 2023, Nature Communications, rooftop PV China (via codex, batch 2)

- Zotero: `CRAKEP8V`
- Analysis: [[papers/2023-NC-rooftop-pv-china-carbon]] (address `c-000012`, 32.8KB)
- Receipt: all checks pass. `fulltext_source: main-pdf`.
- Key insight: bottom-up rooftop assessment for 354 Chinese cities converts a national policy target (PV by 2030) into a city-level deployment map with grid-parity overlay. Cross-system anchor with Wang 2023 N (utility-scale PV+wind plant placement) — rooftop vs utility-scale resolution contrast.
- Initial wrapper-side receipt extraction failed (multi-line JSON bug); rescued from stdout manually. Wrapper fixed for future runs.

## [2026-05-11] ingest | Zheng et al. 2020, Joule, data center load migration + curtailment (via codex, batch 2)

- Zotero: `UELISBYS`; main PDF `2LS5AM2J`
- Analysis: [[papers/2020-J-data-center-load-migration-curtailment]] (address `c-000011`, 36.5KB)
- Receipt: all checks pass. `fulltext_source: main-pdf`.
- Key insight: spatial load migration as demand-side mitigation. Codex autodetected three cross-paper anchors in its own Cross-references: with Che 2025 J (threshold-based system TEA), Kikstra 2021 NE (demand-side load-change framing), Giovanniello 2024 NE (hourly grid-emissions + flexible H2 relevance). This is the **first batch where codex generated cross-paper anchors automatically**, validating contract V2.

## [2026-05-11] ingest | Klaaßen & Steffen 2023, Nature Climate Change, net-zero investment meta-analysis (via codex, batch 2)

- Zotero: `A4EZAC5U`
- Analysis: [[papers/2023-NCC-net-zero-investment-shifts-europe]] (address `c-000010`, 33.5KB)
- Receipt: all checks pass. `fulltext_source: main-pdf` (via ETH accepted-version PDF + Nature page fallback; Zotero MCP blocked as usual).
- Key insight: meta-analysis as primary archetype. Harmonizing 21 European net-zero scenarios converts a fragmented literature into a citable headline (10x clean-energy investment, 9x fossil disinvestment). Method note: deals with scenario-set noise by harmonization, not by adding a 22nd scenario.

## [2026-05-11] ingest | Liu et al. 2015, Nature, China CO2 emissions revised (via codex, batch 2)

- Zotero: `H998SFTH`
- Analysis: [[papers/2015-N-china-fossil-cement-co2-revised]] (address `c-000009`, 35.3KB)
- Receipt: all checks pass. `fulltext_source: main-pdf` (via author-uploaded PDF; Zotero MCP blocked; SQLite lookup also missed). Note: DA/CA not explicit in published paper.
- Key insight: this is the famous 2015 Liu paper that cut China's reported 2000-2013 fossil + cement CO2 by ~14%. Archetype is data-correction-as-primary-contribution — pre-tier-1-energy-literature, but landed in Nature because the magnitude was policy-relevant globally. Useful counterpoint to modeling-heavy papers in the lab.

## [2026-05-11] ingest | Kikstra et al. 2021, Nature Energy, COVID-19 demand scenarios (via codex)

- Zotero: `QDU6TZYF` (parent journalArticle)
- Paper package: `.raw/papers/QDU6TZYF/` (7 stubs + codex receipt + logs)
- Analysis: [[papers/2021-NE-kikstra-covid-energy-demand-scenarios]] (address `c-000008`, 35KB)
- Composed by: `codex exec` (gpt-5.5 + xhigh) per `_templates/codex-ingest-contract.md`
- Receipt: all checks pass. `fulltext_source: main-pdf` via local Zotero PDF (SI not in Zotero per DA).
- Key insight: demand-side perturbation can act as a scenario lever in IAMs without changing supply assumptions. The paper anchors the IAM-side "what counts as a credible exogenous shock" debate.
- Random sample (codex pick #3 of 3).

## [2026-05-11] ingest | Zeyen et al. 2023, Nature Communications, endogenous learning green H2 (via codex)

- Zotero: `T3YPX6LR` (parent journalArticle); one PDF child
- Paper package: `.raw/papers/T3YPX6LR/` (7 stubs + codex receipt + logs)
- Analysis: [[papers/2023-NC-endogenous-learning-green-h2-europe]] (address `c-000007`, 40KB / largest of the codex batch)
- Composed by: `codex exec` (gpt-5.5 + xhigh) per `_templates/codex-ingest-contract.md`
- Receipt: all checks pass. `fulltext_source: main-pdf` via local Zotero SQLite + storage cache.
- **Critical cross-paper anchor**: paper 2 (Giovanniello 2024 NE) explicitly diagnoses Zeyen's framework as "non-compete" additionality (annual matching looks safer because contracted H2 resources are optimized *after* non-H2 grid investments). Co-ingesting both in this batch is the seed for a future `patterns/methods/additionality-counterfactuals` page once paper count hits 10.
- Key insight: endogenous learning in sector-coupled models removes the exogenous-cost-trajectory degree of freedom that critics of Yang 2022 (paper 1) and Wang 2023 (paper 3) would otherwise exploit.
- Random sample (codex pick #2 of 3).

## [2026-05-11] ingest | Che et al. 2025, Joule, space-based solar Europe (via codex)

- Zotero: `M9HYZCZE` (parent journalArticle); NO PDF attachment in Zotero (Henry to add)
- Paper package: `.raw/papers/M9HYZCZE/` (7 stubs + codex receipt + logs)
- Analysis: [[papers/2025-J-space-based-solar-europe]] (address `c-000006`, 34KB)
- Composed by: `codex exec` (gpt-5.5 + xhigh) per `_templates/codex-ingest-contract.md`
- Receipt: all checks pass. `fulltext_source: unknown` (Zotero had no PDF child; codex used publisher HTML + PyPSA-Eur repo pages as supplemental).
- Method note: PyPSA-Eur (well-known European open-source power-system model). Code repository linked in CA.
- Key insight: emerging energy technologies become decision-relevant when their cost-availability pair crosses a system-cost threshold. Frames the SBSP question as "at what cost-availability point does the optimizer choose it" rather than "is SBSP cheap enough today."
- Action item: attach PDF to Zotero parent item M9HYZCZE to enable future SI / source-data analysis.
- Random sample (codex pick #1 of 3).

## [2026-05-11] ingest | Wang et al. 2023, Nature, PV+wind China 3844 plants (via codex)

- Zotero: `T5W8LVA9` (parent); PDFs `DM5DMFZD` (main) + `UVK9RAXN` (SI); 19 authors
- Paper package: `.raw/papers/T5W8LVA9/` (7 stubs + codex receipt + logs)
- Analysis: [[papers/2023-N-china-pv-wind-3844-plants]] (address `c-000005`, 30KB, 274 lines)
- Composed by: `codex exec` (gpt-5.5 + xhigh) per `_templates/codex-ingest-contract.md`
- Receipt: all checks pass (18 sections, banned-words clean, em-dash clean, 3-label discipline applied, 5+5+5+5 KB outputs)
- Deviation: Zotero MCP failed in `workspace-write` sandbox; codex fall-back was Nature publisher HTML (article + Table 1 pages). Pre-extraction attachment hint prevented Peer-Review-File trap.
- Key insight: archetype is "method-instantiation-as-object" (3,844-plant national map = Fig 1 = signature visual). Cross-paper anchor with paper 1 (TIMES black-box vs plant-by-plant); discussed in §15 critical analysis.
- Methodology note: codex's contract worked end-to-end on first valid call. Random samples (M9HYZCZE, T3YPX6LR, QDU6TZYF) deferred pending user authorization after this validation.

## [2026-05-11] ingest | Giovanniello et al. 2024, Nature Energy, H2 additionality + time-matching (via codex)

- Zotero: `8IMLJZAH` (parent journalArticle); PDF `2YD6VCF2`
- Paper package: `.raw/papers/8IMLJZAH/` (7 stubs + codex receipt + logs)
- Analysis: [[papers/2024-NE-h2-additionality-time-matching]] (address `c-000004`, 38KB, 292 lines)
- Composed by: `codex exec` (gpt-5.5 + xhigh) per `_templates/codex-ingest-contract.md`
- Receipt: all checks pass (18 sections, banned-words clean, em-dash clean, 3-label discipline applied, 5+5+5+5 KB outputs)
- Deviation: Zotero MCP failed in sandbox; codex fall-back was local Zotero SQLite read + storage text cache (different fallback than paper 3, but `fulltext_source` was the main PDF).
- Key insight: archetype is "policy dispute resolved by boundary diagnosis." Paper turns a conflict between Ricks 2023 (hourly needed) and Zeyen 2023 (annual fine) into a hidden-counterfactual diagnosis (compete vs non-compete additionality). Phased PTC recommendation = annual now, hourly post-2030, eventually no time-matching as grid decarbonizes.
- Toolchain fix: `scripts/codex-ingest-paper.sh` v1 had bash 3.2 HEREDOC-in-`$()` parse bug (macOS default bash). Rewrote to use `mktemp` + stdin redirect. Test PR cycle: 1 failure, 1 success.
- Contract design: `_templates/codex-ingest-contract.md` v1 in production. Cross-references CLAUDE.md anti-fluff list + 3-label discipline + 18-section template.

## [2026-05-11] ingest | Yang et al. 2022, Nature Energy, China HTA clean hydrogen

- Zotero: `PIQKGJNB` (parent journalArticle); PDF attachment `MYQEQR3K`; notes `7I3UWH2F`, `J2BKDKY2`
- Paper package: `.raw/papers/PIQKGJNB/` (7 stubs: `metadata.json`, `zotero-attachments.md`, `data-availability.md`, `code-availability.md`, `repository-links.md`, `article-page.md`, `asset-status.md`)
- Analysis: [[papers/2022-NE-china-hta-clean-hydrogen]] (address `c-000003`)
- Pages created: 8 (1 wiki paper-analysis page + 7 paper-package stubs)
- Pages updated: 3 ([[index]], [[hot]], [[log]])
- Key insight: A Nature Energy paper can win on richer boundaries + headline monetization + a workhorse TIMES model, with figures sequenced one-per-reviewer-concern (existence -> screening -> deployment -> headline economics -> granularity -> robustness).
- Method note: pre-review-brief and research-blueprint applied inline rather than via separate skill subagents. N=1 means cosine-sim against the library is degenerate; the Nature Energy structural fingerprint was applied from existing knowledge.
- Discrepancy flagged in critical analysis §15: paper text says fleet bus 61% HFC market share by 2060, Fig 5a panel reports 56% for fleet buses; either edit-time drift or differing definitions, paper does not reconcile.
- Toolchain fix: `scripts/allocate-address.sh` patched to fall back to atomic `mkdir`-based locking when GNU `flock` is unavailable (macOS does not ship `flock` by default). Existing `flock` path preserved on Linux; tests/test_allocate_address.sh should still pass under Linux.
- Address-allocator state: counter 3 -> 4 after reserving `c-000003` for this paper.


## [2026-05-11] retheme | Vault forked to Top Paper Lab

- Type: structural rebrand + new constitution
- Action: forked from public `claude-obsidian` v1.6.0 plugin vault into personal Top Paper Lab.
- Plugin scaffold removed from active root: `.claude-plugin/` → `wiki/_meta/dropped-plugin-scaffold/.claude-plugin/`. Upstream public plugin continues at <https://github.com/AgriciDaniel/claude-obsidian>; this vault no longer participates in plugin distribution.
- Wiki re-skeletonized to 4 folders: `papers/` (per-paper analyses), `patterns/` (cross-paper synthesis), `playbook/` (personal writing principles), `projects/` (Henry's own manuscripts). All four start empty.
- Pre-fork content moved to `wiki/_meta/`: `canvases/`, `comparisons/`, `concepts/`, `entities/`, `folds/`, `meta/`, `questions/`, `sources/`, `getting-started.md`, `overview.md`. Snapshot of old `hot.md` and `index.md` stored as `wiki/_meta/old-hot.md` and `wiki/_meta/old-index.md`.
- `index.md` and `hot.md` rewritten for TPL identity and scope (energy-systems / renewable integration / green hydrogen / TEA).
- `CLAUDE.md` rewritten as TPL constitution (Source-of-truth hierarchy, Evidence/Inference/Lesson labels, anti-fluff rule, ingest workflow orchestrating `pre-review-brief` + `research-blueprint`, cross-page-update rule that activates at paper 10, lint workflow with TPL-specific checks).
- `.gitignore` extended to exclude `.raw/papers/**/main.pdf`, `.raw/papers/**/supplementary/**`, `.raw/papers/**/source-data/**`. Text metadata files (`metadata.json`, `data-availability.md`, etc.) remain tracked.
- 3 new templates added under `_templates/`: `paper-analysis.md`, `pattern-page.md`, `project-page.md`.
- `wiki/papers.base` Obsidian Bases dashboard added.
- `.raw/zotero_manifest/` scaffold created.
- DragonScale machinery untouched: `make test` still expected green. Vault counter still at 3.
- Next: Henry organizes Zotero `Top Paper Lab` collection; Claude Code builds manifest via Zotero MCP; Henry picks first seed paper.

---

## [2026-04-24] save | v1.6.0 public release notes (Teams, Karpathy-style)
- Type: release doc + visual assets
- Locations (new): `docs/releases/v1.6.0.md` (346 lines, 6 sections, Karpathy-style prose), `wiki/meta/dragonscale-mechanism-overview.svg` (4-mechanism diagram with shared .vault-meta/ gate), `wiki/meta/dragonscale-6-test-flow.svg` (validation timeline), `wiki/meta/dragonscale-frontier-graph.svg` (M4 candidate + 3 filed pages)
- Locations (modified): `wiki/meta/2026-04-24-v1.6.0-release-session.md` (cross-reference added pointing to public release notes)
- Scope: Teams approach. R1 (chair) wrote 3 original SVGs per SVG Diagram Style Guide. R2 (codex worker) drafted Karpathy-style release prose. R3 (chair) stitched SVGs, pivoted Wikipedia imagery to text links only (no binary vendoring per permission). R4 (codex verifier) returned ACCEPT WITH FIXES, 3 wording fixes on version narrative. R5 (chair) applied fixes, committed.
- Style: direct, short, signal-dense, lists over prose, no em dashes, no marketing terms. Verifier confirmed zero em-dashes and zero banned marketing language ('revolutionary', 'seamless', 'world-class', 'game-changing', 'unlock', 'transform').
- Distribution (all three destinations covered): (1) `docs/releases/v1.6.0.md` public-facing file (commit `85515bb`), (2) `wiki/meta/2026-04-24-v1.6.0-release-session.md` internal engineering record (cross-linked), (3) GitHub Release body (user to paste from docs/releases/v1.6.0.md when ready to `gh release create v1.6.0`).
- Wikipedia imagery: referenced as text link to `https://en.wikipedia.org/wiki/Dragon_curve` rather than hotlinked or vendored. Cleaner license-wise (no CC-BY-SA attribution needed) and no external dependency. The 3 original SVGs carry the visual load instead.
- PII scan post-write: `docs/releases/v1.6.0.md` + all three SVGs are clean. No `/home/` paths, no real emails, no tokens.
- Next recommended: user runs `gh release create v1.6.0 --notes-file docs/releases/v1.6.0.md` when ready to cut the public release. This also creates the annotated tag.

## [2026-04-24] save | DragonScale end-to-end validation pass (Teams, 6 tests)
- Type: validation + first real fold + first real autoresearch
- Tests executed (all green):
  - T0 ollama pull `nomic-embed-text`: done (274MB, 15s wall)
  - T1 M1 dry-run k=3 via codex: DRY-RUN OK, 8 children, no em-dashes
  - T2 M2 real allocate: counter advanced 2 to 3, got `c-000002` (unassigned reservation; gap acceptable per spec)
  - T3 M3 full tiling with model present: 41 pages scanned, 21 embedded, 20 correctly skipped (meta/excluded/embed-error), 0 errors at >=0.9, 15 pairs in 0.8-0.9 review band (top 0.8822 Compounding Knowledge vs LLM Wiki Pattern, a legitimate semantic neighbor), report at `wiki/meta/tiling-report-2026-04-24.md`
  - T4 M1 commit via codex: first real fold committed, `wiki/folds/fold-k3-from-2026-04-23-to-2026-04-24-n8.md` (115 lines, 8 children, flat extractive). Flips the long-standing "no fold committed yet" status
  - T6 M4 autoresearch no-topic via codex: selected "How does the LLM Wiki pattern work?" as candidate (score 1.7022, #3 after skipping top-1 source + top-2 self-reference); 6 web fetches (Karpathy gist, RAG paper arXiv 2005.11401, MemGPT arXiv 2310.08560, Obsidian docs); 3 new concept pages filed, each with Primary Sources
- Locations (new): `wiki/folds/fold-k3-from-2026-04-23-to-2026-04-24-n8.md`, `wiki/meta/tiling-report-2026-04-24.md`, `wiki/concepts/Persistent Wiki Artifact.md`, `wiki/concepts/Source-First Synthesis.md`, `wiki/concepts/Query-Time Retrieval.md`
- Locations (modified): `.vault-meta/address-counter.txt` (2 to 3), `wiki/index.md` (3 concept links), `wiki/concepts/_index.md` (3 concept links)
- Scope: six-test menu the user approved. Codex gpt-5.4 for T1/T4/T6 (sub-agent delegation); chair for T0/T2/T3 (one-shot shell) and all integration (index, log, hot, commit).
- Style: all new content uses colons or parens instead of em-dashes. Pre-existing em-dashes in index entries and wiki/concepts/_index.md left as-is (clean-room boundary; deferred to F-slice style pass).
- Tests still green: `make test` passes (74+ assertions).
- Integration: chair added the 3 new concepts to `wiki/index.md` and `wiki/concepts/_index.md` with colon-style descriptions so the fresh pages are discoverable. The cluster extends `[[How does the LLM Wiki pattern work]]` and cross-references `[[LLM Wiki Pattern]]`.
- Next recommended slice: either (G) commit this test batch and declare v1.6.0 validated, or (H) run a second fold k=3 now that 8 newer entries exist above this one and close the hierarchical-fold-not-yet-supported loop in a future phase.

## [2026-04-24] save | v1.6.0 closeout (Teams, chair-led)
- Type: docs + release hygiene
- Locations (new): wiki/meta/2026-04-24-v1.6.0-release-session.md (release session summary, 346 lines), wiki/meta/boundary-frontier-2026-04-24.md (first M4 run artifact against this vault), docs/dragonscale-guide.md (user-facing DragonScale guide, 563 lines)
- Locations (modified): wiki/hot.md (tag-claim fix, Scripts line adds boundary-score, tests line adds test_boundary_score, push-line drift, tiling line-count, one em-dash), docs/install-guide.md (version 1.5.0 to 1.6.0, DragonScale callout expanded to all four mechanisms, "hierarchical log folds" corrected to "flat extractive log folds", points to docs/dragonscale-guide.md), README.md (DragonScale parenthetical expanded to all four mechanisms plus guide link)
- Scope: Teams approach, chair-led. Slice A (2 codex read-only explorers: closeout punch list + doc-surface map). Slice B (6 bounded writes: 4 chair, 2 codex workers, non-overlapping write scopes). Slice C (codex adversarial verifier, ACCEPT WITH FIXES). Slice D (fix pass + log entry + manual commit of docs + README).
- Verifier: C1 found 11 items across 6 files. All 11 applied. Flag typos `--allow-remote-ollama` and `--report PATH` corrected in release-session; boundary-frontier provenance corrected to `--top 7` to match default vs explicit top; hot.md tiling line-count claim stripped to avoid drift; hot.md "local tag only" corrected to "local commits only, no git tag"; install-guide log-fold wording corrected from "hierarchical" to "flat extractive"; dragonscale-guide rollback wording corrected (`.vault-meta/` is a shared gate across M2+M3+M4, not per-mechanism).
- Model: codex gpt-5.4 used throughout. User requested gpt-5.5; not reachable via codex CLI 0.123.0 / this account at the time. models_cache lists max gpt-5.4, and the API rejects gpt-5.5 with "does not exist or you do not have access". Existing config already has `service_tier = "fast"` and `sandbox_mode = "workspace-write"`, matching the "fast for chatgpt with permission of full access" intent.
- Tests: `make test` passes. test_allocate_address.sh (shell, 12 assertions), test_tiling_check.py (python, 18 assertions), test_boundary_score.py (python, 44 assertions). Zero ollama dependency.
- Tags: still no local v1.5.0 / v1.5.1 / v1.6.0 tags. User controls tag creation and push. Pre-existing tags unchanged (v1.1, v1.4.0 through v1.4.3).
- Deliberately NOT done: no real M1 fold committed; no M3 end-to-end run (needs `ollama pull nomic-embed-text`); pre-existing em-dashes in install-guide.md and README.md left untouched (clean-room boundary, not in write scope this slice); CLAUDE.md pre-existing uncommitted change left untouched.
- Next recommended slice: either (E) push to origin/main and create annotated tags v1.5.0, v1.5.1, v1.6.0 in landing order, or (F) dedicated style pass to scrub pre-existing em-dashes across install-guide.md, README.md, and any other wiki files flagged by a grep scan.

## [2026-04-24] save | DragonScale Phase 4 — boundary-first autoresearch shipped (v1.6.0)
- Type: feature release
- Locations (new): scripts/boundary-score.py (with --top, --page, --json, stdout-only CLI), tests/test_boundary_score.py (40+ assertions)
- Locations (modified): skills/autoresearch/SKILL.md (new Topic Selection section A/B/C with helper-failure fallback), commands/autoresearch.md (no-topic candidate flow with agenda-control label), wiki/concepts/DragonScale Memory.md (v0.4: M4 flipped from NOT IMPLEMENTED to shipped; exact formula without recency floor; filename-stem disclosure; fence-handling qualifiers), CHANGELOG.md, .claude-plugin/{plugin,marketplace}.json (1.5.0 -> 1.6.0), Makefile (test-boundary target), wiki/hot.md, wiki/index.md, wiki/concepts/_index.md (status drift resolved).
- Scope: boundary-first autoresearch as opt-in Topic Selection mode. `/autoresearch` without a topic surfaces top-5 frontier pages; user picks/overrides/declines. Explicit helper-failure fallback to user-ask. Labeled "agenda control" throughout to match the spec's scope disclosure.
- Correctness: filename-stem resolution including folder-qualified `[[notes/Foo]]` -> Foo.md. Self-loops, unresolved targets, meta-targets, symlinks, and vault escapes all excluded. Code-fence parser handles backticks AND tildes with CommonMark length tracking (longer opening fence is not closed by shorter inner fence). Indented blocks intentionally not filtered (Obsidian bullet convention).
- Recency: exp(-days/30), no floor. Stale pages approach zero weight so they do not dominate frontier ranking.
- Review rounds: codex adversarial Phase 4 round 1 (10 items: 7 reject + 3 refine). Round 2 (7 accept + 3 still-reject: folder-qualified stem, docstring floor mention, hot.md historical drift). Round 3 (3 accept, PASS).
- Phase 3.6 (pre-Phase-4 hardening) already landed as v1.5.1: tiling --report VAULT_ROOT confinement, rollout baseline, AGENTS.md consistency, wiki-ingest .raw/ contradiction, install-guide version.
- All four DragonScale mechanisms now shipped and opt-in. 44 commits ahead of origin/main, no push.

## [2026-04-24] save | DragonScale Phase 3.5 — cross-phase hardening to v1.5.0
- Type: release hardening
- Locations (new): bin/setup-dragonscale.sh (opt-in installer), tests/test_allocate_address.sh, tests/test_tiling_check.py, Makefile, CHANGELOG.md
- Locations (modified): hooks/hooks.json (+.vault-meta/ staging), agents/wiki-ingest.md (single-writer rule for addresses), agents/wiki-lint.md (Mechanism 2+3 checks), skills/wiki-ingest/SKILL.md (aligned non-DragonScale wording), wiki/concepts/DragonScale Memory.md (M2 severity matches lint, M4 marked NOT IMPLEMENTED, seed page gets address c-000001), .claude-plugin/{plugin.json,marketplace.json} (1.4.2/1.4.3 → 1.5.0), README.md (11 skills + DragonScale callout), wiki/hot.md (refreshed for v1.5.0), .raw/.manifest.json (address_map now has DragonScale Memory.md → c-000001), .gitignore (.vault-meta/.tiling.lock + cache), .vault-meta/address-counter.txt (advanced to 2).
- Scope: resolve the 10 hold-ship items from the cross-phase audit. Add reproducible test harness (make test passes). Version-bump plugin.json and marketplace.json to 1.5.0. Create CHANGELOG.md. Refresh hot cache.
- Review rounds: codex 3.5a (5/5 accept on doc/agent fixes), codex final holistic (10/10 accept on audit items + 2 surgical regression fixes: wiki-ingest/wiki-lint non-DragonScale wording alignment, README skill count).
- Tests: `make test` runs 12 shell assertions (allocator) + 18 python assertions (tiling-check). All pass; no ollama dependency.
- Phase 3.5 complete. Repo state: 6 developer commits added this pass (f2e73c1, 2b49a0c, 8b28e48, 19ad7e4, 365f557, 2e7dd16). Total 39 commits ahead of origin/main. No push.

## [2026-04-24] save | DragonScale Phase 3 — semantic tiling MVP
- Type: skill update + new script + threshold state
- Locations: scripts/tiling-check.py (485 lines), .vault-meta/tiling-thresholds.json (seed defaults), skills/wiki-lint/SKILL.md (109-line Semantic Tiling section + item #10 in checks), wiki/concepts/DragonScale Memory.md (Mechanism 3 cost framing clarified)
- Scope: opt-in embedding-based duplicate detection via ollama nomic-embed-text. Default bands error>=0.90, review>=0.80, explicitly documented as conservative seeds (not literature-backed interpolation). Calibration procedure documented, not automated.
- Security: default OLLAMA_URL locked to 127.0.0.1; non-localhost requires --allow-remote-ollama flag. Symlinks and vault-root escapes rejected before file reads (prevents data exfil).
- Correctness: cache keyed on sha256(model+body); orphan GC on save; model-drift auto-invalidation on load.
- Concurrency: flock(LOCK_EX) on .vault-meta/.tiling.lock; per-PID temp file for atomic writes.
- Scale: warn >500 pages; hard-fail exit 4 at >5000 pages.
- Exit codes: 0/2/3/4/10/11 distinctly surfaced in wiki-lint wiring (not collapsed into "unknown").
- Review rounds: 4 codex exec adversarial passes covering security, cache correctness, feature gate, inclusion logic, scale, threshold honesty, concurrency, exit codes, model drift, terminology coupling.
  Round 1: 10 items -> 7 reject + 3 refine.
  Round 2: 6 accept + 4 still-reject (symlink ordering, prose sync, exit-code wiring, terminology in checklist + "no API cost" claim).
  Round 3: 3 accept + 1 still-reject (cost-framing phrasing).
  Round 4: accept.
- Final verdict: 10/10 accept.
- Phase 3 complete. All three DragonScale mechanisms that were in-scope for the initial spec are now shipped as opt-in features. Mechanism 4 (boundary-first autoresearch) was flagged as agenda-control out-of-scope per the v0.2 scope boundary; may or may not ship as a future phase.

## [2026-04-23] save | DragonScale Phase 2 — deterministic page addresses MVP
- Type: skill update + new script
- Locations: scripts/allocate-address.sh, skills/wiki-ingest/SKILL.md (Address Assignment section), skills/wiki-lint/SKILL.md (Address Validation section), wiki/concepts/DragonScale Memory.md (Mechanism 2 rewritten v0.2→v0.3), .vault-meta/address-counter.txt, .raw/.manifest.json (new)
- Scope: MVP address format `c-NNNNNN` (creation-order counter, zero-padded 6 digits). Rollout baseline 2026-04-23. Legacy pages exempt until deliberate backfill (future `l-` prefix). No content hash, no fold-ancestry encoding in the MVP (both deferred).
- Concurrency: atomic allocation via flock-guarded Bash helper. Counter recovery from max observed `c-` address, never silent reset to 1.
- Lint: post-rollout pages without address are errors; legacy pages without address are informational. Optional `.vault-meta/legacy-pages.txt` manifest grandfathers pages with missing/wrong `created:` metadata.
- Re-ingest idempotency: `.raw/.manifest.json` `address_map` preserves path→address mapping across re-ingests and renames.
- Naming: mechanism renamed from "content-addressable paths" to "deterministic page addresses" (the MVP is a counter, not a content hash; the old name was overclaim).
- Review rounds: 2 codex exec adversarial passes. Round 1: 8 rejects covering counter mutation, race conditions, uniqueness atomicity, missing-file recovery, terminology drift, silent regression path, legacy classification, re-ingest idempotency. Round 2: 7 accept + 1 reject (manifest.json absent). Round 3 (item 8 only): accept after creating `.raw/.manifest.json`.
- Final verdict: 8/8 accept.
- Phase 2 complete. Phase 3 (semantic tiling lint) gated on human approval.

## [2026-04-23] save | DragonScale Phase 1 — wiki-fold skill shipped
- Type: skill
- Location: skills/wiki-fold/SKILL.md, skills/wiki-fold/references/fold-template.md
- Scope: flat extractive fold over raw wiki/log.md entries. Dry-run default via Bash stdout (no Write tool, avoids PostToolUse hook residue). Structural idempotency via deterministic fold_id. Duplicate-range detection. Fold-of-folds explicitly out of scope.
- Review rounds: 3 codex exec adversarial passes. Round 1: 1 refine + 6 reject across 7 items (allowed-tools, hook-mutation risk, idempotency claim, dry-run faithfulness, children structure, Mechanism 1 coverage, auto-commit conflict). Round 2: 6 accept + 1 reject (25/26 count inversion). Round 3 (item 4 only): accept.
- Final verdict: 7/7 accept.
- Dry-run artifact: /tmp/wiki-fold-dry-run-v2.md (not committed). fold_id: fold-k3-from-2026-04-10-to-2026-04-23-n8.
- Phase 1 complete. Phase 2 (content-addressable paths) gated on human approval.

## [2026-04-23] save | DragonScale Memory v0.2 — post-adversarial-review
- Type: concept revision
- Location: wiki/concepts/DragonScale Memory.md
- Review: codex exec adversarial review rejected all 7 load-bearing claims in v0.1
- Changes: weakened LSM analogy, removed strong prompt-cache claim, replaced 0.85 threshold with calibration procedure, justified 2^k as MVP convenience, acknowledged scope-boundary leak for boundary-first autoresearch, added Operational Policies section (retention/tombstones/versioning/conflict/concurrency/provenance/ACL), tagged claims as [sourced]/[derived]/[conjecture], narrowed tagging scope per re-review
- Re-review result: 7/7 accepted (after one surgical fix on tagging-scope language)
- Phase 0 complete. Phase 1 (wiki-fold skill) gated on human approval.

## [2026-04-23] save | DragonScale Memory — Phase 0 design doc (proposed)
- Type: concept
- Location: wiki/concepts/DragonScale Memory.md
- From: brainstorming session on applying Heighway dragon curve properties to LLM wiki memory architecture
- Scope: memory-layer only, NOT agent reasoning. Four mechanisms: (1) fold operator (LSM-style exponential compaction at 2^k log entries), (2) content-addressable page paths for prompt-cache stability, (3) semantic tiling lint (embedding-based dedup, 0.85 cosine threshold), (4) boundary-first autoresearch scoring
- Status: proposed. Phase 0 pending codex adversarial review. Phase 1+ (fold skill, address anchors, tiling lint, boundary score) gated on review pass.
- Primary sources verified: Dragon curve (Wikipedia, boundary dim 1.523627086), Regular paperfolding sequence (OEIS A014577), LSM trees (arXiv 2504.17178, LevelDB 10x level ratio), MemGPT (arXiv 2310.08560), Anthropic prompt caching docs (5min/1hr TTL, 20-block lookback)
- Links updated: wiki/concepts/_index.md, wiki/index.md

## [2026-04-15] save | Claude SEO v1.9.0 Slides and GitHub Release
- Type: session
- Location: wiki/meta/2026-04-15-slides-and-release-session.md
- From: built 15-slide HTML presentation deck (v190.html), fixed hardcoded path in release_report.py, pushed 68 files to GitHub, tagged v1.9.0, created GitHub release with PDF asset
- Key lessons: Path.home() not hardcoded paths, git pull --rebase before big pushes, Chrome blocks file:// cross-origin images, .claude/ always in .gitignore
- Release: https://github.com/AgriciDaniel/claude-seo/releases/tag/v1.9.0

## [2026-04-15] save | Claude SEO v1.9.0 Release Report — PDF Complete
- Type: session
- Location: wiki/meta/2026-04-15-release-report-session.md
- From: full session completing the v1.9.0 PDF release report. Dark theme, 13 pages, 1.53 MB. Fixed logo (double-space filename), empty spaces, page-break orphans, file:// URL encoding.
- Key fixes: `urllib.parse.quote()` for file:// URIs; `display:table-cell` is atomic in WeasyPrint (no page-break); fixed `height:297mm` causes empty space; replaced orphan tables with paragraphs
- Challenge v2 added: keyword LEADS, $600 prize pool, deadline April 28
- Output: `~/Desktop/Claude-SEO-v1.9.0-Release-Report.pdf`

## [2026-04-14] save | Claude SEO v1.9.0 — Pro Hub Challenge Integration Session
- Type: session + 4 concept pages + 1 entity page
- Location: wiki/meta/2026-04-14-claude-seo-v190-session.md
- From: full v1.9.0 implementation session — reviewed 5 community submissions, integrated 4 new skills (seo-cluster, seo-sxo, seo-drift, seo-ecommerce), enhanced seo-hreflang, added DataForSEO cost guardrails
- Pages created: [[2026-04-14-claude-seo-v190-session]], [[Claude SEO]], [[Pro Hub Challenge]], [[Semantic Topic Clustering]], [[Search Experience Optimization]], [[SEO Drift Monitoring]]
- Review rounds: 4 (code review x3 + cybersecurity audit). Score: 87 → 93 → 97 → 85 security
- Key learnings: always verify subagent output (40-line count error caught), insertion-point bugs caught by max-effort plan review, pre-existing security debt identified (10 of 15 findings)

## [2026-04-14] save | SVG Diagram Style Guide
- Type: concept
- Location: wiki/concepts/SVG Diagram Style Guide.md
- From: extracted design tokens from 17 production SVGs in claude-ads/assets/diagrams/
- Covers: colors, typography, layout primitives, card patterns, arrow connectors, numbered circles, file naming

## [2026-04-14] save | Community CTA Footer Rollout
- Type: decision
- Location: wiki/meta/2026-04-14-community-cta-rollout.md
- From: session adding Skool community footer to 6 skill repos (claude-ads, claude-seo, claude-obsidian, claude-blog, banana-claude, claude-cybersecurity)
- Key insight: frequency calibration per tool type; single-point orchestrator instruction pattern

## [2026-04-10] save | Backlink Empire - Blog Posts, Karpathy Gist, GitHub Cross-Linking
- Type: session
- Location: wiki/meta/2026-04-10-backlink-empire-session.md
- From: full session covering blog creation (claude-obsidian + claude-canvas), Karpathy gist comment, 26 GitHub README updates with Author/community/backlink sections, homepage URLs on 10 repos, topics on 25 repos, rankenstein.pro backlinks on 5 SEO repos
- Blog posts: agricidaniel.com/blog/claude-obsidian-ai-second-brain, agricidaniel.com/blog/claude-canvas-ai-visual-production
- Impact: ~87 new backlinks from DA 96 github.com, 6 rankenstein.pro backlinks, 25 Skool community links

## [2026-04-08] save | claude-obsidian v1.4 Release Session
- Type: session
- Location: wiki/meta/claude-obsidian-v1.4-release-session.md
- From: full release cycle covering v1.1 (URL/vision/delta tracking, 3 new skills), v1.4.0 (audit response, multi-agent compat, Bases dashboard, em dash scrub, security history rewrite), and v1.4.1 (plugin install command hotfix)
- Key lessons: plugin install is 2-step (marketplace add then install), allowed-tools is not valid frontmatter, Bases uses filters/views/formulas not Dataview syntax, hook context does not survive compaction, git filter-repo needs 2 passes for full scrub

## [2026-04-08] ingest | Claude + Obsidian Ecosystem Research
- Type: research ingest
- Source: `.raw/claude-obsidian-ecosystem-research.md`
- Queries: 6 parallel web searches + 12 repo deep-reads
- Pages created: [[claude-obsidian-ecosystem]], [[cherry-picks]], [[claude-obsidian-ecosystem-research]], [[Ar9av-obsidian-wiki]], [[Nexus-claudesidian-mcp]], [[ballred-obsidian-claude-pkm]], [[rvk7895-llm-knowledge-bases]], [[kepano-obsidian-skills]], [[Claudian-YishenTu]]
- Key finding: 16+ active Claude+Obsidian projects; 13 cherry-pick features identified for v1.3.0+
- Top gap confirmed: no delta tracking, no URL ingestion, no auto-commit

## [2026-04-07] session | Full Audit, System Setup & Plugin Installation
- Type: session
- Location: wiki/meta/full-audit-and-system-setup-session.md
- From: 12-area repo audit, 3 fixes, plugin installed to local system, folder renamed

## [2026-04-07] session | claude-obsidian v1.2.0 Release Session
- Type: session
- Location: wiki/meta/claude-obsidian-v1.2.0-release-session.md
- From: full build session — v1.2.0 plan execution, cosmic-brain→claude-obsidian rename, legal/security audit, branded GIFs, PDF install guide, dual GitHub repos


- Source: `.raw/` (first ingest)
- Pages updated: [[index]], [[log]], [[hot]], [[overview]]
- Key insight: The wiki pattern turns ephemeral AI chat into compounding knowledge — one user dropped token usage by 95%.

## [2026-04-07] setup | Vault initialized

- Plugin: claude-obsidian v1.1.0
- Structure: seed files + first ingest complete
- Skills: wiki, wiki-ingest, wiki-query, wiki-lint, save, autoresearch
