from __future__ import annotations

import unittest

import pandas as pd

from strategy_game_agents.traces import ParticipantTraceSchema, summarize_trace


class ParticipantTraceSchemaTest(unittest.TestCase):
    def test_validates_and_summarizes_trace(self) -> None:
        trace = pd.DataFrame(
            [
                {"participant_id": "p1", "round": 2, "option_id": "safe", "payoff": 5.5},
                {"participant_id": "p1", "round": 1, "option_id": "risky_uniform", "payoff": 8.0},
                {"participant_id": "p2", "round": 1, "option_id": "safe", "payoff": 5.5},
            ]
        )

        normalized = ParticipantTraceSchema(allowed_options=["safe", "risky_uniform"]).validate(trace)
        summary = summarize_trace(normalized)

        self.assertEqual(normalized.iloc[0]["round"], 1)
        self.assertEqual(summary["participants"], 2.0)
        self.assertAlmostEqual(summary["risky_choice_rate"], 1 / 3)

    def test_rejects_duplicate_participant_round(self) -> None:
        trace = pd.DataFrame(
            [
                {"participant_id": "p1", "round": 1, "option_id": "safe", "payoff": 5.5},
                {"participant_id": "p1", "round": 1, "option_id": "risky_uniform", "payoff": 8.0},
            ]
        )

        with self.assertRaises(ValueError):
            ParticipantTraceSchema().validate(trace)


if __name__ == "__main__":
    unittest.main()
