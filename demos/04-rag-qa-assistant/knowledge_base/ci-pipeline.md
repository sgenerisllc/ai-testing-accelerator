# CI Pipeline

Our continuous integration pipeline runs on GitHub Actions and is defined in `.github/workflows/test.yml`.

## How tests are discovered

To add a new test to the CI pipeline, place your spec file in the `tests/` directory. The CI workflow automatically discovers files matching `*.spec.ts` or `*.spec.py` and runs them in parallel shards. Tag your test with `@smoke` or `@regression` to control which CI stage executes it.

## Stages

The pipeline has three stages:

1. **Lint & type-check** — runs ESLint, Prettier, and mypy. Must pass before tests start.
2. **Smoke tests** — fast subset (~3 minutes). Tagged with `@smoke`. Blocks merge.
3. **Regression suite** — full E2E suite (~15 minutes). Tagged with `@regression`. Runs on merge to main.

## Parallelization

Tests are sharded across 4 workers. To increase parallelism, edit the `matrix.shard` field in `test.yml`. Each shard runs in its own container with a clean database snapshot.

## Artifacts

Failed test runs upload:
- Playwright traces (`trace.zip`)
- Screenshots at point of failure
- Video recording of the test
- HTML test report

Retention is 30 days.

## Re-running failed tests

CI supports automatic retry of failed tests up to 2 times. After 2 retries, a failure is considered real and the job fails. To disable retry for a specific test, use `test.fail()` annotation.

## Environment variables

Required secrets are stored in GitHub repo settings:
- `BASE_URL` — target environment URL
- `TEST_USER_EMAIL` / `TEST_USER_PASSWORD` — seeded test account
- `STRIPE_TEST_KEY` — sandbox payment key

Never commit secrets to the repo. Use the `secrets.*` namespace in workflows.
