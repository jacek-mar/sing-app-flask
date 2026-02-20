"""Flask Sing App - Admin Blueprint Routes"""
from flask import render_template, redirect, url_for, flash, abort, request, current_app
from flask_login import login_required, current_user
from app.admin import admin_bp
from app.admin.forms import UserForm
from app.models import User
from app.extensions import db
from app.utils import conditional_login_required


def admin_required(f):
    """Decorator: requires both login and is_admin=True."""
    from functools import wraps

    @wraps(f)
    def decorated(*args, **kwargs):
        if current_app.config.get('REQUIRE_LOGIN'):
            if not current_user.is_authenticated:
                return redirect(url_for('auth.login', next=request.url))
            if not current_user.is_admin:
                abort(403)
        return f(*args, **kwargs)
    return decorated


@admin_bp.route('/users')
@admin_required
def users_list():
    users = User.query.order_by(User.id).all()
    return render_template('admin/users_list.html',
                           title='User Management',
                           active_page='admin_users',
                           users=users)


@admin_bp.route('/users/new', methods=['GET', 'POST'])
@admin_required
def user_create():
    form = UserForm()
    if form.validate_on_submit():
        if User.query.filter(
            (User.username == form.username.data) |
            (User.email == form.email.data)
        ).first():
            flash('Username or email already exists.', 'warning')
            return redirect(url_for('admin.user_create'))
        user = User(
            username=form.username.data,
            email=form.email.data,
            is_admin=form.is_admin.data,
            is_active=form.is_active.data,
        )
        if form.password.data:
            user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'User "{user.username}" created.', 'success')
        return redirect(url_for('admin.users_list'))
    return render_template('admin/user_form.html',
                           title='New User',
                           active_page='admin_users',
                           form=form,
                           action='Create')


@admin_bp.route('/users/<int:user_id>/edit', methods=['GET', 'POST'])
@admin_required
def user_edit(user_id):
    user = User.query.get_or_404(user_id)
    form = UserForm(obj=user)
    if form.validate_on_submit():
        user.username = form.username.data
        user.email = form.email.data
        user.is_admin = form.is_admin.data
        user.is_active = form.is_active.data
        if form.password.data:
            user.set_password(form.password.data)
        db.session.commit()
        flash(f'User "{user.username}" updated.', 'success')
        return redirect(url_for('admin.users_list'))
    return render_template('admin/user_form.html',
                           title=f'Edit {user.username}',
                           active_page='admin_users',
                           form=form,
                           action='Update',
                           user=user)


@admin_bp.route('/users/<int:user_id>/delete', methods=['POST'])
@admin_required
def user_delete(user_id):
    user = User.query.get_or_404(user_id)
    if user.username == 'admin':
        flash('Cannot delete the default admin user.', 'danger')
        return redirect(url_for('admin.users_list'))
    db.session.delete(user)
    db.session.commit()
    flash(f'User "{user.username}" deleted.', 'success')
    return redirect(url_for('admin.users_list'))
