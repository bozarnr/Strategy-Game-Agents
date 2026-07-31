# Strategy Game Agents

A small repeated-choice experiment repo with baseline agents, trace validation, and simple behavioral fitting. The browser page can collect choices; the Python package replays baseline decision rules and compares them against participant-like traces.

## Showcase

- [Agent Comparison Report](reports/agent-comparison.md): safe, epsilon-greedy, and loss-averse baselines plus trace-schema and fitting capabilities.

## Related repos

- [AI-Alpha-Research-Lab](https://github.com/bozarnr/AI-Alpha-Research-Lab): formula search, evaluation, and rejection gates.
- [Paper-Alpha-Replications](https://github.com/bozarnr/Paper-Alpha-Replications): replication notes with claim ceilings.
- [Quant-Research-Toolkit](https://github.com/bozarnr/Quant-Research-Toolkit): reusable checks for factor panels and diagnostics.
- [Strategy-Game-Agents](https://github.com/bozarnr/Strategy-Game-Agents): repeated-choice experiments and baseline agents.

## What is here

- Repeated-game engine with deterministic seeding.
- Agents: fixed preference, epsilon-greedy learning, and loss-averse utility.
- Metrics: cumulative payoff, risky-choice rate, regret, and round-level traces.
- Participant trace schema: required columns, duplicate checks, allowed-option checks, and sorted normalized output.
- Baseline fitting: loss-aversion and epsilon-greedy grids matched to observed risky-choice rates.
- Tests for reproducibility, learning updates, regret accounting, trace validation, and fitting output.

## Run

```powershell
python -m pip install -e .
python -m strategy_game_agents.demo
python -m unittest discover -s tests -v
```

## Minimal API

```python
import pandas as pd

from strategy_game_agents import (
    EpsilonGreedyAgent,
    ParticipantTraceSchema,
    RepeatedChoiceGame,
    fit_epsilon_greedy_by_risky_rate,
    fixed_option,
    risky_uniform_option,
    run_simulation,
)

game = RepeatedChoiceGame(
    options=[fixed_option("safe", payoff=5.5), risky_uniform_option("risky_uniform", low=0, high=12)],
    rounds=10,
    seed=42,
)
result = run_simulation(game, EpsilonGreedyAgent(epsilon=0.2, seed=7))

trace = pd.DataFrame([
    {"participant_id": "p1", "round": 1, "option_id": "safe", "payoff": 5.5},
    {"participant_id": "p1", "round": 2, "option_id": "risky_uniform", "payoff": 9.0},
])
validated = ParticipantTraceSchema(allowed_options=["safe", "risky_uniform"]).validate(trace)
fit = fit_epsilon_greedy_by_risky_rate(validated, game)
```

## Evidence boundary

See [evidence/validation-boundary.md](evidence/validation-boundary.md). This is experiment tooling and simulation code, not a behavioral theorem or trading model.
