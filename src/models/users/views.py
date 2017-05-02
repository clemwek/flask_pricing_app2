from flask import Blueprint

user_blueprint = Blueprint('users', __name__)


@user_blueprint.route('/login')
def user_login():
    pass


@user_blueprint.route('/register')
def user_register():
    pass


@user_blueprint.route('/alerts')
def user_alerts():
    pass


@user_blueprint.route('/logout')
def user_logout():
    pass


@user_blueprint.route('/for_user/<string:user_id>')
def get_user_alert(user_id):
    pass
