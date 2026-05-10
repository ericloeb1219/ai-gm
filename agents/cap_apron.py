"""Cap/Apron Agent — CBA-aware trade math.

Validates trade legality (salary matching, traded player
exceptions), models cap and apron implications, flags hard
cap triggers and draft pick freeze risks, projects multi-
season cap impact.

Currently stubbed. Real implementation in v0.2.
"""

from models.trade import Trade, AgentReport


def run_cap_apron(trade: Trade) -> AgentReport:
    """Validate trade math and surface CBA implications."""

    return AgentReport(
        agent_name="Cap/Apron",
        summary=(
            "Trade is legal under salary matching rules but pushes "
            "Team A across the second apron, triggering hard-cap and draft-pick consequences."
        ),
        confidence=0.91,
        key_findings=[
            "Salary match: outgoing $23.4M / incoming $22.1M — within 125% rule. Legal.",
            "Team A: post-trade salary projects $1.2M over the second apron.",
            "Hard cap triggered for Team A this season — cannot exceed $189.5M for any reason.",
            "Team A's 2032 first-round pick becomes frozen (cannot be traded for 6 years).",
            "Team B: stays under all aprons; full mid-level exception remains available.",
        ],
    )