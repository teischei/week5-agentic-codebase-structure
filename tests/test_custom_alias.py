from uuid import uuid4

from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def unique_alias():
    return f"class-{uuid4().hex[:8]}"


def test_custom_alias_creates_a_redirect():
    alias = unique_alias()
    response = client.post(
        "/shorten",
        json={"url": "https://example.com/custom", "alias": alias},
    )

    assert response.status_code == 200
    assert response.json() == {"code": alias, "short_url": f"/{alias}"}

    redirect = client.get(f"/{alias}", follow_redirects=False)
    assert redirect.status_code == 307
    assert redirect.headers["location"] == "https://example.com/custom"


def test_duplicate_custom_alias_returns_conflict():
    alias = unique_alias()
    client.post("/shorten", json={"url": "https://example.com/first", "alias": alias})

    response = client.post(
        "/shorten",
        json={"url": "https://example.com/second", "alias": alias},
    )

    assert response.status_code == 409
    assert response.json()["detail"] == "alias already in use"


def test_blank_custom_alias_is_rejected():
    response = client.post(
        "/shorten",
        json={"url": "https://example.com/blank", "alias": "   "},
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "alias must not be blank"


def test_reserved_custom_alias_is_rejected():
    response = client.post(
        "/shorten",
        json={"url": "https://example.com/docs", "alias": "docs"},
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "alias is not available"
