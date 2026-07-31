# Agent Comparison Report

This report uses the deterministic 10-round demo game: one safe option pays 5.5 and one risky option draws an integer from 1 to 10. The two options have the same expected value, so the point is behavior, not alpha.

| Agent | Total payoff | Mean payoff | Risky choice rate | Realized regret | Read |
|---|---:|---:|---:|---:|---|
| always_safe | 55.0 | 5.50 | 0.00 | 0.0 | reference behavior |
| epsilon_greedy | 50.5 | 5.05 | 0.10 | 0.0 | explores once, then stays mostly safe in this seed |
| loss_averse | 55.0 | 5.50 | 0.00 | 0.0 | avoids the risky option when expected values tie |

## What this shows

The repo now has two halves that can meet later: the browser experiment collects human choices, and the Python package can replay baseline decision rules. The current demo does not explain human behavior yet; it creates the measurement surface needed to compare humans with agents.

## Next useful artifact

Add a participant trace schema, then fit baseline parameters on anonymized or synthetic traces. That would turn this from a toy simulation into an experiment-analysis loop.
