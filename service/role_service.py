from starter import db
from model import Role


class RoleService:

    def __init__(self):
        self.db = db

    def create_role(self, role):
        self.db.session.add(role)
        self.db.session.commit()

    def is_exist(self, name):
        role = self.find_role_by_name(name)
        return role is not None

    def update_role(self, role):
        current_role = Role.query.filter_by(id=role.id).first()
        for key, value in role.as_dict().items():
            if value is not None:
                setattr(current_role, key, value)
        db.session.commit()

    def delete_role(self, id):
        role = Role.query.filter_by(id=id).first()
        self.db.session.delete(role)
        self.db.session.commit()

    def find_role_by_id(self, id):
        role = Role.query.filter_by(id=id).first()
        return role.as_dict() if role else None

    def find_role_by_name(self, name):
        return Role.query.filter_by(name=name).first()

    def list_user(self):
        return {'roles': [role.as_dict() for role in Role.query.all()]}

