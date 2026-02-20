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


@main_bp.route('/settings')
@conditional_login_required
def settings():
    """
    Settings page - displays current configuration.
    
    Shows all configurable settings and their current values.
    This page is only visible when user is logged in (or REQUIRE_LOGIN=false).
    """
    from flask import current_app
    
    # Get configuration values to display
    config_items = {
        'Application': {
            'Version': current_app.config.get('APP_VERSION', '1.0.0'),
            'Environment': current_app.config.get('FLASK_CONFIG', 'development'),
        },
        'Features': {
            'Demo Mode': 'Enabled' if current_app.config.get('DEMO_MODE') else 'Disabled',
            'Examples': 'Enabled' if current_app.config.get('ENABLE_EXAMPLES') else 'Disabled',
            'Dark Theme Default': 'Enabled' if current_app.config.get('ENABLE_DARK_THEME') else 'Disabled',
        },
        'Security': {
            'Require Login': 'Yes' if current_app.config.get('REQUIRE_LOGIN') else 'No (Demo Mode)',
            'Registration': 'Enabled' if current_app.config.get('ENABLE_REGISTRATION') else 'Disabled',
            'Security Level': current_app.config.get('SECURITY_LEVEL', 'demo'),
        },
        'Performance': {
            'Cache Type': current_app.config.get('CACHE_TYPE', 'SimpleCache'),
            'Compression': 'Enabled' if current_app.config.get('COMPRESS_MIMETYPES') else 'Disabled',
        },
    }
    
    return render_template('main/settings.html',
        title='Settings',
        active_page='settings',
        page_title='System Settings',
        page_subtitle='Configuration Overview',
        config_items=config_items)
