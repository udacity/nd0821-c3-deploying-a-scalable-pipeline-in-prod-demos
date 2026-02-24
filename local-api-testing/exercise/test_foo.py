# test_foo.py

import pytest
from fastapi.testclient import TestClient
from foo import app

client = TestClient(app)


def test_get_items_default_count():
    """
    Test the GET endpoint without providing the query parameter.
    
    Expected:
    - Status code should indicate success.
    - The default value of `count` should be used.
    """
    response = client.get("/items/5")

    # TODO: Assert the correct status code
    # assert response.status_code == ?

    # TODO: Assert the correct JSON response
    # assert response.json() == ?


def test_get_items_with_query_param():
    """
    Test the GET endpoint with a valid query parameter.
    
    Expected:
    - Status code should indicate success.
    - Response should reflect the provided `count` value.
    """
    response = client.get("/items/5?count=3")

    # TODO: Assert the correct status code

    # TODO: Assert the correct JSON response


def test_get_items_invalid_path_param():
    """
    Test the endpoint with a malformed path parameter
    (e.g., non-integer item_id).
    
    Expected:
    - Validation error should occur.
    """
    response = client.get("/items/abc")

    # TODO: Assert the correct error status code


def test_get_items_invalid_query_param():
    """
    Test the endpoint with an invalid query parameter
    (e.g., non-integer count).
    
    Expected:
    - Validation error should occur.
    """
    response = client.get("/items/5?count=abc")

    # TODO: Assert the correct error status code