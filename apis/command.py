from flask_jwt_extended import jwt_required
from flask_restplus import Namespace, Resource
cli_api = Namespace('cli', description='cli related operations')


@cli_api.route('/<string:name>')
class Command(Resource):

    @jwt_required
    @cli_api.doc('get greeting by name', security='jwt')
    def get(self, name):
        return 'Hello, {}!'.format(name)


