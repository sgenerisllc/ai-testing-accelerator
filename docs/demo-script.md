# 🎬 Demo Script

A complete, timed script for presenting this repository to engineering leaders.

**Total runtime: 15 minutes** (10 min demo + 5 min Q&A).

---

## Pre-Demo Checklist

- [ ] Terminal font size bumped to 18pt
- [ ] All 5 demos verified working that morning
- [ ] README.md open in a browser tab
- [ ] Architecture docs open in a tab
- [ ] Slides backup ready (in case of demo failure)

---

## Opening (90 seconds)

> "Most QA teams are stuck in 2018: manual test writing, hours debugging flaky tests, tribal knowledge locked in senior engineers' heads.
>
> Today I'm going to show you what 2026 QA workflows can look like. Five demos. Each one targets a real pain point. All running locally, no cloud, no setup. Then we'll talk about what it would take to pilot this with your team in 8 weeks."

Open the README in browser. Scroll past the maturity model.

> "We'll move through five capabilities. Each takes about 90 seconds."

---

## Demo 1: Prompt-to-Test Generator (90s)

**The pain:** "Writing a Playwright test takes 15-30 minutes."

```bash
cd demos/01-prompt-to-test-generator
python generator.py "test user login with valid credentials"
```

**Show the output. Then:**

```bash
python generator.py "verify checkout flow with credit card payment"
```

**Land it:** "Five seconds. A solid first draft with accessibility-first locators. Imagine this as a reviewed starting point against your Jira backlog."

---

## Demo 2: AI Failure Analyzer (90s)

**The pain:** "An on-call engineer spends 30 minutes parsing a CI failure log at 2 AM."

```bash
cd ../02-ai-failure-analyzer
cat sample-failure.log    # Show the dense raw log
```

> "Watch this become actionable in 2 seconds."

```bash
python analyzer.py sample-failure.log
```

**Walk through:** failure type, ranked causes, code snippet fix.

```bash
python analyzer.py sample-failure.log --format jira
```

**Land it:** "30 minutes of triage → 30 seconds. Across 50 failures a week, that's 25 engineer-hours."

---

## Demo 3: Self-Healing Locators (90s)

**The pain:** "Frontend team renames a button class → 20 tests fail → on-call ping."

```bash
cd ../03-self-healing-locators
python heal.py
```

**Walk through:** Strategy 1 fails (old ID), Strategy 2 fails (no test-id), Strategy 3 succeeds (role+name).

**Land it:** "Three fallback layers. Test passed. CI green. The team gets a Slack DM saying 'your selector drifted, here's the suggested fix.'"

---

## Demo 4: RAG QA Assistant (90s)

**The pain:** "A new QA hire takes 3 months to ramp up because knowledge is locked in senior engineers' heads."

```bash
cd ../04-rag-qa-assistant
python rag.py "How do I add a new test to the CI pipeline?"
```

**Highlight:** the answer comes with cited sources.

```bash
python rag.py "What is the flaky test policy?"
python rag.py "Can I disable a test?"
```

**Land it:** "Every answer cites a doc. The system has a place to say 'not found' instead of guessing. Drop in your internal docs, add retrieval evals, and new hires get useful answers faster."

---

## Demo 5: Autonomous Agent (120s — the headline)

**The pain:** "All four of the above still need a human manually wiring the loop together. What if we automated the bounded loop and kept humans on approval?"

```bash
cd ../05-autonomous-playwright-agent
python agent.py --intent "verify checkout flow" --force-fail
```

**Watch the audience.** The perceive → plan → act → reflect → act-again loop is the important concept.

**Pause at the failure.** Say: "Watch what happens now."

**Pause at the recovery.** Say: "It diagnosed the failure, applied a bounded repair in this demo, and re-ran."

**Show the generated file:**

```bash
cat generated/test_verify_checkout_flow.py
```

**Land it:** "This is the pattern every participant adapts in week 8 — customized to their company's stack, with confidence gates and a production hardening plan."

---

## Closing & Pitch (90 seconds)

> "We just covered five capabilities in 10 minutes. In an 8-week program, your team builds each of these and customizes them to your stack.
>
> The investment is $500 per participant — $3,000 for a 6-person team. In teams that adopt the workflows and measure the baseline, the ROI model can reach up to ~130×.
>
> Three next steps: [hold up three fingers]
>
> 1. **30-minute discovery call** to confirm fit
> 2. **Free demo session** for your full team — they see this live and Q&A directly
> 3. **Pre-assessment** of your team's baseline so we can tailor the cohort
>
> Which of those makes sense as a next step for you?"

---

## Q&A Anticipated Questions

| Question | Quick Answer |
|----------|--------------|
| "Does this work with our stack?" | Yes — agent patterns are stack-agnostic. We adapt during pre-assessment. |
| "Do we need to buy OpenAI credits?" | No — demos work offline. Pilot costs vary by model and usage; add budget caps before production. |
| "What about data privacy?" | We teach on-prem / local-model patterns. No customer data leaves your environment. |
| "How is this different from Copilot?" | Copilot helps individuals write code. This builds team-level autonomous systems. |
| "Can our DevOps team take it?" | Absolutely — DevOps + QA + SDETs are the ideal audience. |
| "What if a participant falls behind?" | Office hours, recordings, buddy reviews, and scoped capstone tracks. |

---

## Failure Modes & Recovery

**If a demo fails on stage:**
1. Don't panic. Say: "Let me show you the recorded version."
2. Switch to slides or play a screen recording (always have one ready).
3. Resume the next demo. Mention you'll send the working version after.

**If the audience seems skeptical:**
- Pivot to the cost section in the README
- Show the executive proposal
- Offer a no-cost demo session for their full team

**If the audience seems sold:**
- Skip closing pitch, go straight to "When can we kick off?"
- Move to scheduling the pre-assessment
