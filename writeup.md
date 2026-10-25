# Week 5 Writeup: The Link Shortener

## Root guidance AGENTS.md

I put the general information an agent needs for every task in `AGENTS.md`. It explains that this project is a small FastAPI and SQLite link shortener, identifies the important files, and gives the commands for setup, testing, and running the server. The guide gives boundaries and a workflow from planning through verification. This information should be broadly available because an agent needs it before making any change in the repository.

## Scoped instruction

I put the testing rules in `tests/AGENTS.md`. The instruction applies when an agent works on files inside the `tests` folder. It says to test through the public FastAPI API, include success and failure cases, keep tests independent, and use unique aliases because the SQLite database persists between runs. These details are useful for test work but would add extra context during other changes. Codex can read the root `AGENTS.md` for repository context and the nested test guide when it is working in tests.

## Reusable workflow

My reusable workflow is in `.agents/skills/implement-link-task/SKILL.md`. It is named `implement-link-task` and describes a repeatable way to complete one task from `docs/TASKS.md`. The workflow reads the guidance and task, plans before editing, adds a failing public API test, makes the smallest change, runs pytest, and performs a final read-only review. It also tells the agent not to commit or push without the user asking. Codex discovers project skills from the `.agents/skills` folder and can invoke this skill by its name.

## Planning and implementation

I chose the custom alias task. `POST /shorten` needed an optional alias, it needed to store that alias as the short code when available, and it needed to return a 409 response when another link already used it. The plan identified `main.py` and a new test file as the affected areas. I added tests first for a successful alias redirect, a duplicate alias, and a blank alias. They failed before implementation, then passed after I added the optional request field and the SQLite insert with a conflict response.

## Review and result

The first review returned REVISE because an alias like `docs` could be stored even though FastAPI already uses that route. An alias containing a slash would also not behave like one short code. I added a small reserved alias list, rejected slashes, and added a test for the `docs` alias. The second review returned ACCEPT because the route now gives clear responses for success, duplicate aliases, blank aliases, and reserved aliases. The final test run passed all seven tests.

## What I learned

This assignment showed me that a repository can help an agent without needing a long prompt every time. The root guide gives the agent the big picture, while the test guide only appears when the details are useful. The reusable workflow also made the plan, implementation, and review steps easier to keep separate. The review was useful because it found a real route conflict that I did not think about when I first planned the feature.
