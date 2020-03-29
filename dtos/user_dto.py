from flask_restplus import Namespace, fields

user_api = Namespace('user', description='user related operations')
user_dto = user_api.model('User', {
    'id': fields.Integer(required=True, description='user id'),
    'email': fields.String(required=True, description='user email'),
    'username': fields.String(required=True, description='user name'),
    'created_time': fields.String(required=True, description='user created time')
})
