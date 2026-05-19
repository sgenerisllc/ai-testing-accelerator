# Advanced Labs

Hands-on exercises for Weeks 6-7. RAG systems, MCP workflows, and autonomous agents.

These labs assume you've completed beginner and intermediate tracks.

---

## Lab 01: RAG Basics

**Goal:** Build a minimal RAG system from scratch.

**Tasks:**
- Index 5+ markdown files into a TF-IDF retriever (start from [Demo 04](../../demos/04-rag-qa-assistant/))
- Add cosine similarity scoring
- Implement top-K retrieval
- Compare extractive vs generative answers (with `OPENAI_API_KEY` set)

**Time:** 2 hours  
**Stretch:** Replace TF-IDF with sentence-transformers embeddings.

---

## Lab 02: MCP / CLI Tool

**Goal:** Build a CLI that integrates AI into a real workflow.

**Tasks:**
- Create a `qa-tool` CLI using `click` or `typer`
- Add a `qa-tool generate <intent>` command (wrapping Demo 01)
- Add a `qa-tool analyze <log>` command (wrapping Demo 02)
- Add a `qa-tool ask <question>` command (wrapping Demo 04)
- Package with `pip install -e .` and add tab completion

**Time:** 3 hours  
**Stretch:** Publish to TestPyPI.

---

## Lab 03: Agent Loop

**Goal:** Build the perceive → plan → act → reflect loop from scratch.

**Tasks:**
- Reproduce the 4-phase loop of [Demo 05](../../demos/05-autonomous-playwright-agent/)
- Replace `phases.py` mock logic with real LLM calls
- Add a 5th phase: "memorize" — store outcomes for future learning
- Run on 10 distinct intents and report success rate

**Time:** 4 hours  
**Stretch:** Add a budget cap that aborts if AI cost exceeds $0.50/run.

---

## Lab 04: Self-Healing in Real Playwright

**Goal:** Wire the heal logic from [Demo 03](../../demos/03-self-healing-locators/) into a live Playwright test.

**Tasks:**
- Create a Playwright project with a test pointing at a broken selector
- Hook the heal logic to run on `TimeoutError`
- Auto-suggest the fix in the test report
- Bonus: open a GitHub PR with the suggested fix using `gh` CLI

**Time:** 3 hours

---

## Lab 05: Multi-Agent Orchestration

**Goal:** Split the autonomous agent into specialized sub-agents.

**Tasks:**
- Refactor the agent into Planner, Author, Runner, Analyst agents (see [`agentic-qa-system.md`](../../architecture/agentic-qa-system.md))
- Define a structured message format for inter-agent communication
- Add a Reviewer agent that can veto Author output
- Log all agent conversations to a JSONL file for replay

**Time:** 5 hours  
**Stretch:** Add observability via Langsmith or Helicone.

---

## Lab 06: Confidence-Gated Auto-Merge

**Goal:** Build the production safety layer.

**Tasks:**
- For each AI repair, compute a confidence score (rule-based or LLM-rated)
- Auto-apply repairs with confidence > 90%
- Open a draft PR for confidence 70-90%
- Escalate to Slack for confidence < 70%
- Track outcomes: how often did auto-applied repairs actually fix the bug?

**Time:** 4 hours

---

## Submission & Capstone Bridge

Advanced labs feed directly into your [capstone project](../../capstone/final-showcase.md). Pick labs that align with your capstone scope.

## Going Beyond

Post-program, contribute back:
- Open issues for improvements
- Submit PRs with new labs or demos
- Mentor next cohort
