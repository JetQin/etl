from util.encrypt_util import RSAEncryption


class Config:
    PROFILE = 'development'
    HOST = 'localhost'
    PORT = 5000
    PRIVATE_KEY_PATH = ''
    PUBLIC_KEY_PATH = ''
    DB_USERNAME = ''
    DB_PASSWORD = ''
    LOG_FILE = ''

    JWT_HEADER_TYPE = ''
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
    JWT_ISSUER = 'io.github.jetqin'
    JWT_LIFETIME_SECONDS = 600
    JWT_ALGORITHM = 'RS256'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):

    private_key_path = '/Users/jet/code/python/etl-app/config/jetqin.key'
    public_key_path = '/Users/jet/code/python/etl-app/config/jetqin.pub'
    RSA = RSAEncryption(private_key_path, public_key_path)

    with open(private_key_path) as pri_key_file:
        JWT_PRIVATE_KEY = pri_key_file.read()
    with open(public_key_path) as pub_key_file:
        JWT_PUBLIC_KEY = pub_key_file.read()

    DEBUG = True
    PROFILE = 'dev'
    HOST = 'localhost'
    DB_HOST = 'localhost'
    DB_PORT = 3306
    DB_USERNAME = '7ddc5736a04b0336854565dc0fdfa01e94469aa038957c0f314d82722b09ab1518d1f0cb4f2e93313cfe37ca4668d2395cee286ff113727a4c0c6f48b1c33cacdfbb1b5e5f7963219189a6674e6a628153c0c65ce5ffd7c7023bc9f590a20ef2951ea5da338cce2a20a75ee6be86eddead27d6b0cade570a0424fdc8a2cd8969c396c1c9a04d5dba1a371b2089d7c92cc5757a9d4a491717048619b58ab21cde476181b47869dd0f7682d858902f817b5da545f377bfe416b78da32e8a53f2e0a45af09f7ca936ac671cb795263068d1d004f198f6818fbc3c928a4d29e06f8f5ac287aba500b88f443622c484b09bc749805f4c7251b45c254514c8975bdfad'
    DB_PASSWORD = '7ddc5736a04b0336854565dc0fdfa01e94469aa038957c0f314d82722b09ab1518d1f0cb4f2e93313cfe37ca4668d2395cee286ff113727a4c0c6f48b1c33cacdfbb1b5e5f7963219189a6674e6a628153c0c65ce5ffd7c7023bc9f590a20ef2951ea5da338cce2a20a75ee6be86eddead27d6b0cade570a0424fdc8a2cd8969c396c1c9a04d5dba1a371b2089d7c92cc5757a9d4a491717048619b58ab21cde476181b47869dd0f7682d858902f817b5da545f377bfe416b78da32e8a53f2e0a45af09f7ca936ac671cb795263068d1d004f198f6818fbc3c928a4d29e06f8f5ac287aba500b88f443622c484b09bc749805f4c7251b45c254514c8975bdfad'
    DB_SCHEMA_NAME = 'etl'
    LOG_FILE = './logging.yaml'

    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{}:{}@{}:{}/{}'.format(
        RSA.decrypt(DB_USERNAME), RSA.decrypt(DB_PASSWORD), DB_HOST, DB_PORT, DB_SCHEMA_NAME)


class TestConfig(Config):

    private_key_path = '/Users/jet/code/python/etl-app/config/jetqin.key'
    public_key_path = '/Users/jet/code/python/etl-app/config/jetqin.pub'
    RSA = RSAEncryption(private_key_path, public_key_path)

    JWT_BLACKLIST_ENABLED = False
    JWT_ALGORITHM = 'RS256'
    with open(private_key_path) as pri_key_file:
        JWT_PRIVATE_KEY = pri_key_file.read()
    with open(public_key_path) as pub_key_file:
        JWT_PUBLIC_KEY = pub_key_file.read()

    DEBUG = False
    TESTING = True
    PROFILE = 'test'
    HOST = 'localhost'
    DB_HOST = 'localhost'
    DB_PORT = 3306
    DB_USERNAME = '7ddc5736a04b0336854565dc0fdfa01e94469aa038957c0f314d82722b09ab1518d1f0cb4f2e93313cfe37ca4668d2395cee286ff113727a4c0c6f48b1c33cacdfbb1b5e5f7963219189a6674e6a628153c0c65ce5ffd7c7023bc9f590a20ef2951ea5da338cce2a20a75ee6be86eddead27d6b0cade570a0424fdc8a2cd8969c396c1c9a04d5dba1a371b2089d7c92cc5757a9d4a491717048619b58ab21cde476181b47869dd0f7682d858902f817b5da545f377bfe416b78da32e8a53f2e0a45af09f7ca936ac671cb795263068d1d004f198f6818fbc3c928a4d29e06f8f5ac287aba500b88f443622c484b09bc749805f4c7251b45c254514c8975bdfad'
    DB_PASSWORD = '7ddc5736a04b0336854565dc0fdfa01e94469aa038957c0f314d82722b09ab1518d1f0cb4f2e93313cfe37ca4668d2395cee286ff113727a4c0c6f48b1c33cacdfbb1b5e5f7963219189a6674e6a628153c0c65ce5ffd7c7023bc9f590a20ef2951ea5da338cce2a20a75ee6be86eddead27d6b0cade570a0424fdc8a2cd8969c396c1c9a04d5dba1a371b2089d7c92cc5757a9d4a491717048619b58ab21cde476181b47869dd0f7682d858902f817b5da545f377bfe416b78da32e8a53f2e0a45af09f7ca936ac671cb795263068d1d004f198f6818fbc3c928a4d29e06f8f5ac287aba500b88f443622c484b09bc749805f4c7251b45c254514c8975bdfad'
    DB_SCHEMA_NAME = 'etl'
    LOG_FILE = '/Users/jet/code/python/etl-app/logging.yaml'

    SQLALCHEMY_DATABASE_URI = 'sqlite:///../etl-app.db'


configs = dict(
    dev=DevConfig(),
    test=TestConfig()
)

