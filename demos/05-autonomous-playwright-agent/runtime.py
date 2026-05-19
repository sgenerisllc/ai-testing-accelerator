"""
Mock Playwright runtime.

Simulates test execution for the agent demo. The default behaviour:
  • First iteration fails with ELEMENT_DISABLED if --force-fail is set
  • Subsequent iterations (with `repaired=True`) succeed
  • Without --force-fail, tests pass on first iteration

To run real Playwright tests, replace `mock_execute` with:
    subprocess.run(["pytest", test_file], capture_output=True)
and parse the result.
"""

from __future__ import annotations

import random
import time
from pathlib import Path

from phases import ExecutionResult


def mock_execute(
    test_file: Path,
    iteration: int,
    force_fail: bool,
    repaired: bool,
) -> ExecutionResult:
    """Pretend to run the test; return a deterministic result."""
    # Simulate the test taking some time.
    time.sleep(0.4)

    # If user asked for a failure and we haven't repaired yet, fail.
    if force_fail and not repaired:
        return ExecutionResult(
            passed=False,
            failed_step=5,
            error_type="ELEMENT_DISABLED",
            error_message="button.checkout-now is disabled",
        )

    # Without forced fail, very rarely simulate a flaky scenario on iter 1.
    if iteration == 1 and not force_fail and random.random() < 0.05:
        return ExecutionResult(
            passed=False,
            failed_step=3,
            error_type="ELEMENT_NOT_VISIBLE",
            error_message="form input not visible",
        )

    return ExecutionResult(passed=True)
