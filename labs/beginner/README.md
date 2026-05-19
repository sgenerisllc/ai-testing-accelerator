# Beginner Labs

Hands-on exercises for Weeks 1-2. Focused on Python automation and Playwright fundamentals.

---

## Lab 01: Python Warm-Up

**Goal:** Refresh Python skills required for testing.

**Tasks:**
- Write a function that parses a list of test results and returns pass/fail counts
- Use type hints and a dataclass for the result structure
- Write 3 pytest unit tests for your function

**Time:** 30 min  
**Output:** `python warmup.py` should print parsed stats

---

## Lab 02: First Playwright Test

**Goal:** Install Playwright and write your first test.

**Tasks:**
1. Set up a Playwright project (`pip install playwright && playwright install`)
2. Write a test that visits `https://playwright.dev` and asserts the title contains "Playwright"
3. Run it with `--headed` so you can see the browser

**Time:** 45 min  
**Output:** One passing test

---

## Lab 03: Page Objects

**Goal:** Refactor a "spaghetti" test into a Page Object Model.

**Tasks:**
1. Start with a single test function with all logic inline (provided)
2. Extract a `LoginPage` class with methods for each interaction
3. Update the test to use the page object
4. Add a second test that reuses the same page object

**Time:** 60 min  
**Output:** Two tests using a shared `LoginPage` class

---

## Lab 04: GitHub Actions

**Goal:** Run your Playwright tests in CI.

**Tasks:**
1. Add a `.github/workflows/test.yml` workflow
2. Install Playwright browsers in the workflow
3. Upload the HTML report as an artifact
4. Push and watch it run

**Time:** 60 min  
**Output:** Green checkmark on a GitHub commit

---

## Lab 05: API Testing

**Goal:** Test a REST API with Python.

**Tasks:**
1. Use `requests` to test `https://jsonplaceholder.typicode.com/posts`
2. Validate status codes, response shape, and a key field
3. Write a parameterized pytest covering GET, POST, PUT, DELETE
4. Bonus: add JSON schema validation

**Time:** 60 min  
**Output:** 4+ passing API tests

---

## Lab 06: Hybrid Tests

**Goal:** Combine UI and API in a single test.

**Tasks:**
1. Seed data via API (`POST /users`)
2. Use Playwright to log in as that user
3. Verify the UI reflects the API state
4. Tear down via API (`DELETE /users/:id`)

**Time:** 75 min  
**Output:** One end-to-end test demonstrating hybrid pattern

---

## Submission

For each lab:
1. Create a folder under `labs/beginner/your-name/lab-NN/`
2. Include code + a short README explaining your approach
3. Submit via PR to the cohort repo
4. Tag your buddy for review

## Help

- **Stuck?** Drop a question in `#cohort-2026-help`
- **Office hours:** Fridays 4pm
- **Live debug:** Book a 15-min slot via the cohort calendar
