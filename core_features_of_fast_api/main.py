from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

class TaggedItem(BaseModel):
    name: str
    tags: Union[str, list[str]]  # Updated for Python 3.13 style
    item_id: int
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Example Item",
                    "tags": ["example", "test"],
                    "item_id": 1
                }
            ]
        }
    }

app = FastAPI()

@app.post("/items/", response_model=TaggedItem)
async def create_item(item: TaggedItem) -> TaggedItem:
    return item

@app.get("/items/{item_id}")
async def get_items(item_id: int, count: int = 1) -> dict[str, str]:
    return {"fetch": f"Fetched {count} of {item_id}"}
