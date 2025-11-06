@echo off
REM setup.bat - Setup script for DataSync Pro v2.0 on Windows

echo.
echo ========================================================================
echo DataSync Pro v2.0 - Environment Setup (Windows)
echo ========================================================================
echo.

REM Check Python version
echo 1. Checking Python version...
python --version
echo.

REM Create virtual environment if it doesn't exist
if not exist ".venv" (
    echo 2. Creating virtual environment...
    python -m venv .venv
    echo    [OK] Virtual environment created
) else (
    echo 2. Virtual environment already exists
)
echo.

REM Activate virtual environment
echo 3. Activating virtual environment...
call .venv\Scripts\activate.bat
echo    [OK] Virtual environment activated
echo.

REM Upgrade pip
echo 4. Upgrading pip...
python -m pip install --upgrade pip setuptools wheel
echo    [OK] pip upgraded
echo.

REM Install dependencies
echo 5. Installing dependencies...
pip install -r requirements.txt
echo    [OK] Dependencies installed
echo.

REM Verify installation
echo 6. Verifying installation...
python -c "import aiohttp, asyncio, datasync; print('   [OK] All packages imported successfully')"
echo.

REM Display environment information
echo 7. Environment Information:
echo    Python executable: 
python -c "import sys; print('   ' + sys.executable)"
echo    Python version: 
python --version
echo.

echo ========================================================================
echo Setup complete! Virtual environment is ready.
echo ========================================================================
echo.
echo Next steps:
echo   - Run tests: run_tests.bat
echo   - Run corrected examples: python test_corrected_example1.py
echo.
pause
