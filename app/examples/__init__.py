"""
Flask Sing App - Examples Blueprint

This blueprint contains 50+ demo pages from the Sing App HTML5 template.
It can be disabled by setting ENABLE_EXAMPLES=false in .env
"""
from flask import Blueprint

examples_bp = Blueprint('examples', __name__)

# Import routes after blueprint creation to avoid circular imports
from app.examples import routes  # noqa: E402, F401
