"""
Flask Sing App - Configuration
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env file from project root
env_path = Path(__file__).parent / '.env'
load_dotenv(env_path)


class Config:
    """Base configuration"""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'change-me-in-development')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Feature toggles
    ENABLE_EXAMPLES = os.environ.get('ENABLE_EXAMPLES', 'true').lower() == 'true'
    ENABLE_DARK_THEME = os.environ.get('ENABLE_DARK_THEME', 'false').lower() == 'true'
    GOOGLE_MAPS_API_KEY = os.environ.get('GOOGLE_MAPS_API_KEY', '')
    
    # Asset configuration
    ASSETS_DEBUG = False
    
    # Database - will use default if not set
    @property
    def SQLALCHEMY_DATABASE_URI(self):
        return os.environ.get('DATABASE_URL', 'sqlite:///dev.db')


class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    ENV = 'development'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'
    ASSETS_DEBUG = True


class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    ENV = 'production'
    
    @property
    def SQLALCHEMY_DATABASE_URI(self):
        uri = os.environ.get('DATABASE_URL')
        if not uri:
            raise ValueError('DATABASE_URL must be set in production')
        return uri
    
    @property
    def SECRET_KEY(self):
        key = os.environ.get('SECRET_KEY')
        if not key or key == 'change-me-in-development':
            raise ValueError('A strong SECRET_KEY must be set in production')
        return key


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
