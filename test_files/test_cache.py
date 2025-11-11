"""
Test Cache Manager example from corrected_readme.md
"""
import asyncio
import sys
import os
import shutil

# Add parent directory to path to import datasync
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from datasync import CacheManager


async def test_cache():
    """Test the Cache Manager example"""
    print("Testing Cache Manager example...")
    
    # Use a test cache directory
    cache_dir = "test_cache_dir"
    
    # Clean up if exists
    if os.path.exists(cache_dir):
        shutil.rmtree(cache_dir)
    
    try:
        cache = CacheManager(cache_dir)
        await cache.store("users", "{'id': 1}")
        result = await cache.get("users")
        print(f"Stored and retrieved: {result}")
        
        # Test getting non-existent key
        result2 = await cache.get("nonexistent")
        print(f"Non-existent key result: {result2}")
        
        print("[PASS] Cache Manager test passed")
    except Exception as e:
        print(f"Error: {type(e).__name__}: {e}")
        raise
    finally:
        # Clean up
        if os.path.exists(cache_dir):
            shutil.rmtree(cache_dir)


if __name__ == "__main__":
    asyncio.run(test_cache())

