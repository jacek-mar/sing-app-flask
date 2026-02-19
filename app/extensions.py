"""
Flask Sing App - Extensions
"""
from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy
db = SQLAlchemy()


def init_extensions(app):
    """
    Initialize Flask extensions for the application.
    
    Args:
        app: Flask application instance
    """
    # Initialize SQLAlchemy
    db.init_app(app)
    
    # Initialize Flask-Assets (optional - for SCSS compilation)
    _init_assets(app)
    
    app.logger.info('Flask extensions initialized.')


def _init_assets(app):
    """
    Initialize Flask-Assets for optional SCSS compilation.
    
    Falls back to prebuilt CSS if libsass is not available.
    """
    try:
        from flask_assets import Environment, Bundle
        from pathlib import Path
        
        assets = Environment(app)
        scss_path = Path(app.static_folder) / 'scss'
        
        if scss_path.exists():
            css_bundle = Bundle(
                'scss/application.scss',
                filters='libsass',
                output='css/application.min.css',
                depends=['scss/**/*.scss']
            )
            assets.register('css_all', css_bundle)
            app.logger.info('Flask-Assets SCSS bundle registered.')
        else:
            app.logger.info('No scss/ directory found - using prebuilt CSS.')
            
    except ImportError:
        app.logger.info('libsass not available - using prebuilt CSS.')
    except Exception as e:
        app.logger.warning(f'Asset initialization failed: {e}')
