# CLAUDE.md

## Project Overview
A Python arithmetic calculator library with a Flask-based web GUI. The core
module (`calculator_app.calculator`) exposes individual arithmetic functions;
the web module (`calculator_app.web`) wraps them in a REST API served
alongside a self-contained single-page UI.

## Modules
| Module | Description |
|---|---|
| `calculator_app.calculator` | Pure arithmetic functions: `add`, `subtract`, `multiply`, `divide`, `power`, `sqrt` |
| `calculator_app.web` | Flask app with `GET /` (UI) and `POST /calculate` (JSON API) |

## Running the Web Server
```bash
# Development server (default: http://127.0.0.1:5000)
uv run calculator-web

# Custom host/port via environment variables
HOST=0.0.0.0 PORT=8080 uv run calculator-web
```

## POST /calculate API
```
POST /calculate
Content-Type: application/json

{"expression": "3+4"}

# Success → 200
{"result": 7.0}

# Error → 400
{"error": "Division by zero"}
```

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
