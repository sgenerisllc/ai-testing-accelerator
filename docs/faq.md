# ❓ Frequently Asked Questions

---

## About the Program

### Who is this for?

QA engineers, SDETs, DevOps engineers, and developers who write integration/E2E tests. No AI background required.

### Do participants need prior Playwright experience?

No. Week 1-2 covers Playwright from scratch. Prior Selenium/Cypress experience helps but isn't required.

### What programming language is used?

Primarily **Python 3.10+** for AI tooling, with **TypeScript Playwright** examples where appropriate.

### Is there homework between sessions?

Yes — typically 3-5 hours of lab work per week. Self-paced; not graded. Office hours are available.

### What's the time commitment?

~10-12 hours per week:
- 6 hours live sessions (Mon/Wed/Fri × 2 hrs)
- 1 hour optional office hours
- 3-5 hours self-paced labs

### What happens if a participant misses a session?

All sessions are recorded and posted within 24 hours. Participants can ask follow-up questions in cohort Slack.

### Minimum attendance for certification?

70% of live sessions + all labs + capstone project.

---

## About the Technology

### Do the demos require an OpenAI API key?

No. **Every demo runs offline by default** using pattern matching and deterministic templates. Setting `OPENAI_API_KEY` enables enhanced LLM-powered output, but is optional.

### What's the cost of running this in production?

For a typical mid-sized engineering team:
- Demo 01-03 (rule-based features): **$0**
- Demo 04 (RAG): ~$10-30/month with cloud embeddings, or $0 with local models
- Demo 05 (autonomous agent): ~$30-100/month depending on usage

Total: **$50-150/month** for a 50-engineer org.

### Will this work with our internal stack?

Yes. Agent patterns are stack-agnostic. During pre-assessment we tailor:
- Frontend framework (React, Vue, Angular, Svelte, etc.)
- Backend (Node, Python, Go, Java, .NET, Rails, etc.)
- CI (GitHub Actions, GitLab CI, Jenkins, CircleCI, etc.)
- Ticketing (Jira, Linear, Asana, etc.)

### What about data privacy / compliance?

We teach **on-premise** and **local-model** patterns for sensitive environments (healthcare, fintech, government).

- Local LLM options: Llama 3, Mistral, Phi-3 (via Ollama)
- Local embeddings: sentence-transformers
- No customer data needs to leave your network

### How is this different from GitHub Copilot?

| Copilot | This Accelerator |
|---------|------------------|
| Helps individuals write code | Builds team-level autonomous systems |
| Inline code suggestions | Full agent loops with reflection |
| One-shot generations | Multi-step planning + repair |
| Per-developer subscription | Team-wide infrastructure |

They're complementary, not competing.

### Can I use Claude / Gemini / local models instead of OpenAI?

Yes. The code is structured so that any model is swappable. See `phases.py` in Demo 05 for the pattern.

---

## About the Demos

### Why do the demos use mocks instead of real Playwright execution?

Three reasons:
1. **Zero setup** — anyone can run a demo in 30 seconds
2. **Deterministic** — predictable output for presentations
3. **Focus** — the agent logic is the interesting part; runtime is plumbing

In the program, participants wire real Playwright into Demo 05 during Week 7.

### Can I extend the demos for my own use?

Absolutely. The MIT license permits any use. The capstone project is exactly this — extending demos to your stack.

### Why TF-IDF for RAG instead of vector embeddings?

For the demo scale (4 docs), TF-IDF performs equally well and requires zero dependencies. The `Retriever` class is a drop-in interface — swap for Chroma, Qdrant, or OpenAI embeddings in 10 lines of code.

---

## About the Business

### What's the investment?

$500 per participant. Recommended cohort: 6 participants = $3,000 total.

### What's included?

- 24 live sessions (48 hours of instruction)
- All labs and demo repos
- Session recordings (yours to keep)
- Pre-assessment + completion report
- Certificates
- Capstone project + code review
- 30-day post-program Slack support

### What's NOT included?

- OpenAI/cloud LLM costs (negligible — usually $0 during program)
- Production deployment of capstone (some teams do this themselves; consulting available separately)
- Custom curriculum modules (quoted separately)

### Can we have a larger cohort?

Yes. Up to 12 participants per cohort at $500 each. For 12+, we split into parallel cohorts.

### What's the cancellation policy?

Full refund up to 2 weeks before kickoff. After kickoff, prorated refund minus session-recording costs.

### Do you offer corporate training packages?

Yes. For enterprise clients (3+ cohorts/year), we offer:
- Reduced per-participant pricing
- Customized curriculum modules
- Embedded consulting hours
- White-labeled deliverables

Contact [sg@sgeneris.xyz](mailto:sg@sgeneris.xyz) for enterprise quotes.

---

## About the Outcomes

### What will participants actually be able to do?

See [`curriculum/learning-outcomes.md`](../curriculum/learning-outcomes.md) for the full list. Highlights:
- Generate Playwright tests from plain English in seconds
- Diagnose CI failures with AI-generated reports
- Build self-healing test suites
- Create RAG-grounded documentation assistants
- Deploy autonomous testing agents in CI

### Will participants get a job change / promotion?

Many do. Roles graduates have moved into:
- AI-Augmented QA Engineer
- Senior SDET with AI specialization
- Test Automation Architect
- AI Testing Tooling Lead

### What's the typical ROI?

For a 6-person team:
- **Investment:** $3,000
- **Year-1 savings:** ~$400K (flake reduction, faster triage, faster onboarding)
- **ROI:** ~130×

See the [executive proposal](../proposal/executive-proposal.md) for full math.

---

## Still Have Questions?

- **General inquiries:** [sg@sgeneris.xyz](mailto:sg@sgeneris.xyz)
- **Live demo request:** Same email — ask for a free 30-min demo session
- **Bulk pricing:** Same email — mention cohort size
