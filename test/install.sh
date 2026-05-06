#!/bin/bash
set -e

# Update pip
python3 -m pip install --upgrade pip

# Install dependencies from requirements-docs.txt
if [ -f requirements-docs.txt ]; then
    python3 -m pip install -r requirements-docs.txt
fi
