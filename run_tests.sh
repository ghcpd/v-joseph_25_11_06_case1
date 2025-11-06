#!/usr/bin/env bash

# Start a simple HTTP server to serve files from test_server
python -m http.server --directory test_server 8000 &
SERVER_PID=$!

# Allow server to come up
sleep 1

# Run tests
python -m pip install -r requirements.txt
python test_files/test_quickstart_corrected.py
python test_files/test_cache_corrected.py
python test_files/test_advanced_corrected.py

# Stop server
kill $SERVER_PID
