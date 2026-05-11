# Code Availability: PIQKGJNB

Source: Yang et al. 2022, *Nature Energy*, "Code availability" section.

## Verbatim statement

> The analysis is based on the IEA-ETSAP model tool VEDA-TIMES with its official introduction for model tools and algorithm shown at https://iea-etsap.org/index.php/documentation and https://iea-etsap.org/docs/Documentation_for_the_TIMES_Model-PartIII.pdf.

## Structural classification

| Property | Value |
|---|---|
| Has GitHub / Zenodo / OSF deposit? | No |
| Has institutional model documentation URL? | Yes (IEA-ETSAP) |
| Custom code / scripts deposited? | No |
| Custom model parameterization deposited? | No (referred to Supplementary tables only) |
| Reproducible from public materials? | No, in the strict sense. The TIMES framework is documented but VEDA-TIMES is a commercial/licensed tool; the specific China-MAPLE parameterization is in Supplementary Information but not as a runnable model file |
| 2026 Nature compliance? | Acceptable in 2022; would face reviewer pushback in 2026 |

## External references in CA

- `https://iea-etsap.org/index.php/documentation` (model family documentation)
- `https://iea-etsap.org/docs/Documentation_for_the_TIMES_Model-PartIII.pdf` (algorithm spec)

## Lesson for my own CA statements

Evidence: the paper outsources reproducibility to the institutional framework rather than depositing model files.

Inference: this is the dominant pattern for TIMES / MESSAGE / GCAM / IMAGE-class integrated models — the family is open-documented but per-paper parameterization is not. Reviewers in 2022 accepted this. In 2026 they increasingly do not.

Lesson: if I use a TIMES-class workhorse, deposit my parameterization tables and any GAMS / pre-processing scripts on Zenodo as a single archive with a DOI. Cite that DOI in CA. This is cheap insurance against reviewer 3.
