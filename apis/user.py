from datetime import datetime
from flask_restplus import Resource, Namespace, fields
from model.user_role import User
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
user_id_parser.add_argument('id', type=int, required=True, help='user id', location='form')


@user_api.route('/list')
class UserList(Resource):

    def __init__(self, api=user_api):
        self.api = api
        self.service = UserService()

    @user_api.doc(description='retrieve user list')
    # @user_api.marshal_with(list_user_dto)
    def get(self):
        return self.service.list_user()


@user_api.route('/')
class User(Resource):

    def __init__(self, api=user_api):
        self.api = api
        self.service = UserService()

    @user_api.doc(description='retrieve user by user name', parser=user_id_parser)
    @user_api.marshal_with(user_dto)
    def get(self):
        args = user_id_parser.parse_args()
        id = args['id']
        user = self.service.find_user_by_id(id)
        if not user:
            user_api.abort(204)

        return user

    @user_api.doc(description='create user', parser=user_parser)
    @user_api.marshal_with(user_dto)
    def post(self):
        args = user_parser.parse_args()
        name = args['username']
        password = args['password']
        email = args['email']
        user = User(username=name, password_hash=password, email=email, created_time=datetime.now())
        # user = User(name, password, email, datetime.now())
        self.service.create_user(user)
        return self.service.find_user_by_name(name)
