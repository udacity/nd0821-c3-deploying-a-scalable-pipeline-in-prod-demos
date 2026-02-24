# bar.py

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Value(BaseModel):
    value: int

# Use POST action to send data to the server
@app.post(...)
async def exercise_function(...):
    return {"path": path, "query": query, "body": body}
