---
zotero_key: KWNBZ8FA
title: "AI data centres as grid-interactive assets"
journal: "Nature Energy"
year: 2026
doi: "10.1038/s41560-025-01927-1"
topic: [data-centres, grid-flexibility, demand-response, ai-electricity-demand, flexible-loads]
paper_type: [experimental, data-driven, policy-analysis]
main_contribution: [method-novelty, policy-relevance, mechanism-clarification]
method_type: [field-demonstration, workload-orchestration, demand-response, simulator-calibrated-control, dvfs]
data_assets:
  main_pdf: true
  supplementary: false
  source_data: false
  data_statement: true
  code_statement: true
  code_repository: true
relevance_to_my_research: medium
ingest_status: reviewed
address: c-000024
created: 2026-05-11
tags:
  - paper-analysis
---

# AI data centres as grid-interactive assets

> Zotero: `KWNBZ8FA` · DOI: 10.1038/s41560-025-01927-1 · Journal: Nature Energy (2026)

## 1. One-sentence contribution

Evidence: Colangelo et al. show, through a Phoenix field trial on a 256-GPU production AI cluster, that software workload orchestration can reduce cluster power by 25% for 3 hours during grid peak periods while keeping job quality-of-service thresholds intact (abstract, Figs. 2-4, Table 2).

## 2. Archetype classification

Evidence: This is a field-demonstration paper with a data-driven control layer: the paper tests a software power-orchestration platform on real cloud infrastructure, uses measured GPU and workload telemetry, and reports utility-style demand-response events for APS, SRP and a CAISO re-enactment (Phoenix field trial; Methods).

Inference: The paper also works as a policy-facing technology validation paper, confidence high. Its central audience is not only AI systems researchers but also utilities, regulators and grid planners deciding whether data centres should be treated as fixed loads or flexible resources.

Lesson: For Henry's own energy-system work, a strong applied paper can win by converting a contested planning assumption into a measured operating mode: define the old assumption, build the operational test, then show the planning consequence.

## 3. Real value sources

