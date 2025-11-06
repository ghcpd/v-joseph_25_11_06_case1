from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from datasync import CacheManager
import asyncio

async def run_cache():
    cache = CacheManager("cache")
    await cache.store("users", "{'id': 1}")
    print(await cache.get("users"))

if __name__ == '__main__':
    asyncio.run(run_cache())
