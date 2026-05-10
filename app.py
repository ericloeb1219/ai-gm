"""AI GM — Streamlit UI.

Lets the user input a proposed NBA trade between two teams,
runs it through the 5-agent pipeline, and displays the
recommendation alongside each specialist report.
"""

import streamlit as st

from models.trade import Trade, TradePackage, Player
from orchestrator import analyze_trade


# ---------- Page config ----------

st.set_page_config(
    page_title="AI GM",
    page_icon="🏀",
    layout="centered",
)

st.title("🏀 AI GM")
st.caption("An agentic AI front office for NBA trades.")


# ---------- Trade input form ----------

st.header("Propose a trade")

POSITIONS = ["PG", "SG", "SF", "PF", "C"]

col_a, col_b = st.columns(2)

with col_a:
    st.subheader("Team A sends")
    team_a = st.text_input("Team A", value="Lakers", key="team_a")
    player_a_name = st.text_input("Player name", value="Player A", key="pa_name")
    player_a_pos = st.selectbox("Position", POSITIONS, index=2, key="pa_pos")
    player_a_salary = st.number_input(
        "Salary ($M)", min_value=0.0, value=23.4, step=0.5, key="pa_sal"
    )
    player_a_age = st.number_input(
        "Age", min_value=18, max_value=45, value=26, key="pa_age"
    )

with col_b:
    st.subheader("Team B sends")
    team_b = st.text_input("Team B", value="Celtics", key="team_b")
    player_b_name = st.text_input("Player name", value="Player B", key="pb_name")
    player_b_pos = st.selectbox("Position", POSITIONS, index=1, key="pb_pos")
    player_b_salary = st.number_input(
        "Salary ($M)", min_value=0.0, value=22.1, step=0.5, key="pb_sal"
    )
    player_b_age = st.number_input(
        "Age", min_value=18, max_value=45, value=28, key="pb_age"
    )

submitted = st.button("Analyze trade", type="primary", use_container_width=True)


# ---------- Run the pipeline on submit ----------

if submitted:
    trade = Trade(packages=[
        TradePackage(
            team=team_a,
            players_out=[Player(
                name=player_a_name, team=team_a,
                position=player_a_pos, salary=player_a_salary, age=player_a_age,
            )],
        ),
        TradePackage(
            team=team_b,
            players_out=[Player(
                name=player_b_name, team=team_b,
                position=player_b_pos, salary=player_b_salary, age=player_b_age,
            )],
        ),
    ])

    with st.spinner("Running 5-agent analysis..."):
        rec = analyze_trade(trade)

    st.divider()

    # ---------- Recommendation header ----------

    st.header("Recommendation")

    verdict_col, conf_col = st.columns(2)
    verdict_col.metric("Verdict", rec.verdict)
    conf_col.metric("Confidence", f"{rec.confidence:.0%}")

    st.markdown(f"**GM reasoning:** {rec.reasoning}")

    # ---------- Per-agent reports ----------

    st.divider()
    st.header("Agent reports")
    st.caption("Click any agent to see its full reasoning.")

    for report in rec.agent_reports:
        with st.expander(
            f"**{report.agent_name}**  ·  confidence {report.confidence:.0%}"
        ):
            st.markdown(f"_{report.summary}_")
            st.markdown("**Key findings:**")
            for finding in report.key_findings:
                st.markdown(f"- {finding}")