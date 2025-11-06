import asyncio
import os
from datasync import DataSync, CacheManager

async def main():
    cache = CacheManager('tmp_cache')
    await cache.store('hello', 'world')
    v = await cache.get('hello')
    print('cache-value:', v)

    # Use a dummy local server URL that will 404; we just test exception handling
    ds = DataSync('https://httpbin.org')
    try:
        data = await ds.fetch_remote('/status/200')
        print('fetched:', data[:20])
    except Exception as e:
        print('fetch error:', e)

if __name__ == '__main__':
    asyncio.run(main())
