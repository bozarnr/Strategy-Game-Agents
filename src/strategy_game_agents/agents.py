from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np

from .game import PayoffOption


class StrategyAgent:
    def choose(self, round_index: int, options: list[PayoffOption]) -> str:
        raise NotImplementedError

    def observe(self, option_id: str, payoff: float) -> None:
        return None


@dataclass
class FixedPreferenceAgent(StrategyAgent):
    option_id: str

    def choose(self, round_index: int, options: list[PayoffOption]) -> str:
        if self.option_id not in {option.option_id for option in options}:
            raise ValueError(f"unknown option_id: {self.option_id}")
        return self.option_id


@dataclass
class EpsilonGreedyAgent(StrategyAgent):
    epsilon: float = 0.1
    seed: int = 0
    counts: dict[str, int] = field(default_factory=dict)
    values: dict[str, float] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not 0 <= self.epsilon <= 1:
            raise ValueError("epsilon must be in [0, 1]")
        self._rng = np.random.default_rng(self.seed)

    def choose(self, round_index: int, options: list[PayoffOption]) -> str:
        ids = [option.option_id for option in options]
        for option_id in ids:
            self.counts.setdefault(option_id, 0)
            self.values.setdefault(option_id, 0.0)
        untried = [option_id for option_id in ids if self.counts[option_id] == 0]
        if untried:
            return untried[0]
        if self._rng.random() < self.epsilon:
            return str(self._rng.choice(ids))
        return max(ids, key=lambda option_id: (self.values[option_id], option_id))

    def observe(self, option_id: str, payoff: float) -> None:
        old_count = self.counts.get(option_id, 0)
        old_value = self.values.get(option_id, 0.0)
        new_count = old_count + 1
        self.counts[option_id] = new_count
        self.values[option_id] = old_value + (payoff - old_value) / new_count


@dataclass
class LossAverseAgent(StrategyAgent):
    reference_point: float = 5.5
    loss_multiplier: float = 2.0

    def choose(self, round_index: int, options: list[PayoffOption]) -> str:
        return max(options, key=self._utility_proxy).option_id

    def _utility_proxy(self, option: PayoffOption) -> float:
        gain = option.expected_value - self.reference_point
        if gain >= 0:
            return gain
        return self.loss_multiplier * gain
