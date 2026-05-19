"""
Autonomous Playwright Agent CLI.

Runs a four-phase agent loop:
    perceive → plan → act → reflect → (repeat)

Usage:
    python agent.py --intent "verify checkout flow"
    python agent.py --intent "test user login" --force-fail
    python agent.py --intent "test signup" --verbose
"""

from __future__ import annotations

import argparse
import sys
import time
from datetime import datetime
from pathlib import Path

from phases import (
    ExecutionResult,
    Perception,
    Reflection,
    TestPlan,
    generate_test_code,
    perceive,
    plan,
    reflect,
)
from runtime import mock_execute

MAX_ITERATIONS = 3
GENERATED_DIR = Path(__file__).parent / "generated"


def _box(title: str, lines: list[str]) -> str:
    width = 62
    out = [f"┌─ {title} ".ljust(width, "─")]
    out.extend(f"│ {line}" for line in lines)
    out.append("└" + "─" * (width - 1))
    return "\n".join(out)


def _print_perceive(p: Perception) -> None:
    print(_box(
        "PERCEIVE",
        [
            "Parsing intent...",
            f"✓ Detected domain: {p.domain}",
            f"✓ Required actions: {' → '.join(p.actions)}",
            f"✓ Confidence: {p.confidence}%",
        ],
    ))


def _print_plan(test_plan: TestPlan) -> None:
    lines = ["Generating test plan..."]
    for i, step in enumerate(test_plan.steps, start=1):
        lines.append(f"✓ Step {i}: {step}")
    print(_box("PLAN", lines))


def _print_act(iteration: int, test_file: Path, result: ExecutionResult) -> None:
    lines = [
        f"✓ Generated test file: generated/{test_file.name}",
        "✓ Executing test...",
    ]
    if result.passed:
        lines.append(f"✓ PASSED — all steps green")
    else:
        lines.append(
            f"✗ FAILED: Step {result.failed_step} — {result.error_message}"
        )
    print(_box(f"ACT (iteration {iteration})", lines))


def _print_reflect(reflection: Reflection) -> None:
    print(_box(
        "REFLECT",
        [
            "Analyzing failure...",
            f"✓ Root cause: {reflection.root_cause}",
            f"✓ Confidence: {reflection.confidence}%",
            f"✓ Repair strategy: {reflection.repair_strategy}",
        ],
    ))


def run_agent(intent: str, force_fail: bool, verbose: bool) -> int:
    GENERATED_DIR.mkdir(exist_ok=True)
    start = time.perf_counter()

    print("🤖 AUTONOMOUS PLAYWRIGHT AGENT")
    print("═" * 62)
    print(f"Intent:   {intent}")
    print(f"Started:  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    # Phase 1: Perceive
    perception = perceive(intent)
    _print_perceive(perception)
    print()

    # Phase 2: Plan
    test_plan = plan(perception)
    _print_plan(test_plan)
    print()

    repaired = False
    repairs_applied = 0
    for iteration in range(1, MAX_ITERATIONS + 1):
        # Phase 3: Act
        test_code = generate_test_code(test_plan, intent, repaired=repaired)
        test_file = GENERATED_DIR / f"test_{test_plan.name}.py"
        test_file.write_text(test_code)

        result = mock_execute(
            test_file=test_file,
            iteration=iteration,
            force_fail=force_fail,
            repaired=repaired,
        )
        _print_act(iteration, test_file, result)
        print()

        if result.passed:
            elapsed = time.perf_counter() - start
            print(f"🎉 Mission accomplished in {iteration} iteration(s).")
            print(f"   • Test file:       generated/{test_file.name}")
            print(f"   • Total time:      {elapsed:.1f}s")
            print(f"   • Self-repaired:   {'Yes' if repairs_applied else 'No'}"
                  f"{f' ({repairs_applied} repair applied)' if repairs_applied else ''}")
            return 0

        # Phase 4: Reflect
        reflection = reflect(result)
        _print_reflect(reflection)
        print()

        if reflection.confidence < 50:
            print("⚠️  Confidence too low to auto-repair. Escalating to human.")
            return 2

        repaired = True
        repairs_applied += 1

    print(f"💥 Exhausted {MAX_ITERATIONS} iterations without success. Escalating.")
    return 1


def main() -> int:
    parser = argparse.ArgumentParser(description="Autonomous Playwright testing agent.")
    parser.add_argument("--intent", required=True, help="Plain English testing intent")
    parser.add_argument("--force-fail", action="store_true",
                        help="Force the first iteration to fail (demo the repair loop)")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose internal logging")
    args = parser.parse_args()
    return run_agent(args.intent, args.force_fail, args.verbose)


if __name__ == "__main__":
    sys.exit(main())
