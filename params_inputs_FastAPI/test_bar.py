from typing import Any
import pytest
from fastapi.testclient import TestClient

from bar import app

client = TestClient(app)


@pytest.mark.anyio
async def test_post() -> None:
    r = client.post("/42?query=5", json={"value": 10})
    response_data = r.json()
    assert r.status_code == 200
    assert response_data["path"] == 42
    assert response_data["query"] == 5
    assert response_data["body"] == {"value": 10}
