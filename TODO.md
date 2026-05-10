# TODO — Week 1: Ugly Skeleton

**Goal by end of Week 1:** A working end-to-end skeleton. User submits a trade in Streamlit → 5 stubbed agents "process" it → GM agent synthesizes → recommendation displayed. Looks terrible. Works.

**Why it matters:** Once this exists, every future week is just replacing stubs with real logic. No more "where do I start" anxiety.

**Estimated time:** ~5 hours across 4 sessions. Pad if needed; don't compress.

---

## Session 0 — 60-min activation

- [x] Create GitHub repo `gm-copilot` (public, MIT)
- [x] Push `README.md`
- [x] Buy domain (`gmcopilot.app` or `gmcopilot.ai`)
- [x] Add 2 recurring 2-hour blocks to calendar for the next 6 weeks
- [x] Draft Day-1 LinkedIn post in `posts/day-1-launch.md` (do not post yet)
- [x] Push this `TODO.md` to the repo

---

## Session 1 — Project structure (90 min)

- [x] Create directory layout:

```
gm-copilot/
├── app.py              # Streamlit entry
├── orchestrator.py     # Wires agents together
├── agents/
│   ├── __init__.py
│   ├── scout.py
│   ├── architect.py
│   ├── cap_apron.py
│   ├── context.py
│   └── gm.py
├── models/
│   ├── __init__.py
│   └── trade.py
├── posts/              
├── requirements.txt
├── .gitignore
├── .env.example
├── README.md
└── TODO.md
```

- [x] `requirements.txt`:

```
streamlit
anthropic
pydantic
python-dotenv
langgraph     # not used in Week 1, but installing now to fail fast on env issues
```

- [x] `.gitignore`: include `.env`, `__pycache__/`, `.streamlit/`, `.venv/`

- [x] `.env.example`: just `ANTHROPIC_API_KEY=`

- [x] Create local `.env` with your real key (never commit)

- [x] `pip install -r requirements.txt` succeeds without errors

---

## Session 2 — Data models + stub agents (90 min)

### Build `models/trade.py`

```python
from pydantic import BaseModel
from typing import List

class Player(BaseModel):
    name: str
    team: str
    position: str
    salary: float  # in millions
    age: int

class TradePackage(BaseModel):
    """One side of a trade — what one team is sending."""
    team: str
    players_out: List[Player]

class Trade(BaseModel):
    packages: List[TradePackage]

class AgentReport(BaseModel):
    agent_name: str
    summary: str
    confidence: float  # 0–1
    key_findings: List[str]

class Recommendation(BaseModel):
    verdict: str  # "Approve" | "Reject" | "Mixed"
    confidence: float
    reasoning: str
    agent_reports: List[AgentReport]
```

### Build agent stubs (one per file)

Pattern for `agents/scout.py`:

```python
from models.trade import Trade, AgentReport

def run_scout(trade: Trade) -> AgentReport:
    return AgentReport(
        agent_name="Scout",
        summary="[STUB] Pure player value assessment. Real metrics come Week 4.",
        confidence=0.7,
        key_findings=[
            "[STUB] Player A: 26y wing, neutral age curve, no recent injuries.",
            "[STUB] Player B: 28y guard, slight decline trajectory.",
        ],
    )
```

Repeat for:

- [x] `agents/architect.py` → `run_architect(trade)` (theme: archetype/fit/redundancy)
- [x] `agents/cap_apron.py` → `run_cap_apron(trade)` (theme: trade math/apron impact)
- [x] `agents/context.py` → `run_context(trade)` (theme: timing + intangibles)
- [x] `agents/gm.py` → `run_gm(trade, reports: List[AgentReport]) -> Recommendation` (synthesizes)

Make each stub return *visibly different* fake content so the synthesis looks alive. The GM stub should reference the others by name.

---

## Session 3 — Orchestrator + Streamlit UI (90 min)

### Build `orchestrator.py`

