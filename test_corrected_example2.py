"""
test_corrected_example2.py
Test the corrected cache example with proper async/await and required parameter
"""
import asyncio
import sys
import traceback
import os
import shutil
from datasync import CacheManager

print("=" * 70)
print("TEST 2: Corrected Cache Usage - CacheManager with async/await")
print("=" * 70)

async def test_cache_usage():
    """Test corrected cache example"""
    test_cache_dir = "test_cache_example2"
    
    try:
        # Clean up if exists
        if os.path.exists(test_cache_dir):
            shutil.rmtree(test_cache_dir)
        
        # Create cache manager with cache_dir parameter (CORRECTED)
        cache = CacheManager(test_cache_dir)
        print("✓ Created CacheManager with cache_dir parameter")
        
        # Store data using await (CORRECTED)
        test_value = "{'id': 1}"
        await cache.store("users", test_value)
        print(f"✓ Stored data: {test_value}")
        
        # Verify cache file was created
        cache_file = os.path.join(test_cache_dir, "users.cache")
        assert os.path.exists(cache_file), "Cache file not created"
        print(f"✓ Cache file created at: {cache_file}")
        
        # Retrieve data using await (CORRECTED)
        retrieved_data = await cache.get("users")
        print(f"✓ Retrieved data: {retrieved_data}")
        
        # Verify data matches
        assert retrieved_data == test_value, f"Data mismatch: {retrieved_data} != {test_value}"
        print("✓ Retrieved data matches stored data")
        
        # Test non-existent key
        non_existent = await cache.get("non_existent_key")
        assert non_existent is None, "Should return None for missing keys"
        print("✓ Non-existent key returns None")
        
        print("\n✓ All cache operations work correctly with async/await")
        return True
        
    except Exception as e:
        print(f"✗ Test failed: {e}")
        traceback.print_exc()
        return False
    
    finally:
        # Clean up
        if os.path.exists(test_cache_dir):
            shutil.rmtree(test_cache_dir)
            print(f"\nCleaned up test cache directory: {test_cache_dir}")

# Run the test
result = asyncio.run(test_cache_usage())
print(f"\nTest Result: {'PASSED' if result else 'FAILED'}")
sys.exit(0 if result else 1)
