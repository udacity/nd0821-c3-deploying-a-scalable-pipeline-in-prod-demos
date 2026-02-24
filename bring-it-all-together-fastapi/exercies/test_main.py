import pytest
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_ingest_data_success_without_issues():
    """
    Test a valid request.
    Expected:
    - status code indicates success
    - response body matches the expected output format/content
    """
    payload = {"feature_1": 0.0, "feature_2": "ok"}  # edge case: feature_1 == 0 allowed
    r = client.post("/data/", json=payload)

    # TODO: Assert success status code
    # assert r.status_code == ?

    # TODO: Assert response body
    # assert r.json() == ?


def test_ingest_data_fails_when_feature_1_negative():
    """
    Test invalid feature_1 (negative).
    Expected:
    - status code indicates client error (your choice, but must be consistent)
    - response includes a clear error message
    """
    payload = {"feature_1": -1.0, "feature_2": "ok"}
    r = client.post("/data/", json=payload)

    # TODO: Assert failure status code
    # assert r.status_code == ?

    # TODO: Assert error message (detail)
    # body = r.json()
    # assert body["detail"] == ?


def test_ingest_data_fails_when_feature_2_too_long():
    """
    Test invalid feature_2 (length > 280).
    Expected:
    - status code indicates client error
    - response includes a clear error message
    """
    payload = {"feature_1": 1.0, "feature_2": "x" * 281}
    r = client.post("/data/", json=payload)

    # TODO: Assert failure status code
    # assert r.status_code == ?

    # TODO: Assert error message (detail)
    # body = r.json()
    # assert body["detail"] == ?


def test_malformed_url_returns_error():
    """
    Test a malformed URL (endpoint does not exist).
    Expected:
    - status code indicates not found
    """
    payload = {"feature_1": 1.0, "feature_2": "ok"}
    r = client.post("/bad-url", json=payload)

    # TODO: Assert 404 (or appropriate not-found status code)
    # assert r.status_code == ?