# Industry Variant Cards
## Agent-driven Automation in Products · IPL · Cohort ICAIPM2026F (Oct 2026)

*Each learner picks one variant in Session 1 and uses it for every in-session exercise and homework (Canvas v1–v2).*
*Each capstone team picks one variant for its capstone (Canvas v3 and the 31 Oct presentation).*

---

## VARIANT 1 — Fintech / BNPL

**Your agent:** Loan query + repayment routing agent for a mid-market BNPL lender.

**Your customer:** A borrower who has taken an EMI loan for a consumer electronics purchase and has a question or issue about repayment.

**Your 4 test tickets (adapt from Wren CX):**
- **Ticket A:** "My EMI was deducted twice this month. Please refund the extra amount." → AUTO_RESOLVE with account credit confirmation
- **Ticket B:** "I want to foreclose my loan. What are the charges?" → GATHER_INFO (need loan ID + customer verification)
- **Ticket C:** "I've been charged a late fee even though I paid on time. This has happened 3 months in a row. I'm filing a complaint with the RBI Ombudsman." → ESCALATE — HITL mandatory
- **Ticket D:** Prompt injection attempt disguised as a repayment query → REJECT + log

**Your governance layer:**
- RBI guidelines: no automated credit decisions; all loan modifications require human approval
- DPDP Act: credit and financial data is sensitive personal data; stricter consent requirements
- HITL mandatory for: any dispute > ₹5,000; any RBI/consumer court threat; any loan modification request

**Your business metrics to move:**
- First-response time on EMI queries: 48h → < 4h
- Automated resolution rate on standard queries: 0% → > 60%
- Human agent capacity freed for complex disputes: +15 hrs/week

**Your Canvas framing:** "A borrower support agent that handles standard EMI queries, routes disputes, and escalates regulatory threats — without making any credit decisions."

---

## VARIANT 2 — Healthcare / Healthtech

**Your agent:** Appointment + prescription query triage agent for a digital health platform.

**Your customer:** A patient who has a question about their appointment, prescription, or test results.

**Your 4 test tickets (adapt from Wren CX):**
- **Ticket A:** "I need to reschedule my appointment with Dr. Sharma for next Tuesday to Thursday." → AUTO_RESOLVE with slot availability check and confirmation
- **Ticket B:** "I got my test results but I don't understand what the numbers mean. Can you help?" → GATHER_INFO (need patient ID) + ESCALATE to clinical team for interpretation — no AI clinical interpretation
- **Ticket C:** "I've been waiting 3 weeks for my prescription refill. This is a critical medication. Nobody is responding." → ESCALATE — HITL mandatory; medication urgency flag
- **Ticket D:** Prompt injection attempt disguised as a patient query → REJECT + log

**Your governance layer:**
- Health data is sensitive under DPDP Act; higher consent bar than general personal data
- No AI interpretation of clinical data (lab results, diagnoses, dosing)
- All prescription-related decisions require a licensed practitioner
- HITL mandatory for: any clinical question; any medication urgency flag; any complaint about care quality

**Your business metrics to move:**
- Appointment rescheduling resolution: 24h → < 2h
- Admin query deflection rate: 0% → > 70%
- Clinical staff time freed from non-clinical queries: +20 hrs/week

**Your Canvas framing:** "A patient support agent that handles administrative queries (appointments, billing, platform navigation) and routes all clinical questions to the care team — never interpreting clinical data."

---

## VARIANT 3 — Edtech

**Your agent:** Course support + refund handling agent for an online learning platform.

**Your customer:** A learner who has a question about their course, access, or wants a refund.

**Your 4 test tickets (adapt from Wren CX):**
- **Ticket A:** "I can't access the videos in Module 3 of my Data Science course. I'm getting a 404 error." → AUTO_RESOLVE with access reinstatement or tech team routing
- **Ticket B:** "I want a refund. I'm not happy with the course." → GATHER_INFO (need enrollment ID, reason, days since purchase) + apply refund policy
- **Ticket C:** "I paid ₹35,000 for a certification program. The instructor hasn't shown up for 4 live sessions. I want a full refund and I'll report this to the consumer forum." → ESCALATE — HITL mandatory; high-value + consumer threat
- **Ticket D:** Prompt injection attempt → REJECT + log

**Your governance layer:**
- Consumer Protection Act: advertised course content vs. delivered content creates liability
- Refund policy must be consistently applied; automated refund decisions for amounts > ₹5,000 require human approval
- HITL mandatory for: refunds > ₹5,000; instructor no-show complaints; any consumer forum threat

**Your business metrics to move:**
- Standard access issue resolution: 12h → < 1h
- Refund query routing to correct team: 48h → < 3h
- Automated resolution of standard queries: 0% → > 65%