```python
from agents.scout import run_scout
from agents.architect import run_architect
from agents.cap_apron import run_cap_apron
from agents.context import run_context
from agents.gm import run_gm
from models.trade import Trade, Recommendation

def analyze_trade(trade: Trade) -> Recommendation:
    scout = run_scout(trade)
    architect = run_architect(trade)
    cap = run_cap_apron(trade)
    context = run_context(trade)
    return run_gm(trade, [scout, architect, cap, context])
```

> Note: Sequential calls in Week 1 is intentional. LangGraph migration is a Week 2 task, and itself becomes a build-in-public post: *"Why I started without LangGraph and added it later."*

### Build `app.py` (Streamlit)

```python
import streamlit as st
from models.trade import Trade, TradePackage, Player
from orchestrator import analyze_trade

st.title("GM Copilot")
st.caption("An agentic AI front office for NBA trades.")

st.subheader("Team A sends:")
a_player = st.text_input("Player", "Test Player A", key="a")
a_team = st.text_input("From team", "Lakers", key="ta")
a_salary = st.number_input("Salary ($M)", value=20.0, key="sa")

st.subheader("Team B sends:")
b_player = st.text_input("Player", "Test Player B", key="b")
b_team = st.text_input("From team", "Celtics", key="tb")
b_salary = st.number_input("Salary ($M)", value=22.0, key="sb")

if st.button("Analyze trade"):
    trade = Trade(packages=[
        TradePackage(team=a_team, players_out=[
            Player(name=a_player, team=a_team, position="F", salary=a_salary, age=26)
        ]),
        TradePackage(team=b_team, players_out=[
            Player(name=b_player, team=b_team, position="G", salary=b_salary, age=28)
        ]),
    ])
    rec = analyze_trade(trade)

    st.header("Recommendation")
    st.metric("Verdict", rec.verdict)
    st.metric("Confidence", f"{rec.confidence:.2f}")
    st.write(rec.reasoning)

    st.header("Agent reports")
    for r in rec.agent_reports:
        with st.expander(f"{r.agent_name}  ·  confidence {r.confidence:.2f}"):
            st.write(r.summary)
            for f in r.key_findings:
                st.markdown(f"- {f}")
```

### Run end-to-end

- [ ] `streamlit run app.py`
- [ ] Form renders ✓
- [ ] Submit triggers analysis ✓
- [ ] All 5 agent reports show in expanders ✓
- [ ] No crashes ✓

---

## Session 4 — Ship it (30 min)

- [ ] Final commit + push to GitHub
- [ ] Take a screenshot of the working ugly UI (this is *the* asset for Day-1 post)
- [ ] Add screenshot to `posts/day-1-launch.md`
- [ ] Post Day-1 launch to LinkedIn (or schedule it)
- [ ] Update repo description on GitHub with one-liner: *"An agentic AI front office for NBA trades."*

---

## Done criteria for Week 1

- [ ] Public GitHub repo with running code
- [ ] Streamlit app works locally end-to-end with stub data
- [ ] All 5 agents return distinct stubbed outputs
- [ ] Day-1 post posted (or scheduled)
- [ ] Frame shifted: no more "what should this do?" — only "make this stub real"

---

## First-15-minutes ritual (every session)

1. Open the repo
2. `git log -1` — see last commit
3. `streamlit run app.py` — confirm it still works (it should, even with stubs)
4. Open `TODO.md`, find the next unchecked box
5. Write today's intent in one sentence at the top of a scratch note
6. Start

No deciding required. The next box is the next thing.

---

## What "stuck" looks like — and what to do

- **Stuck on environment setup?** Cap at 30 min. If still stuck, abandon `.venv` and use system Python. Polish later.
- **Stuck on a stub's "fake content"?** Just write nonsense. The whole point is the stubs get replaced. Two-line stubs are fine.
- **Stuck on Streamlit layout?** Default everything. No CSS this week.
- **30+ minutes in docs?** Stop. Ask Claude.

---

## What unlocks at end of Week 1

- A working artifact you can show people (recruiters, friends, co-workers)
- Day-1 LinkedIn post live → public commitment to the build → loss-aversion engaged
- Confidence that this project is real and shippable
- Week 2 isn't "where do I start" — it's "open `agents/cap_apron.py` and replace the stub"