| Dimension | Top driver? | Evidence | Inference | Lesson |
|---|---|---|---|---|
| Problem importance | Yes | Evidence: The abstract frames AI demand growth as a source of grid reliability risk, infrastructure cost and interconnection delay. | Inference: The venue fit comes from putting data-centre load growth inside electricity planning, confidence high. | Lesson: Frame the load not as a computing problem alone but as a grid-planning bottleneck with cost and timing consequences. |
| Problem novelty | Medium | Evidence: The introduction notes prior HPC and CPU-based demand-response work, then distinguishes GPU AI workloads with stricter service needs. | Inference: The gap is less "nobody thought of data-centre flexibility" and more "nobody field-tested GPU AI flexibility under utility event rules", confidence high. | Lesson: Narrow novelty by changing the operational regime, hardware class and validation setting. |
| Method novelty | Yes | Evidence: The platform schedules jobs, changes resource allocation and applies GPU power limits under SLA constraints using a simulator trained on power-performance behaviour (Fig. 1; Methods). | Inference: The method's value is orchestration across several control knobs rather than a single algorithmic trick, confidence high. | Lesson: Present the method as a control stack with inputs, knobs, simulator and constraints. |
| Data novelty | Yes | Evidence: The trial covers 33 experiments, 212 individual jobs and measured cluster power traces from a production-grade 256-GPU cluster (Table 2; Methods). | Inference: Access to industry infrastructure is a central value source, confidence high. | Lesson: When data access is rare, make the scale, duration and operating partner visible early. |
| System boundary | Yes | Evidence: The study connects AI workload parameters, cluster telemetry and grid signals from utilities and Amperon forecasts (Fig. 1; Methods). | Inference: The boundary expansion from server to grid event is the paper's main systems move, confidence high. | Lesson: Draw the boundary so the intervention touches both the technical asset and the system operator need. |
| Case-study design | Yes | Evidence: APS and SRP peak events were run on 1 May and 3 May 2025, and the CAISO 2020 event was re-enacted with stepped curtailment targets (Figs. 2-4). | Inference: Three event types make the result more transferable than a single lab stress test, confidence medium. | Lesson: Use multiple event archetypes to show the same mechanism under normal peak and emergency conditions. |
| Result impact | Yes | Evidence: The headline result is 25% reduction for 3 hours, with 15-minute ramps and zero SLA violations across all experiments (abstract; Evaluation metrics). | Inference: The result matters because the unit is grid-operational power, not only energy efficiency, confidence high. | Lesson: Pick outcome metrics that match the stakeholder decision: power target compliance, service preservation and simulator error. |
| Mechanism explanation | Medium | Evidence: The paper identifies DVFS, job pausing and resource reallocation as the three control knobs, and Fig. 6 shows workload throughput sensitivity to power caps. | Inference: The mechanism is credible for batch training and tolerant inference but thinner for real-time inference, confidence high. | Lesson: Make the mechanism conditional by workload class instead of claiming blanket flexibility. |
| Comprehensiveness | No | Evidence: The field trial is one Phoenix cluster with four workload ensembles and no full multi-region market simulation. | Inference: The paper deliberately chooses field validity over wide geographic coverage, confidence high. | Lesson: Do not pretend a field demonstration covers the whole sector. State the operational slice and use it well. |
| Policy / industry implication | Yes | Evidence: The discussion ties flexibility to interconnection prioritization, lower tariffs, flexibility payments and constrained regions such as Northern Virginia, Silicon Valley and Texas. | Inference: The grid-planning implication is that some AI load could be modeled as partially curtailable capacity, confidence medium. | Lesson: Translate a technical result into the tariff, interconnection and planning variables decision-makers can act on. |
| Writing / narrative | Yes | Evidence: The abstract moves from AI load growth to grid stress, then to a measured 25% reduction without hardware changes. | Inference: The writing succeeds by making the paper a demonstration of a new asset category, confidence high. | Lesson: Build the story around category conversion: from fixed consumer to controllable grid participant. |
| Figure / table craft | Yes | Evidence: Fig. 1 gives architecture, Figs. 2-4 show grid event traces, Fig. 5 validates the simulator, Fig. 6 explains power-performance trade-offs, and Tables 1-2 define workloads and runs. | Inference: The figure sequence mirrors the argument chain from system to event proof to mechanism, confidence high. | Lesson: Put architecture before evidence, event traces before validation, and mechanism after proof. |

**Top 3 value drivers**:
1. Evidence: Real field demonstration on a 256-GPU production cluster with utility event targets.
2. Evidence: A system boundary that connects AI workload control to grid peak management.
3. Evidence: Measured service-preserving power reduction across 33 experiments and 212 jobs.

**What it does NOT win on**: Evidence: It does not provide multi-region deployment economics, full interconnection queue modeling or market revenue optimization. The Discussion explicitly calls for larger-scale deployments, more grid programmes and economic viability assessment.

**Most likely reason it cleared the top-tier bar**: Inference: Nature Energy likely valued the paper because it converts a fast-moving AI electricity-demand concern into a measured, near-term grid-flexibility mechanism with industry partners and utility-facing metrics, confidence high.

## 4. Research question & framing

Evidence: The paper asks whether GPU-driven AI workloads contain enough operational flexibility to participate in demand response and grid stabilization while respecting service-level guarantees (introduction).

Inference: The research question is framed as an assumption reversal: grid planners commonly treat data centres as continuously high-power loads, while the paper tests whether orchestration can make them controllable loads, confidence high.

Lesson: State the question in stakeholder terms. For Henry's work, ask not only "what is technically possible" but "which planning assumption changes if this flexibility is real."

## 5. Introduction structure (paragraph table)

