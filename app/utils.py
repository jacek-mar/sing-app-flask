"""
Flask Sing App - Utility Functions
"""
from functools import wraps
from flask import redirect, url_for, request, current_app
from flask_login import current_user


def conditional_login_required(f):
    """
    Enforces login only when REQUIRE_LOGIN=true in config.

    In demo mode (REQUIRE_LOGIN=false, the default), all routes are accessible
    without authentication. When REQUIRE_LOGIN=true, unauthenticated users are
    redirected to /auth/login with the original URL preserved in ?next=.

    Usage:
        @main_bp.route('/')
        @conditional_login_required
        def index():
            ...
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_app.config.get('REQUIRE_LOGIN') and not current_user.is_authenticated:
            return redirect(url_for('auth.login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function
