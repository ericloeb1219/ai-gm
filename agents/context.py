"""Context Agent — timing and intangibles.

Timing: strength of schedule, competitive window, conference
dynamics, draft pick value relative to expected finish.

Intangibles: player and coach relationship history (positive
or negative), locker room composition, veteran presence and
leadership value, mentorship dynamics for young players.

Currently stubbed. Real implementation in v0.4.
"""

from models.trade import Trade, AgentReport


def run_context(trade: Trade) -> AgentReport:
    """Assess timing and intangibles surrounding the trade."""

    return AgentReport(
        agent_name="Context",
        summary=(
            "Timing favors the receiving team's contention window; "
            "intangibles raise mild concern about locker room fit."
        ),
        confidence=0.58,
        key_findings=[
            "Team A is in a 2-year contention window — incoming player's prime aligns.",
            "Team B is rebuilding — outgoing veteran removes a mentor for two rookies on rookie-scale deals.",
            "Player B previously played for Team A's head coach in 2019; reporting at the time noted friction.",
            "No public locker-room red flags for the incoming player to Team A.",
            "Schedule note: Team A's remaining schedule is 6th-toughest in the league post-deadline.",
        ],
    )