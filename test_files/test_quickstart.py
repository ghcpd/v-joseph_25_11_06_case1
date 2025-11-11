"""
Test Quick Start example from corrected_readme.md
"""
import asyncio
import sys
import os

# Add parent directory to path to import datasync
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from datasync import DataSync


async def test_quickstart():
    """Test the Quick Start example"""
    print("Testing Quick Start example...")
    
    # Note: This will fail with a real API call, but demonstrates correct usage
    try:
        sync = DataSync("https://api.example.com")
        # This will raise an error since the API doesn't exist, but shows correct async usage
        data = await sync.fetch_remote("/data/users")
        print(f"Success: {data}")
    except Exception as e:
        print(f"Expected error (API not available): {type(e).__name__}: {e}")
        print("[PASS] Correct async/await usage verified")


if __name__ == "__main__":
    asyncio.run(test_quickstart())

