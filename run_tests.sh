#!/usr/bin/env bash
set -e
. .venv/bin/activate
python test_files/quick_start.py
python test_files/cache_test.py
python test_files/advanced_test.py

echo "All tests finished."