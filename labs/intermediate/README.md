# Intermediate Labs

Hands-on exercises for Weeks 3-5. Production-grade automation patterns and the first taste of AI.

---

## Lab 01: Accessible Locators

**Goal:** Replace brittle CSS locators with accessibility-first patterns.

**Tasks:**
- Start with a test using `page.locator('.btn-primary')`
- Refactor to `page.get_by_role('button', name='Submit')`
- Audit all locators in `tests/` and report which need fixing

**Time:** 45 min

---

## Lab 02: Network Mocking

**Goal:** Mock API responses to test edge cases.

**Tasks:**
- Mock `GET /api/products` to return an empty array → assert "No products" message
- Mock the same endpoint to return 500 → assert error UI
- Use `page.route` and `route.fulfill`

**Time:** 60 min

---

## Lab 03: Auth State Reuse

**Goal:** Don't re-log-in for every test.

**Tasks:**
- Implement a `globalSetup` that logs in once and saves storage state
- Reuse the state in `playwright.config.ts`
- Reduce a 20-test auth flow from 8 minutes to 1 minute

**Time:** 60 min

---

## Lab 04: Parallel Execution

**Goal:** Run the full suite in under 5 minutes.

**Tasks:**
- Configure `workers: 4` in `playwright.config.ts`
- Add `test.describe.configure({ mode: 'parallel' })` where safe
- Identify and fix tests that can't run in parallel
- Report speedup ratio

**Time:** 75 min

---

## Lab 05: Visual Regression

**Goal:** Catch unintended UI changes.

**Tasks:**
- Add a baseline screenshot for the home page
- Make a small CSS change and watch the test fail
- Approve the new baseline
- Discuss: when is visual testing worth the maintenance cost?

**Time:** 60 min

---

## Lab 06: Reporting

**Goal:** Make CI failures easy to triage.

**Tasks:**
- Enable HTML report in `playwright.config.ts`
- Upload as a CI artifact
- Add Allure reporting (optional)
- Bonus: post a summary comment on the PR with pass/fail counts

**Time:** 45 min

---

## Lab 07: Prompt Engineering

**Goal:** Get reliable test code from an LLM.

**Tasks:**
- Write a prompt that produces a Playwright test for "user can update profile"
- Iterate on the prompt: add examples, system message, output constraints
- Compare output quality across 3 prompt versions
- Document what worked

**Time:** 90 min  
**Reference:** [Demo 01](../../demos/01-prompt-to-test-generator/) shows the working pattern.

---

## Submission

Same format as beginner labs: PR to the cohort repo with code + brief writeup.

## Stretch Goals

After completing these labs, try the [advanced labs](../advanced/).
