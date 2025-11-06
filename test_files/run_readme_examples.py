import asyncio
import traceback

errors = []

# Quick Start example from README
try:
    # As in README: from datasync import fetch_remote
    from datasync import fetch_remote
    data = fetch_remote("/data/users")
    print(data)
except Exception as e:
    errors.append(('quick_start', traceback.format_exc()))

# Cache example from README
try:
    from datasync import CacheManager
    cache = CacheManager()
    cache.store("users", "{'id': 1}")
    print(cache.get("users"))
except Exception as e:
    errors.append(('cache_usage', traceback.format_exc()))

# Advanced Example from README
try:
    from datasync import DataSync
    sync = DataSync("https://api.example.com")
    result = sync.sync_all({
        "data/users": "output/users.json",
        "data/info": "output/info.json"
    })
    # README expects a synchronous list; make sure coroutine is awaited
    if hasattr(result, '__await__'):
        errors.append(('advanced_example', 'sync_all returned a coroutine; should be awaited'))
    else:
        print(result)
except Exception as e:
    errors.append(('advanced_example', traceback.format_exc()))

# Write defects to defects.txt
with open('defects.txt', 'w', encoding='utf-8') as f:
    if not errors:
        f.write('No defects found\n')
    else:
        for name, trace in errors:
            f.write(f"Example: {name}\n")
            f.write(trace)
            f.write('\n\n')

print('Completed run; defects written to defects.txt')