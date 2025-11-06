#!/usr/bin/env bash
# Simple setup script for Linux/macOS
python3 -m venv .venv
. .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
