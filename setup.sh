#!/bin/bash
# setup.sh - Setup script for DataSync Pro v2.0 development environment

echo "========================================================================"
echo "DataSync Pro v2.0 - Environment Setup"
echo "========================================================================"
echo ""

# Check Python version
echo "1. Checking Python version..."
python_version=$(python --version 2>&1)
echo "   $python_version"
echo ""

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "2. Creating virtual environment..."
    python -m venv .venv
    echo "   ✓ Virtual environment created"
else
    echo "2. Virtual environment already exists"
fi
echo ""

# Activate virtual environment
echo "3. Activating virtual environment..."
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    source .venv/Scripts/activate
else
    source .venv/bin/activate
fi
echo "   ✓ Virtual environment activated"
echo ""

# Upgrade pip
echo "4. Upgrading pip..."
python -m pip install --upgrade pip setuptools wheel
echo "   ✓ pip upgraded"
echo ""

# Install dependencies
echo "5. Installing dependencies..."
pip install -r requirements.txt
echo "   ✓ Dependencies installed"
echo ""

# Verify installation
echo "6. Verifying installation..."
python -c "import aiohttp, asyncio, datasync; print('   ✓ All packages imported successfully')"
echo ""

# Display environment information
echo "7. Environment Information:"
echo "   Python executable: $(which python)"
echo "   Python version: $(python --version)"
echo "   Virtual environment: $(echo $VIRTUAL_ENV)"
echo ""

echo "========================================================================"
echo "Setup complete! Virtual environment is ready."
echo "========================================================================"
echo ""
echo "Next steps:"
echo "  - Run tests: bash run_tests.sh"
echo "  - Run corrected examples: python test_corrected_example1.py"
echo ""
