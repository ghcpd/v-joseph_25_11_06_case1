# DataSync Pro v2.0 — Corrected Tutorial

## Installation

```bash
pip install -r requirements.txt
```

## Quick Start

Correct usage (API exposes DataSync class — methods are async):

```python
import asyncio
from datasync import DataSync

async def main():
    ds = DataSync("https://api.example.com")
    data = await ds.fetch_remote("/data/users")
    print(data)

asyncio.run(main())
```

## Using Cache

CacheManager methods are asynchronous; await them:

```python
import asyncio
from datasync import CacheManager

async def main():
    cache = CacheManager()
    await cache.store("users", "{'id': 1}")
    print(await cache.get("users"))

asyncio.run(main())
```

## Advanced Example

```python
import asyncio
from datasync import DataSync

async def main():
    ds = DataSync("https://api.example.com")
    result = await ds.sync_all({
        "data/users": "output/users.json",
        "data/info": "output/info.json"
    })
    print(result)

asyncio.run(main())
```

Expected Output:
```
['output/users.json', 'output/info.json']
```

## Environment Variables

The package currently does not auto-load a .env or `BASE_URL`; set it in code or use python-dotenv yourself:

```python
from dotenv import load_dotenv
import os

load_dotenv()
base = os.getenv('BASE_URL', 'https://api.example.com')
```