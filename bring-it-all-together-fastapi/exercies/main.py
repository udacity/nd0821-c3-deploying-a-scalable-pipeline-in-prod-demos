from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class Data(BaseModel):
    feature_1: float
    feature_2: str


# TODO: Add API metadata (name/title, brief description, version)
# Hints:
# - FastAPI(title="...", description="...", version="...")
app = FastAPI(
    # title="TODO",
    # description="TODO",
    # version="TODO",
)


@app.post("/data/")
async def ingest_data(data: Data):
    """
    POST method that ingests data for a (hypothetical) ML model.

    Requirements:
    - feature_1 must be non-negative (>= 0)
    - feature_2 must be 280 characters or less
    - If validation fails, raise HTTPException with an appropriate status code
      and a clear message describing the issue.
    """

    # TODO: Validate feature_1
    # if data.feature_1 < 0:
    #     raise HTTPException(status_code=..., detail="...")

    # TODO: Validate feature_2 length
    # if len(data.feature_2) > 280:
    #     raise HTTPException(status_code=..., detail="...")

    # TODO: Return a response (could be the input data, or a message, etc.)
    return {
        # "TODO": "..."
    }