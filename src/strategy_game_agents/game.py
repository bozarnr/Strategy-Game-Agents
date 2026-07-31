from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

import numpy as np


PayoffSampler = Callable[[np.random.Generator], float]


@dataclass(frozen=True)
class PayoffOption:
    option_id: str
    description: str
    expected_value: float
    sampler: PayoffSampler

    def draw(self, rng: np.random.Generator) -> float:
        return float(self.sampler(rng))


@dataclass(frozen=True)
class RepeatedChoiceGame:
    options: list[PayoffOption]
    rounds: int = 10
    seed: int = 0

    def __post_init__(self) -> None:
        if self.rounds <= 0:
            raise ValueError("rounds must be positive")
        if len(self.options) < 2:
            raise ValueError("at least two options are required")
        ids = [option.option_id for option in self.options]
        if len(set(ids)) != len(ids):
            raise ValueError("option_id values must be unique")

    @property
    def best_expected_value(self) -> float:
        return max(option.expected_value for option in self.options)

    def option_by_id(self, option_id: str) -> PayoffOption:
        for option in self.options:
            if option.option_id == option_id:
                return option
        raise KeyError(option_id)


def fixed_option(option_id: str, payoff: float) -> PayoffOption:
    return PayoffOption(
        option_id=option_id,
        description=f"fixed payoff {payoff}",
        expected_value=float(payoff),
        sampler=lambda _rng: float(payoff),
    )


def risky_uniform_option(option_id: str, low: int, high: int) -> PayoffOption:
    if low > high:
        raise ValueError("low cannot exceed high")
    return PayoffOption(
        option_id=option_id,
        description=f"uniform integer payoff [{low}, {high}]",
        expected_value=(low + high) / 2.0,
        sampler=lambda rng: float(rng.integers(low, high + 1)),
    )
