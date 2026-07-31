from __future__ import annotations

from .agents import EpsilonGreedyAgent, FixedPreferenceAgent, LossAverseAgent
from .game import RepeatedChoiceGame, fixed_option, risky_uniform_option
from .simulation import run_simulation


def build_demo_game(seed: int = 42) -> RepeatedChoiceGame:
    return RepeatedChoiceGame(
        options=[
            fixed_option("safe_fixed_5_5", payoff=5.5),
            risky_uniform_option("risky_uniform_1_10", low=1, high=10),
        ],
        rounds=10,
        seed=seed,
    )


def main() -> None:
    game = build_demo_game()
    agents = {
        "always_safe": FixedPreferenceAgent("safe_fixed_5_5"),
        "epsilon_greedy": EpsilonGreedyAgent(epsilon=0.2, seed=7),
        "loss_averse": LossAverseAgent(reference_point=5.5, loss_multiplier=2.25),
    }
    for name, agent in agents.items():
        result = run_simulation(game, agent)
        print(name, result.summary())


if __name__ == "__main__":
    main()
