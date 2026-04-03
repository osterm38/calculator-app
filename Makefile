.PHONY: test lint fmt check install clean

install:
	uv sync --all-extras

test:
	uv run pytest tests/ -v

lint:
	uv run ruff check src/ tests/
	uv run ty check src/ 

fmt:
	uv run ruff format src/ tests/
	uv run ruff check --fix src/ tests/
	uv run ty check --fix src/

check: lint test

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -name "*.pyc" -delete
