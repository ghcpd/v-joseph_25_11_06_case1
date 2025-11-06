"""
Test Example 1: Simple usage
README says: from datasync import fetch_remote
"""
import sys
import traceback

print("=" * 60)
print("Testing Example 1: Simple usage - fetch_remote")
print("=" * 60)

try:
    # Try importing as documented in README
    from datasync import fetch_remote
    print("✓ Successfully imported fetch_remote from datasync")
except ImportError as e:
    print("✗ FAILED: Cannot import fetch_remote")
    print(f"  Error: {e}")
    traceback.print_exc()
    print("\n  Analysis: fetch_remote is not exported in __all__")
    print("  README example is BROKEN\n")

# Check what's actually available
print("\nChecking actual exports from datasync module:")
try:
    import datasync
    print(f"  Available: {dir(datasync)}")
    print(f"  __all__: {datasync.__all__ if hasattr(datasync, '__all__') else 'Not defined'}")
except Exception as e:
    print(f"  Error: {e}")
    traceback.print_exc()

# Check DataSync class
print("\nChecking DataSync class structure:")
try:
    from datasync import DataSync
    sync = DataSync("https://api.example.com")
    print(f"  Methods: {[m for m in dir(sync) if not m.startswith('_')]}")
    
    # Check if fetch_remote exists as method
    if hasattr(sync, 'fetch_remote'):
        print("  ✓ fetch_remote exists as instance method (requires await/async)")
    else:
        print("  ✗ fetch_remote NOT found as instance method")
except Exception as e:
    print(f"  Error: {e}")
    traceback.print_exc()
