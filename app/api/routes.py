"""
Flask Sing App - API Blueprint Routes
"""
from flask import jsonify, request, current_app
from app.api import api_bp
from app.models import User
from app.extensions import db


# ── Error handlers (JSON instead of HTML for API consumers) ──────────────────

@api_bp.errorhandler(404)
def api_not_found(e):
    return jsonify(error='Not Found', message=str(e)), 404


@api_bp.errorhandler(405)
def api_method_not_allowed(e):
    return jsonify(error='Method Not Allowed'), 405


@api_bp.errorhandler(400)
def api_bad_request(e):
    return jsonify(error='Bad Request', message=str(e)), 400


# ── Users ─────────────────────────────────────────────────────────────────────

@api_bp.route('/users', methods=['GET'])
def get_users():
    """List users. Supports ?page= and ?per_page= query parameters."""
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 20, type=int), 100)
    query = User.query.filter_by(is_active=True).order_by(User.id)
    pagination = query.paginate(page=page, per_page=per_page, error_out=False)
    return jsonify({
        'users': [u.to_dict() for u in pagination.items],
        'total': pagination.total,
        'page': pagination.page,
        'pages': pagination.pages,
    })


@api_bp.route('/users', methods=['POST'])
def create_user():
    """Create a user. Expects JSON: {username, email, password}."""
    data = request.get_json(silent=True)
    if not data:
        return jsonify(error='JSON body required'), 400
    required = ('username', 'email', 'password')
    missing = [f for f in required if not data.get(f)]
    if missing:
        return jsonify(error=f'Missing fields: {", ".join(missing)}'), 400
    if User.query.filter(
        (User.username == data['username']) | (User.email == data['email'])
    ).first():
        return jsonify(error='Username or email already exists'), 409
    user = User(username=data['username'], email=data['email'])
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict()), 201


@api_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify(user.to_dict())


@api_bp.route('/users/<int:user_id>', methods=['PUT', 'PATCH'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.get_json(silent=True) or {}
    if 'email' in data:
        user.email = data['email']
    if 'is_active' in data:
        user.is_active = bool(data['is_active'])
    if 'password' in data and data['password']:
        user.set_password(data['password'])
    db.session.commit()
    return jsonify(user.to_dict())


@api_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return '', 204


# ── Existing stub endpoints (unchanged) ──────────────────────────────────────

@api_bp.route('/settings')
def get_settings():
    return jsonify({
        'theme': 'dark' if current_app.config.get('ENABLE_DARK_THEME') else 'light',
        'sidebar': 'static',
        'notifications': 13,
    })


@api_bp.route('/notifications')
def get_notifications():
    return jsonify([
        {'type': 'user', 'avatar': '/static/demo/img/people/a3.jpg',
         'text': '1 new user just signed up!', 'time': '2 mins ago'},
        {'type': 'system', 'icon': 'fa-solid fa-upload',
         'text': '2.1.0-pre-alpha just released.', 'time': '5h ago'},
        {'type': 'system', 'icon': 'fa-solid fa-bolt',
         'text': 'Server load limited.', 'time': '7h ago'},
    ])


@api_bp.route('/messages')
def get_messages():
    return jsonify([
        {'from': 'Philip Smith', 'avatar': '/static/demo/img/people/a5.jpg',
         'text': 'Hey, are you there?', 'time': '12:18 AM'},
    ])
