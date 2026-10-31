"""Reproduce mixed-effects results using corrected Total SSQ scores."""

from pathlib import Path
import warnings

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf


DATA_PATH = (
    Path(__file__).resolve().parent
    / "restricted"
    / "vr_experiment_internal_pseudonymized.csv"
)


def prepare_data(path: Path = DATA_PATH) -> pd.DataFrame:
    df = pd.read_csv(path).rename(
        columns={
            "participant_id": "participant",
            "ssq_total_score": "SSQ",
            "fps": "FPS",
            "posture": "Posture",
            "trial_order": "Trial",
            "motion_sickness_history": "Motion",
            "vr_familiarity": "VR",
        }
    )
    df["FPS"] = df["FPS"].astype("category")
    df["Posture"] = pd.Categorical(
        df["Posture"], categories=["Sitting", "Standing"]
    )
    df["Motion"] = df["Motion"].astype("category")
    df["VR"] = df["VR"].astype("category")
    # Center at the mean trial so the conditional main effects are interpretable.
    df["Trial_centered"] = df["Trial"] - df["Trial"].mean()
    return df


def fit_model(df: pd.DataFrame, include_traits: bool):
    formula = "SSQ ~ FPS * Posture * Trial_centered"
    if include_traits:
        formula += " + Motion + VR"
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        result = smf.mixedlm(
            formula,
            df,
            groups=df["participant"],
            re_formula="~Trial_centered",
        ).fit(reml=True, method="cg", maxiter=5000, disp=False)
    if not result.converged:
        raise RuntimeError("Mixed-effects model failed to converge")
    return result


def linear_contrast(result, weights: dict[str, float]) -> pd.Series:
    names = result.model.exog_names
    contrast = np.zeros((1, len(names)))
    for term, weight in weights.items():
        contrast[0, names.index(term)] = weight
    test = result.t_test(contrast)
    interval = test.conf_int()[0]
    return pd.Series(
        {
            "estimate": float(test.effect),
            "standard_error": float(test.sd),
            "ci_low": float(interval[0]),
            "ci_high": float(interval[1]),
            "p_value": float(test.pvalue),
        }
    )


def main() -> None:
    df = prepare_data()
    for label, include_traits in [
        ("Technical-factor model", False),
        ("Adjusted participant-trait model", True),
    ]:
        result = fit_model(df, include_traits)
        print(f"\n{label} (converged={result.converged})")
        fixed = result.model.exog_names
        intervals = result.conf_int()
        table = pd.DataFrame(
            {
                "estimate": result.params[fixed],
                "ci_low": intervals.loc[fixed, 0],
                "ci_high": intervals.loc[fixed, 1],
                "p_value": result.pvalues[fixed],
            }
        )
        print(table.round(4).to_string())

        # Average each contrast equally over the two levels of the other factor.
        posture = linear_contrast(
            result,
            {
                "Posture[T.Standing]": 1.0,
                "FPS[T.90]:Posture[T.Standing]": 0.5,
            },
        )
        fps = linear_contrast(
            result,
            {
                "FPS[T.90]": 1.0,
                "FPS[T.90]:Posture[T.Standing]": 0.5,
            },
        )
        print("\nMarginal contrasts at average trial order")
        print(pd.DataFrame({"Standing - Sitting": posture, "90 - 60 FPS": fps}).T.round(4))


if __name__ == "__main__":
    main()
