"""GM Agent — synthesis and final recommendation.

Takes the four specialist reports and produces a single
recommendation. Surfaces agreement, disagreement, and
confidence. Weights specialists differently based on team
philosophy (a contender weighs Architect heavily; a rebuilding
team leans on Scout's youth-curve work).

Currently stubbed. Real implementation in v0.5.
"""

from typing import List
from models.trade import Trade, AgentReport, Recommendation


def run_gm(trade: Trade, reports: List[AgentReport]) -> Recommendation:
    """Synthesize specialist reports into a final recommendation."""

    return Recommendation(
        verdict="Mixed",
        confidence=0.62,
        reasoning=(
            "Scout and Architect broadly agree the trade improves Team A more than Team B. "
            "Cap/Apron raises a serious concern — the second-apron crossing locks Team A "
            "into limited roster flexibility for years. Context flags a coach-player history "
            "worth investigating before approving. Net: directionally a good basketball trade "
            "for the receiving team, but the cap consequences and intangibles warrant pause."
        ),
        agent_reports=reports,
    )