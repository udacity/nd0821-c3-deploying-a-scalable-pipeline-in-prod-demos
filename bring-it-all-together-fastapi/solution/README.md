# Solution: Bringing It All Together ✅

## Overview

This solution demonstrates a complete FastAPI application that:

- Defines a Pydantic request body model
- Implements a `POST /ingest_data` endpoint
- Validates business logic using `HTTPException`
- Includes API metadata (title, description, version)
- Uses FastAPI's `TestClient` to verify correct behavior

The solution follows defensive API design principles suitable for protecting a machine learning model from invalid input.

------------------------------------------------------------------------

## What This Solution Implements

### 1️⃣ Request Model

``` python
class Data(BaseModel):
    feature_1: float
    feature_2: str
```

FastAPI automatically handles:

- Required fields
- Type validation
- Schema validation errors (422)

------------------------------------------------------------------------

### 2️⃣ Business Logic Validation

The endpoint performs additional validation:

- `feature_1` must be non-negative
- `feature_2` must be 280 characters or fewer

If validation fails, the API raises:

``` python
raise HTTPException(status_code=400, detail="Clear error message")
```

### Why 400?

- 422 → Schema/type validation (handled by FastAPI)
- 400 → Business rule validation failure

This separation ensures clear and meaningful error handling.

------------------------------------------------------------------------

## API Metadata

The FastAPI app includes:

``` python
app = FastAPI(
    title="ML Data Ingestion API",
    description="Validates input data before sending it to a machine learning model.",
    version="1.0.0"
)
```

This enhances:

- Swagger documentation
- OpenAPI schema clarity
- API maintainability

View documentation at:

http://127.0.0.1:8000/docs

------------------------------------------------------------------------

## Running the Application

Start the server:

``` bash
uvicorn main:app --reload
```

Test manually:

``` bash
curl -X POST "http://127.0.0.1:8000/ingest_data" -H "Content-Type: application/json" -d '{"feature_1": 5.0, "feature_2": "valid input"}'
```

------------------------------------------------------------------------

## Running the Tests

Automated tests are included using `TestClient`.

Run:

``` bash
pytest
```

The tests verify:

- Valid input returns 200
- Negative `feature_1` returns 400
- `feature_2` over 280 characters returns 400
- Incorrect types return 422

------------------------------------------------------------------------

## Expected Status Code Summary

  Scenario                 Status Code
  ------------------------ -------------
  Valid input              200
  feature_1 \< 0           400
  feature_2 \> 280 chars   400
  Wrong types              422

------------------------------------------------------------------------

## Key Concepts Demonstrated

- Pydantic request models
- Manual validation with `HTTPException`
- Proper error status code usage
- API metadata configuration
- Automated API testing
- Defensive programming for ML pipelines

------------------------------------------------------------------------

## Production Insight

In real-world ML systems:

- Invalid input must be rejected immediately
- Clear error messages reduce debugging time
- Schema validation and business validation must be sarated
- Tests must cover both success and failure paths

This solution follows those principles.

------------------------------------------------------------------------

## Optional Enhancements

- Add structured JSON error responses
- Add logging for validation failures
- Expand validation rules
- Integrate with a mock ML model
- Add CI pipeline for automated test runs

