from __future__ import annotations

import unittest

import pandas as pd

from strategy_game_agents.fitting import fit_epsilon_greedy_by_risky_rate, fit_loss_aversion_by_risky_rate
from strategy_game_agents.game import RepeatedChoiceGame, fixed_option, risky_uniform_option


class TraceFittingTest(unittest.TestCase):
    def setUp(self) -> None:
        self.game = RepeatedChoiceGame(
            options=[fixed_option("safe", 5.5), risky_uniform_option("risky_uniform", 0, 12)],
            rounds=8,
            seed=11,
        )
        self.trace = pd.DataFrame(
            [
                {"participant_id": "p1", "round": 1, "option_id": "safe", "payoff": 5.5},
                {"participant_id": "p1", "round": 2, "option_id": "risky_uniform", "payoff": 9.0},
                {"participant_id": "p1", "round": 3, "option_id": "safe", "payoff": 5.5},
            ]
        )

    def test_fits_loss_aversion_baseline(self) -> None:
        result = fit_loss_aversion_by_risky_rate(self.trace, self.game)

        self.assertEqual(result.agent_name, "loss_averse")
        self.assertGreaterEqual(result.distance, 0.0)
        self.assertIn("loss_multiplier", result.as_dict()["params"])

    def test_fits_epsilon_greedy_baseline(self) -> None:
        result = fit_epsilon_greedy_by_risky_rate(self.trace, self.game)

        self.assertEqual(result.agent_name, "epsilon_greedy")
        self.assertGreaterEqual(result.distance, 0.0)
        self.assertIn("epsilon", result.as_dict()["params"])


if __name__ == "__main__":
    unittest.main()
