# DataSync Pro v2.0 (Corrected Tutorial)

This corrected tutorial fixes API usage mismatches with the implementation. The DataSync API is asynchronous and methods should be awaited. `CacheManager` requires a `cache_dir` argument. `fetch_remote` is a method on `DataSync`, not a top-level function. The library does not currently read `BASE_URL` from `.env` — pass it to `DataSync` explicitly.

## Installation

```bash
pip install -r requirements.txt
```

---

## Quick Start (corrected)

```python
import asyncio
from datasync import DataSync

async def main():
    # Create DataSync, passing base_url explicitly
    sync = DataSync("http://127.0.0.1:8080")
    data = await sync.fetch_remote("/data/users")
    print(data)

asyncio.run(main())
```

Notes:
- `DataSync.fetch_remote` is asynchronous and must be awaited or run with `asyncio.run`.
- `fetch_remote` is not exported as a top-level function.

---

## Using Cache (corrected)

```python
import asyncio
from datasync import CacheManager

async def main():
    cache = CacheManager(cache_dir="cache_dir")
    await cache.store("/users", "{'id': 1}")
    print(await cache.get("/users"))

asyncio.run(main())
```

Notes:
- `CacheManager` requires `cache_dir` to specify where cached files are stored.
- `store` and `get` are asynchronous functions, use `await`.
- Keys are used to create filenames by replacing `/` with `_`. Using leading `/` will produce file names starting with underscore.

---

## Advanced Example (corrected)

```python
import asyncio
from datasync import DataSync

async def main():
    sync = DataSync("http://127.0.0.1:8080")
    mapping = {
        "data/users": "output/users.json",
        "data/info": "output/info.json",
    }
    result = await sync.sync_all(mapping)
    print(result)  # ['output/users.json', 'output/info.json']

asyncio.run(main())
```

Notes:
- `sync_all` is asynchronous. It returns a coroutine that resolves to a list of output paths when awaited.

---

## Environment Variables

The current implementation does not read `BASE_URL` from `.env` or environment variables. `DataSync` requires a `base_url` argument during initialization.

---

## How to run the test suite

1. Create a virtual environment and activate it (or use `setup.sh`).
2. Install dependencies: `pip install -r requirements.txt`.
3. Run tests: `./run_tests.sh` (or run `python -m pytest test_files/tests` directly).

---

## Additional Notes

- All examples are asynchronous; use `asyncio.run` when executing from scripts.
- Cache key normalization: keys are converted to file names by replacing `/` with `_`, e.g., `/data/users` -> `_data_users.cache`.
