# DataSync Pro v2.0 — Corrected Tutorial Examples

This file contains corrected, working examples that match the actual API in the `datasync` package in this repository.

## Install

Use the included `requirements.txt` to install required libs in your virtualenv:

```bash
pip install -r requirements.txt
```

---

## Quick Start (corrected)

This library exposes `DataSync` as an async class; there is no top-level `fetch_remote` function.

```python
from datasync import DataSync
import asyncio

# Provide a base URL (or set using environment in your own code)
sync = DataSync("http://localhost:8000")

# Use asyncio to call the async method
data = asyncio.run(sync.fetch_remote("/data/users"))
print(data)
```

---

## Using Cache (corrected)

`CacheManager` requires a `cache_dir` and exposes async `store`/`get` methods:

```python
from datasync import CacheManager
import asyncio

cache = CacheManager("cache")

async def example():
    await cache.store("users", "{'id': 1}")
    print(await cache.get("users"))

asyncio.run(example())
```

---

## Advanced Example (corrected)

`DataSync.sync_all` is also async. Example shows how to use it with a simple HTTP server that serves sample files located in `test_server/`.

```python
from datasync import DataSync
import asyncio

sync = DataSync("http://localhost:8000")
mapping = {
    "data/users": "output/users.json",
    "data/info": "output/info.json",
}

result = asyncio.run(sync.sync_all(mapping))
print(result)
```

`sync_all` returns a list of saved file paths; run this example after starting a simple HTTP server:

```bash
python -m http.server --directory test_server 8000
```

---

## Environment / .env

The library doesn't read `.env` by itself. If you prefer `BASE_URL` in `.env`, do it in your app:

```python
from datasync import DataSync
from dotenv import load_dotenv
import os

load_dotenv()
base = os.getenv('BASE_URL')
sync = DataSync(base)
```

---

## Notes
- All public methods that perform network or I/O are async; examples must `await` them or run inside an event loop.
- `CacheManager` requires a `cache_dir` parameter; the README example without a parameter is incorrect.
- There is no exported top-level `fetch_remote` function; use `DataSync.fetch_remote`.