| ¶ | Function | Core info | Writing move | Why it works | Lesson |
|---|---|---|---|---|---|
| P1 | Problem and prior-work contrast | Evidence: AI GPU clusters are increasing electricity demand; US AI data-centre demand could reach tens of gigawatts by 2030; prior work focused on CPU/HPC demand response or industry carbon-aware allocation. | Moves from macro grid stress to why existing data-centre demand-response evidence is incomplete. | It makes the gap operational, not merely bibliographic. | Lesson: Put the planning pain and the evidence limitation in the same paragraph. |
| P2 | Gap, hypothesis and field-test preview | Evidence: The authors argue that software orchestration can preserve AI QoS while meeting grid response commitments, then state the Phoenix 256-GPU production-cluster demonstration. | Converts the gap into a testable hypothesis and immediately names the field setting. | It gives the reader proof of seriousness before the Results section begins. | Lesson: Use the final intro paragraph to move from need to hypothesis to asset, site and test. |

**Gap paragraph**: Evidence: P2 is the gap paragraph because it says scalable software solutions that respect AI SLAs and offer real-time power modulation are needed, then states the central hypothesis.

**Transferable Intro template extracted from this paper**:

Evidence: Start with demand growth as a system stressor. Contrast existing evidence with the operational regime the paper targets. State the hypothesis as a change in asset behavior. Name the field setting and the exact performance commitment before the first Results heading.

## 6. Lit-gap & contribution construction

Evidence: The literature gap is built through three contrasts: CPU/HPC studies versus GPU AI workloads, simulation or analytical models versus field trial, and broad carbon-aware allocation or load shedding versus SLA-preserving real-time power modulation (introduction).

Inference: The paper avoids a crowded "data centres and demand response" gap by specifying the missing combination: GPU AI cluster, production cloud facility, utility event target, measured power response and explicit workload QoS, confidence high.

Lesson: When a field has many related studies, make the contribution a precise combination of setting, asset, control objective and validation standard.

## 7. Method / model / design (adapt to archetype)

Evidence: The method is a software power-orchestration platform that takes grid signals, telemetry and job parameters as inputs, then schedules jobs, changes GPU allocations, pauses jobs and applies NVIDIA-SMI power caps (Fig. 1; Implementation).

Evidence: Jobs were tagged into Flex 0 through Flex 3 tiers: no performance reduction, up to 10%, up to 25% and up to 50% average throughput reduction over a 3-6 hour period (System architecture; Table 1).

Evidence: The simulator estimates power-performance relationships from pre-measured job profiles and recommends controls subject to power targets and job SLA constraints (Methods).

Evidence: The evaluation metrics are power-reduction compliance, QoS preservation and simulator accuracy; the authors report zero SLA violations and 4.52% RMSE relative to average experiment power (Evaluation metrics).

Inference: The design's strength is that it treats demand response as constrained control rather than voluntary load shedding, confidence high.

Lesson: For optimization and TEA work, define the operational contract first: what can be curtailed, for how long, under which performance bounds and with which grid signal.

## 8. Data & case-study design

Evidence: The trial site is an Oracle Phoenix Region Cloud data centre with 256 NVIDIA A100 GPUs, Databricks MosaicML orchestration, Weights & Biases telemetry and Amperon grid-demand forecasting tools (Phoenix field trial).

Evidence: The workload ensembles mix training, fine tuning and inference tasks using MPT and LLaMA 3.1 models, C4 pre-training data, and Dolly and P3 fine-tuning data (Methods; Table 1).

Evidence: The two live utility events were designed around APS and SRP peak periods on 1 May and 3 May 2025; the synthetic emergency event re-enacted the August 2020 CAISO load shed sequence (Figs. 2-4).

Inference: Phoenix is a strong case because heat-driven peak demand makes data-centre flexibility easy to connect to system stress, confidence medium.

Lesson: Choose a case where the system stress is visible in the same time window as the intervention.

