#!/bin/bash

# Deployment script for PythonAnywhere

echo "=== Starting Deployment ==="

# Update code from repository
echo "Updating code from repository..."
git pull origin main

# Install/update dependencies
echo "Installing/updating dependencies..."
pip install -r requirements.txt

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Clear cache if using Memcached
# echo "Clearing cache..."
# python manage.py clear_cache

echo "=== Deployment Complete ==="
echo "Please reload your web app from the PythonAnywhere Web tab"
