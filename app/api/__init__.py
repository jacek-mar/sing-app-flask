"""
Flask Sing App - API Blueprint
"""
from flask import Blueprint

api_bp = Blueprint('api', __name__)

# Import routes after blueprint creation to avoid circular imports
from app.api import routes  # noqa: E402, F401
