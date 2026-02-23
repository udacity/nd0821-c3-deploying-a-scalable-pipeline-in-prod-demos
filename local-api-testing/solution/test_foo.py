# test_foo.py

import pytest
from fastapi.testclient import TestClient
from foo import app

client = TestClient(app)


def test_get_items_default_count():
    """Test GET without query parameter (default count=1)."""
    response = client.get("/items/5")
    
    assert response.status_code == 200
    assert response.json() == {"fetch": "Fetched 1 of 5"}


def test_get_items_with_query_param():
    """Test GET with valid query parameter."""
    response = client.get("/items/5?count=3")
    
    assert response.status_code == 200
    assert response.json() == {"fetch": "Fetched 3 of 5"}


def test_get_items_invalid_path_param():
    """Test malformed URL with non-integer item_id."""
    response = client.get("/items/abc")
    
    assert response.status_code == 422  # FastAPI validation error


def test_get_items_invalid_query_param():
    """Test malformed query parameter (non-integer count)."""
    response = client.get("/items/5?count=abc")
    
    assert response.status_code == 422  # FastAPI validation error