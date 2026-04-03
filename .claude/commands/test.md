Use the `tester` agent to run the test suite and fix any failures.

The tester agent will:
1. Run `make test`
2. Diagnose any failures
3. Fix source code (never test files) until all tests pass
4. Run `make lint` to confirm no new issues

Report the final test status and a summary of any changes made.
