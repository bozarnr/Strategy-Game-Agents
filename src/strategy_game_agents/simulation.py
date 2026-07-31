from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd

from .agents import StrategyAgent
from .game import RepeatedChoiceGame


@dataclass(frozen=True)
class SimulationResult:
    trace: pd.DataFrame
    best_expected_value: float

    def summary(self) -> dict[str, float]:
        total_payoff = float(self.trace["payoff"].sum())
        risky_rate = float(self.trace["is_risky"].mean())
        realized_regret = float(self.trace["regret"].sum())
        return {
            "rounds": float(len(self.trace)),
            "total_payoff": total_payoff,
            "mean_payoff": float(self.trace["payoff"].mean()),
            "risky_choice_rate": risky_rate,
            "realized_regret": realized_regret,
        }


def run_simulation(game: RepeatedChoiceGame, agent: StrategyAgent) -> SimulationResult:
    rng = np.random.default_rng(game.seed)
    rows = []
    for round_index in range(1, game.rounds + 1):
        chosen_id = agent.choose(round_index, game.options)
        option = game.option_by_id(chosen_id)
        payoff = option.draw(rng)
        agent.observe(chosen_id, payoff)
        rows.append(
            {
                "round": round_index,
                "option_id": chosen_id,
                "payoff": payoff,
                "expected_value": option.expected_value,
                "is_risky": "risky" in chosen_id.lower(),
                "regret": max(game.best_expected_value - option.expected_value, 0.0),
            }
        )
    return SimulationResult(pd.DataFrame(rows), best_expected_value=game.best_expected_value)
