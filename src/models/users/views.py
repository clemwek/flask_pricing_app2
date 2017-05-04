from flask import Blueprint, request, session, url_for, render_template
from werkzeug.utils import redirect

from src.models.users.user import User
import src.models.users.errors as UserErrors

user_blueprint = Blueprint('users', __name__)


@user_blueprint.route('/login', methods=['GET', 'POST'])
def user_login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['hashed']

        try:
            if User.is_login_valid(email, password):
                session['email'] = email
                return redirect(url_for('.user_alerts'))
        except UserErrors.UserError as e:
            return e.message
    return render_template('users/loin.html')


@user_blueprint.route('/register', methods=['GET', 'POST'])
def user_register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['hashed']

        try:
            if User.register_user(email, password):
                session['email'] = email
                return redirect(url_for('.user_alerts'))
        except UserErrors.UserError as e:
            return e.message
    return render_template('users/register.html')


@user_blueprint.route('/alerts')
def user_alerts():
    return 'We are getting here'


@user_blueprint.route('/logout')
def user_logout():
    pass


@user_blueprint.route('/for_user/<string:user_id>')
def get_user_alert(user_id):
    pass
