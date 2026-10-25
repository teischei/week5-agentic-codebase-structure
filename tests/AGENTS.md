# Test Guidance

These instructions apply only to files inside `tests/`.

- Test behavior through FastAPI `TestClient`
- Cover both a successful request and a failure or edge case
- Make each test independent and create its own data
- Use a unique alias when a test needs an unused value because `links.db` persists between test runs
- Assert status codes, response JSON, or redirect headers instead of database rows or helper functions
- Use `follow_redirects=False` when checking redirects
- Run `python -m pytest -q` after changing tests or application behavior