## 9. Results architecture

| Section | Main message | Evidence used | Role in argument | Why this order | Lesson |
|---|---|---|---|---|---|
| System architecture and flexibility framework | Software can convert job-level flexibility into grid-facing power control. | Evidence: Fig. 1 architecture and Table 1 workload ensembles with Flex 0-3 tags. | Defines the mechanism before showing event results. | The reader needs the control vocabulary before interpreting power traces. | Lesson: Introduce the control surface before the performance proof. |
| Phoenix field trial | The platform hit utility event targets while keeping workload service thresholds. | Evidence: Figs. 2-4 show SRP, APS and CAISO-style events; Table 2 lists 33 runs. | Provides the main empirical claim. | Field results come before model validation because they carry the paper's credibility. | Lesson: Put the strongest external-facing evidence before diagnostics. |
| Simulator performance accuracy | The predictive layer was accurate enough for real-time orchestration. | Evidence: Fig. 5 reports measured versus simulated cluster power and 4.52% RMSE in text. | Defends the control layer behind the field response. | After proving the event, the paper explains why the software can be trusted. | Lesson: Use validation figures to support the action mechanism, not as isolated model metrics. |
| Discussion mechanism and limits | The method can scale under conditions, but workload mix, geography and market design remain open. | Evidence: Fig. 6 power-cap throughput curves; limitations paragraph on Flex 0, multi-zone deployment and market programmes. | Converts the field trial into a research and policy agenda. | It moves from one cluster to broader deployment without hiding limits. | Lesson: Make scale-up claims conditional on the constraints your own data reveal. |

## 10. Figures & tables argument function

| Item | Shows | Proves | Role | Why in main text | Design lesson |
|---|---|---|---|---|---|
| Fig. 1 | Evidence: Grid signal, telemetry, job parameters, simulator and orchestration engine. | The platform is a system connecting grid and compute decisions. | Mechanism map. | Without it, the work could read like ad hoc throttling. | Lesson: Use an architecture figure to make cross-sector causality visible. |
| Table 1 | Evidence: Four workload ensembles with model types, node counts and Flex levels. | The trial spans training, fine tuning and inference rather than one toy job. | Design specification. | The SLA labels are central to the claim. | Lesson: Put operational constraints in a table so readers can audit them. |
| Fig. 2 | Evidence: SRP load and GPU cluster power during a 16:30-19:30 event, plus flex-tier performance. | The platform can sustain a 25% reduction while meeting thresholds. | Flagship utility proof. | It combines grid event timing and workload performance. | Lesson: Pair system signal and asset response in one figure. |
| Fig. 3 | Evidence: APS load and GPU cluster power during an 18:00-21:00 event. | The result repeats under a second local utility event. | Replication under another peak. | A second utility trace reduces the chance that Fig. 2 is a one-off. | Lesson: Use a second case to show repeatability across operating partners. |
| Fig. 4 | Evidence: CAISO 2020 re-enactment with 15% then 25% curtailment targets. | The controller can follow stepped emergency requirements. | Stress-test proof. | Emergency-style response extends beyond routine peak shaving. | Lesson: Add a severe event scenario after normal events. |
| Table 2 | Evidence: 33 experimental runs across ensembles, control knobs, policies, targets and durations. | The paper tested more than the three narrative events. | Experimental coverage table. | It makes the field trial auditable. | Lesson: Use a compact run matrix to support the breadth of the test campaign. |
| Fig. 5 | Evidence: Simulator and measured cluster power traces during a reduction event. | The simulator can track aggregate cluster behavior well enough to guide controls. | Validation of control model. | It justifies the predictive layer in Fig. 1. | Lesson: Validate the model on the same operational metric used for control. |
| Fig. 6 | Evidence: Throughput versus measured GPU power for several workloads and GPU allocations. | Workload power sensitivity differs, so flexibility must be workload-aware. | Mechanism and boundary condition. | It explains why one policy cannot fit all jobs. | Lesson: End the figure sequence with a mechanism plot that explains the field result. |

