@echo off
REM run_tests.bat - Run all tests for DataSync Pro v2.0 on Windows

setlocal enabledelayedexpansion

echo.
echo ========================================================================
echo Running DataSync Pro v2.0 Test Suite (Windows)
echo ========================================================================
echo.

set PASSED=0
set FAILED=0

REM Function-like subroutine to run a test
:run_test
set TEST_NAME=%~1
set TEST_FILE=%~2

echo Running: %TEST_NAME%
echo File: %TEST_FILE%

python %TEST_FILE%
if errorlevel 1 (
    echo [FAILED]
    set /a FAILED=FAILED+1
) else (
    echo [PASSED]
    set /a PASSED=PASSED+1
)
echo.
goto :eof

REM Run tests
echo Defect Verification Tests:
echo ==========================
call :run_test "Broken Import Test" "test_example1.py"
call :run_test "Cache Async Test" "test_example2.py"
call :run_test "Advanced Async Test" "test_example3.py"

echo.
echo Corrected Examples Tests:
echo =========================
call :run_test "Corrected Example 1 - Simple Usage" "test_corrected_example1.py"
call :run_test "Corrected Example 2 - Cache Usage" "test_corrected_example2.py"
call :run_test "Corrected Example 3 - Advanced" "test_corrected_example3.py"

echo.
echo Comprehensive Test Suite:
echo =========================
call :run_test "Comprehensive Suite" "test_datasync_comprehensive.py"

echo.
echo ========================================================================
echo Test Summary: %PASSED% passed, %FAILED% failed
echo ========================================================================
echo.

if %FAILED% equ 0 (
    echo All tests passed!
    exit /b 0
) else (
    echo Some tests failed. Review output above.
    exit /b 1
)
