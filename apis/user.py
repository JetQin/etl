from flask import Response
from flask_jwt_extended import jwt_required
from flask_restplus import Resource, Namespace, fields
from model import User
from service import UserService

user_api = Namespace('user', description='user related operations')
user_dto = user_api.model('User', {
    'id': fields.Integer(required=True, description='user id'),
    'email': fields.String(required=True, description='user email'),
    'username': fields.String(required=True, description='user name'),
    'created_time': fields.String(description='user created time')
})

list_user_dto = user_api.model('ListUser', {
    'users': fields.Nested(user_dto, description='The User')
})

user_parser = user_api.parser()
user_parser.add_argument('email', type=str, required=True, help='email', location='form')
user_parser.add_argument('username', type=str, required=True, help='user name', location='form')
user_parser.add_argument('password', type=str, required=True, help='password', location='form')

user_id_parser = user_api.parser()
user_id_parser.add_argument('id', type=int, required=True, help='user id', location='args')

update_use_parser = user_api.parser()
update_use_parser.add_argument('id', type=int, required=True, help='id', location='form')
update_use_parser.add_argument('email', type=str, required=False, help='email', location='form')
update_use_parser.add_argument('username', type=str, required=False, help='username', location='form')
update_use_parser.add_argument('password', type=str, required=False, help='password', location='form')


user_role_parser = user_api.parser()
user_role_parser.add_argument('user_id', type=int, required=True, help='user id', location='args')
user_role_parser.add_argument('role_id', type=list, required=False, help='user id', location='args')


@user_api.route('/list')
class UserList(Resource):

    def __init__(self, api=user_api):
        self.api = api
        self.service = UserService()

    @jwt_required
    @user_api.doc(description='retrieve user list', security='jwt')
    @user_api.marshal_with(list_user_dto)
    def get(self):
        return self.service.list_user()


@user_api.route("/assign")
class UserRole(Resource):
    def __init__(self, api=user_api):
        self.api = api
        self.service = UserService()

    @jwt_required
    @user_api.doc(description='assign role to user', parser=user_role_parser, security='jwt')
    @user_api.marshal_with(user_dto)
    def post(self):
        try:
            args = user_role_parser.parse_args()
            user_id = args['user_id']
            role_id = args['role_id']
            self.service.assign_role(user_id, role_id)
            return self.service.find_user_by_id(user_id)
        except:
            user_api.abort(500, 'Server error')


@user_api.route("/")
class UserCreate(Resource):

    def __init__(self, api=user_api):
        self.api = api
        self.service = UserService()

    @jwt_required
    @user_api.doc(description='create user', parser=user_parser, security='jwt')
    @user_api.marshal_with(user_dto)
    def post(self):
        args = user_parser.parse_args()
        name = args['username']
        password = args['password']
        email = args['email']
        if not self.service.is_exist(name):
            self.service.create_user(User(username=name, password=password, email=email))
            return self.service.find_user_by_name(name)
        else:
            user_api.abort(202, 'User already exist')

    @jwt_required
    @user_api.doc(description='retrieve user by user id', parser=user_id_parser, security='jwt')
    @user_api.marshal_with(user_dto)
    def get(self):
        args = user_id_parser.parse_args()
        id = args['id']
        user = self.service.find_user_by_id(id)
        if not user:
            user_api.abort(Response('No user found'))
        return user

    @jwt_required
    @user_api.doc(description='update user', parser=update_use_parser, security='jwt')
    def put(self):
        args = update_use_parser.parse_args()
        id = args['id']
        email = args['email']
        username = args['username']
        password = args['password']
        self.service.update_user(User(id=id, email=email, username=username, password=password))
        return self.service.find_user_by_id(id)

    @jwt_required
    @user_api.doc(description='delete user', parser=user_id_parser, security='jwt')
    def delete(self):
        args = user_id_parser.parse_args()
        id = args['id']
        self.service.delete_user(id)
        return Response("delete success")
