from functools import wraps
from flask import session, redirect, url_for

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'user' not in session:
            return redirect(url_for('auth.login'))
        return func(*args, **kwargs)
    return wrapper

def is_logged_in():
    return 'user' in session

def logout_user():
    session.clear()
