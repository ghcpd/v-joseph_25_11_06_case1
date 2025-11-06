"""
Test Example 3: Advanced Example - DataSync
README shows sync_all being called without await
But it's an async method
"""
import asyncio
import sys
import traceback

print("=" * 60)
print("Testing Example 3: Advanced Example - DataSync")
print("=" * 60)

async def test_datasync():
    try:
        from datasync import DataSync
        print("✓ Successfully imported DataSync")
        
        sync = DataSync("https://api.example.com")
        print("✓ Created DataSync instance")
        
        # Check sync_all method
        print("\nTesting sync_all()...")
        print(f"  Type: {type(sync.sync_all)}")
        print(f"  Is coroutine function: {asyncio.iscoroutinefunction(sync.sync_all)}")
        
        # Try as README shows (sync)
        try:
            mapping = {
                "data/users": "output/users.json",
                "data/info": "output/info.json"
            }
            result = sync.sync_all(mapping)
            print(f"  ✗ sync_all() returned {type(result).__name__} - is coroutine, needs await")
        except Exception as e:
            print(f"  Error: {e}")
        
        print("\nNote: sync_all requires real HTTP calls to test properly")
        print("  - Would need a working API endpoint")
        print("  - Methods are async, README shows sync usage")
        
    except Exception as e:
        print(f"✗ Error: {e}")
        traceback.print_exc()

asyncio.run(test_datasync())
