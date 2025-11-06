import asyncio
import aiohttp
import os
from .cache import CacheManager

class DataSync:
    def __init__(self, base_url, cache_dir="cache"):
        self.base_url = base_url.rstrip("/")
        self.cache = CacheManager(cache_dir)

    async def fetch_remote(self, endpoint):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status != 200:
                    raise RuntimeError(f"Failed to fetch {endpoint}: {resp.status}")
                data = await resp.text()
                await self.cache.store(endpoint, data)
                return data

    async def sync_local(self, endpoint, local_path):
        data = await self.fetch_remote(endpoint)
        os.makedirs(os.path.dirname(local_path), exist_ok=True)
        with open(local_path, "w", encoding="utf-8") as f:
            f.write(data)
        return local_path

    async def sync_all(self, mapping):
        results = []
        for endpoint, path in mapping.items():
            result = await self.sync_local(endpoint, path)
            results.append(result)
        return results
