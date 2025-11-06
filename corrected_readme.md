# DataSync Pro v2.0 - Corrected Examples

Examples updated to reflect actual async APIs and class initializers.

Quick Start (async):

```python
import asyncio
from datasync import DataSync

async def main():
    ds = DataSync("https://api.example.com")
    data = await ds.fetch_remote('/data/users')
    print(data)

asyncio.run(main())
```

Using Cache (async):

```python
import asyncio
from datasync import CacheManager

async def main():
    cache = CacheManager('cache')
    await cache.store('users', "{'id': 1}")
    print(await cache.get('users'))

asyncio.run(main())
```

Advanced Example (async):

```python
import asyncio
from datasync import DataSync

async def main():
    sync = DataSync('https://api.example.com')
    result = await sync.sync_all({
        'data/users': 'output/users.json',
        'data/info': 'output/info.json'
    })
    print(result)

asyncio.run(main())
```
