# Agent-driven Automation in Products
**Institute of Product Leadership · Cohort ICAIPM2026F · October 2026**
Prof. Shameek Chakravarty

| Session | Date (Saturdays, 6:00–9:00 PM IST) | Theme | Materials |
|---|---|---|---|
| 1 | 3 Oct | Foundations, the AI-native PRD, first agent builds | [`session1/`](session1/) |
| 2 | 17 Oct | MCP, planning, multi-agent systems, the eval problem | [`session2/`](session2/) |
| 3 | 24 Oct | Eval harness, guardrails, token economics, HITL, capstone scoping | Added before the session |
| 4 | 31 Oct | Capstone presentations | Added before Session 3 |

New materials are added to this repo before each session. Pull (or re-download) before every class.

**How you'll work:** every session runs on one case, Wren CX, and you work on your own. The capstone is different: your team picks its own problem, from a sample list you'll receive or, better, one of your own. **Three pieces of homework:** two in the gap after Session 1, and one team checkpoint after Session 2 that feeds straight into the capstone (see below). Everything else happens in the session; the capstone is the only other take-home work.

## Start Here

1. **Read the case:** [`case-study/wren-cx-case-study.md`](case-study/wren-cx-case-study.md). Wren CX is the running case for Sessions 1–3.
2. **Optional:** [`case-study/industry-variant-cards.md`](case-study/industry-variant-cards.md) shows the same case in five other industries, if you want to play around. Not needed for any session.
3. **Open tonight's handbook:** [`session2/Session2_Student_Handbook.md`](session2/Session2_Student_Handbook.md) (Session 1: [`session1/Session1_Student_Handbook.md`](session1/Session1_Student_Handbook.md)). There are no slides: we work through the handbook together in class, and every prompt is in it, ready to paste.

## What's Here

| Folder | Contents |
|---|---|
| `case-study/` | The Wren CX case + optional industry variant cards |
| `sample_data/` | Support tickets (`wren_tickets.json`), the simulated CRM (`crm_orders.json`), the golden dataset (`golden_dataset.csv`) and inputs for the PM workflows (`pm_workflow_inputs/`) |
| `mcp-server/` | The Wren mock MCP server (ticket inbox + CRM) for Session 2. Python 3 standard library, nothing to install |
| `templates/` | The Agent Opportunity Canvas (blank) and a filled example for Wren CX |
| `session1/` | The Session 1 handbook |
| `session2/` | The Session 2 handbook |

## Tools

- **Google Antigravity** is the main build tool for the course. If it isn't working tonight, run the Session 1 prompts in any LLM chat (Claude, ChatGPT, Gemini). **Have Antigravity working before Session 2.**
- **Agentic AI Lab:** https://agentic-ai-lab-rho.vercel.app. Browser simulations of each concept on the same Wren case. The handbook links to the right lab at the right point. No login needed.

## Homework 1 — due Sat 10 Oct, end of day

1. Form your capstone team and freeze it.
2. Pick your capstone problem: from the sample list you'll receive or, better, your own. Not Wren.
3. Fill the full Agent Opportunity Canvas ([`templates/agent-opportunity-canvas.md`](templates/agent-opportunity-canvas.md)) for it, as a team. Model: [`templates/agent-opportunity-canvas-wren-sample.md`](templates/agent-opportunity-canvas-wren-sample.md).
4. Submit the team list, problem statement and canvas by Saturday 10 October, end of day.

## Homework 2 — Agent Teardown (individual), due Fri 16 Oct, end of day

Test one live AI assistant or agent five ways (happy path, missing information, ambiguous, high-stakes, a harmless "ignore your instructions" probe), map it onto canvas boxes 1, 6, 9, 12 and 13, diagnose where it breaks, and write three spec lines you'd add to its PRD. One page with screenshots; no real account changes or personal data.

Details for both: section 10 of the Session 1 handbook.

## Before Session 2 (Sat 17 Oct, 6:00 PM) — connect MCP

Pull this repo, then take 5 minutes before class:

1. Install Python 3 if you don't have it. Step-by-step for Mac and Windows: https://agentic-ai-lab-rho.vercel.app/setup
2. Register the Wren MCP server: follow [`mcp-server/README.md`](mcp-server/README.md).
3. Ask the agent: *"List the tools on the wren MCP server."* You should see 4 tools.

If it won't connect, don't worry: the handbook has simulated tool outputs so you can follow along.

## Homework 3 — Capstone Canvas v2 (team), due Thu 22 Oct, 11:59 PM IST

Capstone work brought forward, about 2 hours: list your team members, add one measured baseline with its source, run the three-sentence test on every agent (redraw box 10), write 10 golden examples for your own capstone, and rewrite boxes 13–14 as spec lines with a number, its reason, and the cost of a miss. One submission per team through the usual form.

Details: Homework 3 in [the Session 2 handbook](session2/Session2_Student_Handbook.md#homework-3--capstone-canvas-v2-team-due-thu-22-oct-1159-pm-ist-about-2-hours).

## Before Session 3 (Sat 24 Oct)

Bring `golden_mine.csv` (the six rows you label in Session 2) and your team's canvas v2.
