"""
Integration test with mock HTTP server
"""
import asyncio
import sys
import os
import shutil
from aiohttp import web

# Add parent directory to path to import datasync
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from datasync import DataSync, CacheManager


async def handler_users(request):
    """Mock handler for /data/users endpoint"""
    return web.Response(text='{"id": 1, "name": "John Doe"}')


async def handler_info(request):
    """Mock handler for /data/info endpoint"""
    return web.Response(text='{"version": "2.0", "status": "ok"}')


async def test_with_mock_server():
    """Test DataSync with a mock HTTP server"""
    print("Testing with mock HTTP server...")
    
    # Create mock server
    app = web.Application()
    app.router.add_get('/data/users', handler_users)
    app.router.add_get('/data/info', handler_info)
    
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8080)
    await site.start()
    
    try:
        # Test DataSync
        sync = DataSync("http://localhost:8080")
        
        # Test fetch_remote
        data = await sync.fetch_remote("data/users")
        print(f"Fetched data: {data}")
        assert '{"id": 1' in data or '"id": 1' in data
        
        # Test sync_all
        output_dir = "test_output"
        if os.path.exists(output_dir):
            shutil.rmtree(output_dir)
        
        result = await sync.sync_all({
            "data/users": f"{output_dir}/users.json",
            "data/info": f"{output_dir}/info.json"
        })
        
        print(f"Synced files: {result}")
        assert len(result) == 2
        assert f"{output_dir}/users.json" in result
        assert f"{output_dir}/info.json" in result
        
        # Verify files exist
        assert os.path.exists(f"{output_dir}/users.json")
        assert os.path.exists(f"{output_dir}/info.json")
        
        # Test cache
        cache = CacheManager("test_cache")
        await cache.store("test_key", "test_value")
        cached_value = await cache.get("test_key")
        assert cached_value == "test_value"
        print(f"Cached value: {cached_value}")
        
        print("[PASS] Integration test passed")
        
        # Clean up
        if os.path.exists(output_dir):
            shutil.rmtree(output_dir)
        if os.path.exists("test_cache"):
            shutil.rmtree("test_cache")
        if os.path.exists("cache"):
            shutil.rmtree("cache")
            
    finally:
        await runner.cleanup()


if __name__ == "__main__":
    asyncio.run(test_with_mock_server())

