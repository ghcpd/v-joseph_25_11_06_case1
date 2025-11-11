#!/bin/bash

# Run all test cases for DataSync Pro v2.0

echo "=========================================="
echo "Running DataSync Pro v2.0 Test Suite"
echo "=========================================="
echo ""

# Activate virtual environment
if [ -d ".venv" ]; then
    echo "Activating virtual environment..."
    source .venv/bin/activate
else
    echo "Warning: .venv not found. Please run setup.sh first."
    exit 1
fi

# Check if dependencies are installed
if ! python -c "import aiohttp" 2>/dev/null; then
    echo "Error: aiohttp not installed. Please run setup.sh first."
    exit 1
fi

# Run tests
echo ""
echo "Test 1: Quick Start Example"
echo "---------------------------"
python test_files/test_quickstart.py
echo ""

echo "Test 2: Cache Manager Example"
echo "------------------------------"
python test_files/test_cache.py
echo ""

echo "Test 3: Advanced Example"
echo "-------------------------"
python test_files/test_advanced.py
echo ""

echo "Test 4: Integration Test (with mock server)"
echo "--------------------------------------------"
python test_files/test_integration.py
echo ""

echo "=========================================="
echo "All tests completed!"
echo "=========================================="

