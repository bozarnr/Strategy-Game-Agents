from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from .agents import EpsilonGreedyAgent, LossAverseAgent
from .game import RepeatedChoiceGame
from .simulation import run_simulation
from .traces import summarize_trace


@dataclass(frozen=True)
class TraceFitResult:
    agent_name: str
    distance: float
    target_risky_rate: float
    simulated_risky_rate: float
    params: dict[str, float]

    def as_dict(self) -> dict[str, object]:
        return {
            "agent_name": self.agent_name,
            "distance": self.distance,
            "target_risky_rate": self.target_risky_rate,
            "simulated_risky_rate": self.simulated_risky_rate,
            "params": self.params,
        }


def fit_loss_aversion_by_risky_rate(
    trace,
    game: RepeatedChoiceGame,
    multipliers: Iterable[float] = (1.0, 1.5, 2.0, 2.5, 3.0),
) -> TraceFitResult:
    target = summarize_trace(trace)["risky_choice_rate"]
    candidates: list[TraceFitResult] = []
    for multiplier in multipliers:
        agent = LossAverseAgent(loss_multiplier=float(multiplier))
        simulated = run_simulation(game, agent).summary()["risky_choice_rate"]
        candidates.append(
            TraceFitResult(
                agent_name="loss_averse",
                distance=abs(simulated - target),
                target_risky_rate=target,
                simulated_risky_rate=simulated,
                params={"loss_multiplier": float(multiplier)},
            )
        )
    return min(candidates, key=lambda result: (result.distance, result.params["loss_multiplier"]))


def fit_epsilon_greedy_by_risky_rate(
    trace,
    game: RepeatedChoiceGame,
    epsilons: Iterable[float] = (0.0, 0.05, 0.1, 0.2, 0.35, 0.5),
) -> TraceFitResult:
    target = summarize_trace(trace)["risky_choice_rate"]
    candidates: list[TraceFitResult] = []
    for epsilon in epsilons:
        agent = EpsilonGreedyAgent(epsilon=float(epsilon), seed=game.seed)
        simulated = run_simulation(game, agent).summary()["risky_choice_rate"]
        candidates.append(
            TraceFitResult(
                agent_name="epsilon_greedy",
                distance=abs(simulated - target),
                target_risky_rate=target,
                simulated_risky_rate=simulated,
                params={"epsilon": float(epsilon)},
            )
        )
    return min(candidates, key=lambda result: (result.distance, result.params["epsilon"]))
