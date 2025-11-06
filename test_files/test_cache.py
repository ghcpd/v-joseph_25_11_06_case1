from datasync import CacheManager

cache = CacheManager()
cache.store("users", "{'id': 1}")
print(cache.get("users"))
