import asyncio
from datasync import CacheManager

async def main():
    cache = CacheManager(".cache_test")
    await cache.store("users", "{'id': 1}")
    val = await cache.get("users")
    print(val)

if __name__ == '__main__':
    asyncio.run(main())
