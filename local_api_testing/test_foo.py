from typing import Any
from fastapi.testclient import TestClient
import pytest

from foo import app

client = TestClient(app)


@pytest.mark.anyio
async def test_get_path() -> None:
    r = client.get("/items/42")
    assert r.status_code == 200
    assert r.json() == {"fetch": "Fetched 1 of 42"}


@pytest.mark.anyio
async def test_get_path_query() -> None:
    r = client.get("/items/42?count=5")
    assert r.status_code == 200
    assert r.json() == {"fetch": "Fetched 5 of 42"}


@pytest.mark.anyio
async def test_get_malformed() -> None:
    r = client.get("/items")
    assert r.status_code == 404  # More specific assertion for 404 Not Found
