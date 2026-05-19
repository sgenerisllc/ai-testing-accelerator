"""
Failure pattern definitions for the AI Failure Analyzer.

Each pattern is a deterministic classifier that examines a raw log
and returns a structured root-cause analysis. The patterns are
ordered by specificity: more specific patterns are matched first.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Analysis:
    failure_type: str
    severity: str  # LOW | MEDIUM | HIGH | CRITICAL
    confidence: int  # 0-100
    root_cause: str
    likely_causes: list[tuple[str, str]] = field(default_factory=list)  # (severity, description)
    suggested_fix: str = ""
    fix_snippet: str = ""
    test_location: str = "unknown"


def _extract_test_location(log: str) -> str:
    """Heuristically pull the failing 'file:line' from the log.

    Prefers locations near failure markers (✗, FAIL, Error, 'failed').
    Falls back to the last match in the log (failures usually come last).
    """
    import re

    pattern = re.compile(r"([\w./-]+\.(?:spec|test)\.(?:ts|js|py)):(\d+)")
    failure_markers = ("✗", "FAIL", "TimeoutError", "Error:", "failed")

    # Prefer matches that appear after a failure marker
    for marker in failure_markers:
        idx = log.find(marker)
        if idx != -1:
            match = pattern.search(log, idx)
            if match:
                return f"{match.group(1)}:{match.group(2)}"

    # Fall back to the last match in the log
    matches = pattern.findall(log)
    if matches:
        file_, line = matches[-1]
        return f"{file_}:{line}"
    return "unknown"


def analyze_element_disabled(log: str) -> Analysis | None:
    if "TimeoutError" in log and "element is not enabled" in log:
        return Analysis(
            failure_type="ELEMENT_DISABLED",
            severity="HIGH",
            confidence=92,
            test_location=_extract_test_location(log),
            root_cause=(
                "The target element is rendered but disabled when the click "
                "occurs. This typically means form validation has not passed "
                "or required state (e.g., cart contents, address selection) "
                "is missing."
            ),
            likely_causes=[
                ("HIGH", "Required form fields not filled before click"),
                ("MEDIUM", "Cart/state not loaded — race condition"),
                ("LOW", "Backend validation API returned an error"),
            ],
            suggested_fix=(
                "Wait for the element to be enabled before clicking, "
                "and assert any prerequisite state explicitly."
            ),
            fix_snippet=(
                "await expect(page.locator('button.checkout-now'))\n"
                "    .toBeEnabled({ timeout: 10000 });\n"
                "await page.click('button.checkout-now');"
            ),
        )
    return None


def analyze_element_not_visible(log: str) -> Analysis | None:
    if "TimeoutError" in log and ("not visible" in log or "waiting for element to be visible" in log):
        return Analysis(
            failure_type="ELEMENT_NOT_VISIBLE",
            severity="HIGH",
            confidence=88,
            test_location=_extract_test_location(log),
            root_cause=(
                "The element exists in the DOM but is not visible. "
                "Common causes: late render, modal overlay, off-screen position."
            ),
            likely_causes=[
                ("HIGH", "Element rendered after expected wait window"),
                ("MEDIUM", "A modal or overlay is covering the element"),
                ("LOW", "Element is scrolled out of viewport"),
            ],
            suggested_fix="Use explicit visibility wait and scroll-into-view.",
            fix_snippet=(
                "await page.locator('selector').scrollIntoViewIfNeeded();\n"
                "await expect(page.locator('selector')).toBeVisible();"
            ),
        )
    return None


def analyze_strict_mode_violation(log: str) -> Analysis | None:
    if "strict mode violation" in log.lower():
        return Analysis(
            failure_type="LOCATOR_AMBIGUOUS",
            severity="MEDIUM",
            confidence=95,
            test_location=_extract_test_location(log),
            root_cause="The locator matched more than one element.",
            likely_causes=[
                ("HIGH", "Selector too generic"),
                ("MEDIUM", "Duplicate components on the page"),
            ],
            suggested_fix="Use a more specific locator (test-id, role+name, or .nth()).",
            fix_snippet="page.get_by_role('button', name='Submit', exact=True)",
        )
    return None


def analyze_network_error(log: str) -> Analysis | None:
    if "net::ERR_" in log or "Connection refused" in log or "ECONNREFUSED" in log:
        return Analysis(
            failure_type="NETWORK_ERROR",
            severity="CRITICAL",
            confidence=90,
            test_location=_extract_test_location(log),
            root_cause="A network request failed during the test run.",
            likely_causes=[
                ("CRITICAL", "Backend service is down"),
                ("HIGH", "API endpoint URL misconfigured"),
                ("MEDIUM", "DNS/CDN issue"),
            ],
            suggested_fix="Verify service health and environment URLs.",
            fix_snippet="# Add a pre-test health check:\n# requests.get(BASE_URL + '/health').raise_for_status()",
        )
    return None


def analyze_assertion_failure(log: str) -> Analysis | None:
    if "expect(" in log and ("Expected:" in log or "Received:" in log):
        return Analysis(
            failure_type="ASSERTION_MISMATCH",
            severity="MEDIUM",
            confidence=80,
            test_location=_extract_test_location(log),
            root_cause="An assertion's expected value did not match the actual value.",
            likely_causes=[
                ("HIGH", "Fixture data drifted from expectations"),
                ("MEDIUM", "Backend behavior changed"),
                ("LOW", "Test assertion is too brittle"),
            ],
            suggested_fix="Review fixtures and use more resilient assertions.",
            fix_snippet="expect(value).toContain('partial match')",
        )
    return None


PATTERN_FUNCTIONS = [
    analyze_element_disabled,
    analyze_element_not_visible,
    analyze_strict_mode_violation,
    analyze_network_error,
    analyze_assertion_failure,
]


def classify(log: str) -> Analysis:
    """Run all patterns; return the first match or a generic fallback."""
    for fn in PATTERN_FUNCTIONS:
        result = fn(log)
        if result is not None:
            return result

    return Analysis(
        failure_type="UNKNOWN",
        severity="MEDIUM",
        confidence=40,
        test_location=_extract_test_location(log),
        root_cause="The failure does not match a known pattern. Manual review needed.",
        likely_causes=[("MEDIUM", "Novel failure mode — escalate to senior engineer")],
        suggested_fix="Inspect the log manually and add a pattern if recurring.",
    )
