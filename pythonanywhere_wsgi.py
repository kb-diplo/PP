# This file contains the WSGI configuration required to serve your web application
# It works by setting the 'application' callable to a Django WSGI application

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Add your project directory to the Python path
path = '/home/mbugualawrence/Personal-portfolio'
if path not in sys.path:
    sys.path.append(path)

# Load environment variables from .env file
env_path = os.path.join(path, '.env')
if os.path.exists(env_path):
    load_dotenv(env_path)

# Set environment variables
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'
os.environ['PYTHONPATH'] = path

# Activate the virtualenv if needed
activate_this = '/home/mbugualawrence/.virtualenvs/portfolio_env/bin/activate_this.py'
if os.path.exists(activate_this):
    with open(activate_this) as f:
        exec(f.read(), {'__file__': activate_this})

# Import Django's WSGI handler
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
