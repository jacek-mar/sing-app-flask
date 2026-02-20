"""
Flask Sing App - Main Blueprint Routes
"""
from flask import render_template
from app.main import main_bp
from app.utils import conditional_login_required


@main_bp.route('/')
@conditional_login_required
def index():
    """
    Main dashboard - Analytics page.
    
    This is the core page that is always enabled regardless of ENABLE_EXAMPLES.
    """
    return render_template('main/index.html',
        title='Sing App Dashboard',
        active_page='dashboard_analytics',
        page_title='Analytics',
        page_subtitle='Company Performance')
