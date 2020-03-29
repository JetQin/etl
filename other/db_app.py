# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from model import User
# from datetime import datetime
#
# # app = Flask(__name__)
# # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://dbuser:dbuser@localhost:3306/etl'
# # db = SQLAlchemy(app)
#
#
# # class User(db.Model):
# #     id = db.Column(db.Integer, primary_key=True)
# #     username = db.Column(db.String(80), unique=True, nullable=False)
# #     email = db.Column(db.String(120), unique=True, nullable=False)
# #
# #     def __repr__(self):
# #         return '<User %r>' % self.username
#
#
#
# from app import create_app, db
#
# app = create_app()
#
# @app.route('/')
# def hello_world():
#     return 'Hello, World!'
#
#
# @app.route("/init")
# def init():
#     with app.app_context():
#         db.create_all()
#         admin = User(username='admin', email='admin@example.com', created_time=datetime.now())
#         guest = User(username='guest', email='guest@example.com', created_time=datetime.now())
#
#         db.session.add(admin)
#         db.session.add(guest)
#         db.session.commit()
#
#
# if __name__ == "__main__":
#     app.run(debug=True)
