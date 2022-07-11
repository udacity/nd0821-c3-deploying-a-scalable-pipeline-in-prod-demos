from typing import Union, List
from fastapi import FastAPI, HTTPException

from pydantic import BaseModel


class Data(BaseModel):
    feature_1: float
    feature_2: str


app = FastAPI(
    title="Exercise API",
    description="An API that demonstrates checking the values of your inputs.",
    version="1.0.0",
)


@app.post("/data/")
async def ingest_data(data: Data):
    if data.feature_1 < 0:
        raise HTTPException(status_code=400, detail="feature_1 needs to be above 0.")
    if len(data.feature_2) > 280:
        raise HTTPException(
            status_code=400,
            detail=f"feature_2 needs to be less than 281 characters. It has {len(data.feature_2)}.",
        )
    return data
