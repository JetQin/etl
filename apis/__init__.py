from flask import  Blueprint
from flask_restplus import Api
from apis.auth import auth_api as auth_ns
from apis.command import cli_api as cli_ns
from apis.user import user_api as user_ns
from apis.role import role_api as role_ns
from apis.metrics import metrics_api as metrics_ns

authorizations = {
    'jwt': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

api_v1 = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(api_v1, title='ETL App', version='1.0', description='ETL Flask App Best Practice', authorizations=authorizations)

api.add_namespace(auth_ns)
api.add_namespace(cli_ns)
api.add_namespace(user_ns)
api.add_namespace(role_ns)
api.add_namespace(metrics_ns)
