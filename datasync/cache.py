import os
import asyncio

class CacheManager:
    def __init__(self, cache_dir):
        self.cache_dir = cache_dir
        os.makedirs(cache_dir, exist_ok=True)

    async def store(self, key, value):
        await asyncio.sleep(0.05)
        # sanitize key to filesystem-safe filename: replace everything not alnum or _ with _
        safe_key = ''.join(c if (c.isalnum() or c in ('_', '-')) else '_' for c in key)
        filename = os.path.join(self.cache_dir, safe_key.replace("/", "_") + ".cache")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(value)

    async def get(self, key):
        safe_key = ''.join(c if (c.isalnum() or c in ('_', '-')) else '_' for c in key)
        filename = os.path.join(self.cache_dir, safe_key.replace("/", "_") + ".cache")
        if not os.path.exists(filename):
            return None
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
