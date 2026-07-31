# Agent Comparison

This project is a clean-room behavioral simulation sandbox. It focuses on decision-process modeling rather than claiming a production trading strategy.

## Current Capability

- `RepeatedChoiceGame` defines repeated risky-choice tasks with deterministic seeds.
- `FixedPreferenceAgent`, `EpsilonGreedyAgent`, and `LossAverseAgent` provide comparable baseline behaviors.
- `run_simulation` emits a round-level trace with payoff, expected value, risky-choice flag, and realized regret.
- `ParticipantTraceSchema` validates human or synthetic participant traces before fitting.
- `fit_loss_aversion_by_risky_rate` and `fit_epsilon_greedy_by_risky_rate` fit simple interpretable baselines against observed risky-choice rates.

## Why It Matters

The project now reads less like a toy game and more like a small experimental economics/agent-modeling toolkit: controlled games, reproducible traces, participant-level schema validation, and baseline fitting that can be extended toward richer strategic or quant-behavior experiments.