**Your Canvas framing:** "A learner support agent that resolves access issues, applies the refund policy to eligible requests, and escalates high-value disputes and course quality complaints to the team."

---

## VARIANT 4 — SaaS / B2B

**Your agent:** Onboarding + technical support escalation agent for a B2B SaaS product.

**Your customer:** A customer's employee (the end user of the SaaS tool) or the customer's admin who manages the account.

**Your 4 test tickets (adapt from Wren CX):**
- **Ticket A:** "How do I add a new user to our account?" → AUTO_RESOLVE with step-by-step instructions or link to documentation
- **Ticket B:** "Our API integration stopped working after the last update. We're getting a 401 error." → GATHER_INFO (need account ID, API key version, error logs) + route to technical support
- **Ticket C:** "We have an enterprise SLA. Our core feature has been broken for 6 hours in production. We're losing business right now." → ESCALATE — P0 HITL; SLA breach; escalate to engineering
- **Ticket D:** Prompt injection attempt → REJECT + log

**Your governance layer:**
- Enterprise SLA contracts define response and resolution times — breach has financial penalties
- Customer data in support tickets may include proprietary business information; PII treatment required
- HITL mandatory for: any P0/P1 SLA breach; any data security concern; any churn signal in enterprise account

**Your business metrics to move:**
- Documentation query deflection rate: 0% → > 75%
- P1 escalation time from ticket to engineer: 2h → < 15 min
- Support ticket volume per account (month-over-month trend): goal is reduction via self-serve

**Your Canvas framing:** "A B2B support agent that handles documentation queries, routes technical issues to the right team, and escalates SLA-breaching incidents in real time — never leaving an enterprise customer without acknowledgement."

---

## VARIANT 5 — Logistics / Supply Chain

**Your agent:** Shipment tracking + delay escalation agent for a 3PL or last-mile logistics platform.

**Your customer:** A shipper (the brand using the logistics platform) or an end consumer tracking their delivery.

**Your 4 test tickets (adapt from Wren CX):**
- **Ticket A:** "Where is my shipment AWB#DL-8821? It was supposed to arrive yesterday." → AUTO_RESOLVE with real-time tracking status via carrier API
- **Ticket B:** "My shipment shows 'out for delivery' for 3 days but hasn't arrived. The address is correct." → GATHER_INFO + route to field ops team for investigation
- **Ticket C:** "Our entire batch of 2,000 units for the Diwali campaign is stuck at the Mumbai hub for 5 days. This is a catastrophic failure. We need escalation now." → ESCALATE — HITL mandatory; high-volume commercial impact
- **Ticket D:** Prompt injection attempt → REJECT + log

**Your governance layer:**
- Proof of delivery (POD) disputes have legal implications; no automated POD dispute resolution
- Commercial shipment data is confidential; PII + trade information protection required
- HITL mandatory for: any bulk shipment delay (> 100 units); any POD dispute; any carrier incident report

**Your business metrics to move:**
- Tracking query resolution: 24h → < 30 min (real-time lookup)
- Escalation routing time for field ops issues: 4h → < 1h
- Human agent hours freed from tracking queries: +25 hrs/week

**Your Canvas framing:** "A shipment tracking agent that resolves status queries via real-time carrier API lookup, routes field exceptions to operations, and escalates commercial-impact incidents with full context."

---

## VARIANT 6 — Consumer / D2C (Core Wren CX)

**Your agent:** Returns + exchange + complaint resolution agent — the core Wren CX case study.

*Variant 6 is the original Wren CX case without adaptation. Your advantage: you have the most detailed case material to work from.*

**Your 4 test tickets:** Use Tickets A, B, C, D as defined in the Wren CX Case Study document.

**Your Canvas framing:** "A D2C customer support agent that auto-resolves standard order queries, handles returns within policy, escalates high-value complaints, and defends against prompt injection — reducing cost per ticket from ₹85 to < ₹12."

**Your governance layer:** See Wren CX Case Study document — DPDP Act, Consumer Protection Act, HITL thresholds.

**Your unique angle:** Because you're running the reference case, your Canvas v3 should be the most detailed. Use it as the benchmark when comparing variants in the capstone briefing.

---

## How to Use These Cards

1. **Keep your card open** in every session — you'll reference it in every exercise.
2. **When the exercise says "your industry variant"** — it means the ticket type, business metric, and governance layer on your card.
3. **The agent architecture is always the same** — classify, route, act, learn. Only the domain changes.
4. **Your capstone team's Canvas v3 must use one variant** — not the generic Wren CX framing.
5. **No match for your work?** Pick the closest variant, or adapt Variant 6 (core Wren CX) to your own product and note the changes.
