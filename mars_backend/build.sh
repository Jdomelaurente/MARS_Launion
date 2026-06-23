#!/usr/bin/env bash
# build.sh — Render build script for mars_backend (Django)

set -o errexit

echo "=== Step 1: Install Python dependencies ==="
pip install -r requirements.txt

echo "=== Step 2: Collect static files ==="
python manage.py collectstatic --no-input

echo "=== Step 3: Apply database migrations ==="
python manage.py migrate

echo "=== Step 4: Create default admin account ==="
python create_admin.py

echo "=== Build complete ==="
