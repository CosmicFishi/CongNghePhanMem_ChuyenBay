from functools import wraps
from flask import session, request, redirect, url_for
from flask_login import current_user
from saleapp.models import UserRole

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            return redirect('/admin' )

        return f(*args, **kwargs)

    return decorated_function


def login_admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated and current_user.type_user == UserRole.ADMIN:
            return f(*args, **kwargs)
        else:
            return redirect('/admin' )

    return decorated_function


def login_staff_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated and current_user.type_user == UserRole.STAFF:
            return f(*args, **kwargs)
        else:
            return redirect('/login-staff')

    return decorated_function