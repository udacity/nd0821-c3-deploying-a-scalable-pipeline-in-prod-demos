from typing import Union, List
from fastapi import FastAPI
from pydantic import BaseModel

class TaggedItem(BaseModel):
    name: str
    tags: Union[str, List[str]]
    item_id: int

app = FastAPI()

@app.post("/items/")
async def create_item(item: TaggedItem):
    return item

@app.get("/items/{item_id}")
async def get_items(item_id: int, count: int = 1):
    return {"fetch": f"Fetched {count} of {item_id}"}
