class Config:
    profile = 'development'
    host = 'localhost'


class DevConfig(Config):
    profile = 'development'
    host = 'dev-localhost'

    mysql = {
        'username': 'dbuser',
        'password': 'dbuser'
    }


class TestConfig(Config):
    profile = 'test'
    host = 'test-localhost'
    mysql = {
        'username': 'dbuser',
        'password': 'dbuser'
    }


class ProdConfig(Config):
    profile = 'prod'
    host = 'prod-localhost'
    mysql = {
        'username': 'dbuser',
        'password': 'dbuser'
    }