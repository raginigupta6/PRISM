# PRISM: Characterizing the Interplay of Posture and Rendering Performance in VR Cybersickness

**PRISM** (**P**osture and **R**endering **I**nteractions in **S**ickness **M**easurement) is a controlled human-experience study, dataset, and evaluation suite for characterizing VR cybersickness under varying rendering and user conditions.

Cybersickness depends on more than rendering performance: physical posture, individual susceptibility, headset calibration, and prior exposure all shape how users experience the same VR content. PRISM links Simulator Sickness Questionnaire (SSQ) outcomes to the system and human context in which they were collected, so researchers can test whether conclusions drawn from rendering configurations alone change once posture, participant traits, and exposure history are taken into account.

## At a glance

| | |
|---|---|
| Design | 2 × 2 within-subjects (frame rate × posture) |
| Participants | 19 (15 male, 4 female), ages 18 to 45+, university population |
| Exposures | 76 trials (4 per participant, 3 minutes each) |
| Frame rate | Configured 60 and 90 FPS |
| Posture | Sitting and standing |
| Outcome | SSQ: Nausea (N), Oculomotor (O), Disorientation (D), and Total |
| Context | Motion sickness history, VR familiarity, gaming experience, IPD calibration, trial order |

## Study design

### Apparatus

- **Headset:** Pico Neo 3, streamed wirelessly over ALVR + SteamVR from a Windows PC with an NVIDIA RTX 3080.
- **Stream:** HEVC (H.265), 4288 × 2256, constant 30 Mbps target bitrate; adaptive frame rate disabled, foveated rendering enabled.
- **Content:** a modified version of Unity Technologies' open-source FPS Sample. Participants move with joystick-controlled smooth locomotion while physically seated or standing, producing visual motion without matching physical movement.
- **IPD calibration:** each participant's IPD was measured with the EyeMeasure mobile app, and the headset was set to the nearest supported preset (58, 63.5, or 69 mm). IPD mismatch is recorded as `|IPD_measured − IPD_configured|`.

### Protocol

Each participant completed four three-minute exposures, one per frame-rate × posture combination. Trials are grouped into frame-rate blocks to minimize configuration changes, with posture alternating within each block. Four counterbalanced sequences vary the starting frame rate and posture (Si = sitting, St = standing):

| Seq. | Trial 1 | Trial 2 | Trial 3 | Trial 4 |
|---|---|---|---|---|
| 1 | 60-St | 60-Si | 90-Si | 90-St |
| 2 | 60-Si | 60-St | 90-St | 90-Si |
| 3 | 90-St | 90-Si | 60-Si | 60-St |
| 4 | 90-Si | 90-St | 60-St | 60-Si |

Participants removed the headset and completed the SSQ immediately after each trial. A five-minute recovery interval separated trials within a frame-rate block, and a ten-minute break separated the two blocks. A pre-exposure baseline SSQ was also collected.

## Dataset

PRISM organizes measurements into participant-level and trial-level records.

| Category | Recorded information |
|---|---|
| Study population | 19 participants; 76 trials |
| System configuration | Configured 60/90 FPS; headset and streaming settings |
| Interaction conditions | Sitting and standing posture |
| Participant context | Age group, gender, gaming experience, VR familiarity, motion sickness history, vision correction |
| Headset calibration | Measured IPD, selected preset, IPD mismatch |
| Exposure history | Trial order, condition sequence, recovery intervals |
| Symptom outcomes | Baseline and post-exposure N/O/D subscores, raw sums, and Total SSQ |

### Files

| File | Description |
|---|---|
| `vr_experiment_public_candidate.csv` | Trial-level dataset: participant pseudonym, trial order, FPS, posture, N/O/D weighted subscores, and corrected Total SSQ. No demographics or IPD. |
| `restricted/vr_experiment_internal_pseudonymized.csv` | Full trial-level dataset with participant context (age group, gender, VR familiarity, motion sickness history, gaming hours, vision correction), IPD measurements, baseline SSQ, raw N/O/D sums, and the legacy incorrect total kept for audit (`legacy_total_ssq_incorrect`). |
| `restricted/participant_key.csv` | Placeholder for the pseudonym key; contains no identifiers. |
| `analysis_starter.py` | Validates the public CSV and produces condition-level descriptive statistics. |
| `corrected_mixed_models.py` | Reproduces the corrected mixed-effects estimates and marginal contrasts. |
| `VR_Experiment_corrected.ipynb` | Executed notebook validating corrected Total SSQ values, with condition summaries and within-participant tests. |
| `SSQ_correction_impact.md` | Audit of the SSQ scoring correction and which results it affects. |
| `SSQ_minimal_revision_text.md` | Paper revision text consistent with the corrected scoring. |

