# QA Onboarding Guide

Welcome to the team. This guide gets you productive on day one.

## Day 1: Environment Setup

1. **Clone the test repo**

   ```bash
   git clone git@github.com:acme/qa-tests.git
   cd qa-tests
   ```

2. **Install dependencies**

   ```bash
   npm install
   npx playwright install --with-deps
   ```

3. **Run tests locally**

   To run tests locally, execute `npm test` from the repo root. To run a single test, use `npx playwright test tests/auth.spec.ts --headed`. The `--headed` flag opens a real browser window so you can see what's happening.

4. **Verify your environment**

   Run the smoke suite: `npm run test:smoke`. It should complete in under 3 minutes.

## Day 2: Read the Standards

Required reading:
- `testing-standards.md` — quality bar, flaky test policy
- `playwright-best-practices.md` — locator strategy, fixtures
- `ci-pipeline.md` — how tests run in CI

## Day 3: Write Your First Test

Pick a `good first issue` from the backlog. Pair with your onboarding buddy. Submit a PR by end of day.

## Week 1: Capstone

Your first-week capstone:
1. Add 3 tests to the smoke suite
2. Run the regression suite locally and triage any failures
3. Present to the team in Friday's QA sync

## Common Issues

### "My tests pass locally but fail in CI"

Usually due to:
- Hardcoded paths (use `process.env.BASE_URL`)
- Timing assumptions (CI is slower; use explicit waits)
- Missing fixtures (CI runs with fresh DB)

### "I can't find the right locator"

Use Playwright Inspector: `npx playwright test --debug`. It suggests resilient locators interactively.

### "My test is flaky"

See the flaky test policy in `testing-standards.md`. Quarantine first, then fix.

## Who to Ask

- **Test infrastructure:** #qa-platform Slack
- **CI issues:** #devops Slack
- **Coverage strategy:** Your team lead
- **AI testing tools:** #ai-qa Slack

## Resources

- Internal: `wiki/qa-handbook`
- Playwright docs: [playwright.dev](https://playwright.dev)
- This RAG assistant: ask me anything!
