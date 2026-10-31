"""Safe starter analysis for the de-identified VR dataset.

The Total SSQ score is reconstructed from the validated weighted subscores:
TS = (N/9.54 + O/7.58 + D/13.92) * 3.74.
"""

from pathlib import Path

import pandas as pd


DATA_FILE = Path(__file__).with_name("vr_experiment_public_candidate.csv")
REQUIRED_COLUMNS = {
    "participant_id",
    "trial_order",
    "fps",
    "posture",
    "nausea_subscore",
    "oculomotor_subscore",
    "disorientation_subscore",
    "ssq_total_score",
}


def load_data(path: Path = DATA_FILE) -> pd.DataFrame:
    df = pd.read_csv(path)
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")
    if len(df) != 76 or df["participant_id"].nunique() != 19:
        raise ValueError("Expected 76 trials from 19 participants.")
    if df.duplicated(["participant_id", "trial_order"]).any():
        raise ValueError("Participant/trial keys must be unique.")
    return df


def summarize_conditions(df: pd.DataFrame) -> pd.DataFrame:
    outcomes = [
        "nausea_subscore",
        "oculomotor_subscore",
        "disorientation_subscore",
        "ssq_total_score",
    ]
    return (
        df.groupby(["fps", "posture"])[outcomes]
        .agg(["count", "mean", "std", "median"])
        .round(2)
    )


if __name__ == "__main__":
    data = load_data()
    print(summarize_conditions(data).to_string())
