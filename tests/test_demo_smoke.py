from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run_demo(relative_dir: str, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, *args],
        cwd=ROOT / relative_dir,
        text=True,
        capture_output=True,
        check=True,
    )


def test_prompt_to_test_generator_runs_offline() -> None:
    result = run_demo(
        "demos/01-prompt-to-test-generator",
        "generator.py",
        "test user login with valid credentials",
    )

    assert "from playwright.sync_api import Page, expect" in result.stdout
    assert "get_by_label(\"Email\")" in result.stdout


def test_failure_analyzer_classifies_sample_log() -> None:
    result = run_demo(
        "demos/02-ai-failure-analyzer",
        "analyzer.py",
        "sample-failure.log",
    )

    assert "Failure Type:   ELEMENT_DISABLED" in result.stdout
    assert "Confidence:     92%" in result.stdout


def test_self_healing_locator_demo_runs() -> None:
    result = run_demo("demos/03-self-healing-locators", "heal.py")

    assert "Final strategy:       ROLE_NAME" in result.stdout


def test_rag_assistant_returns_cited_answer() -> None:
    result = run_demo(
        "demos/04-rag-qa-assistant",
        "rag.py",
        "How do I run tests locally?",
    )

    assert "Sources:" in result.stdout
    assert "knowledge_base/onboarding.md" in result.stdout


def test_autonomous_agent_repair_loop_runs_offline() -> None:
    result = run_demo(
        "demos/05-autonomous-playwright-agent",
        "agent.py",
        "--intent",
        "verify checkout flow",
        "--force-fail",
    )

    assert "Self-repaired:   Yes" in result.stdout
