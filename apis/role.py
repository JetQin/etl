from flask import Response
from flask_jwt_extended import jwt_required
from flask_restplus import Resource, Namespace, fields
from model import Role
from service import RoleService


role_api = Namespace('role', description='role manager operations')
role_dto = role_api.model('Role', {
    'id': fields.Integer(required=True, description='role id'),
    'name': fields.String(required=True, description='role name'),
    'description': fields.String(required=True, description='role description'),
    'created_time': fields.String(description='role created time')
})

list_role_dto = role_api.model('ListRole', {
    'roles': fields.Nested(role_dto, description='the role')
})

role_parser = role_api.parser()
role_parser.add_argument('name', type=str, required=True, help='name', location='form')
role_parser.add_argument('description', type=str, required=True, help='description', location='form')

update_role_parser = role_api.parser()
update_role_parser.add_argument('id', type=str, required=True, help='id', location='form')
update_role_parser.add_argument('name', type=str, required=False, help='name', location='form')
update_role_parser.add_argument('description', type=str, required=False, help='description', location='form')


role_id_parser = role_api.parser()
role_id_parser.add_argument('id', type=int, required=True, help='user id', location='args')


@role_api.route('/list')
class RoleList(Resource):

    def __init__(self, api=role_api):
        self.api = api
        self.service = RoleService()

    @jwt_required
    @role_api.doc(description='retrieve user list', security='jwt')
    @role_api.marshal_with(list_role_dto)
    def get(self):
        return self.service.list_user()


@role_api.route("/")
class RoleCreate(Resource):

    def __init__(self, api=role_api):
        self.api = api
        self.service = RoleService()

    @jwt_required
    @role_api.doc(description='create role', parser=role_parser, security='jwt')
    @role_api.marshal_with(role_dto)
    def post(self):
        args = role_parser.parse_args()
        name = args['name']
        description = args['description']
        if not self.service.is_exist(name):
            self.service.create_role(Role(name=name, description=description))
            return self.service.find_role_by_name(name)
        else:
            return Response('role already exist')

    @jwt_required
    @role_api.doc(description='update role', parser=update_role_parser, security='jwt')
    @role_api.marshal_with(role_dto)
    def put(self):
        args = update_role_parser.parse_args()
        id = args['id']
        name = args['name']
        description = args['description']
        self.service.update_role(Role(id=id, name=name, description=description))
        return self.service.find_role_by_name(name)

    @jwt_required
    @role_api.doc(description='retrieve role by role id', parser=role_id_parser, security='jwt')
    @role_api.marshal_with(role_dto)
    def get(self):
        args = role_id_parser.parse_args()
        id = args['id']
        user = self.service.find_role_by_id(id)
        if not user:
            role_api.abort(Response('No role found'))
        return user

    @jwt_required
    @role_api.doc(description='delete role', parser=role_id_parser, security='jwt')
    def delete(self):
        args = role_id_parser.parse_args()
        id = args['id']
        self.service.delete_role(id)
        return Response("delete success")
