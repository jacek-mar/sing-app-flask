"""
Flask Sing App - Extensions
"""
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_caching import Cache
from flask_compress import Compress

# Initialize SQLAlchemy
db = SQLAlchemy()

# Initialize Flask-Login
login_manager = LoginManager()

# Initialize Flask-Migrate
migrate = Migrate()

# Initialize Flask-Caching
cache = Cache()

# Initialize Flask-Compress
compress = Compress()


def init_extensions(app):
    """
    Initialize Flask extensions for the application.

    Flask-Assets is initialized separately in app.assets via create_app().
    """
    db.init_app(app)
    migrate.init_app(app, db)

    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Please log in to access this page.'
    login_manager.login_message_category = 'warning'

    # Initialize Flask-Caching
    cache.init_app(app)

    # Initialize Flask-Compress
    compress.init_app(app)

    # Apply security middleware based on SECURITY_LEVEL
    _apply_security(app)

    app.logger.info('Flask extensions initialized.')


def _apply_security(app):
    """
    Apply security middleware based on SECURITY_LEVEL config.

    demo        — CSRF on forms (handled by Flask-WTF automatically)
    basic       — demo + rate limiting on auth routes
    production  — basic + secure HTTP headers
    """
    level = app.config.get('SECURITY_LEVEL', 'demo')

    if level in ('basic', 'production'):
        try:
            from flask_limiter import Limiter
            from flask_limiter.util import get_remote_address
            limiter = Limiter(
                app=app,
                key_func=get_remote_address,
                default_limits=[]   # no global limit; applied per route
            )
            app.extensions['limiter'] = limiter
            app.logger.info('Rate limiting enabled (SECURITY_LEVEL=%s).', level)
        except ImportError:
            app.logger.warning('Flask-Limiter not installed; rate limiting skipped.')

    if level == 'production':
        try:
            from flask_talisman import Talisman
            Talisman(
                app,
                force_https=False,   # set True behind a TLS-terminating proxy
                strict_transport_security=True,
                session_cookie_secure=True,
                content_security_policy={
                    'default-src': "'self'",
                    'script-src': ["'self'", "'unsafe-inline'", "cdnjs.cloudflare.com",
                                   "cdn.jsdelivr.net", "unpkg.com", "code.jquery.com"],
                    'style-src': ["'self'", "'unsafe-inline'", "cdnjs.cloudflare.com",
                                  "cdn.jsdelivr.net"],
                    'img-src': ["'self'", "data:"],
                    'font-src': ["'self'", "cdnjs.cloudflare.com"],
                }
            )
            app.logger.info('Secure headers applied (SECURITY_LEVEL=production).')
        except ImportError:
            app.logger.warning('Flask-Talisman not installed; secure headers skipped.')
