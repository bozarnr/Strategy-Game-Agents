import unittest

from strategy_game_agents.agents import EpsilonGreedyAgent, LossAverseAgent
from strategy_game_agents.demo import build_demo_game
from strategy_game_agents.game import fixed_option, risky_uniform_option
from strategy_game_agents.simulation import run_simulation


class StrategyAgentTest(unittest.TestCase):
    def test_epsilon_greedy_updates_value_estimates(self) -> None:
        game = build_demo_game()
        agent = EpsilonGreedyAgent(epsilon=0.0, seed=1)
        result = run_simulation(game, agent)
        self.assertEqual(len(result.trace), 10)
        self.assertIn("safe_fixed_5_5", agent.values)
        self.assertIn("risky_uniform_1_10", agent.values)

    def test_loss_averse_agent_prefers_safe_when_expected_values_tie(self) -> None:
        options = [fixed_option("safe", 5.5), risky_uniform_option("risky", 1, 10)]
        agent = LossAverseAgent(reference_point=5.5, loss_multiplier=3.0)
        self.assertEqual(agent.choose(1, options), "safe")


if __name__ == "__main__":
    unittest.main()
