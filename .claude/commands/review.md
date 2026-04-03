Use the `reviewer` agent to review the current git diff (staged + unstaged changes).

Run:
```bash
git diff HEAD
```

Pass the output to the reviewer agent and ask it to evaluate the changes for correctness, safety, and style issues before commit.
