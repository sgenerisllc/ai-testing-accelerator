# 🏆 Capstone: Final Showcase

Each participant ships a **production-ready autonomous testing agent** customized to their team's tech stack.

This is the moment everything clicks: 8 weeks of foundations, automation, AI, and agents converge into one cohesive deliverable.

---

## Capstone Requirements

Your capstone must include:

### 1. A Real Tech Stack
Pick your actual company's stack — or a public open-source project. Examples:
- Frontend: React, Vue, Angular, Svelte, Next.js
- Backend: Node, Python, Go, Java, .NET
- CI: GitHub Actions, GitLab CI, CircleCI, Jenkins

### 2. An Agent That Performs At Least 3 Of:

- ✅ Auto-generates Playwright tests from Jira tickets or PR descriptions
- ✅ Auto-analyzes failed CI runs and posts a structured report
- ✅ Auto-repairs broken selectors using a self-healing strategy
- ✅ Answers QA questions using a RAG system over your team's docs
- ✅ Runs autonomously in CI and posts results to Slack/Jira

### 3. Production-Grade Polish

- Clean, readable code (passes lint and review)
- Comprehensive README in your project repo
- Unit tests for critical paths
- Cost controls (budget cap, caching)
- Observability (structured logs)

### 4. A Demo Video (Optional but Recommended)
A 3-5 minute screen recording walking through your agent in action.

---

## Suggested Project Scopes

| Project Idea | Best For | Difficulty |
|--------------|----------|------------|
| Slack bot that runs tests on `/test <feature>` | QA team enablement | ⭐⭐ |
| GitHub Action that auto-generates tests for new PRs | DevOps focus | ⭐⭐⭐ |
| RAG assistant over your team's runbooks | New-hire onboarding | ⭐⭐ |
| Flaky-test detector + auto-quarantine | CI stability | ⭐⭐⭐⭐ |
| Multi-agent orchestrator (Planner/Author/Reviewer) | Architecture-minded | ⭐⭐⭐⭐⭐ |
| AI test-coverage gap analyzer for a code repo | Coverage-focused | ⭐⭐⭐ |
| Visual-regression bot with auto-baseline-suggestion | UI-heavy products | ⭐⭐⭐⭐ |

---

## Timeline

| Week 8 Day | Activity |
|------------|----------|
| **Monday** | Scope confirmation + architecture review (30 min/participant) |
| **Tuesday-Thursday** | Build (instructor on-call in cohort Slack) |
| **Friday morning** | Final integration + rehearsal |
| **Friday afternoon** | **🎬 Capstone Demo Day** |

---

## Demo Day Format

Each participant presents for **8 minutes**:

1. **Problem statement** (1 min) — "My team's biggest QA pain"
2. **Solution architecture** (2 min) — diagram + tech stack
3. **Live demo** (4 min) — show the agent working end-to-end
4. **Impact + next steps** (1 min) — projected ROI for their team

Followed by 2 minutes of Q&A.

---

## Evaluation Rubric

| Criterion | Weight | What "Excellent" Looks Like |
|-----------|--------|-----------------------------|
| **Technical execution** | 30% | Clean code, runs reliably, handles edge cases |
| **Real-world applicability** | 25% | Solves a genuine problem; deploy-ready |
| **AI integration quality** | 20% | Thoughtful use of AI; sensible fallbacks |
| **Presentation clarity** | 15% | Confident, structured, time-managed |
| **Innovation** | 10% | Goes beyond the demos; original ideas |

---

## What Past Participants Have Built

*(Examples — anonymized scenarios)*

- **Fintech SDET:** Built a Slack bot that takes a Jira ticket and posts back a complete test plan + Playwright spec within 30 seconds. Adopted by their team within 2 weeks.

- **E-commerce QA Lead:** Created a flaky test auto-quarantiner that reduced their team's CI flake rate from 8% to 1.2% in a month.

- **DevOps Engineer:** Shipped a GitHub Action that comments on every PR with AI-summarized test impact analysis. Now used company-wide.

- **Healthcare QA Engineer:** RAG assistant over HIPAA compliance docs + test cases. Cut compliance audit prep time by 70%.

---

## Resources

- All 5 demos in this repo — fork and extend
- [`architecture/`](../architecture/) — system design patterns
- [`labs/advanced/`](../labs/advanced/) — preparatory exercises
- Cohort Slack #capstone-help — instructor on-call

---

## After the Capstone

Your capstone is **yours to keep and deploy**. We encourage you to:

1. Open-source it (with your company's approval)
2. Write a blog post about your learnings
3. Present it at your company's all-hands
4. Mentor the next cohort

The best capstones often become the foundation of new company-internal tools.

---

## Submission

By Demo Day Friday 9am:
1. Push your code to a GitHub repo (public or private)
2. Submit the repo URL + a 1-paragraph summary via the cohort form
3. Be ready to present in your scheduled slot

---

**Make it bold. Make it real. Make it ship.** 🚀
