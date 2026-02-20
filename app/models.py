"""
Flask Sing App - Database Models
"""
from datetime import datetime, timezone
from werkzeug.security import generate_password_hash, check_password_hash
from app.extensions import db


class User(db.Model):
    """
    User model for authentication and user management.
    """
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(256))
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc).replace(tzinfo=None))
    is_active = db.Column(db.Boolean, default=True)
    
    def set_password(self, password):
        """
        Set the user's password using secure hashing.
        
        Args:
            password: Plain text password
        """
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        """
        Verify the user's password.
        
        Args:
            password: Plain text password to verify
            
        Returns:
            bool: True if password matches
        """
        return check_password_hash(self.password_hash, password)
    
    def to_dict(self):
        """
        Convert user to dictionary for JSON serialization.
        
        Returns:
            dict: User data as dictionary
        """
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'is_active': self.is_active,
        }
    
    def __repr__(self):
        return f'<User {self.username}>'
