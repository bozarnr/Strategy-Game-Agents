# Competition Evidence Ladder

This repository treats game-agent progress as an evidence problem, not a leaderboard story. A candidate can only make the claim supported by its strongest observed evidence level.

## Ladder

1. `source_only`: idea or rule exists, but no replay or run evidence.
2. `replay_observed`: behavior was observed in a saved trace.
3. `rule_reproduced`: the agent can reproduce a known behavior under controlled replay.
4. `distribution_calibrated`: simulation statistics match the observed trace distribution closely enough for local experiments.
5. `local_screened`: candidate survives local adversarial or holdout screens.
6. `official_observed`: candidate has official-run evidence, but not enough support for promotion.
7. `official_supported`: official evidence supports the candidate under the fixed challenge budget.
8. `submission_ready`: candidate, evidence, and operational checks are all ready for final submission.

## Boundary

The useful public signal is the discipline: candidates carry a `claim_ceiling`, a primary bottleneck, and the next required evidence step. That makes it harder to accidentally promote a lucky local result into an unsupported public claim.
