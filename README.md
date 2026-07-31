# Strategy Game Agents

A small repeated-choice experiment repo with baseline agents. The original page collects 10-round behavioral-finance choices; the Python package adds replayable decision rules and simple comparison metrics.

网页用于收集人类选择，Python 包用于跑基线 agent。后续可以把人类轨迹和 agent 轨迹放到同一套指标里比较，但当前版本还不解释真实投资行为，也不产生交易信号。

## Showcase

- [Agent Comparison Report](reports/agent-comparison.md): safe, epsilon-greedy, and loss-averse baselines on the deterministic 10-round game.

## Related repos

- [AI-Alpha-Research-Lab](https://github.com/bozarnr/AI-Alpha-Research-Lab): formula search, evaluation, and rejection gates.
- [Paper-Alpha-Replications](https://github.com/bozarnr/Paper-Alpha-Replications): replication notes with claim ceilings.
- [Quant-Research-Toolkit](https://github.com/bozarnr/Quant-Research-Toolkit): reusable checks for factor panels and diagnostics.
- [Strategy-Game-Agents](https://github.com/bozarnr/Strategy-Game-Agents): repeated-choice experiments and baseline agents.

## What is here

- Repeated-game engine with deterministic seeding.
- Agents: fixed preference, epsilon-greedy learning, and loss-averse utility.
- Metrics: cumulative payoff, risky-choice rate, regret, and round-level traces.
- Tests for reproducibility, learning updates, regret accounting, and loss-aversion behavior.

## Run

```powershell
python -m pip install -e .
python -m strategy_game_agents.demo
python -m unittest discover -s tests -v
```

## Minimal API

```python
from strategy_game_agents.agents import EpsilonGreedyAgent
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
```

## Evidence boundary

See [evidence/validation-boundary.md](evidence/validation-boundary.md). This is experiment tooling and simulation code, not a behavioral theorem or trading model.
