from typing import Annotated
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, ConfigDict


class Data(BaseModel):
    model_config = ConfigDict(json_schema_extra={
        "examples": [
            {
                "feature_1": 42.0,
                "feature_2": "sample text"
            }
        ]
    })
    
    feature_1: Annotated[float, Field(gt=0, description="Must be a positive number")]
    feature_2: Annotated[str, Field(max_length=280, description="Text field limited to 280 characters")]


app = FastAPI(
    title="Exercise API",
    description="An API that demonstrates checking the values of your inputs.",
    version="1.0.0",
    openapi_version="3.1.0",
)


@app.post("/data/", response_model=Data)
async def ingest_data(data: Data) -> Data:
    # Validation happens automatically through Pydantic
    # Additional business logic can be added here if needed
    return data
