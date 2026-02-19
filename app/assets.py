"""
Flask Sing App - Asset Bundles Configuration

Defines SCSS/CSS and JS bundles for the application using Flask-Assets.
"""
from flask_assets import Bundle, Environment

def init_assets(app):
    """Initialize Flask-Assets with SCSS compilation."""
    assets = Environment(app)
    
    # Ensure output directory exists
    import os
    static_dir = app.config.get('STATIC_DIR', 'static')
    css_output_dir = os.path.join(static_dir, 'css')
    os.makedirs(css_output_dir, exist_ok=True)
    
    # SCSS/CSS Bundles
    # Main application styles
    main_scss = Bundle(
        'sass/application.scss',
        output='css/application.css',
        filters=['libsass'],
        depends=['sass/**/*.scss']
    )
    
    # Dark theme styles
    dark_scss = Bundle(
        'sass/application-dark.scss',
        output='css/application-dark.css',
        filters=['libsass'],
        depends=['sass/**/*.scss']
    )
    
    # Register CSS bundles
    assets.register('main_css', main_scss)
    assets.register('dark_css', dark_scss)
    
    # JavaScript Bundles
    # Main app JavaScript
    main_js = Bundle(
        'js/app.js',
        output='js/app.min.js',
        filters='rjsmin'
    )
    
    # Register JS bundles
    assets.register('main_js', main_js)
    
    return assets
