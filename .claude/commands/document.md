Use the `documenter` agent to audit and improve documentation across the codebase.

If a specific file or function was mentioned, focus there first. Otherwise, do a full audit of `src/`.

The documenter agent will:
1. Find all public functions/classes missing docstrings or type annotations
2. Add or update them using Google-style docstrings
3. Run `make lint` to verify
4. Report everything it changed
