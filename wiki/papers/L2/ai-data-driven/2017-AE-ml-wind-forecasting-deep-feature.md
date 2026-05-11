---
zotero_key: "W86HHD6H"
title: "A data-driven multi-model methodology with deep feature selection for short-term wind forecasting"
journal: "Applied Energy"
year: 2017
doi: "10.1016/j.apenergy.2017.01.043"
topic:
  - wind-forecasting
  - machine-learning
  - ensemble-forecasting
  - feature-selection
paper_type:
  - forecasting-method
  - data-driven-model
main_contribution:
  - two-layer-ensemble
  - deep-feature-selection
  - deterministic-and-probabilistic-forecasting
method_type:
  - machine-learning
  - ensemble-learning
  - feature-selection
  - probabilistic-forecasting
journal_role: applied_flagship
ingest_depth: B_medium
subdomain_primary:
  - ai-data-driven
subdomain_secondary:
  - re-tech-resources
  - power-systems
data_assets:
  main_pdf: true
  supplementary: false
  data_statement: false
  code_statement: false
  code_repository: false
relevance_to_my_research: medium
ingest_status: draft
address: c-000030
tags:
  - paper-analysis
  - L2
  - B-medium
---

# A data-driven multi-model methodology with deep feature selection for short-term wind forecasting

> Zotero: `W86HHD6H` · DOI: 10.1016/j.apenergy.2017.01.043 · Journal: Applied Energy (2017) · **L2 medium summary**

## 1. One-paragraph summary

**Evidence:** Feng et al. build a 1-hour-ahead wind-speed forecasting workflow in which ANN, SVR, GBM, and RF models first generate forecasts, then a second-layer blending model combines them into deterministic and probabilistic outputs. **Evidence:** The feature-selection pipeline is PCA, Granger causality, ACF/PACF, and RFE, tested on 2015 SURFRAD data from seven U.S. stations using NMAE and NRMSE. **Evidence:** Their best multi-model plus deep-feature setup improves NMAE by up to 30.87% and NRMSE by up to 30.03% against single-algorithm models, and beats persistence at all seven locations. **Inference (medium):** The reusable value is a compact ML validation recipe: multi-site data, nested model comparison, feature ablation, and uncertainty bands.

## 2. Why it's in the lab

**Subdomain fit**: `ai-data-driven` primary because the paper's subject is an ML forecasting architecture, not merely an energy model that happens to use ML. `re-tech-resources` and `power-systems` are secondary because the task is wind-resource forecasting for scheduling, dispatch, reserve, curtailment, and storage-operation decisions.

**Why this paper rather than skip**: **Evidence:** Applied Energy is locked as `applied_flagship`, and the paper gives an applied-ML structure: literature gap, algorithm stack, feature-selection pipeline, seven-location case, deterministic metrics, and probabilistic reliability/sharpness checks. **Lesson:** For Henry's forecasting or surrogate-model sections, justify an ensemble by showing why one algorithm fails across sites, then make the ensemble answer that failure.

## 3. Method note (compressed)

- **Evidence:** First layer: ANN, SVR with linear and polynomial kernels, GBM with Gaussian and Laplacian loss, and RF; second layer: blending algorithms tested for generalizability.
- **Evidence:** Feature selection is staged: PCA removes low-contribution variables, GCT tests causal usefulness, ACF/PACF selects wind-speed lags, and RFE trims the final lagged feature set.
- **Evidence:** Case boundary is seven SURFRAD stations, 2015-01-01 to 2015-12-31, minute data cleaned and averaged to hourly data; the target is 1-hour-ahead wind speed.
- **Evidence:** The data are split into thirds: first-layer training, second-layer training from first-layer forecasts plus observations, and final validation.

## 4. Parameter highlights

| Parameter | Value | Unit | Year / context | Source | Reusable for Henry? |
|---|---:|---|---|---|---|
| Case locations | 7 | stations | SURFRAD, 2015 | Table 1, Section 3.1 | Yes, as multi-site validation pattern |
| Raw temporal resolution | 1 | minute | Averaged to hourly | Section 3.1 | Yes, for preprocessing disclosure |
| Retained PCA variables | 4 | variables | Wind speed, temperature, humidity, pressure | Table 2 | Yes, as feature-screen example |
| Final BND feature subset | 15 | lagged features | RFE selected after RMSE tradeoff | Fig. 7, Section 3.2.4 | Yes, as compute-accuracy tradeoff |
| Best BND RFE RMSE before tradeoff | 0.897 | m/s | 30-feature model | Fig. 7, Section 3.2.4 | Maybe, case-specific |
| Best reported improvement | 30.87 / 30.03 | % NMAE / NRMSE | Deep-feature ensemble vs single algorithms | Tables 11-12, Section 3.4 | Yes, as benchmark effect size |

**Bank rows produced**: no parameter-bank rows for physical energy-system parameters. `.raw/papers/W86HHD6H/bank-candidates.md` records method and sensitivity candidates only.

## 5. Three lessons

1. **Ensemble justification should be empirical, not decorative** (method): **Evidence:** The paper first shows that no single first-layer algorithm dominates across all seven locations, then shows that the two-layer ensemble improves single-algorithm accuracy by up to 23.8% NMAE and 25.6% NRMSE even before deep feature selection. **Lesson:** When using an ensemble in Henry's work, include a site-by-site or scenario-by-scenario table showing why model diversity is needed.
2. **Feature selection needs a staged audit trail** (method): **Evidence:** The workflow moves from PCA to GCT to ACF/PACF to RFE, and Section 3.2 reports why wind direction and pressure are dropped while wind-speed, temperature, and humidity lags remain. **Lesson:** For data-driven energy models, describe feature elimination as a sequence of tests, not as a black-box preprocessor.
3. **Probabilistic outputs make the forecast useful for operations** (figure): **Evidence:** Figures 9-11 pair deterministic traces with confidence intervals, reliability diagrams, and sharpness diagrams, and the conclusion links improved forecasts to unit commitment, economic dispatch, reserves, curtailment, and storage scheduling. **Lesson:** If Henry reports a forecasting model, add uncertainty visuals that map directly to operator decisions.

## 6. Top-vs-applied note (one line)

**Inference (medium):** This is L2 rather than L1 because the contribution is an applied forecasting workflow and benchmark study, not a field-level reframing of renewable integration.

## Cross-references

- Zotero: `W86HHD6H`
- Subdomain hub: [[wiki/subdomains/ai-data-driven]]
- Bank pages updated: none directly by this ingest
- Pattern pages this paper informs (subdomain): [[wiki/patterns/subdomain/ai-data-driven]]
- Related L2 papers in this subdomain: first L2 applied-flagship page in `ai-data-driven`

## Promotion notes (optional)

- Promote to L2-A if Henry plans to reuse the two-layer ensemble or staged feature-selection chain in a forecasting, dispatch-surrogate, or wind-to-hydrogen uncertainty model.
