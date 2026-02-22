# Exercise: Parameters and Input in FastAPI

In this exercise, you will create a simple FastAPI application that
handles:

- One path parameter
- One query parameter
- One request body field

Your endpoint should return all three values in a dictionary.

------------------------------------------------------------------------

## Objective

Write a FastAPI app that:

1. Defines a POST endpoint
2. Accepts:
    - A path parameter
    - A query parameter
    - A JSON body with a single field
3. Returns:
```json
{ "path": "...", "query": "...", "body": "..." }
```
------------------------------------------------------------------------

## Provided Files

- bar.py → Main FastAPI application (you will modify this)
- test_bar.py → Unit tests (do not modify)

------------------------------------------------------------------------

## Step 1 --- Create the FastAPI App

In bar.py:

- Import FastAPI
- Create an app = FastAPI() instance

------------------------------------------------------------------------

## Step 2 --- Define the POST Endpoint

Your function must:

- Use @app.post(...)
- Accept:
    - A path parameter
    - A query parameter
    - A request body

Example structure (fill in the missing pieces):
```python
@app.post("/items/{path}") 
async def exercise_function(path: str, query: str, body: BodyModel): 
    return {"path": path, "query": query, "body": body.field}
```
------------------------------------------------------------------------

## Step 3 --- Define the Request Body

Use Pydantic to define a request body model with one field.

Example:
```python
from pydantic import BaseModel

class BodyModel(BaseModel): field: str
```
------------------------------------------------------------------------

## Step 4 --- Run the App

Start the server:
```python
uvicorn bar:app --reload
```
Open:
```
http://127.0.0.1:8000/docs
```
Use Swagger UI to test your endpoint.

------------------------------------------------------------------------

## Step 5 --- Run Tests
```shell
pytest
```
All tests in test_bar.py should pass.

------------------------------------------------------------------------

## Example Request

POST:
```url
/items/hello?query=world
```
Body:
```json
{ "field": "fastapi" }
```
Expected response:
```json
{ "path": "hello", "query": "world", "body": "fastapi" }
```
------------------------------------------------------------------------

## Key Concepts

- Path parameters → defined in the route
- Query parameters → function arguments
- Request body → Pydantic model
- FastAPI auto-generates documentation
- Async function definition

------------------------------------------------------------------------

## Goal

After completing this exercise, you should understand:

- How FastAPI parses different types of inputs
- How Pydantic validates request bodies
- How to structure a minimal FastAPI service
- How to test FastAPI endpoints

Happy coding!

