import unittest

from strategy_game_agents.evidence import CompetitionEvidence, decision_boundary, next_evidence_step


class CompetitionEvidenceTests(unittest.TestCase):
    def test_evidence_ladder_controls_claims(self):
        evidence = CompetitionEvidence(
            candidate_id="agent-v5.5",
            level="local_screened",
            games_observed=48,
            primary_bottleneck="adversarial_policy_shift",
            claim_ceiling="local screen passed, official support not established",
        )

        self.assertTrue(evidence.can_claim("distribution_calibrated"))
        self.assertFalse(evidence.can_claim("official_supported"))
        self.assertEqual(next_evidence_step(evidence.level), "official_observed")
        self.assertEqual(decision_boundary(evidence), "continue_to_official_observed")

    def test_supported_candidate_passes_default_boundary(self):
        evidence = CompetitionEvidence(
            candidate_id="agent-v6",
            level="official_supported",
            games_observed=300,
            primary_bottleneck="none",
            claim_ceiling="officially supported under fixed challenge budget",
        )

        self.assertEqual(decision_boundary(evidence), "candidate_supported")

    def test_invalid_level_raises(self):
        with self.assertRaises(ValueError):
            CompetitionEvidence(
                candidate_id="bad",
                level="hand_wavy",
                games_observed=0,
                primary_bottleneck="unknown",
                claim_ceiling="none",
            )


if __name__ == "__main__":
    unittest.main()
