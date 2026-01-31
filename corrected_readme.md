# DataSync Pro v2.0 - CORRECTED

A fully asynchronous data synchronization library with built-in caching.

---

## Installation

```bash
pip install aiohttp python-dotenv
```

---

## Quick Start

### ✓ CORRECT: Simple Usage with DataSync Class

```python
import asyncio
from datasync import DataSync

async def main():
    sync = DataSync("https://api.example.com")
    data = await sync.fetch_remote("/data/users")
    print(data)

# Run the async function
asyncio.run(main())
```

**Important Notes:**
- `fetch_remote()` is an async method on the `DataSync` class (not a module-level function)
- Must use `await` keyword
- Must run within async context using `asyncio.run()` or inside an `async def` function

---

## Using Cache

### ✓ CORRECT: Cache Manager with Async Methods

```python
import asyncio
from datasync import CacheManager

async def main():
    # Create cache manager with cache directory
    cache = CacheManager("cache")
    
    # Store data (async operation)
    await cache.store("users", "{'id': 1}")
    
    # Retrieve data (async operation)
    data = await cache.get("users")
    print(data)  # Output: {'id': 1}

# Run the async function
asyncio.run(main())
```

**Important Notes:**
- `CacheManager` requires a `cache_dir` parameter
- Both `store()` and `get()` are async coroutine functions
- Must use `await` keyword for both methods
- Files are stored with `.cache` extension in the specified directory

---

## Advanced Example - Synchronizing Multiple Endpoints

### ✓ CORRECT: Sync Multiple Files with DataSync

```python
import asyncio
from datasync import DataSync

async def main():
    sync = DataSync("https://api.example.com")
    
    # Define endpoint-to-file mappings
    mapping = {
        "data/users": "output/users.json",
        "data/info": "output/info.json"
    }
    
    # Sync all files (async operation)
    result = await sync.sync_all(mapping)
    
    # Result is list of saved file paths
    print(result)

# Run the async function
asyncio.run(main())
```

**Expected Output:**
```
['output/users.json', 'output/info.json']
```

**Important Notes:**
- `sync_all()` is an async coroutine function
- Must use `await` keyword
- Returns list of file paths that were successfully synced
- Creates output directories automatically
- Writes fetched data to local files

---

## Using with Environment Variables

### ✓ CORRECT: Load BASE_URL from .env

Create a `.env` file:
```
BASE_URL=https://api.example.com
```

Then use it:
```python
import asyncio
import os
from dotenv import load_dotenv
from datasync import DataSync

async def main():
    load_dotenv()
    base_url = os.getenv("BASE_URL")
    
    sync = DataSync(base_url)
    data = await sync.fetch_remote("/data/users")
    print(data)

asyncio.run(main())
```

---

## Module Exports

The `datasync` module exports the following:

```python
from datasync import DataSync, CacheManager

# DataSync Class
# - Constructor: DataSync(base_url, cache_dir="cache")
# - Methods:
#   - async fetch_remote(endpoint) -> str
#   - async sync_local(endpoint, local_path) -> str
#   - async sync_all(mapping: dict) -> list

# CacheManager Class
# - Constructor: CacheManager(cache_dir)
# - Methods:
#   - async store(key, value) -> None
#   - async get(key) -> str or None
```

---

## Key Implementation Details

### Async/Await Requirement
All network and file operations use `async` functions to prevent blocking. This requires:
1. Python 3.7 or higher
2. All methods to be called with `await` keyword
3. Code to run within async context

### Cache Behavior
- Cache stores data in `cache_dir` parameter specified during initialization
- Keys with `/` characters are converted to `_` in filenames
- Cached files have `.cache` extension
- Files are stored as plain text

### Error Handling
- HTTP requests that don't return status 200 raise `RuntimeError`
- File I/O errors propagate as standard Python exceptions
- Use try/except blocks to handle async operation failures:

```python
import asyncio
from datasync import DataSync

async def main():
    sync = DataSync("https://api.example.com")
    try:
        data = await sync.fetch_remote("/invalid/endpoint")
    except RuntimeError as e:
        print(f"Error: {e}")

asyncio.run(main())
```

---

## Common Mistakes to Avoid

### ❌ WRONG: Missing await

```python
# This WILL NOT WORK
result = sync.fetch_remote("/data/users")  # Returns coroutine object
print(result)  # Prints: <coroutine object ...>
```

### ✓ CORRECT: Using await

```python
# This WORKS
result = await sync.fetch_remote("/data/users")  # Fetches actual data
print(result)  # Prints: actual data
```

---

### ❌ WRONG: Missing async context

```python
# This WILL NOT WORK
from datasync import DataSync
sync = DataSync("https://api.example.com")
result = await sync.fetch_remote("/data/users")  # SyntaxError: await outside async function
```

### ✓ CORRECT: Using asyncio.run()

```python
# This WORKS
import asyncio
from datasync import DataSync

async def main():
    sync = DataSync("https://api.example.com")
    result = await sync.fetch_remote("/data/users")
    return result

asyncio.run(main())
```

---

### ❌ WRONG: Missing CacheManager parameter

```python
# This WILL NOT WORK
cache = CacheManager()  # TypeError: missing required argument 'cache_dir'
```

### ✓ CORRECT: Providing cache_dir

```python
# This WORKS
cache = CacheManager("cache")  # Specify where to store cache files
```

---

## Dependencies

- **Python**: 3.7+
- **aiohttp**: 3.0.0+ (for async HTTP requests)
- **python-dotenv**: 0.19.0+ (for .env file support)

---

## Requirements Status

- ✓ All examples use correct async/await syntax
- ✓ All parameters are properly specified
- ✓ All exports are correctly imported
- ✓ Error handling examples provided
- ✓ Common mistakes documented