Extended Data figures: Evidence: The Zotero main-PDF text does not expose Extended Data figure captions, and no supplementary attachment is present in Zotero. N/A for this ingest tier.

## 11. Discussion & Conclusion

Evidence: The Discussion elevates the result from cluster power control to interconnection and planning: flexible data centres could unlock existing system headroom, avoid some infrastructure upgrades, receive demand-response credits and support constrained regions.

Evidence: The paper also names limits: Flex 0 workloads were not modified, single-site throttling cannot cover all latency-sensitive jobs, larger multi-zone deployments are needed, and market participation beyond emergency demand response remains future work.

Inference: The conclusion overstates the generality of the Phoenix demonstration when it says existing AI clusters can become reliable grid-support assets, confidence medium. The evidence supports "some workload mixes under defined event durations and SLA tiers", not every AI cluster.

Lesson: In Henry's own papers, let the final paragraph widen the implication but keep the transfer conditions visible.

## 12. Argument chain (compressed)

```text
AI data-centre electricity growth is straining grids
  -> Grid planning often treats data centres as fixed high-power loads
  -> GPU AI workloads may contain service-preserving flexibility
  -> Build a software orchestration layer with grid signals, telemetry, SLA tags and simulator-based control
  -> Test it on a 256-GPU Phoenix production cluster
  -> Achieve 25% power reduction for 3 hours in APS and SRP peak events
  -> Re-enact a CAISO emergency event with stepped reductions
  -> Show zero SLA violations and 4.52% simulator power RMSE
  -> Explain workload-specific power-performance trade-offs
  -> Argue that flexible AI data centres can help grid planning, interconnection and demand-response programmes
```

**Weakest link**: Inference: The jump from one Phoenix cluster to broad interconnection reform is plausible but not fully quantified, confidence high.

**Strongest link**: Evidence: The field traces in Figs. 2-4 directly connect grid event windows to measured cluster power reductions and workload performance thresholds.

## 13. Writing strategy extracted

Evidence: The abstract packs the paper's core proof into one sentence: 256 GPUs, representative AI workloads, hyperscale Phoenix facility, 25% reduction, 3 hours and service guarantees.

Inference: The writing strategy is to make every audience see its object: AI developers see QoS, utilities see peak reduction, planners see interconnection relief, and energy researchers see flexible load, confidence high.

Lesson: In an interdisciplinary paper, write the headline result with all boundary conditions in place: asset size, location, duration, reduction, stakeholder metric and constraint.

## 14. Research-design strategy extracted

Evidence: The design combines live utility events, a historical emergency re-enactment, a run matrix across policies and a simulator validation step.

Inference: This is a layered validation strategy: real event proof, stress-event proof, repeatability matrix and control-model check, confidence high.

Lesson: For Henry's wind-solar-hydrogen or building-flexibility work, do not rely on one scenario. Build a validation ladder: realistic event, stress event, parameter matrix and model-error check.

## 15. Critical analysis

Evidence: The paper acknowledges that real-time inference, streaming and model serving were treated as Flex 0 and not modified.

Evidence: The field trial used one cluster, one region and partner-selected workload ensembles. The paper calls for full data-centre telemetry, multiple zones and broader market-programme tests.

Inference: The economic claim is underdeveloped, confidence high. The paper discusses lower tariffs, payments and avoided infrastructure but does not model revenue, customer compensation or utility cost allocation.

Inference: The carbon and energy effects are secondary, confidence high. The Methods state energy efficiency is not a direct metric because consumed energy depends on the utility power target and event duration; one SRP example observed a 5% energy reduction.

Lesson: Do not copy the broad policy language without adding a cost-allocation model if Henry's target paper is TEA or policy analysis.

## 16. Transfer to my own work

