---
name: implement-link-task
description: Implement one small Link Shortener task with a plan, public API tests, verification, and a final review.
---

# Implement Link Task

Use this workflow when completing one task from `docs/TASKS.md`.

1. Read `AGENTS.md`, the selected task, the related route, and the related tests
2. Explain the expected behavior and files that need to change without editing
3. Add a failing test through the public HTTP API and include success plus failure coverage
4. Make the smallest implementation change that satisfies the test
5. Run `python -m pytest -q`
6. Review the final diff without editing and answer `ACCEPT` or `REVISE` with a short reason
7. Summarize the implementation and any remaining risk

Do not commit, push, add new dependencies, or expand beyond the selected task unless the user asks.
