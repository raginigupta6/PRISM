# SSQ correction impact audit

## Bottom line

Both the analysis notebook and the paper must change. Editing only the numbers in Overleaf is not sufficient because the original notebook repeatedly uses the incorrectly calculated Total SSQ columns as outcomes for plots, deltas, regressions, machine-learning models, and narrative conclusions.

The corrected dataset has 76 trials from 19 participants. All corrected totals validate against:

```text
Total SSQ = (N / 9.54 + O / 7.58 + D / 13.92) * 3.74
```

where N, O, and D are the already-weighted subscale scores.

## Numerical impact

| Statistic | Legacy incorrect total | Corrected Total SSQ |
|---|---:|---:|
| Mean | 394.44 | 37.60 |
| Median | 352.79 | 33.66 |
| Minimum | 0.00 | 0.00 |
| Maximum | 1260.38 | 115.94 |

Corrected condition means:

| Condition | n | Mean | SD | Median |
|---|---:|---:|---:|---:|
| 60 FPS, Sitting | 19 | 32.68 | 24.80 | 26.18 |
| 60 FPS, Standing | 19 | 42.91 | 28.38 | 37.40 |
| 90 FPS, Sitting | 19 | 37.79 | 30.94 | 33.66 |
| 90 FPS, Standing | 19 | 37.01 | 25.12 | 41.14 |

Compact within-participant diagnostic tests using corrected totals:

| Contrast | Mean difference | p-value |
|---|---:|---:|
| 90 FPS minus 60 FPS | -0.39 | 0.9371 |
| Standing minus Sitting | 4.72 | 0.2599 |
| FPS by posture difference-in-differences | -11.02 | 0.1246 |

These tests do not support a significant overall FPS effect, posture effect, or FPS-by-posture interaction. They are diagnostics; the final mixed-effects model should still be rerun after its specification is reviewed.

## Problems in the original notebook

1. Multiple cells directly select the legacy `Post-VR SSQ Total Score` columns, so their outputs are invalid after the scoring correction.
2. The first cell is tied to Google Colab and a personal Drive path, so it is not repository-reproducible.
3. Cell 19 contains `pip install pingouin` as invalid Python instead of a notebook shell or magic command.
4. Cell 62 contains a stray `presentation` token and cannot parse.
5. Missing gender is inferred from participant names and every other name defaults to male. Gender must remain missing/unknown unless self-reported.
6. Some paired tests compare raw arrays without first aligning observations by participant and condition. Pairing should use an explicit participant-level pivot.
7. The notebook describes change from pre-VR baseline, but its `trial_deltas` function uses the previous post-trial score as the baseline after Trial 1. Those are different estimands and need distinct names and analyses.
8. The cumulative analysis takes a cumulative sum of four post-trial SSQ scores. A cumulative sum is guaranteed to rise when scores are nonnegative, so it cannot establish physiological accumulation or a “12-minute wall.”
9. Several cells contain duplicated analyses and hard-coded prose conclusions that are not linked to validation checks.

## Paper sections requiring regeneration

- Abstract: the 312-point posture effect, 410-points-per-trial claim, 12-minute wall, IPD variance claim, and symptom percentages.
- Results 4.1 and Table 4/Figure 4: all Total SSQ ranges, means, subgroup comparisons, and ANOVAs.
- Results 4.3, Figure 5, Tables 5-6: recompute after defining whether delta means pre-baseline change or trial-to-trial change.
- Results 4.4, Tables 7-8: refit both mixed-effects models using corrected totals and a reviewed repeated-measures specification.
- Results 4.5 and Figure 6: remove the cumulative-sum inference; analyze post-trial score or correctly defined change over trial order instead.
- Results 4.6, Figure 7, Table 9: retrain and validate the IPD model with corrected totals. With only 19 participants, participant-level grouped cross-validation and uncertainty reporting are essential.
- Conclusions and design recommendations: rewrite after corrected inferential results are known.

The weighted Nausea, Oculomotor, and Disorientation subscales themselves remain numerically usable if the original symptom severities were summed correctly. Their repeated-measures tests and interpretations should still be independently verified. A pie chart made by summing the three overlapping weighted subscales should not be described as each subscale's percentage contribution to Total SSQ.
