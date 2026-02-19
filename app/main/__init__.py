"""
Flask Sing App - Main Blueprint
"""
from flask import Blueprint

main_bp = Blueprint('main', __name__)

# Import routes after blueprint creation to avoid circular imports
from app.main import routes  # noqa: E402, F401
