# AI GM

> An agentic AI front office for NBA trades.

AI GM analyzes NBA trades the way a front office actually would — through specialized agents that each handle a different dimension of the decision, then synthesize their work into a recommendation with reasoning trails, dissenting views, and a confidence score.

Most online NBA trade tools check whether the salary math works. AI GM also evaluates whether the trade makes sense as a basketball decision, with each agent's reasoning surfaced alongside the final recommendation.

🚧 **Status:** Early development. See [Roadmap](#roadmap) for current state.

---

## Why this exists

The 2023 CBA's second-apron rules made NBA team-building genuinely complex. Hard caps, traded player exceptions, sign-and-trade restrictions, draft pick freezes — most public-facing trade tools haven't kept up. They tell you whether two contracts can be legally combined; they don't tell you whether either team should *want* to do it.

AI GM is a working prototype of what an in-house front-office decision-support tool might look like if you started fresh with modern agentic AI patterns: explicit specialization, transparent reasoning trails, and CBA-aware logic from the ground up.

---

## What it does

**Input:** a proposed or actual NBA trade.

**Output:**
- Per-agent analysis from five specialized agents
- Synthesized recommendation with confidence level
- Reasoning trail showing how each agent contributed
- Dissenting views surfaced when agents disagree

---

## Architecture

```
                     User: proposed trade
                               │
                               ▼
        ┌──────────┬───────────┴───────────┬──────────┐
        ▼          ▼                       ▼          ▼
    ┌───────┐ ┌───────────┐         ┌───────────┐ ┌───────────┐
    │ Scout │ │ Architect │         │ Cap/Apron │ │  Context  │
    └───┬───┘ └─────┬─────┘         └─────┬─────┘ └─────┬─────┘
        │           │                     │             │
        └───────────┴──────────┬──────────┴─────────────┘
                               ▼
                         ┌──────────┐
                         │    GM    │
                         │ (synth)  │
                         └────┬─────┘
                              ▼
              Recommendation + reasoning trail
```

### The five agents

**Scout Agent.** Pure player evaluation. Advanced metrics (EPM, LEBRON, RAPM, BPM, on/off splits), age curves, injury history, durability. Intentionally roster-agnostic — outputs what you're getting in raw talent terms, nothing more.

**Architect Agent.** Team fit and roster construction. Classifies players by archetype (3-and-D wing, primary creator, rim protector, ball-handler, switchable defender), assesses scheme fit, models lineup synergy and positional balance, detects redundancy, and judges whether the player is additive to each team given current roster needs.

**Cap/Apron Agent.** CBA-aware trade math. Validates trade legality (salary matching, traded player exceptions), models cap and apron implications, flags hard cap triggers and draft pick freeze risks, projects multi-season cap impact.

**Context Agent.** Timing and intangibles — everything that doesn't show up in the box score. *Timing:* strength of schedule, competitive window (contender vs. rebuild), conference dynamics, draft pick value relative to expected finish. *Intangibles:* player and coach relationship history (positive or negative), locker room composition, veteran presence and leadership value, mentorship dynamics for young players.

**GM Agent.** Synthesizes the four specialist reports into a single recommendation. Surfaces agreement, disagreement, and confidence — and weights specialists differently based on team philosophy (a contender weighs Architect heavily; a rebuilding team leans on Scout's youth-curve work). Designed to reason like a GM weighing competing inputs from a staff, including knowing when to overrule them.

---

## Tech stack

- **Agent orchestration:** LangGraph
- **LLM:** Claude Sonnet 4.5 via the Anthropic API
- **Backend:** Python 3.11, FastAPI
- **Frontend:** Streamlit (v1) → Next.js (post-launch)
- **Data:** `nba_api`, Basketball Reference, Spotrac (cap), nbastatR

---

## Roadmap

- [ ] **v0.1** — End-to-end skeleton with five stub agents
- [ ] **v0.2** — Cap/Apron Agent fully implemented
- [ ] **v0.3** — Architect Agent fully implemented
- [ ] **v0.4** — Scout + Context Agents fully implemented
- [ ] **v0.5** — GM synthesis, polish, real-trade case studies
- [ ] **v1.0** — Public release

**Post-v1 directions:** multi-sport extension (NFL, MLB), recommender mode (proactive trade suggestions), integration with public trade rumor feeds, GM persona modes (rebuild GM vs. contender GM, risk-on vs. risk-off).

---

## Quickstart

```bash
git clone https://github.com/ericloeb1219/ai-gm.git
cd ai-gm
pip install -r requirements.txt
streamlit run app.py
```

*(Quickstart will be updated as the codebase materializes.)*

---

## About

I'm Eric — Manager of Product & Revenue Analytics at Peacock/NBCUniversal, where I lead sports and streaming analytics across the Olympics, World Cup, Sunday Night Football, Premier League, and Big Ten. I previously interned with the LA Clippers analytics group, building CLV and retention models. USC MS Business Analytics; UC Berkeley AI certification.

AI GM is a personal project exploring what front-office decision-support tools could look like if built today with modern agentic AI patterns.

[LinkedIn](https://linkedin.com/in/eric-loeb)

---

## License

MIT