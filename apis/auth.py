from flask import Response
from flask_restplus import Resource, Namespace, fields
from flask_jwt_extended import (
    jwt_required, create_access_token, create_refresh_token, get_raw_jwt,
    get_jwt_identity, jwt_refresh_token_required
)
from service import UserService, is_token_revoked, revoke_token, add_token_to_database
from starter import app, jwt, logger


auth_api = Namespace('auth', description='authorization related operations')
login_parser = auth_api.parser()
login_parser.add_argument('username', type=str, required=True, help='user name', location='form')
login_parser.add_argument('password', type=str, required=True, help='password', location='form')


@jwt.token_in_blacklist_loader
def check_if_token_revoked(decoded_token):
    return is_token_revoked(decoded_token)


@auth_api.route('/login')
class AuthLogin(Resource):

    def __init__(self, api=auth_api):
        self.api = api
        self.service = UserService()

    @auth_api.doc(description='login auth', parser=login_parser)
    def post(self):
        args = login_parser.parse_args()
        name = args['username']
        password = args['password']
        logger.info("user %s login", name)
        user = self.service.find_user_by_name(name)
        if user and user.check_password(password):
            access_token = create_access_token(identity=user.id)
            refresh_token = create_refresh_token(identity=user.id)
            # Store the tokens in our store with a status of not currently revoked.
            add_token_to_database(access_token, app.config['JWT_IDENTITY_CLAIM'])
            add_token_to_database(refresh_token, app.config['JWT_IDENTITY_CLAIM'])
            ret = {'access_token': access_token, 'refresh_token': refresh_token}
            return ret
        else:
            return Response('Auth failed')


@auth_api.route('/logout')
class AuthLogout(Resource):

    @jwt_required
    @auth_api.doc(security='jwt')
    def post(self):
        jwt = get_raw_jwt()
        current_user = get_jwt_identity()
        logger.info("user %s logout", current_user)
        revoke_token(jti=jwt['jti'], user=current_user)
        return Response('Logout successfully')


@auth_api.route('/refresh')
class AuthRefresh(Resource):

    @jwt_refresh_token_required
    @auth_api.doc(security='jwt')
    def post(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user)
        logger.info("user %s refresh token", current_user)
        add_token_to_database(access_token, app.config['JWT_IDENTITY_CLAIM'])
        ret = {'access_token': access_token }
        return ret
