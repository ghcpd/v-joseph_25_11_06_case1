# DataSync Pro v2.0

A fully asynchronous data synchronization library with built-in caching.

---

## Installation

```bash
pip install aiohttp python-dotenv
```

---

## Quick Start (Corrected)

```python
import asyncio
from datasync import DataSync

async def main():
    ds = DataSync("https://api.example.com")
    content = await ds.fetch_remote("data/users")
    print(content)

if __name__ == "__main__":
    asyncio.run(main())
```

---

## Using Cache (Corrected)

```python
import asyncio
from datasync import CacheManager

async def main():
    cache = CacheManager("cache")
    await cache.store("users", "{'id': 1}")
    data = await cache.get("users")
    print(data)

if __name__ == "__main__":
    asyncio.run(main())
```

---

## Advanced Example (Corrected)

```python
import asyncio
from datasync import DataSync
from dotenv import load_dotenv
import os

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://api.example.com")

async def main():
    ds = DataSync(BASE_URL)
    mapping = {
        "data/users": "output/users.json",
        "data/info": "output/info.json"
    }
    results = await ds.sync_all(mapping)
    print("Synchronized files:", results)

if __name__ == "__main__":
    asyncio.run(main())
```

---

## Expected Output

```
Synchronized files: ['output/users.json', 'output/info.json']
```
