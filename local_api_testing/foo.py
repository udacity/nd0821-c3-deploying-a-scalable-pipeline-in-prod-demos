from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
    title="Sample API",
    description="A simple API demonstrating path and query parameters",
    version="1.0.0",
    openapi_version="3.1.0"
)

class FetchResponse(BaseModel):
    fetch: str = Field(description="A message indicating what was fetched")

    model_config = {
        "json_schema_extra": {
            "examples": [
                {"fetch": "Fetched 1 of 42"}
            ]
        }
    }

@app.get("/items/{item_id}", response_model=FetchResponse)
async def get_items(
    item_id: int = Field(..., description="The ID of the item to fetch"),
    count: int = Field(1, ge=1, description="Number of items to fetch")
) -> FetchResponse:
    return FetchResponse(fetch=f"Fetched {count} of {item_id}")
