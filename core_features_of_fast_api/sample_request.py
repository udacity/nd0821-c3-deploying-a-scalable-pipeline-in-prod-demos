import requests
import json

import httpx
from typing import TypedDict

class Item(TypedDict):
    name: str
    tags: list[str]  # Updated for Python 3.13 style
    item_id: int

# Define data globally so it can be used in both async and sync code
data: Item = {
    "name": "My Item",
    "tags": ["tag1", "tag2"],
    "item_id": 42
}

async def main() -> None:

    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://127.0.0.1:8000/items/",
            json=data,  # httpx will handle JSON serialization
        )
        print(response.json())

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())

    # Also demonstrate synchronous requests
    r = requests.post("http://127.0.0.1:8000/items/", data=json.dumps(data))
    print(r.json())
