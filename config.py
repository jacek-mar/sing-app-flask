"""
Flask Sing App - Configuration
"""
import os


class Config:
    """Base configuration"""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'change-me-in-development')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///dev.db')

    # Feature toggles
    ENABLE_EXAMPLES = os.environ.get('ENABLE_EXAMPLES', 'true').lower() == 'true'
    ENABLE_DARK_THEME = os.environ.get('ENABLE_DARK_THEME', 'false').lower() == 'true'
    GOOGLE_MAPS_API_KEY = os.environ.get('GOOGLE_MAPS_API_KEY', '')

    # Asset configuration
    ASSETS_DEBUG = False

    # --- NEW: Authentication toggles ---
    # false = demo mode (no login required); true = enforce login on all pages
    REQUIRE_LOGIN = os.environ.get('REQUIRE_LOGIN', 'false').lower() == 'true'
    # false = registration form hidden; true = /auth/register is accessible
    ENABLE_REGISTRATION = os.environ.get('ENABLE_REGISTRATION', 'false').lower() == 'true'

    # --- NEW: Security level ---
    # demo     = CSRF on forms only (default — no friction for evaluators)
    # basic    = demo + rate limiting on login (5 attempts/minute)
    # production = basic + secure headers (HSTS, X-Frame-Options, CSP)
    SECURITY_LEVEL = os.environ.get('SECURITY_LEVEL', 'demo')

    # CSRF always enabled (Flask-WTF); only disabling in tests
    WTF_CSRF_ENABLED = True


class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'
    ASSETS_DEBUG = True


class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', '')
    SECRET_KEY = os.environ.get('SECRET_KEY', '')


class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    WTF_CSRF_ENABLED = False


# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig,
}
