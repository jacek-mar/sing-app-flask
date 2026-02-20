"""
Flask Sing App - Extensions
"""
from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy
db = SQLAlchemy()


def init_extensions(app):
    """
    Initialize Flask extensions for the application.

    Flask-Assets is initialized separately in app.assets via create_app().
    """
    db.init_app(app)
    app.logger.info('Flask extensions initialized.')