Evidence: The paper's transferable unit is a flexible load contract: reduction magnitude, event duration, ramping, performance constraints and event signal.

Inference: For wind-solar-hydrogen integration, this maps directly to electrolyzer flexibility, hydrogen storage dispatch or data-centre co-location with renewables, confidence high.

Lesson: In a green-hydrogen TEA paper, describe flexibility not only as capacity factor or curtailment absorption. Specify the service contract: how much load can move, for how long, what output metric is protected and what compensation is needed.

Lesson: For building decarbonization or demand response, use the same figure logic: architecture of control, real event traces, run matrix and mechanism plot.

## 17. KB outputs (mandatory)

### 5 Permanent Notes (atomic, evergreen, with `Evidence:` from this paper)

1. AI data-centre flexibility must be defined by workload service tiers, not by aggregate load alone. Evidence: The paper uses Flex 0-3 tags with explicit throughput allowances and reports zero SLA violations across the trial. Lesson: When modeling flexible demand, represent both power reduction and protected service metric.
2. A field trial becomes more persuasive when the event window is chosen by grid stress, not by laboratory convenience. Evidence: APS and SRP events were aligned with utility peak periods on 1 May and 3 May 2025. Lesson: Anchor experiments to the external system signal that decision-makers already use.
3. Software-only demand response can be tested without batteries when the controlled asset has internal scheduling slack. Evidence: The platform used job pausing, GPU reallocation and DVFS, with no hardware retrofit or storage requirement. Lesson: Before adding storage to a model, test whether operational slack can supply part of the flexibility.
4. Simulator validation should be tied to the control variable. Evidence: The simulator is evaluated on power prediction against measured cluster power and reports 4.52% RMSE relative to average experiment power. Lesson: Validate the model on the metric that triggers operational decisions.
5. Flexible-load papers need both event traces and mechanism plots. Evidence: Figs. 2-4 show grid-event response, while Fig. 6 shows workload-specific throughput response to GPU power caps. Lesson: Pair outcome proof with a mechanism figure so readers know when the result transfers.

### 5 Writing Lessons

1. Evidence: The title names the asset category, not the algorithm. Lesson: Use titles that state the new role of the system.
2. Evidence: The abstract gives asset size, location, duration, reduction and service constraint. Lesson: Put all boundary conditions in the headline result.
3. Evidence: The introduction distinguishes CPU/HPC prior work from GPU AI workloads. Lesson: Build the gap by changing the operating regime.
4. Evidence: Fig. 1 appears before event traces. Lesson: Give readers the control architecture before asking them to trust performance plots.
5. Evidence: The Discussion names both deployment regions and remaining workload limits. Lesson: Widen the implication only after naming transfer conditions.

### 5 Research-Design Lessons

1. Evidence: The study uses live APS and SRP events plus a CAISO emergency re-enactment. Lesson: Combine normal-operation and stress-event validation.
2. Evidence: Table 2 spans control knobs, policies, targets and durations. Lesson: Use a run matrix to show the test campaign, not only flagship cases.
3. Evidence: Flex 0 workloads are protected from modification. Lesson: Include non-flexible demand explicitly instead of assuming every load can move.
4. Evidence: The platform profiles job power-performance relationships before event execution. Lesson: Calibrate flexibility models on asset-specific response curves.
5. Evidence: The Methods state energy efficiency is not the direct target metric. Lesson: Match metrics to service type: demand response is a power and timing service before it is an energy-saving claim.

### 5 Future Research Questions

1. Inference: What tariff or capacity-payment design would compensate AI customers for Flex 1-3 participation without harming user trust, confidence medium?
2. Inference: How much interconnection capacity could be accelerated if planners modeled data centres with event-limited curtailability instead of fixed peak load, confidence medium?
3. Inference: How does multi-region workload migration compare with single-site throttling for real-time inference and model serving, confidence high?
4. Inference: What is the life-cycle cost trade-off among software flexibility, on-site storage and backup generation for AI data-centre grid services, confidence medium?
5. Inference: Can similar SLA-tiered flexibility contracts be built for electrolyzers, district cooling, EV depots or building loads, confidence high?

