import csv
import unittest
from pathlib import Path

from strategy_game_agents.evidence import CompetitionEvidence


class SampleDataTests(unittest.TestCase):
    def test_agent_evidence_sample_matches_schema(self):
        with Path("sample_data/agent_evidence_sample.csv").open(encoding="utf-8") as handle:
            rows = list(csv.DictReader(handle))

        self.assertEqual(len(rows), 3)
        for row in rows:
            with self.subTest(candidate_id=row["candidate_id"]):
                evidence = CompetitionEvidence(
                    candidate_id=row["candidate_id"],
                    level=row["level"],
                    games_observed=int(row["games_observed"]),
                    primary_bottleneck=row["primary_bottleneck"],
                    claim_ceiling=row["claim_ceiling"],
                )
                self.assertFalse(evidence.can_claim("submission_ready"))


if __name__ == "__main__":
    unittest.main()
