"""
test_datasync_comprehensive.py
Comprehensive test suite for DataSync Pro v2.0
Verifies all documented functionality and edge cases
"""
import asyncio
import sys
import traceback
import os
import shutil
import json
from unittest.mock import patch, AsyncMock, MagicMock
from datasync import DataSync, CacheManager

class TestRunner:
    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.tests = []
    
    def add_test(self, name, func):
        self.tests.append((name, func))
    
    async def run_all(self):
        print("=" * 70)
        print("COMPREHENSIVE TEST SUITE - DataSync Pro v2.0")
        print("=" * 70)
        
        for test_name, test_func in self.tests:
            print(f"\n{test_name}...")
            try:
                result = await test_func()
                if result:
                    self.passed += 1
                    print(f"  ✓ PASSED")
                else:
                    self.failed += 1
                    print(f"  ✗ FAILED")
            except Exception as e:
                self.failed += 1
                print(f"  ✗ FAILED: {e}")
                traceback.print_exc()
        
        print("\n" + "=" * 70)
        print(f"SUMMARY: {self.passed} passed, {self.failed} failed")
        print("=" * 70)
        
        return self.failed == 0

# Test functions
async def test_datasync_init():
    """Test DataSync initialization"""
    try:
        sync = DataSync("https://api.example.com")
        assert sync.base_url == "https://api.example.com"
        
        sync2 = DataSync("https://api.example.com/")
        assert sync2.base_url == "https://api.example.com"  # strips trailing slash
        
        return True
    except Exception as e:
        print(f"    Error: {e}")
        return False

async def test_datasync_cache_dir():
    """Test DataSync cache directory creation"""
    try:
        cache_dir = "test_cache_dir_01"
        if os.path.exists(cache_dir):
            shutil.rmtree(cache_dir)
        
        sync = DataSync("https://api.example.com", cache_dir=cache_dir)
        assert os.path.exists(cache_dir), "Cache directory not created"
        
        shutil.rmtree(cache_dir)
        return True
    except Exception as e:
        print(f"    Error: {e}")
        return False

async def test_cachemanager_store_retrieve():
    """Test CacheManager store and retrieve"""
    try:
        cache_dir = "test_cache_02"
        if os.path.exists(cache_dir):
            shutil.rmtree(cache_dir)
        
        cache = CacheManager(cache_dir)
        
        # Store data
        await cache.store("test_key", "test_value")
        
        # Retrieve data
        data = await cache.get("test_key")
        assert data == "test_value", f"Expected 'test_value', got {data}"
        
        shutil.rmtree(cache_dir)
        return True
    except Exception as e:
        print(f"    Error: {e}")
        return False

async def test_cachemanager_missing_key():
    """Test CacheManager returns None for missing keys"""
    try:
        cache_dir = "test_cache_03"
        if os.path.exists(cache_dir):
            shutil.rmtree(cache_dir)
        
        cache = CacheManager(cache_dir)
        data = await cache.get("nonexistent")
        assert data is None, f"Expected None, got {data}"
        
        shutil.rmtree(cache_dir)
        return True
    except Exception as e:
        print(f"    Error: {e}")
        return False

async def test_cachemanager_key_transformation():
    """Test CacheManager transforms / to _ in filenames"""
    try:
        cache_dir = "test_cache_04"
        if os.path.exists(cache_dir):
            shutil.rmtree(cache_dir)
        
        cache = CacheManager(cache_dir)
        await cache.store("data/users", "user_data")
        
        # Check file was created with transformed name
        filepath = os.path.join(cache_dir, "data_users.cache")
        assert os.path.exists(filepath), f"File not created: {filepath}"
        
        shutil.rmtree(cache_dir)
        return True
    except Exception as e:
        print(f"    Error: {e}")
        return False

async def test_datasync_sync_local():
    """Test DataSync sync_local creates files and directories"""
    try:
        cache_dir = "test_cache_05"
        output_dir = "test_output_01"
        
        # Clean up
        for d in [cache_dir, output_dir]:
            if os.path.exists(d):
                shutil.rmtree(d)
        
        sync = DataSync("https://api.example.com", cache_dir=cache_dir)
        
        # Mock fetch_remote
        async def mock_fetch(endpoint):
            return "test_data"
        
        output_file = os.path.join(output_dir, "subdir", "file.json")
        
        with patch.object(sync, 'fetch_remote', side_effect=mock_fetch):
            result = await sync.sync_local("data/test", output_file)
        
        # Verify file was created
        assert os.path.exists(output_file), f"File not created: {output_file}"
        with open(output_file, 'r') as f:
            content = f.read()
            assert content == "test_data", f"Expected 'test_data', got {content}"
        
        # Clean up
        for d in [cache_dir, output_dir]:
            if os.path.exists(d):
                shutil.rmtree(d)
        
        return True
    except Exception as e:
        print(f"    Error: {e}")
        traceback.print_exc()
        return False

