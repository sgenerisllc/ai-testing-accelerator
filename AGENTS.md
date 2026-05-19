# AGENTS.md — Instructions for AI Coding Agents

This document guides AI agents (Codex, Copilot, Augment, Cursor, etc.) working on this repository.

## Core Principles

1. **Simplicity first.** Prefer readable, well-commented code over clever abstractions.
2. **Offline by default.** All demos must run without paid API keys or internet access.
3. **No hard dependencies on paid services.** OpenAI/Anthropic/etc. integrations must be optional and gated behind environment variables.
4. **Markdown polish matters.** This repo is a public showcase — every file should look professional on GitHub.
5. **No secrets, ever.** Never commit API keys, credentials, customer data, or environment files.

## When Adding New Demos

- Create a new folder under `demos/` following the `NN-demo-name/` naming convention
- Each demo folder must include:
  - `README.md` (purpose, how to run, example I/O, presentation tips)
  - Runnable code (`*.py` or `*.ts`)
  - Sample input file(s) where applicable
  - Sample expected output
- Update the main `README.md` demo overview table
- Add an entry in `docs/demo-script.md` describing live presentation flow

## Code Style

### Python
- Target Python 3.10+
- Use type hints where they improve clarity
- Standard library preferred over third-party packages
- If a third-party package is needed, add it to `requirements.txt` with a pinned minor version
- Format with `black` (line length 100)

### TypeScript / Playwright
- Use Playwright's modern locator API (`page.getByRole`, `getByTestId`, etc.)
- Prefer Playwright Test (`@playwright/test`) over raw Playwright

### Markdown
- Use ATX-style headers (`#`, `##`)
- Mermaid diagrams for architecture/flow visualizations
- Include code blocks with language hints (e.g., ` ```python`)
- Use tables for comparative information

## Optional AI Integration Pattern

When adding optional LLM features, follow this pattern:

```python
import os

def generate(prompt: str) -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        return _call_openai(prompt, api_key)
    return _mock_response(prompt)  # deterministic fallback
```

**Never** require an API key for the default demo path.

## Testing

- Add simple unit tests in a `tests/` subfolder when introducing logic
- Run with `pytest` from the repo root
- Tests must pass offline

## Documentation Updates

When modifying core demos:
- Update `README.md` if capabilities change
- Update `docs/demo-script.md` if presentation flow changes
- Update `architecture/` diagrams if system design changes

## Forbidden Patterns

- ❌ Hardcoded API keys (even fake ones)
- ❌ Real customer data or PII in fixtures
- ❌ Heavy dependencies (TensorFlow, PyTorch, full LangChain) for simple demos
- ❌ Network calls without explicit user opt-in
- ❌ Breaking the offline-default contract

## Preferred Patterns

- ✅ Deterministic mock responses for offline demos
- ✅ Environment variable gates for optional features
- ✅ Small, focused files (< 200 lines each)
- ✅ Clear example inputs and outputs in every demo
- ✅ Mermaid diagrams for architecture

## When in Doubt

Ask: **"Could a developer clone this repo, run one command, and be impressed in under 60 seconds?"**

If not, simplify.
