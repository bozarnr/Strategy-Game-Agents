from __future__ import annotations

from dataclasses import dataclass


EVIDENCE_LADDER = (
    "source_only",
    "replay_observed",
    "rule_reproduced",
    "distribution_calibrated",
    "local_screened",
    "official_observed",
    "official_supported",
    "submission_ready",
)


@dataclass(frozen=True)
class CompetitionEvidence:
    candidate_id: str
    level: str
    games_observed: int
    primary_bottleneck: str
    claim_ceiling: str

    def __post_init__(self) -> None:
        if self.level not in EVIDENCE_LADDER:
            raise ValueError(f"unknown evidence level: {self.level}")
        if self.games_observed < 0:
            raise ValueError("games_observed cannot be negative")
        if not self.candidate_id:
            raise ValueError("candidate_id cannot be empty")

    @property
    def rank(self) -> int:
        return EVIDENCE_LADDER.index(self.level)

    def can_claim(self, required_level: str) -> bool:
        if required_level not in EVIDENCE_LADDER:
            raise ValueError(f"unknown required level: {required_level}")
        return self.rank >= EVIDENCE_LADDER.index(required_level)


def next_evidence_step(level: str) -> str | None:
    if level not in EVIDENCE_LADDER:
        raise ValueError(f"unknown evidence level: {level}")
    index = EVIDENCE_LADDER.index(level)
    if index == len(EVIDENCE_LADDER) - 1:
        return None
    return EVIDENCE_LADDER[index + 1]


def decision_boundary(evidence: CompetitionEvidence, required_level: str = "official_supported") -> str:
    if evidence.can_claim(required_level):
        return "candidate_supported"
    next_step = next_evidence_step(evidence.level)
    if next_step is None:
        return "candidate_ready_for_human_review"
    return f"continue_to_{next_step}"
