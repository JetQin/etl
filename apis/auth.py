# from functools import wraps
# from flask import jsonify, request
# from starter import jwt
# from flask_jwt_extended import (
#     jwt_required, create_access_token,
#     verify_jwt_in_request, create_refresh_token,
#     get_jwt_identity, get_jwt_claims
# )
#
#
# def admin_required(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         verify_jwt_in_request()
#         claims = get_jwt_claims()
#         if claims['roles'] != 'admin':
#             return jsonify(msg='Admins only!'), 403
#         else:
#             return fn(*args, **kwargs)
#     return wrapper
#
# # Create a function that will be called whenever create_access_token
# # is used. It will take whatever object is passed into the
# # create_access_token method, and lets us define what custom claims
# # should be added to the access token.
# @jwt.user_claims_loader
# def add_claims_to_access_token(user):
#     return {'roles': user.roles}
#
#
# # Create a function that will be called whenever create_access_token
# # is used. It will take whatever object is passed into the
# # create_access_token method, and lets us define what the identity
# # of the access token should be.
# @jwt.user_identity_loader
# def user_identity_lookup(user):
#     return user.username
#
#
# @app.route('/login', methods=['POST'])
# def login():
#     username = request.json.get('username', None)
#     password = request.json.get('password', None)
#     # if username != 'test' or password != 'test':
#     #     return jsonify({"msg": "Bad username or password"}), 401
#
#     # Create an example UserObject
#     if username == 'admin':
#         user = UserObject(username='test', roles=['foo', 'admin'])
#     else:
#         user = UserObject(username='test', roles=['foo', 'bar'])
#     # We can now pass this complex object directly to the
#     # create_access_token method. This will allow us to access
#     # the properties of this object in the user_claims_loader
#     # function, and get the identity of this object from the
#     # user_identity_loader function.
#     access_token = create_access_token(identity=user)
#     refresh_token = create_refresh_token(identity=user)
#     ret = {'access_token': access_token, 'refresh_token': refresh_token}
#     return jsonify(ret), 200
#
#
# @app.route('/protected', methods=['GET'])
# @jwt_required
# @admin_required
# def protected():
#     ret = {
#         'current_identity': get_jwt_identity(),  # test
#         'current_roles': get_jwt_claims()['roles']  # ['foo', 'bar']
#     }
#     return jsonify(ret), 200
#
