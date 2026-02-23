import json
from typing import Any

import pytest
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


@pytest.mark.anyio
async def test_post_data_success() -> None:
    data = {"feature_1": 1, "feature_2": "test string"}
    r = client.post("/data/", json=data)  # Using json parameter instead of manual dumps
    assert r.status_code == 200
    response_data = r.json()
    assert response_data["feature_1"] == data["feature_1"]
    assert response_data["feature_2"] == data["feature_2"]


@pytest.mark.anyio
async def test_post_data_fail() -> None:
    data = {"feature_1": -5, "feature_2": "test string"}
    r = client.post("/data/", json=data)
    assert r.status_code == 422  # Pydantic validation error status code
