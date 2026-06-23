#!/usr/bin/env bash
# build.sh — Render build script for mars_backend (Django)
# Render runs this script every time you deploy.

set -o errexit  # Exit immediately if any command fails

# 1. Install Python dependencies
pip install -r requirements.txt

# 2. Collect static files (whitenoise serves them)
python manage.py collectstatic --no-input

# 3. Apply any pending database migrations
python manage.py migrate
