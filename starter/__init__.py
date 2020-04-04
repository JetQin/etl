import os
import yaml
import logging
from logging.config import fileConfig, dictConfig
from datetime import date, datetime
from flask import Flask
from flask.json import JSONEncoder
from flask_cors import CORS
from flask_jwt_extended import (JWTManager)
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from config.setting import configs

# dictConfig({
#     'version': 1,
#     'formatters': {
#         'default': {
#             'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
#         }
#     },
#     'handlers': {
#         'wsgi': {
#             'class': 'logging.handlers.RotatingFileHandler',
#             'level': 'INFO',
#             'filename': 'app.log',
#             'formatter': 'default',
#             'maxBytes': 10485760,
#             'backupCount': 10,
#             'encoding': 'utf-8'
#         }
#     },
#     'root': {
#         'level': 'INFO',
#         'handlers': ['wsgi']
#     }
# })

app = Flask(__name__)

# db init
db = SQLAlchemy()

# encrypt init
bcrypt = Bcrypt()

# cross origin request
cors = CORS()

# json web token support
jwt = JWTManager()

# logger config
logger = app.logger


class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        try:
            if isinstance(obj, (date, datetime)):
                return obj.isoformat()
            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        return JSONEncoder.default(self, obj)


def create_app(profile=None):
    logger.info("***create app**")
    profile = os.environ.get('profile', 'test') if profile is None else profile
    app.config.from_object(configs[profile])
    log_config = os.path.abspath('logging.yaml')
    with open(log_config) as f:
        config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)

    app.json_encoder = CustomJSONEncoder
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    cors.init_app(app)
    from apis import api_v1
    app.register_blueprint(api_v1)
    app.logger.info(app.config)
    with app.app_context():
        logger.info("init db")
        db.create_all()
    return app


