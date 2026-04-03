Use the `pr-creator` agent to commit, push, and open a pull request for the current branch.

Before delegating, confirm:
- `make check` passes (run it if not recently verified)
- We are NOT on `main` or `master`

The pr-creator agent will:
1. Review the full diff
2. Stage and commit with a Conventional Commits message
3. Push the branch
4. Open a PR via `gh pr create` with a structured description
5. Return the PR URL
