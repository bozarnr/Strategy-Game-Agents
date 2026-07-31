# Strategy Game Agents

Behavioral-finance experiment tooling plus clean-room strategy agents for
simulating repeated risky-choice games. The repository started as a web
experiment page; this version adds a reproducible Python core that can replay
simple decision rules and compare agent behavior under bounded evidence.

## What It Shows

- A small repeated-game engine with deterministic seeding.
- Strategy agents: fixed preference, epsilon-greedy learning, and loss-averse
  utility.
- Metrics for cumulative payoff, risky-choice rate, regret against the best
  available option, and round-level traces.
- Participant-trace validation plus interpretable baseline fitting.
- A competition evidence ladder that keeps candidate claims below the strongest
  verified trace, replay, local-screen, or official-run evidence.
- Unit tests that pin reproducibility, regret accounting, behavioral
  parameters, fitting, and evidence boundaries.
- A clear boundary between experiment infrastructure and validated behavioral
  or trading claims.

## Quick Start

```powershell
python -m pip install -e .
python -m strategy_game_agents.demo
python -m unittest discover -s tests -v
```

## Minimal API

```python
from strategy_game_agents.agents import EpsilonGreedyAgent
from strategy_game_agents.evidence import CompetitionEvidence, decision_boundary
from strategy_game_agents.game import RepeatedChoiceGame, fixed_option, risky_uniform_option
from strategy_game_agents.simulation import run_simulation

game = RepeatedChoiceGame(
    options=[
        fixed_option("safe", payoff=5.5),
        risky_uniform_option("risky", low=1, high=10),
    ],
    rounds=10,
    seed=42,
)
result = run_simulation(game, EpsilonGreedyAgent(epsilon=0.2, seed=7))
print(result.summary())

evidence = CompetitionEvidence(
    candidate_id="agent-v5.5",
    level="local_screened",
    games_observed=48,
    primary_bottleneck="adversarial_policy_shift",
    claim_ceiling="local screen passed, official support not established",
)
print(decision_boundary(evidence))
```

## Evidence Boundary

See [evidence/validation-boundary.md](evidence/validation-boundary.md) and
[reports/competition-evidence-ladder.md](reports/competition-evidence-ladder.md).
This is a public research-tooling repository, not a behavioral theorem or
trading model.
