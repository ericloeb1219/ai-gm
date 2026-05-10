"""Scout Agent — pure player evaluation.

Roster-agnostic. Outputs raw talent assessment based on
advanced metrics (EPM, LEBRON, RAPM, BPM), age curves,
injury history, and durability.

Currently stubbed. Real implementation in v0.4.
"""

from models.trade import Trade, AgentReport


def run_scout(trade: Trade) -> AgentReport:
    """Analyze raw player value for every player in the trade."""

    return AgentReport(
        agent_name="Scout",
        summary=(
            "Raw talent assessment is roughly even, with one player "
            "showing a slight age-curve concern."
        ),
        confidence=0.72,
        key_findings=[
            "Player A (26y, F): EPM +2.1 over last 2 seasons, neutral age curve, durable.",
            "Player B (28y, G): LEBRON +0.8, slight downturn last 30 games, two ankle issues this year.",
            "Both players profile as starter-quality; neither is an All-Star tier.",
        ],
    )