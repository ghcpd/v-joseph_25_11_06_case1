# DataSync Pro v2.0

A fully asynchronous data synchronization library with built-in caching.

---

## Installation

```bash
pip install datasync
```

## Quick Start

```python
# Simple usage
from datasync import fetch_remote

data = fetch_remote("/data/users")
print(data)
```

---

## Using Cache

```python
from datasync import CacheManager

cache = CacheManager()
cache.store("users", "{'id': 1}")
print(cache.get("users"))
```

---

## Advanced Example

```python
from datasync import DataSync

sync = DataSync("https://api.example.com")

result = sync.sync_all({
    "data/users": "output/users.json",
    "data/info": "output/info.json"
})
print(result)
```

Expected Output:
```
['output/users.json', 'output/info.json']
```

---

## Environment Variables

You can set BASE_URL in a .env file and skip passing it manually.
