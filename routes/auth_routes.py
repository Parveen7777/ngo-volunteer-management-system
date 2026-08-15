from flask import Blueprint, render_template, request, redirect, url_for, session
from models.user import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.get_user_by_email(email)

        if user and user['password'] == password:
            session['user'] = user['email']
            return redirect(url_for('dashboard.dashboard'))

        return render_template('login.html', error='Invalid email or password')

    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))