async def test_datasync_sync_all():
    """Test DataSync sync_all with multiple files"""
    try:
        cache_dir = "test_cache_06"
        output_dir = "test_output_02"
        
        # Clean up
        for d in [cache_dir, output_dir]:
            if os.path.exists(d):
                shutil.rmtree(d)
        
        sync = DataSync("https://api.example.com", cache_dir=cache_dir)
        
        # Mock fetch_remote with different data per endpoint
        async def mock_fetch(endpoint):
            data = {
                "data/users": "users_data",
                "data/info": "info_data"
            }
            return data.get(endpoint, "unknown")
        
        mapping = {
            "data/users": os.path.join(output_dir, "users.json"),
            "data/info": os.path.join(output_dir, "info.json")
        }
        
        with patch.object(sync, 'fetch_remote', side_effect=mock_fetch):
            result = await sync.sync_all(mapping)
        
        # Verify result
        assert isinstance(result, list), "Result should be list"
        assert len(result) == 2, f"Expected 2 files, got {len(result)}"
        
        # Verify files were created
        for filepath in result:
            assert os.path.exists(filepath), f"File not created: {filepath}"
        
        # Clean up
        for d in [cache_dir, output_dir]:
            if os.path.exists(d):
                shutil.rmtree(d)
        
        return True
    except Exception as e:
        print(f"    Error: {e}")
        traceback.print_exc()
        return False

async def test_datasync_cache_integration():
    """Test DataSync caches fetched data"""
    try:
        cache_dir = "test_cache_07"
        if os.path.exists(cache_dir):
            shutil.rmtree(cache_dir)
        
        sync = DataSync("https://api.example.com", cache_dir=cache_dir)
        
        # Mock fetch_remote
        async def mock_fetch(endpoint):
            return f"data_for_{endpoint}"
        
        # Simulate fetch and cache
        with patch.object(sync, 'fetch_remote', side_effect=mock_fetch):
            data = await sync.fetch_remote("data/test")
        
        # Check cache file exists
        cache_file = os.path.join(cache_dir, "data_test.cache")
        assert os.path.exists(cache_file), f"Cache file not created: {cache_file}"
        
        shutil.rmtree(cache_dir)
        return True
    except Exception as e:
        print(f"    Error: {e}")
        traceback.print_exc()
        return False

async def test_async_functions_are_coroutines():
    """Test that all async functions are properly defined"""
    try:
        sync = DataSync("https://api.example.com")
        cache = CacheManager("test_cache")
        
        # Verify async methods
        assert asyncio.iscoroutinefunction(sync.fetch_remote), "fetch_remote not async"
        assert asyncio.iscoroutinefunction(sync.sync_local), "sync_local not async"
        assert asyncio.iscoroutinefunction(sync.sync_all), "sync_all not async"
        assert asyncio.iscoroutinefunction(cache.store), "cache.store not async"
        assert asyncio.iscoroutinefunction(cache.get), "cache.get not async"
        
        shutil.rmtree("test_cache")
        return True
    except Exception as e:
        print(f"    Error: {e}")
        return False

# Main test runner
async def main():
    runner = TestRunner()
    
    runner.add_test("DataSync initialization", test_datasync_init)
    runner.add_test("DataSync cache directory creation", test_datasync_cache_dir)
    runner.add_test("CacheManager store and retrieve", test_cachemanager_store_retrieve)
    runner.add_test("CacheManager missing key handling", test_cachemanager_missing_key)
    runner.add_test("CacheManager key transformation", test_cachemanager_key_transformation)
    runner.add_test("DataSync sync_local", test_datasync_sync_local)
    runner.add_test("DataSync sync_all", test_datasync_sync_all)
    runner.add_test("DataSync cache integration", test_datasync_cache_integration)
    runner.add_test("Async functions verification", test_async_functions_are_coroutines)
    
    success = await runner.run_all()
    return success

if __name__ == "__main__":
    result = asyncio.run(main())
    sys.exit(0 if result else 1)
