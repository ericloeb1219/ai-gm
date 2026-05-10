"""Orchestrator — coordinates the 5-agent pipeline.

Calls the 4 specialist agents (Scout, Architect, Cap/Apron, Context),
then hands their reports to the GM agent for synthesis.

v0.1: Sequential function calls.
v0.2+: Will migrate to a LangGraph state graph.
"""

from models.trade import Trade, Recommendation
from agents.scout import run_scout
from agents.architect import run_architect
from agents.cap_apron import run_cap_apron
from agents.context import run_context
from agents.gm import run_gm


def analyze_trade(trade: Trade) -> Recommendation:
    """Run a trade through the full agent pipeline."""

    scout_report = run_scout(trade)
    architect_report = run_architect(trade)
    cap_apron_report = run_cap_apron(trade)
    context_report = run_context(trade)

    return run_gm(
        trade=trade,
        reports=[scout_report, architect_report, cap_apron_report, context_report],
    )