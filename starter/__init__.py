import os
import logging
from datetime import date, datetime
from flask import Flask
from flask.json import JSONEncoder
from flask_cors import CORS
from flask_jwt_extended import (JWTManager)
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from config.setting import configs


logger = logging.getLogger(__name__)
app = Flask(__name__)

# db init
db = SQLAlchemy()

# encrypt init
bcrypt = Bcrypt()

# cross origin request
cors = CORS()

# json web token support
jwt = JWTManager()


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


def create_app():
    print("***create app**")
    profile = os.environ.get('profile', 'test')
    app.config.from_object(configs[profile])
    app.json_encoder = CustomJSONEncoder
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    cors.init_app(app)
    # api.init_app(app)
    from apis import api_v1
    app.register_blueprint(api_v1)
    logger.info(app.config)
    with app.app_context():
        print("init db")
        db.create_all()
    return app


# FlaskInjector(app=app, modules=[configure])