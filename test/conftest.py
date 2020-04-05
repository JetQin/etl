import pytest
from flask_jwt_extended import JWTManager, create_access_token
from starter import create_app


@pytest.fixture(scope="session")
def app():
    app = create_app('test')
    return app


@pytest.fixture(scope="session")
def jwt(app):
    with app.app_context():
        return JWTManager(app)


@pytest.fixture(scope="session")
def access_token(app, jwt):
    with app.app_context():
        access_token = create_access_token({'username': 'admin', 'role': 'admin'})
        return access_token


@pytest.fixture
def client(app, access_token):
    client = app.test_client()
    client.environ_base['HTTP_AUTHORIZATION'] = access_token
    return client
