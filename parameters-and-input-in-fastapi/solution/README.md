# Solution: Parameters and Input in FastAPI

This directory contains the complete solution for the Parameters and
Input in FastAPI exercise.

The solution demonstrates how to handle:

- A path parameter
- A query parameter
- A request body using Pydantic
- Returning all values in a structured response

------------------------------------------------------------------------

## Files in This Directory

- bar.py → Completed FastAPI application
- test_bar.py → Unit tests (used to validate the implementation)

------------------------------------------------------------------------

## What This Solution Implements

The solution defines a POST endpoint that:

1. Accepts a path parameter
2. Accepts a query parameter
3. Accepts a JSON body with a single field
4. Returns all three values in a dictionary

------------------------------------------------------------------------

## Example Endpoint

Route structure:
```url
POST /items/{path}?query=value
```
Request body:
```json
{ "field": "example" }
```
Response:
```json
{ "path": "items_value", "query": "query_value", "body": "example" }
```
------------------------------------------------------------------------

## Key Implementation Details

### FastAPI App Initialization
```python
from fastapi import FastAPI

app = FastAPI()
```
------------------------------------------------------------------------

### Request Body Model
```python
from pydantic import BaseModel

class BodyModel(BaseModel): field: str
```
------------------------------------------------------------------------

### Endpoint Definition
```python
@app.post("/items/{path}") 
async def exercise_function(path: str, query: str, body: BodyModel): 
    return { "path": path, "query": query, "body": body.field }
```
------------------------------------------------------------------------

## Running the Application
```shell
uvicorn bar:app --reload
```
Open:
```url
http://127.0.0.1:8000/docs
```
------------------------------------------------------------------------

## Running the Tests
```shell
pytest
```
All tests in test_bar.py should pass.

------------------------------------------------------------------------

## What This Demonstrates

- FastAPI routing
- Path vs query parameters
- Request body parsing
- Pydantic validation
- Async endpoint functions
- Basic API testing with pytest

------------------------------------------------------------------------

## Final Result

You now have a minimal, fully functional FastAPI service that:

- Accepts multiple input types
- Validates input automatically
- Returns structured JSON responses
- Passes automated tests

This pattern forms the foundation for building production-grade APIs.

