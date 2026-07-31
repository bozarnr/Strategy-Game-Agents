import unittest

from strategy_game_agents.agents import FixedPreferenceAgent
from strategy_game_agents.demo import build_demo_game
from strategy_game_agents.simulation import run_simulation


class SimulationTest(unittest.TestCase):
    def test_simulation_is_reproducible(self) -> None:
        first = run_simulation(build_demo_game(seed=9), FixedPreferenceAgent("risky_uniform_1_10"))
        second = run_simulation(build_demo_game(seed=9), FixedPreferenceAgent("risky_uniform_1_10"))
        self.assertEqual(first.trace["payoff"].tolist(), second.trace["payoff"].tolist())

    def test_safe_agent_has_zero_expected_regret_when_options_tie(self) -> None:
        result = run_simulation(build_demo_game(), FixedPreferenceAgent("safe_fixed_5_5"))
        self.assertEqual(result.summary()["realized_regret"], 0.0)
        self.assertEqual(result.summary()["risky_choice_rate"], 0.0)


if __name__ == "__main__":
    unittest.main()
