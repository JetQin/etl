from starter import db
from model import User


class UserService:

    def __init__(self):
        self.db = db

    def create_user(self, user):
        self.db.session.add(user)
        self.db.session.commit()

    def is_exist(self, name):
        user = self.find_user_by_name(name)
        return user is not None

    def update_user(self, user):
        current_user = User.query.filter_by(id=user.id).first()
        for key, value in user.as_dict().items():
            if value is not None:
                setattr(current_user, key, value)
        db.session.commit()

    def delete_user(self, id):
        user = User.query.filter_by(id=id).first()
        self.db.session.delete(user)
        self.db.session.commit()

    def find_user_by_id(self, id):
        user = User.query.filter_by(id=id).first()
        return user.as_dict() if user else None

    def find_user_by_name(self, name):
        return User.query.filter_by(username=name).first()

    def list_user(self):
        return {'users': [user.as_dict() for user in User.query.all()]}

