from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Value(BaseModel):
    value: int = Field(..., description="An integer value")
    
    model_config = {
        "json_schema_extra": {
            "examples": [{"value": 42}]
        }
    }


@app.post("/{path}", response_model=dict[str, int | Value])
async def exercise_function(
    path: int,
    query: int,
    body: Value
) -> dict[str, int | Value]:
    return {"path": path, "query": query, "body": body}
