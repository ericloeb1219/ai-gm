"""Architect Agent — team fit and roster construction.

Classifies players by archetype, assesses scheme fit and
lineup synergy, detects redundancy, and judges whether a
player is additive given each team's existing roster needs.

Currently stubbed. Real implementation in v0.3.
"""

from models.trade import Trade, AgentReport


def run_architect(trade: Trade) -> AgentReport:
    """Evaluate roster fit and archetype redundancy for both teams."""

    return AgentReport(
        agent_name="Architect",
        summary=(
            "Fit is uneven: receiving team gains a needed archetype; "
            "sending team creates frontcourt redundancy."
        ),
        confidence=0.65,
        key_findings=[
            "Team A receives a 3-and-D wing — directly addresses worst-ranked corner-3 defense.",
            "Team B receives a primary creator — but already has two ball-dominant guards on roster.",
            "Lineup data flag: Team B's projected starting 5 has a sub-30th-percentile spacing profile.",
            "Net assessment: trade improves Team A's roster construction more than Team B's.",
        ],
    )