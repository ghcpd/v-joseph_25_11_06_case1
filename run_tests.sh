#!/bin/bash
# run_tests.sh - Run all tests for DataSync Pro v2.0

echo "========================================================================"
echo "Running DataSync Pro v2.0 Test Suite"
echo "========================================================================"
echo ""

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Test results
PASSED=0
FAILED=0

# Function to run a test
run_test() {
    local test_name=$1
    local test_file=$2
    
    echo "Running: $test_name"
    echo "File: $test_file"
    
    if python "$test_file"; then
        echo -e "${GREEN}✓ PASSED${NC}"
        ((PASSED++))
    else
        echo -e "${RED}✗ FAILED${NC}"
        ((FAILED++))
    fi
    echo ""
}

# Run test files
echo "Defect Verification Tests:"
echo "=========================="
run_test "Broken Import Test" "test_example1.py"
run_test "Cache Async Test" "test_example2.py"
run_test "Advanced Async Test" "test_example3.py"

echo ""
echo "Corrected Examples Tests:"
echo "========================="
run_test "Corrected Example 1 - Simple Usage" "test_corrected_example1.py"
run_test "Corrected Example 2 - Cache Usage" "test_corrected_example2.py"
run_test "Corrected Example 3 - Advanced" "test_corrected_example3.py"

echo ""
echo "Comprehensive Test Suite:"
echo "========================="
run_test "Comprehensive Suite" "test_datasync_comprehensive.py"

echo ""
echo "========================================================================"
echo -e "Test Summary: ${GREEN}$PASSED passed${NC}, ${RED}$FAILED failed${NC}"
echo "========================================================================"
echo ""

if [ $FAILED -eq 0 ]; then
    echo -e "${GREEN}All tests passed!${NC}"
    exit 0
else
    echo -e "${RED}Some tests failed. Review output above.${NC}"
    exit 1
fi