## 18. Final summary

**Top 3 lessons**:
1. Evidence: The paper's strongest move is proving a grid-facing service on a production AI cluster, not only simulating it.
2. Evidence: SLA-tiered workload tagging is the bridge between compute operations and grid flexibility.
3. Evidence: The figure sequence works because it moves from architecture to event proof to simulator validation to mechanism.

**Top 3 to transfer**:
1. Lesson: In flexible-load research, define the service contract in power, time, ramp and protected output.
2. Lesson: Use live or historically grounded events as validation anchors.
3. Lesson: Put a run matrix behind flagship cases so the paper does not depend on one event trace.

**Top 3 to NOT blindly copy**:
1. Inference: Do not generalize from one region and cluster to all data-centre markets without a market or planning model, confidence high.
2. Inference: Do not treat all AI workloads as flexible; real-time inference is a hard boundary, confidence high.
3. Inference: Do not frame demand response as energy savings unless the post-event workload completion effect is measured, confidence high.

**One-line takeaway** (the core research skill this paper teaches): Lesson: Turn a grid-planning assumption into a field-testable operating contract, then prove the contract with event traces and protected service metrics.

---

## Pass-2 follow-up (deferred)

Deferred Pass-2 questions:
1. Inference: Compare this paper's local throttling approach with Zheng et al. 2020's cross-data-centre load migration to separate temporal flexibility from spatial flexibility, confidence high.
2. Inference: Revisit the GitHub artefact after a repository-check pass to see whether the code and source data support method transfer into a flexible-load modeling project, confidence medium.
3. Lesson: Mine the paper's partnership structure as a model for energy-AI field demonstrations: operator, hardware vendor, utility, grid-research organization and forecasting provider.

## Cross-references

- Zotero parent key: `KWNBZ8FA`
- Main PDF attachment key: `9YAITN8R`
- Stub files: [[.raw/papers/KWNBZ8FA/metadata.json|metadata]], [[.raw/papers/KWNBZ8FA/zotero-attachments.md|zotero-attachments]], [[.raw/papers/KWNBZ8FA/data-availability.md|data-availability]], [[.raw/papers/KWNBZ8FA/code-availability.md|code-availability]], [[.raw/papers/KWNBZ8FA/repository-links.md|repository-links]], [[.raw/papers/KWNBZ8FA/article-page.md|article-page]], [[.raw/papers/KWNBZ8FA/asset-status.md|asset-status]]
- Related papers in this lab: [[papers/2020-J-data-center-load-migration-curtailment|Zheng et al. 2020, Joule]] shares data-centre flexibility and is cited as cross-site load migration; [[papers/2024-NE-h2-additionality-time-matching|Giovanniello et al. 2024, Nature Energy]] shares grid-connected flexible demand policy logic; [[papers/2022-NE-green-h2-probabilistic-feasibility|Odenweller et al. 2022, Nature Energy]] shares Nature Energy positioning around scale-up feasibility.
- Pattern pages it will inform after paper 10: [[patterns/methods/grid-interactive-flexible-loads]], [[patterns/figures/field-trial-control-response]], [[patterns/discussion/software-only-flexibility-claims]], [[patterns/research-gap-map/data-centre-grid-flexibility]]
- Playbook pages it will inform after paper 20: [[playbook/field-demonstration-paper-template]], [[playbook/figure-sequencing-for-control-papers]], [[playbook/flexible-load-service-contracts]]
- Contradictions: Evidence: No substantive contradiction with existing ingested pages was found in the index-level scan; this paper extends Zheng et al. 2020 by testing single-site workload orchestration rather than spatial load migration.
