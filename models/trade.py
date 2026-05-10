"""Data models for AI GM.

Defines the shape of every object that flows between agents.
Pydantic enforces types and provides free JSON serialization.
"""

from typing import List, Literal
from pydantic import BaseModel, Field


class Player(BaseModel):
    """A single NBA player involved in a trade."""

    name: str
    team: str  # Team the player is currently on
    position: Literal["PG", "SG", "SF", "PF", "C"]
    salary: float = Field(description="Salary in millions of dollars")
    age: int


class TradePackage(BaseModel):
    """One side of a trade — what one team is sending out."""

    team: str
    players_out: List[Player]


class Trade(BaseModel):
    """A proposed or actual NBA trade between two or more teams."""

    packages: List[TradePackage]


class AgentReport(BaseModel):
    """A single agent's analysis of a trade."""

    agent_name: str
    summary: str = Field(description="One- or two-sentence overall take")
    confidence: float = Field(ge=0.0, le=1.0, description="Confidence 0.0 – 1.0")
    key_findings: List[str] = Field(description="Bullet points the agent surfaced")


class Recommendation(BaseModel):
    """The GM agent's final synthesis across all specialist reports."""

    verdict: Literal["Approve", "Reject", "Mixed"]
    confidence: float = Field(ge=0.0, le=1.0)
    reasoning: str = Field(description="GM's explanation tying the agents together")
    agent_reports: List[AgentReport]