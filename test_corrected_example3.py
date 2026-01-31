"""
test_corrected_example3.py
Test the corrected advanced example with mock data (without actual API calls)
"""
import asyncio
import sys
import traceback
import os
import shutil
import json
from unittest.mock import patch, AsyncMock
from datasync import DataSync

print("=" * 70)
print("TEST 3: Corrected Advanced Example - sync_all with async/await")
print("=" * 70)

async def test_sync_all():
    """Test corrected sync_all example with mocked HTTP"""
    test_output_dir = "test_output_example3"
    
    try:
        # Clean up if exists
        if os.path.exists(test_output_dir):
            shutil.rmtree(test_output_dir)
        
        # Create DataSync instance
        sync = DataSync("https://api.example.com")
        print("✓ Created DataSync instance")
        
        # Mock the aiohttp response for testing
        mock_response_text = {
            "data/users": '{"users": [{"id": 1, "name": "Alice"}]}',
            "data/info": '{"version": "2.0", "status": "active"}'
        }
        
        async def mock_fetch(endpoint):
            """Mock fetch_remote to return test data"""
            return mock_response_text.get(endpoint, "{}")
        
        # Define mapping as in README (CORRECTED)
        mapping = {
            "data/users": f"{test_output_dir}/users.json",
            "data/info": f"{test_output_dir}/info.json"
        }
        print(f"✓ Created mapping: {mapping}")
        
        # Mock fetch_remote and call sync_all with await (CORRECTED)
        with patch.object(sync, 'fetch_remote', side_effect=mock_fetch):
            result = await sync.sync_all(mapping)
        
        print(f"✓ Called sync_all with await")
        print(f"✓ Result: {result}")
        
        # Verify result is list of file paths
        assert isinstance(result, list), f"Result should be list, got {type(result)}"
        print("✓ Result is a list (not coroutine)")
        
        # Verify expected files were created
        assert len(result) == 2, f"Expected 2 files, got {len(result)}"
        print(f"✓ Created {len(result)} files")
        
        # Verify files exist and contain data
        for filepath in result:
            assert os.path.exists(filepath), f"File not created: {filepath}"
            with open(filepath, 'r') as f:
                content = f.read()
                assert len(content) > 0, f"File is empty: {filepath}"
            print(f"  ✓ {filepath}")
        
        print("\n✓ Advanced example works correctly with async/await")
        print(f"✓ Expected output achieved: {result}")
        
        return True
        
    except Exception as e:
        print(f"✗ Test failed: {e}")
        traceback.print_exc()
        return False
    
    finally:
        # Clean up
        if os.path.exists(test_output_dir):
            shutil.rmtree(test_output_dir)
            print(f"\nCleaned up test output directory: {test_output_dir}")

# Run the test
result = asyncio.run(test_sync_all())
print(f"\nTest Result: {'PASSED' if result else 'FAILED'}")
sys.exit(0 if result else 1)
