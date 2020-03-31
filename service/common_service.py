from starter import db
from typing import Type


class CommonService:

    def __init__(self):
        self.db = db

    def create(self, entity: Type[db.Model]):
        self.db.session.add(entity)
        self.db.session.commit()

    def exist(self, name):
        entity = self.find_user_by_name(name)
        return entity is not None

    def update(self, entity: Type[db.Model]):
        current_entity = entity.query.filter_by(id=entity.id).first()
        for key, value in entity.as_dict().items():
            if value is not None:
                setattr(current_entity, key, value)
        db.session.commit()

    # def delete(self, id):
    #     user = User.query.filter_by(id=id).first()
    #     self.db.session.delete(user)
    #     self.db.session.commit()
    #
    # def find_user_by_id(self, id):
    #     user = User.query.filter_by(id=id).first()
    #     return user.as_dict() if user else None
    #
    # def find_user_by_name(self, name):
    #     return User.query.filter_by(username=name).first()
    #
    # def list_user(self):
    #     return {'users': [user.as_dict() for user in User.query.all()]}

