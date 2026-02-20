"""
Flask Sing App - Application Factory

This module creates and configures the Flask application.
"""
import os
from flask import Flask, render_template, request, jsonify


def create_app(config_name='development'):
    """
    Create and configure the Flask application.
    
    Args:
        config_name: Configuration name ('development', 'production', 'testing')
        
    Returns:
        Configured Flask application instance
    """
    # Import configuration
    from config import config
    
    # Create Flask application
    app = Flask(
        __name__,
        static_folder='../static',       # Project root static/
        template_folder='../templates'   # Project root templates/
    )
    app.config.from_object(config[config_name])
    
    # Validate production configuration
    if config_name == 'production':
        if not app.config.get('SQLALCHEMY_DATABASE_URI'):
            raise RuntimeError(
                'DATABASE_URL must be set in the environment for production mode.'
            )
        if app.config.get('SECRET_KEY') in ('', 'change-me-in-development'):
            raise RuntimeError(
                'A strong SECRET_KEY must be set in the environment for production mode.'
            )
    
    # Initialize extensions
    from app.extensions import init_extensions
    init_extensions(app)
    
    # Initialize Flask-Assets (SCSS compilation)
    from app.assets import init_assets
    init_assets(app)

    # Auto-create DB tables for demo and development (production uses flask db upgrade)
    if config_name in ('demo', 'development'):
        from app.extensions import db
        with app.app_context():
            db.create_all()

    # Register blueprints
    _register_blueprints(app)
    
    # Register CLI commands
    _register_cli(app)
    
    # Register context processors
    @app.context_processor
    def inject_globals():
        """Inject global variables into template context"""
        from flask_wtf.csrf import generate_csrf
        return {
            'app_name': 'Sing App',
            'app_version': '1.0.0',
            'form_csrf': lambda: f'<input type="hidden" name="csrf_token" value="{generate_csrf()}">',
        }
    
    # Register error handlers
    @app.errorhandler(404)
    def page_not_found(e):
        """Handle 404 errors"""
        # Return JSON for API endpoints
        if request.path.startswith('/api/'):
            return jsonify(error='Not Found'), 404
        return render_template('errors/404.html'), 404
    
    @app.errorhandler(500)
    def internal_error(e):
        """Handle 500 errors"""
        return render_template('errors/500.html'), 500
    
    # Configure logging
    _configure_logging(app)
    
    # Add cache headers for static assets in production
    @app.after_request
    def add_cache_headers(response):
        """
        Add long-lived Cache-Control headers to static assets in production.
        In development (app.debug=True), do nothing so hot-reload works normally.
        """
        if app.debug:
            return response
        if response.content_type and request.path.startswith('/static/'):
            response.cache_control.max_age = 31_536_000   # 1 year
            response.cache_control.immutable = True
            response.cache_control.public = True
        return response
    
    # Health check endpoint — must respond 200 quickly for Render / load balancers
    @app.route('/health')
    def health_check():
        return 'OK', 200

    # Serve node_modules for offline assets (used by application.min.css)
    @app.route('/node_modules/<path:filename>')
    def serve_node_modules(filename):
        """Serve files from static/node_modules folder."""
        from flask import send_from_directory
        import os
        node_modules_path = os.path.join(app.root_path, '..', 'static', 'node_modules')
        return send_from_directory(node_modules_path, filename)
    
    app.logger.info(f'Flask Sing App initialized in {config_name} mode.')
    
    return app


def _register_blueprints(app):
    """
    Register Flask blueprints with the application.
    
    The examples blueprint is conditionally registered based on ENABLE_EXAMPLES config.
    """
    from app.main import main_bp
    from app.api import api_bp
    
    # Register auth blueprint — ALWAYS registered (login/logout routes must exist even in demo mode)
    from app.auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    
    # Register main blueprint (core dashboard - always enabled)
    app.register_blueprint(main_bp)
    
    # Register API blueprint
    app.register_blueprint(api_bp, url_prefix='/api')
    
    # Register admin blueprint (user management)
    from app.admin import admin_bp
    app.register_blueprint(admin_bp, url_prefix='/admin')
    
    # Register examples blueprint (conditionally)
    if app.config.get('ENABLE_EXAMPLES'):
        from app.examples import examples_bp
        app.register_blueprint(examples_bp, url_prefix='/examples')
        app.logger.info('Examples blueprint registered.')
    else:
        app.logger.info('Examples blueprint disabled via ENABLE_EXAMPLES.')


def _register_cli(app):
    """
    Register Flask CLI commands.
    """
    from app.extensions import db
    
    @app.cli.command('init-db')
    def init_db():
        """Initialize the database."""
        db.create_all()
        print('Database initialized.')
    
    @app.cli.command('seed-db')
    def seed_db():
        """Seed the database with sample data."""
        if not app.config.get('ENABLE_EXAMPLES'):
            print('ENABLE_EXAMPLES is False — skipping seed.')
            return
        
        from app.models import User
        
        if User.query.count() == 0:
            u = User(username='admin', email='admin@example.com', is_admin=True)
            u.set_password('admin')
            db.session.add(u)
            db.session.commit()
            print('Sample user created: admin / admin (is_admin=True)')
        else:
            print('Database already has users — skipping seed.')
    
    @app.cli.command('compile-assets')
    def compile_assets():
        """Compile SCSS to CSS using Flask-Assets."""
        from flask_assets import Environment
        
        # Get existing Environment instance from app.extensions
        assets = app.extensions.get('assets')
        if assets is None:
            # Create new if not found (e.g., when running CLI directly)
            assets = Environment(app)
        
        print('Compiling SCSS assets...')
        try:
            assets['main_css'].build()
            print('  Created: static/css/application.css')
            assets['dark_css'].build()
            print('  Created: static/css/application-dark.css')
            print('SCSS compilation complete!')
        except KeyError as e:
            print(f'Bundle not found: {e}. Check app/assets.py bundle registration.')
        except Exception as e:
            print(f'Error compiling assets: {e}')
    
    @app.cli.command('clear-cache')
    def clear_cache():
        """Clear all Flask-Caching entries."""
        from app.extensions import cache
        cache.clear()
        print('Cache cleared.')


def _configure_logging(app):
    """
    Attach a rotating file handler in development mode.
    """
    import logging
    from logging.handlers import RotatingFileHandler
    import os

    if not app.debug:
        return  # production logging handled by WSGI server / syslog

    log_dir = os.path.join(os.path.dirname(app.root_path), 'logs')
    os.makedirs(log_dir, exist_ok=True)
    handler = RotatingFileHandler(
        os.path.join(log_dir, 'app.log'), maxBytes=1_000_000, backupCount=3
    )
    handler.setFormatter(logging.Formatter('[%(asctime)s] %(levelname)s %(module)s: %(message)s'))
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('Logging initialized.')
