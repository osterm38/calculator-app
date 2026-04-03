Use the `orchestrator` agent to take a feature request all the way from idea to pull request.

Pass along any feature description the user provided. The orchestrator will:

1. **Plan** — restate the feature and list what will be built; wait for your approval
2. **Branch** — create a `feature/...` branch
3. **Implement** — delegate to `feature-builder`
4. **Test** — delegate to `tester` to write and pass tests
5. **Lint** — delegate to `linter` to clean up
6. **Document** — delegate to `documenter` for docstrings
7. **Verify** — run `make check` end-to-end
8. **PR** — delegate to `pr-creator` to commit, push, and open the PR

You will be asked to approve the plan in Phase 1 before any code is written.
