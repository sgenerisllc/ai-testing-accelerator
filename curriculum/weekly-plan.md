# 📅 Weekly Plan

## 8-Week Schedule — Mon/Wed/Fri, 2 hours/session

---

## Week 0: Prework & Baseline

Completed asynchronously before kickoff.

| Item | Outcome |
|------|---------|
| Environment setup | Python, Git, Playwright, and editor ready |
| Skills diagnostic | Baseline Python, testing, CI, and AI workflow assessment |
| Product context | Each participant identifies one real QA pain point |
| Metrics baseline | Team records current flake rate, triage time, CI duration, and test authoring time |

**Milestone:** Every participant can run the demo repository and has a scoped improvement target.

---

## Week 1: Python & Playwright Foundations

| Day | Topic | Lab |
|-----|-------|-----|
| **Mon** | Python essentials for testers (functions, classes, typing) | [Beginner Lab 01](../labs/beginner/#lab-01-python-warm-up) |
| **Wed** | Playwright setup, first test, locators | [Beginner Lab 02](../labs/beginner/#lab-02-first-playwright-test) |
| **Fri** | Page Object Model + test organization | [Beginner Lab 03](../labs/beginner/#lab-03-page-objects) |

**Office Hours:** Friday 4pm — Q&A on environment setup

---

## Week 2: CI/CD & API Testing

| Day | Topic | Lab |
|-----|-------|-----|
| **Mon** | GitHub Actions CI/CD pipeline for tests | [Beginner Lab 04](../labs/beginner/#lab-04-github-actions) |
| **Wed** | API testing with `requests` and `httpx` | [Beginner Lab 05](../labs/beginner/#lab-05-api-testing) |
| **Fri** | Hybrid UI + API test patterns | [Beginner Lab 06](../labs/beginner/#lab-06-hybrid-tests) |

**Milestone:** Each participant has a working CI pipeline running their tests.

---

## Week 3: Advanced Locators & Test Patterns

| Day | Topic | Lab |
|-----|-------|-----|
| **Mon** | Accessibility-first locators (`getByRole`, `getByLabel`) | [Intermediate Lab 01](../labs/intermediate/#lab-01-accessible-locators) |
| **Wed** | Network interception and request mocking | [Intermediate Lab 02](../labs/intermediate/#lab-02-network-mocking) |
| **Fri** | Authentication patterns and state reuse | [Intermediate Lab 03](../labs/intermediate/#lab-03-auth-state-reuse) |

---

## Week 4: Scale & Reporting

| Day | Topic | Lab |
|-----|-------|-----|
| **Mon** | Parallel execution and sharding | [Intermediate Lab 04](../labs/intermediate/#lab-04-parallel-execution) |
| **Wed** | Visual regression with screenshots | [Intermediate Lab 05](../labs/intermediate/#lab-05-visual-regression) |
| **Fri** | HTML/Allure reporting + CI artifacts | [Intermediate Lab 06](../labs/intermediate/#lab-06-reporting) |

**Milestone:** Participants run a full test suite in parallel under 5 minutes.

---

## Week 5: Prompt Engineering & LLM Integration

| Day | Topic | Lab |
|-----|-------|-----|
| **Mon** | Prompt engineering, structured output, and reproducible evals | [Intermediate Lab 07](../labs/intermediate/#lab-07-prompt-engineering) |
| **Wed** | LLM-powered test generation — Demo 01 deep dive | `demos/01-prompt-to-test-generator/` |
| **Fri** | AI failure analysis, confidence scoring, and human review — Demo 02 deep dive | `demos/02-ai-failure-analyzer/` |

**Live Demo:** Generate a test plan and first-pass Playwright drafts from a Jira ticket.

---

## Week 6: RAG, MCP & CLI Tools

| Day | Topic | Lab |
|-----|-------|-----|
| **Mon** | RAG fundamentals: chunking, embedding, retrieval | [Advanced Lab 01](../labs/advanced/#lab-01-rag-basics) |
| **Wed** | Build a RAG QA assistant, retrieval evals, and citation checks — Demo 04 deep dive | `demos/04-rag-qa-assistant/` |
| **Fri** | MCP workflows, tool permissions, audit logs, and CLI construction | [Advanced Lab 02](../labs/advanced/#lab-02-mcp--cli-tool) |

**Milestone:** Each participant builds a CLI tool that integrates AI into a real workflow.

---

## Week 7: Autonomous Agents

| Day | Topic | Lab |
|-----|-------|-----|
| **Mon** | Self-healing locators and flake taxonomy — Demo 03 deep dive | `demos/03-self-healing-locators/` |
| **Wed** | Agent loop architecture, guardrails, budgets, and rollback | [Advanced Lab 03](../labs/advanced/#lab-03-agent-loop) |
| **Fri** | Autonomous Playwright agent, observability, and escalation — Demo 05 deep dive | `demos/05-autonomous-playwright-agent/` |

**Live Demo:** Watch an agent generate, run, fail, suggest a repair, and re-run under confidence gates.

---

## Week 8: Capstone

| Day | Activity |
|-----|----------|
| **Mon** | Capstone scope-setting, risk review, and architecture review |
| **Wed** | Build, hardening, and code review session with instructor support |
| **Fri** | **Capstone Demo Day** — live presentations to leadership |

**Deliverable:** Each participant ships a pilot-ready QA workflow plus a production hardening plan.

---

## Time Investment

| Activity | Hours/Week | Total |
|----------|-----------|-------|
| Live sessions (Mon/Wed/Fri × 2 hrs) | 6 | 48 |
| Office hours (optional) | 1 | 8 |
| Lab practice (self-paced) | 3-5 | 24-40 |
| Capstone (Week 8) | 8-10 | 8-10 |
| **Total participant commitment** | **10-12** | **~90** |

---

## Office Hours Format

Every Friday, the hour following the main session:
- Open Q&A
- Live debugging of participant code
- Capstone planning support
- Career guidance for AI-augmented QA roles

---

## Attendance & Recordings

All sessions are recorded and posted within 24 hours. Participants missing live sessions can:
- Watch the recording
- Ask follow-up questions in the cohort Slack
- Drop into the next office hours

**Minimum attendance:** 70% of live sessions for certification.
