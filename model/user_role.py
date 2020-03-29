import flask_bcrypt
from starter import db


association_table = db.Table('ETL_USER_ROLE',
                             db.Column('USER_ID', db.Integer, db.ForeignKey('ETL_USER.id'), primary_key=True),
                             db.Column('ROLE_ID', db.Integer, db.ForeignKey('ETL_ROLE.id'), primary_key=True))


class User(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "ETL_USER"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True)
    password_hash = db.Column(db.String(100))
    email = db.Column(db.String(255), unique=True, nullable=False)
    created_time = db.Column(db.DateTime, nullable=False)

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password_hash, password)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns if c.name != 'password_hash'}

    def __repr__(self):
        return "<User(id='%d', username='%s', email='%s')>" % (self.ID, self.USERNAME, self.EMAIL)


class Role(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "ETL_ROLE"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.String(100), unique=True)
    created_time = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return "<Role(id='%d', name='%s')>" % (self.id, self.name)



