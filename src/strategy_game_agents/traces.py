from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

import pandas as pd


REQUIRED_TRACE_COLUMNS = ("participant_id", "round", "option_id", "payoff")


@dataclass(frozen=True)
class ParticipantTraceSchema:
    allowed_options: tuple[str, ...] = ()

    def __init__(self, allowed_options: Iterable[str] = ()) -> None:
        object.__setattr__(self, "allowed_options", tuple(allowed_options))

    def validate(self, frame: pd.DataFrame) -> pd.DataFrame:
        missing = [col for col in REQUIRED_TRACE_COLUMNS if col not in frame.columns]
        if missing:
            raise ValueError(f"missing trace columns: {missing}")
        normalized = frame.loc[:, list(REQUIRED_TRACE_COLUMNS)].copy()
        if normalized.isna().any().any():
            raise ValueError("trace contains missing participant, round, option, or payoff values")
        normalized["round"] = normalized["round"].astype(int)
        if (normalized["round"] <= 0).any():
            raise ValueError("round values must be positive")
        duplicates = normalized.duplicated(["participant_id", "round"])
        if duplicates.any():
            raise ValueError("trace contains duplicate participant/round observations")
        if self.allowed_options:
            unknown = sorted(set(normalized["option_id"]) - set(self.allowed_options))
            if unknown:
                raise ValueError(f"unknown option_id values: {unknown}")
        return normalized.sort_values(["participant_id", "round"]).reset_index(drop=True)


def summarize_trace(frame: pd.DataFrame) -> dict[str, float]:
    normalized = ParticipantTraceSchema().validate(frame)
    return {
        "participants": float(normalized["participant_id"].nunique()),
        "rounds": float(normalized["round"].nunique()),
        "observations": float(len(normalized)),
        "mean_payoff": float(normalized["payoff"].mean()),
        "risky_choice_rate": float(normalized["option_id"].str.contains("risky", case=False, regex=False).mean()),
    }
