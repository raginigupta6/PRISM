# Minimal SSQ revision package

This is a focused revision, not a rewrite of the entire paper. It preserves the study design, research questions, apparatus, counterbalancing, and the investigation of posture and frame rate, while correcting the SSQ scoring and narrowing unsupported claims.

## 1. Replacement for the SSQ scoring method

### Clinical Scoring Protocol

Simulator Sickness Questionnaire (SSQ) responses were scored according to Kennedy et al. Each of the 16 symptoms was rated from 0 (none) to 3 (severe). Raw symptom ratings were summed according to their membership in the Nausea, Oculomotor, and Disorientation symptom sets, producing the intermediate sums [1], [2], and [3], respectively. Weighted subscale scores were then calculated as N = [1] x 9.54, O = [2] x 7.58, and D = [3] x 13.92. The Total SSQ score was calculated from the unweighted intermediate sums as TS = ([1] + [2] + [3]) x 3.74. Thus, the weighted N, O, and D values were not added together to obtain TS.

## 2. Clarify when SSQ was administered

Use this only after confirming it matches the actual protocol:

> The SSQ was administered once before the experimental session and once immediately after each of the four VR conditions, for five administrations per participant. The pre-session score was used only as an initial participant-level baseline. Because no new pre-condition SSQ was collected after each recovery interval, we do not interpret baseline-adjusted values for Trials 2-4 as condition-specific symptom onset. Instead, post-condition scores are analyzed while accounting for trial order and participant-level repeated measures.

This disclosure directly answers the reviewer's question. Do not say that every condition had its own pre/post SSQ unless eight administrations actually occurred.

## 3. Replacement for Overall Cybersickness Severity

Across 76 post-condition observations from 19 participants, the corrected Total SSQ score had a mean of 37.60 (SD = 27.12), a median of 33.66, and a range of 0.00-115.94. The condition-level means were 32.68 (SD = 24.80) for 60 FPS Sitting, 42.91 (SD = 28.38) for 60 FPS Standing, 37.79 (SD = 30.94) for 90 FPS Sitting, and 37.01 (SD = 25.12) for 90 FPS Standing. These corrected values fall within the valid SSQ range and replace all previously reported totals calculated by summing the weighted subscales.

## 4. Replacement condition table

| Frame rate | Posture | n | Mean | SD | Median |
|---|---|---:|---:|---:|---:|
| 60 FPS | Sitting | 19 | 32.68 | 24.80 | 26.18 |
| 60 FPS | Standing | 19 | 42.91 | 28.38 | 37.40 |
| 90 FPS | Sitting | 19 | 37.79 | 30.94 | 33.66 |
| 90 FPS | Standing | 19 | 37.01 | 25.12 | 41.14 |

## 5. Replacement participant-trait table

These are descriptive trial-level summaries; participant counts are shown separately.

| Trait | Group | Participants | Trials | Corrected SSQ mean +/- SD |
|---|---|---:|---:|---:|
| Motion-sickness history | Never | 6 | 24 | 20.26 +/- 18.29 |
|  | Rarely | 5 | 20 | 41.70 +/- 32.04 |
|  | Sometimes | 6 | 24 | 43.79 +/- 18.86 |
|  | Often | 2 | 8 | 60.78 +/- 31.66 |
| VR familiarity | Experienced | 5 | 20 | 23.56 +/- 20.70 |
|  | Some Experience | 11 | 44 | 37.66 +/- 26.08 |
|  | No Experience | 3 | 12 | 60.78 +/- 25.92 |

Call the motion-sickness item a self-reported history category, not a validated susceptibility score or MSSQ substitute.

## 6. Mixed-model result that can remain, with narrower wording

The corrected mixed-effects model included frame rate, posture, centered trial order, their interactions, and participant-specific random intercepts and trial-order slopes. The overall model-averaged contrast between standing and sitting was +4.48 SSQ points (95% CI [-2.12, 11.08], p = .183), and the corresponding frame-rate contrast was -0.35 points (95% CI [-8.74, 8.03], p = .934). Therefore, the corrected analysis does not support a general main effect of posture or frame rate across all conditions.

At 60 FPS and average trial order, however, the conditional standing coefficient was +10.34 points (p = .035) in the technical-factor model and +10.02 points (p = .041) after including participant traits. This supports a limited statement that standing was associated with higher SSQ scores under the 60-FPS reference condition, not the broader claim that standing universally dominates frame rate.

In the adjusted model, participants in the self-reported Often motion-sickness category had scores 34.34 points higher than the Never reference group (p = .036), and participants with No Experience in VR had scores 34.53 points higher than Experienced participants (p = .032). These estimates are exploratory because the motion-sickness item was not a validated MSSQ measure and the groups were small.

## 7. Minimal abstract replacement

Nineteen participants completed a counterbalanced within-subjects study combining two frame rates (60 and 90 FPS) with seated and standing posture during a smooth-locomotion VR task. After correcting Total SSQ scoring according to Kennedy et al., overall marginal contrasts for frame rate and posture were not statistically significant. A mixed-effects model nevertheless indicated higher SSQ scores for standing under the 60-FPS reference condition, while self-reported motion-sickness history and limited prior VR experience were associated with greater discomfort. These findings suggest that posture effects may be condition-dependent and that individual differences and exposure order should be considered alongside rendering performance. Given the single pre-session baseline and short recovery intervals, the results are interpreted as exploratory rather than as evidence of condition-independent symptom accumulation.

## 8. Claims to preserve, revise, or remove

### Preserve

- The study jointly examines frame rate and posture in a counterbalanced within-subjects VR experiment.
- Corrected condition means show the highest mean for 60 FPS Standing and the lowest for 60 FPS Sitting.
- The conditional standing association at 60 FPS remains statistically significant in the corrected mixed model.
- Self-reported motion-sickness history and lack of prior VR experience remain associated with higher scores in the adjusted model, with exploratory wording.
- The weighted Nausea, Oculomotor, and Disorientation subscale values can remain if their symptom-level sums were originally correct.

### Revise

- Replace “posture was the dominant predictor” with the conditional 60-FPS finding.
- Describe p = .076 for the Oculomotor posture effect as a non-significant trend, not evidence of an effect.
- Describe the one-item motion-sickness measure as self-reported history, not validated susceptibility.
- State exactly how many SSQ administrations occurred and distinguish initial-baseline change from trial-to-trial change.

### Remove unless a new valid analysis supports them

- SSQ values near or above 600 and the severe-score threshold based on that scale.
- The 312-388 point standing effect.
- The approximately 410-point-per-trial accumulation claim.
- The “12-minute wall” or “point of no return.”
- Causal claims that the observed order pattern proves physiological accumulation.
- The claim that IPD mismatch explains approximately 27% of symptom variance until the model is rerun with corrected totals and participant-grouped validation.

## 9. Short reviewer-response wording

> We thank the reviewers for identifying the Total SSQ scoring error. We recalculated every Total SSQ value from the unweighted intermediate symptom sums using TS = ([1] + [2] + [3]) x 3.74, regenerated all affected tables and figures, and reran the statistical models. Corrected scores ranged from 0.00 to 115.94. We also clarified the SSQ administration schedule, removed unsupported severity and cumulative-threshold claims, and narrowed the posture conclusion to the conditional association supported by the corrected mixed-effects model.
