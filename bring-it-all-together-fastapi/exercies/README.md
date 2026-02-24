# Exercise: Bringing It All Together 🚀

## Overview

In this exercise, you will combine everything you have learned about:

- FastAPI endpoints
- Request body validation
- Raising `HTTPException`
- API metadata
- Testing with FastAPI's `TestClient`

Your goal is to build a production-style API that validates data before it is passed to a machine learning model.

------------------------------------------------------------------------

## Your Task

Implement a FastAPI application that:

1. Defines a `POST` endpoint called `/ingest_data`
2. Accepts the following request body:

``` python
from pydantic import BaseModel

class Data(BaseModel):
    feature_1: float
    feature_2: str
```

3. Validates the input data:
    - `feature_1` must be non-negative
    - `feature_2` must contain 280 characters or fewer
4. Raises an appropriate `HTTPException` if validation fails
5. Includes API metadata (title, description, version)
6. Uses FastAPI's `TestClient` to verify failure cases

------------------------------------------------------------------------

## Project Files

Your workspace includes:

- `main.py` → Implement your FastAPI application here
- `test_main.py` → Write tests to verify behavior

------------------------------------------------------------------------

## Implementation Requirements

### 1️⃣ Define the Request Model

Create a `Data` model using Pydantic.

FastAPI will automatically validate: - Data types - Required fields

Invalid types should return `422` (handled automatically).

------------------------------------------------------------------------

### 2️⃣ Implement Business Logic Validation

Inside your `/ingest_data` endpoint:

- Check that `feature_1 >= 0`
- Check that `len(feature_2) <= 280`

If validation fails, raise:

``` python
from fastapi import HTTPException

raise HTTPException(status_code=400, detail="Meaningful error message")
```

Use:

- `400` for business logic validation errors
- `422` for schema/type errors (handled by FastAPI automatically)

------------------------------------------------------------------------

### 3️⃣ Add API Metadata

When creating the FastAPI app, include:

``` python
app = FastAPI(
    title="Your API Name",
    description="Brief description of what your API does.",
    version="1.0.0"
)
```

Verify metadata by visiting:

http://127.0.0.1:8000/docs

------------------------------------------------------------------------

### 4️⃣ Write Tests

Use `TestClient` to verify:

- Valid input returns `200`
- Negative `feature_1` returns `400`
- Overlong `feature_2` returns `400`
- Invalid types return `422`

Run tests with:

``` bash
pytest
```

------------------------------------------------------------------------

## Running the API

Start the server:

``` bash
uvicorn main:app --reload
```

Test manually using curl:

``` bash
curl -X POST "http://127.0.0.1:8000/ingest_data" -H "Content-Type: application/json" -d '{"feature_1": 10.5, "feature_2": "valid input"}'
```

------------------------------------------------------------------------

## Expected Behavior

  Scenario                 Expected Status
  ------------------------ --------------------------
  Valid input              200 OK
  feature_1 \< 0           400 Bad Request
  feature_2 \> 280 chars   400 Bad Request
  Wrong types              422 Unprocessable Entity

------------------------------------------------------------------------

## Helpful Resources

FastAPI Error Handling\
https://fastapi.tiangolo.com/tutorial/handling-errors/

FastAPI Metadata\
https://fastapi.tiangolo.com/tutorial/metadata/

------------------------------------------------------------------------

## What You Are Demonstrating 🎯

- Defensive API design
- Clear and meaningful error handling
- Proper separation of schema validation vs business vidation
- Automated API testing
- Clean, documented FastAPI configuration

