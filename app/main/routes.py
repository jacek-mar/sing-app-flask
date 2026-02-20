"""
Flask Sing App - Main Blueprint Routes
"""
from flask import render_template
from flask_login import current_user
from app.main import main_bp
from app.extensions import cache
from app.utils import conditional_login_required


@main_bp.route('/')
@conditional_login_required
@cache.cached(timeout=300, unless=lambda: current_user.is_authenticated)
def index():
    """
    Main dashboard - Analytics page.
    
    This is the core page that is always enabled regardless of ENABLE_EXAMPLES.
    Cached for 5 minutes for anonymous visitors (demo mode).
    Not cached for authenticated users so personalised data can be added later.
    """
    return render_template('main/index.html',
        title='Sing App Dashboard',
        active_page='dashboard_analytics',
        page_title='Analytics',
        page_subtitle='Company Performance')
