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
- Unit tests that pin reproducibility, regret accounting, and behavioral
  parameters.
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

## 中文说明

这个仓库现在不只是一个 10 轮行为金融实验网页，而是一个可测试的“策略游戏智能体”项目：

- 网页负责收集人类实验数据。
- Python 包负责模拟不同决策规则下的行为。
- 后续可以把人类选择和 agent 选择放到同一套指标下比较。

当前版本只使用合成/程序生成收益，不声称已经解释真实投资行为，也不声称能产生交易策略。

## Evidence Boundary

See [evidence/validation-boundary.md](evidence/validation-boundary.md). This is
a public research-tooling repository, not a behavioral theorem or trading model.
