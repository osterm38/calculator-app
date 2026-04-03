# CLAUDE.md

## Project Overview
<!-- TODO: Describe what this project does in 2-3 sentences -->

## Setup
```bash
uv sync
```

## Common Tasks
```bash
make test       # Run all tests
make lint       # Run ruff + mypy
make fmt        # Auto-format code
make check      # lint + test together
```

## Project Conventions
- Source lives under `src/calculator_app/`
- Tests mirror the source structure: `tests/test_<module>.py`
- All public functions must have type annotations
- Use `pyproject.toml` for all tool configuration — no separate config files

## Coding Rules for Agents
- Never use `print()` for logging — use the `logging` module
- Do not catch bare `Exception` — be specific
- Do not modify `tests/` unless explicitly asked
- Run `make lint` after any edit to source files
- Run `make test` before declaring a task complete
- Keep functions small and focused; prefer composition over inheritance

## What's Off-Limits
- Do not commit `.env` files or secrets
- Do not install packages globally — always update `pyproject.toml`
- Do not delete or overwrite `pyproject.toml` wholesale
