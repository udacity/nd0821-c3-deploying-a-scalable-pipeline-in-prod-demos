import requests
import json

import httpx
from typing import TypedDict, List

class Item(TypedDict):
    name: str
    tags: List[str]
    item_id: int

async def main() -> None:
    data: Item = {
        "name": "My Item",
        "tags": ["tag1", "tag2"],
        "item_id": 42
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://127.0.0.1:8000/items/",
            json=data,  # httpx will handle JSON serialization
        )
        print(response.json())

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())

r = requests.post("http://127.0.0.1:8000/items/", data=json.dumps(data))

print(r.json())
