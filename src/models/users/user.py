import uuid

from src.common.database import Database
from src.common.utils import Utils
import src.models.users.errors as UserErrors


class User(object):
    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return '<User {}>'.format(self.email)

    @staticmethod
    def is_login_valid(email, password):
        """
        
        :param email: 
        :param password: 
        :return: 
        """
        user_data = Database.find_one("users", {"email": email})
        if user_data is None:
            raise UserErrors.UserNotExistError('Your user does not exist')
        if not Utils.check_hashed_password(password, user_data['password']):
            raise UserErrors.IncorrectPasswordError('your password is not correct')
        return True

    @staticmethod
    def register_user(email, password):
        """
        
        :param email: 
        :param password: 
        :return: 
        """
        user_data = Database.find_one('users', {"email": email})

        if user_data is not None:
            raise UserErrors.UserAlreadyRegisteredError('Your email has already been used.')
        if not Utils.email_is_valid(email):
            raise UserErrors.InvalidEmailError('You are not using a valid email.')

        User(email, Utils.hash_password(password)).save_to_db()

        return True

    def save_to_db(self):
        Database.insert("users", self.json())

    def json(self):
        return {
            "_id": self._id,
            "email": self.email,
            "password": self.password
        }
