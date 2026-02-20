"""
WSGI entry point for production servers (gunicorn, uWSGI, etc.).

Usage:
    gunicorn wsgi:app
    gunicorn wsgi:app --bind 0.0.0.0:$PORT --workers 2
"""
import os
from dotenv import load_dotenv

load_dotenv()

from app import create_app

app = create_app(os.environ.get('FLASK_CONFIG', 'production'))
