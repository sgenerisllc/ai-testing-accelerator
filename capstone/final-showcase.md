# 🏆 Capstone: Final Showcase

Each participant ships a **pilot-ready AI-augmented QA workflow** customized to their team's tech stack.

This is the moment everything clicks: 8 weeks of foundations, automation, AI, and agents converge into one cohesive deliverable that can be evaluated safely before production rollout.

---

## Capstone Requirements

Your capstone must include:

### 1. A Real Tech Stack
Pick your actual company's stack — or a public open-source project. Examples:
- Frontend: React, Vue, Angular, Svelte, Next.js
- Backend: Node, Python, Go, Java, .NET
- CI: GitHub Actions, GitLab CI, CircleCI, Jenkins

### 2. One Primary Workflow

Choose one workflow and make it work end-to-end:

- ✅ Generate Playwright test drafts from Jira tickets or PR descriptions
- ✅ Analyze failed CI runs and post a structured report
- ✅ Repair or suggest fixes for broken selectors using a self-healing strategy
- ✅ Answer QA questions using a RAG system over your team's docs
- ✅ Run a controlled CI workflow and post results to Slack, Jira, or GitHub

### 3. Safety & Production Path

- Clean, readable code (passes lint and review)
- Comprehensive README in your project repo
- Unit tests for critical paths
- Cost controls (budget cap, caching, retry limits)
- Observability (structured logs, prompt/response audit trail)
- Human approval gates for code changes, CI changes, and external notifications
- A short production hardening plan covering secrets, rollout, ownership, and rollback

### 4. Optional Stretch Capabilities

If the primary workflow is stable, add one stretch item:

- Second agent role, such as Reviewer or Analyst
- Retrieval evals for a RAG assistant
- GitHub draft PR creation for suggested repairs
- Slack/Jira integration in dry-run mode
- Flake trend dashboard or quarantine policy

### 5. A Demo Video (Optional but Recommended)
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

For cohorts with junior participants, a team capstone is recommended: 3-4 participants share one workflow and split ownership across ingestion, AI logic, execution, and reporting.

---

## Timeline

| Week 8 Day | Activity |
|------------|----------|
| **Monday** | Scope confirmation + architecture review (30 min/participant) |
| **Tuesday-Thursday** | Build, test, and harden (instructor on-call in cohort Slack) |
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
| **Real-world applicability** | 25% | Solves a genuine problem; has a credible production path |
| **AI integration quality** | 20% | Thoughtful use of AI; evals, guardrails, and fallbacks included |
| **Presentation clarity** | 15% | Confident, structured, time-managed |
| **Innovation** | 10% | Goes beyond the demos; original ideas |

---

## Example Target Outcomes

*(Representative outcomes to aim for.)*

- **Fintech SDET:** Slack bot that takes a Jira ticket and posts back a test plan plus Playwright draft in dry-run mode.

- **E-commerce QA Lead:** Flaky-test classifier that identifies likely flakes, suggests quarantine, and tracks repeated failures.

- **DevOps Engineer:** GitHub Action that comments on PRs with AI-summarized test impact and links to relevant test files.

- **Healthcare QA Engineer:** RAG assistant over compliance docs and test cases with citations and unanswered-question tracking.

---

## Resources

- All 5 demos in this repo — fork and extend
- [`architecture/`](../architecture/) — system design patterns
- [`labs/advanced/`](../labs/advanced/) — preparatory exercises
- Cohort Slack #capstone-help — instructor on-call

---

## After the Capstone

Your capstone is **yours to keep and harden for deployment**. We encourage you to:

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

**Make it real enough to evaluate, safe enough to trust, and clear enough to extend.**
