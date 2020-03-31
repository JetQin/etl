from functools import wraps
from flask import jsonify
from flask_jwt_extended import (
    verify_jwt_in_request, get_jwt_claims
)
from starter import jwt


def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt_claims()
        if claims['roles'] != 'admin':
            return jsonify(msg='Admins only!'), 403
        else:
            return fn(*args, **kwargs)

    return wrapper


@jwt.user_claims_loader
def add_claims_to_access_token(user):
    return {'roles': user.roles}


@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.username
