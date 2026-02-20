"""
Flask Sing App - Application Factory

This module creates and configures the Flask application.
"""
import os
from flask import Flask, render_template


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
    
    # Register blueprints
    _register_blueprints(app)
    
    # Register CLI commands
    _register_cli(app)
    
    # Register context processors
    @app.context_processor
    def inject_globals():
        """Inject global variables into template context"""
        return {
            'app_name': 'Sing App',
            'app_version': '1.0.0'
        }
    
    # Register error handlers
    @app.errorhandler(404)
    def page_not_found(e):
        """Handle 404 errors"""
        return render_template('errors/404.html'), 404
    
    @app.errorhandler(500)
    def internal_error(e):
        """Handle 500 errors"""
        return render_template('errors/500.html'), 500
    
    app.logger.info(f'Flask Sing App initialized in {config_name} mode.')
    
    return app


def _register_blueprints(app):
    """
    Register Flask blueprints with the application.
    
    The examples blueprint is conditionally registered based on ENABLE_EXAMPLES config.
    """
    from app.main import main_bp
    from app.api import api_bp
    
    # Register main blueprint (core dashboard - always enabled)
    app.register_blueprint(main_bp)
    
    # Register API blueprint
    app.register_blueprint(api_bp, url_prefix='/api')
    
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
            u = User(username='admin', email='admin@example.com')
            u.set_password('admin')
            db.session.add(u)
            db.session.commit()
            print('Sample user created: admin / admin')
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
