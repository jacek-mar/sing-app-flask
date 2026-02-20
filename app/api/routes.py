"""
Flask Sing App - API Blueprint Routes
"""
from flask import jsonify, current_app
from app.api import api_bp
from app.models import User


@api_bp.route('/users')
def get_users():
    """
    Get list of active users.
    
    Returns:
        JSON array of user objects
    """
    users = User.query.filter_by(is_active=True).limit(50).all()
    return jsonify([u.to_dict() for u in users])


@api_bp.route('/settings')
def get_settings():
    """
    Get application settings.
    
    Returns:
        JSON object with theme and UI settings
    """
    return jsonify({
        'theme': 'light' if not current_app.config.get('ENABLE_DARK_THEME') else 'dark',
        'sidebar': 'static',
        'notifications': 13,
    })


@api_bp.route('/notifications')
def get_notifications():
    """
    Get list of notifications.
    
    Returns:
        JSON array of notification objects
    """
    return jsonify([
        {
            'type': 'user',
            'avatar': '/static/demo/img/people/a3.jpg',
            'text': '1 new user just signed up!',
            'time': '2 mins ago'
        },
        {
            'type': 'system',
            'icon': 'fa-solid fa-upload',
            'text': '2.1.0-pre-alpha just released.',
            'time': '5h ago'
        },
        {
            'type': 'system',
            'icon': 'fa-bolt',
            'text': 'Server load limited.',
            'time': '7h ago'
        },
    ])


@api_bp.route('/messages')
def get_messages():
    """
    Get list of messages.
    
    Returns:
        JSON array of message objects
    """
    return jsonify([
        {
            'from': 'Philip Smith',
            'avatar': '/static/demo/img/people/a5.jpg',
            'text': 'Hey, are you there?',
            'time': '12:18 AM'
        },
    ])
