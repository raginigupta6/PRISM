# PRISM: Characterizing the Interplay of Posture and Rendering Performance in VR Cybersickness (Dataset and evaluation suite)

This private research-team repository contains privacy-reduced derivatives of the original study data plus a restricted participant key. The original files were not modified.

## Files

- `restricted/vr_experiment_internal_pseudonymized.csv`: for the approved research team only. Direct identifiers, consent records, free-text notes, and unused columns were removed. Exact demographics and IPD values remain, so this file is pseudonymized rather than anonymous and must stay restricted. The original incorrectly calculated totals are retained as `legacy_total_ssq_incorrect` solely for audit comparison.
- `restricted/participant_key.csv`: maps study pseudonyms to source participant numbers and names. This is directly identifying human-subject data and is included only for authorized validation.
- `restricted/README.md`: handling and release restrictions for the two restricted files.
- `vr_experiment_public_candidate.csv`: a conservative sharing candidate. It contains participant pseudonyms, trial order, experimental conditions, the three weighted SSQ subscores, and a corrected Total SSQ score. It excludes demographics, exact IPD, consent information, and free text.
- `analysis_starter.py`: validates the public candidate and produces condition-level descriptive statistics using the corrected Total SSQ score.
- `VR_Experiment_corrected.ipynb`: executed research-team notebook that validates the corrected Total SSQ values and reports corrected condition summaries and within-participant diagnostic tests. It reads the restricted pseudonymized dataset.
- `SSQ_correction_impact.md`: audit of the original notebook and the corresponding paper sections that must be regenerated.
- `SSQ_minimal_revision_text.md`: copy-ready, focused paper revisions that preserve defensible claims after corrected scoring.
- `corrected_mixed_models.py`: reproduces the corrected mixed-effects estimates and marginal contrasts used in the minimal revision text.

## SSQ scoring correction

The stored Nausea, Oculomotor, and Disorientation values divide exactly into integer raw sums using their standard multipliers. The Total SSQ score is therefore reconstructed as:

```text
n_raw = N / 9.54
o_raw = O / 7.58
d_raw = D / 13.92
Total SSQ = (n_raw + o_raw + d_raw) * 3.74
```

Do not calculate Total SSQ as `(N + O + D) * 3.74`; N, O, and D have already been multiplied by their own scaling factors.

## Important limitations

1. Do not release any study data until the consent form and human-subjects approval are checked for data-sharing permission.
2. This correction is valid only if each symptom's reported severity (0, 1, 2, or 3) was added to every applicable N/O/D column. Merely counting a non-zero symptom as 1 would make the stored subscores invalid.
3. With only 19 participants, even the public candidate may carry residual re-identification risk. Institutional review is still required.
4. The files under `restricted/` contain identifiable or pseudonymized human-subject data. Limit access to approved study personnel.
5. Never make this repository public: deleting the key later does not remove it from Git history. Create a separate clean repository/export containing only the approved anonymous files for Open Science publication.

## Public release boundary

The intended public candidate is `vr_experiment_public_candidate.csv` plus the analysis code and documentation. Do not copy `restricted/`, raw data, consent records, or Git history into the public Open Science release.
