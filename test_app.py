import click
# from apis import blueprint as api
from flask import Flask, Blueprint
from flask_restplus import Resource, Api,  Namespace, Resource, fields


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


api_v1 = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(api_v1, version='1.0', title='Greeting API', description='Greeting API')
ns = api.namespace('greeting', description='TODO operations')



# @app.cli.command('hello')
# @click.option('--name', default='World')
# def hello_command(name):
#     click.echo('Hello, {name}!')


@ns.route('/<string:name>')
# @api.param('name', 'The greeting identifier')
# @api.response(404, 'User not found')
class HelloWorld(Resource):

    @api.doc('greeting to you')
    # @api.marshal_with(greeting)
    def get(self, name='World'):
        return 'Hello, {}'.format(name)


if __name__ == '__main__':
    app.register_blueprint(api_v1)
    app.run(debug=True)
