"""
Flask Sing App - Examples Blueprint

This blueprint contains 50+ demo pages from the Sing App HTML5 template.
It can be disabled by setting ENABLE_EXAMPLES=false in .env
"""
from flask import Blueprint, redirect, url_for, request, current_app
from flask_login import current_user

examples_bp = Blueprint('examples', __name__)


@examples_bp.before_request
def require_login_if_configured():
    """
    Enforce login for all example routes when REQUIRE_LOGIN=true.
    No-op in demo mode (REQUIRE_LOGIN=false).
    """
    if current_app.config.get('REQUIRE_LOGIN') and not current_user.is_authenticated:
        return redirect(url_for('auth.login', next=request.url))


# Import routes after blueprint creation to avoid circular imports
from app.examples import routes  # noqa: E402, F401
