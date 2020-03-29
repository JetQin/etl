from starter import db
from model import User


class UserService:

    def __init__(self):
        self.db = db

    def create_user(self, user):
        self.db.session.add(user)
        self.db.session.commit()

    def find_user_by_id(self, id):
        return User.query.filter_by(username=id).first()

    def find_user_by_name(self, name):
        user = User.query.filter_by(username=name).first()
        return user.as_dict()

    def list_user(self):
        return [user.as_dict() for user in User.query.all()]

