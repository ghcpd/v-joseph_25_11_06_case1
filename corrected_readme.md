# DataSync Pro v2.0

A fully asynchronous data synchronization library with built-in caching.

---

## Installation

```bash
pip install aiohttp
```

**Note:** This package requires `aiohttp` as a dependency. Install it before using the library.

---

## Quick Start

```python
import asyncio
from datasync import DataSync

async def main():
    sync = DataSync("https://api.example.com")
    data = await sync.fetch_remote("/data/users")
    print(data)

asyncio.run(main())
```

**Note:** All methods in DataSync Pro v2.0 are asynchronous and must be used with `async/await` syntax.

---

## Using Cache

```python
import asyncio
from datasync import CacheManager

async def main():
    cache = CacheManager("cache")
    await cache.store("users", "{'id': 1}")
    result = await cache.get("users")
    print(result)

asyncio.run(main())
```

**Note:** 
- `CacheManager` requires a `cache_dir` parameter specifying the cache directory.
- Both `store()` and `get()` are async methods and must be awaited.

---

## Advanced Example

```python
import asyncio
from datasync import DataSync

async def main():
    sync = DataSync("https://api.example.com")
    
    result = await sync.sync_all({
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

**Note:** `sync_all()` is an async method and must be awaited within an async function.

---

## Environment Variables

You can set BASE_URL in a .env file and skip passing it manually.

---

## API Reference

### DataSync Class

```python
sync = DataSync(base_url, cache_dir="cache")
```

- `base_url` (str): Base URL for API requests
- `cache_dir` (str, optional): Directory for cache storage. Defaults to "cache".

#### Methods

- `async fetch_remote(endpoint)`: Fetches data from the remote endpoint and caches it.
- `async sync_local(endpoint, local_path)`: Fetches data and saves it to a local file.
- `async sync_all(mapping)`: Synchronizes multiple endpoints to local files. Takes a dict mapping endpoints to file paths.

### CacheManager Class

```python
cache = CacheManager(cache_dir)
```

- `cache_dir` (str): Directory for cache storage.

#### Methods

- `async store(key, value)`: Stores a value in the cache.
- `async get(key)`: Retrieves a value from the cache. Returns `None` if not found.

