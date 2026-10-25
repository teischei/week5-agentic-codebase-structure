# Link Shortener Agent Guide

## Purpose

This is a small FastAPI and SQLite service that turns a long http or https URL into a short code. A client can create a link with `POST /shorten` and open it with `GET /{code}`.

## Important files

- `main.py` contains the database setup, request model, and routes
- `test_main.py` contains the starter tests
- `tests/` contains feature tests and scoped test guidance
- `docs/TASKS.md` lists the available small features
- `.agents/skills/implement-link-task/SKILL.md` contains the reusable feature workflow

## Setup and verification

Run these commands from the repository root

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m pytest -q
uvicorn main:app --reload
```

## Product boundaries

- Keep this a small link shortener with SQLite and FastAPI
- Work only on one task from `docs/TASKS.md` at a time
- Keep database access in `main.py` and use parameterized SQL
- Do not add accounts, authentication, a frontend, an ORM, background jobs, or new services
- Return clear HTTP errors for invalid input and missing resources

## Change workflow

1. Read the selected task and this guide
2. Inspect the related route and tests
3. State the expected behavior and affected files before editing
4. Add a failing behavioral test through the public API
5. Make the smallest change that makes the test pass
6. Run `python -m pytest -q`
7. Summarize the change and any remaining risk

Use the `implement-link-task` skill for a complete feature change. Do not commit or push unless the user asks.
