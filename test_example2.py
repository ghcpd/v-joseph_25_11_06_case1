"""
Test Example 2: Using Cache
README says: cache.get("users") should return data
But cache methods are async and need await
"""
import asyncio
import sys
import traceback

print("=" * 60)
print("Testing Example 2: Using Cache")
print("=" * 60)

async def test_cache():
    try:
        from datasync import CacheManager
        print("✓ Successfully imported CacheManager")
        
        cache = CacheManager("test_cache_dir")
        print("✓ Created CacheManager instance")
        
        # Test store - is it async?
        print("\nTesting cache.store()...")
        print(f"  Type: {type(cache.store)}")
        print(f"  Is coroutine function: {asyncio.iscoroutinefunction(cache.store)}")
        
        # Try to call it as README shows (sync)
        try:
            result = cache.store("users", "{'id': 1}")
            print(f"  ✗ store() returned {result} without await - expects coroutine")
        except TypeError as e:
            print(f"  ✗ store() is async but README shows sync usage: {e}")
        
        # Try with await
        await cache.store("users", "{'id': 1}")
        print("  ✓ store() works with await")
        
        # Test get - is it async?
        print("\nTesting cache.get()...")
        print(f"  Type: {type(cache.get)}")
        print(f"  Is coroutine function: {asyncio.iscoroutinefunction(cache.get)}")
        
        # Try sync as README shows
        try:
            result = cache.get("users")
            print(f"  ✗ get() returned {result} without await - expects coroutine")
        except TypeError as e:
            print(f"  ✗ get() is async but README shows sync usage: {e}")
        
        # Try with await
        result = await cache.get("users")
        print(f"  ✓ get() works with await, returned: {result}")
        
    except Exception as e:
        print(f"✗ Error: {e}")
        traceback.print_exc()

asyncio.run(test_cache())
