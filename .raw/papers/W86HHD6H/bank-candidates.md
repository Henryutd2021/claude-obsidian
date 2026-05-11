# Bank Candidates

These are candidates for orchestrator review. This B-medium ingest does not directly merge rows into `wiki/banks/*`.

## Parameter candidates

None. The paper does not provide reusable physical energy-system parameters.

## Sensitivity candidates

| Candidate bank | Variable / design | Values tested | Outcome metric | Evidence | Suggested row |
|---|---|---|---|---|---|
| `wiki/banks/sensitivity-bank/feature-subset-size.md` | RFE feature subset size | Different subset sizes, with 30 features best and 15 chosen for compute tradeoff | RMSE | Fig. 7 and Section 3.2.4 | Feature subset size can be treated as a sensitivity axis in ML energy forecasting; report both best error and chosen compute-aware size. |

## Method candidates

| Candidate bank | Method pattern | Evidence | Suggested row |
|---|---|---|---|
| `wiki/banks/method-bank/ensemble-forecasting.md` | Two-layer ensemble with first-layer ML forecasts and second-layer blending | Fig. 1, Section 2, Tables 9-12 | Use ensemble only after showing cross-site instability of single algorithms. |
| `wiki/banks/method-bank/feature-selection.md` | PCA plus GCT plus ACF/PACF plus RFE sequence | Fig. 2, Section 2.1, Section 3.2 | Present feature selection as a staged audit trail with a reason for each dropped variable. |
| `wiki/banks/method-bank/probabilistic-forecast-validation.md` | Reliability and sharpness diagrams for probabilistic forecast intervals | Figures 9-11, Section 3.5 | Pair deterministic error metrics with uncertainty diagnostics when forecast outputs support dispatch or reserves. |
