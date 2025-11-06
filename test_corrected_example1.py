"""
test_corrected_example1.py
Test the corrected simple usage example with proper async/await
"""
import asyncio
import sys
import traceback
from datasync import DataSync

print("=" * 70)
print("TEST 1: Corrected Simple Usage - fetch_remote with async/await")
print("=" * 70)

async def test_simple_usage():
    """Test corrected simple usage example"""
    try:
        # Create DataSync instance
        sync = DataSync("https://api.example.com")
        print("✓ Created DataSync instance")
        
        # Verify fetch_remote is accessible and is a coroutine function
        assert hasattr(sync, 'fetch_remote'), "fetch_remote method missing"
        assert asyncio.iscoroutinefunction(sync.fetch_remote), "fetch_remote is not async"
        print("✓ fetch_remote is properly defined as async method")
        
        # Note: Cannot actually call fetch_remote without a working API
        # But we can verify the structure is correct
        print("✓ fetch_remote can be called with await (structure verified)")
        print("\nNote: Full execution requires working API endpoint")
        print("      Example usage:")
        print("        data = await sync.fetch_remote('/data/users')")
        print("        print(data)")
        
        return True
        
    except Exception as e:
        print(f"✗ Test failed: {e}")
        traceback.print_exc()
        return False

# Run the test
result = asyncio.run(test_simple_usage())
print(f"\nTest Result: {'PASSED' if result else 'FAILED'}")
sys.exit(0 if result else 1)
