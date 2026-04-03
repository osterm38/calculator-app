Run `make lint` and report the results.

If the output is clean, say so and stop — do not spawn an agent.

If there are errors:
- Ruff errors that weren't auto-fixed: show the file, line, and rule with a one-line explanation
- ty type errors: use the `linter` agent to read the affected files and fix them manually

Do not silently pass if `make lint` exits non-zero.
