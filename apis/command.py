from flask_restplus import Namespace, Resource
cli_api = Namespace('cli', description='cli related operations')


@cli_api.route('/<string:name>')
class Command(Resource):

    @cli_api.doc('get greeting by name')
    def get(self, name):
        return 'Hello, {}!'.format(name)

    @cli_api.doc('command line example')
    def post(self, name):
        cli_api.abort(403)