Participants are identified only by pseudonyms such as `VR-0CE9CD`.

## SSQ scoring

The SSQ comprises 16 symptom items scored 0 to 3, combined into three weighted subscales. The stored N, O, and D values are already weighted, so the Total SSQ is reconstructed from the raw sums:

```text
n_raw = N / 9.54
o_raw = O / 7.58
d_raw = D / 13.92
Total SSQ = (n_raw + o_raw + d_raw) * 3.74
```

Do **not** compute Total SSQ as `(N + O + D) * 3.74`. That double-applies the subscale weights and was the error in the original analysis. Totals reported in early drafts of the paper (for example, means in the hundreds) used this incorrect formula. See [`SSQ_correction_impact.md`](SSQ_correction_impact.md) for the full audit.

## Key observations

- **Individual differences are large.** Symptom severity varies substantially across participants. Motion sickness history and lack of prior VR experience are associated with higher reported symptoms, so pooled averages can hide important differences between users.
- **Higher frame rate does not consistently reduce symptoms.** Corrected Total SSQ condition means:

  | Condition | n | Mean | SD | Median |
  |---|---:|---:|---:|---:|
  | 60 FPS, Sitting | 19 | 32.68 | 24.80 | 26.18 |
  | 60 FPS, Standing | 19 | 42.91 | 28.38 | 37.40 |
  | 90 FPS, Sitting | 19 | 37.79 | 30.94 | 33.66 |
  | 90 FPS, Standing | 19 | 37.01 | 25.12 | 41.14 |

- **Disorientation dominates.** Disorientation is the largest symptom dimension in every condition, and oculomotor discomfort is consistently higher when standing. Mean (± SD) subscale scores:

  | Subscale | 60 Sit | 60 Stand | 90 Sit | 90 Stand |
  |---|---|---|---|---|
  | Nausea | 20.8 ± 16.5 | 27.1 ± 21.0 | 22.1 ± 24.1 | 21.3 ± 18.4 |
  | Oculomotor | 19.3 ± 15.6 | 29.3 ± 25.9 | 26.3 ± 24.0 | 28.5 ± 22.0 |
  | Disorientation | 35.2 ± 29.2 | 50.6 ± 44.8 | 48.4 ± 49.9 | 50.2 ± 40.6 |

  Repeated-measures ANOVA shows no significant main effects or interactions (p > 0.05); posture has a suggestive association with oculomotor discomfort (F = 3.55, p = 0.076).
- **Exposure order matters.** Symptom changes vary across successive trials, so trial order and preceding conditions should be modeled rather than ignored.
- **Headset calibration is worth recording.** Exploratory analysis suggests IPD mismatch may contribute to individual differences in discomfort; this needs validation with more participants.

## Evaluation tasks

PRISM defines four complementary evaluation tasks of increasing context:

| Task | Factors | Objective |
|---|---|---|
| B1 | Frame rate | Estimate configuration-related differences |
| B2 | Frame rate, posture | Examine posture-aware effects and interactions |
| B3 | B2 + user traits | Assess susceptibility and VR familiarity |
| B4 | B3 + trial order | Examine exposure-history sensitivity |

Recommended practice:

- Account for repeated measures with participant-level random effects (for example, linear mixed-effects models).
- Report effect estimates, uncertainty intervals, and sensitivity to participant-level variability.
- For predictive models, keep all observations from a participant in the same train or test partition to avoid participant leakage.

## Getting started

```bash
pip install -r requirements.txt
python analysis_starter.py
python corrected_mixed_models.py
```

Requires Python with pandas, numpy, scipy, and statsmodels (see `requirements.txt`).

## Limitations

1. 19 participants from a university population limits statistical power and generalizability, especially for small susceptibility subgroups.
2. Four short exposures with recovery intervals cannot separate habituation, fatigue, and longer-term carryover.
3. Frame rates are configured settings, not measured delivered performance; wireless latency and frame drops are not isolated.
4. Outcomes are post-exposure questionnaires, not continuous physiological measurements.
5. The SSQ correction assumes each symptom's reported severity (0 to 3) was added to every applicable N/O/D column.

## Future directions

PRISM motivates multimodal VR comfort sensing that synchronizes rendering telemetry (delivered frame rate, frame timing, streaming latency) with wearable physiology (heart rate, HRV, electrodermal activity), eye tracking, EEG, and head and body motion, so discomfort can be detected earlier and rendering adapted to each user.

## Ethics

All participants gave informed consent and were told they could stop at any time. Exposures were limited to three minutes with recovery intervals between trials. Participants are identified only by pseudonyms in this dataset.

## Citation

The paper is currently under anonymous review. Citation details will be added on publication.
