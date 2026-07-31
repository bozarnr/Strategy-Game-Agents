"""Strategy agents for repeated risky-choice games."""

from .agents import EpsilonGreedyAgent, FixedPreferenceAgent, LossAverseAgent
from .fitting import TraceFitResult, fit_epsilon_greedy_by_risky_rate, fit_loss_aversion_by_risky_rate
from .game import PayoffOption, RepeatedChoiceGame, fixed_option, risky_uniform_option
from .simulation import SimulationResult, run_simulation
from .traces import ParticipantTraceSchema, summarize_trace

__all__ = [
    "EpsilonGreedyAgent",
    "FixedPreferenceAgent",
    "LossAverseAgent",
    "PayoffOption",
    "RepeatedChoiceGame",
    "SimulationResult",
    "ParticipantTraceSchema",
    "TraceFitResult",
    "fixed_option",
    "fit_epsilon_greedy_by_risky_rate",
    "fit_loss_aversion_by_risky_rate",
    "risky_uniform_option",
    "run_simulation",
    "summarize_trace",
]
