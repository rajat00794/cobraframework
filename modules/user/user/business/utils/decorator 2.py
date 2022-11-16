# from functools import wraps
# from flask import abort
# import jwt
# import os

# class PermissionData:
#     def __init__(self,dbmanager,instance) -> None:
#         self.dbmanager=dbmanager
#         self.instance=instance

#     def token_required(self,permission,request):
#         if not 'Authorization' in request.headers:
#                abort(401)

#         user = None
#         data = request.headers['Authorization'].encode('ascii','ignore')
#         token = str.replace(str(data), 'Bearer ','')
#         try:
#             user = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=['HS256'])['sub']
#         except:
#             abort(401)
#         data=self.dbmanager.get_one(self.instance,dict(email=user['email']))
#         if data:

# def token_required(f,permission,request,checkpms:function):
#     @wraps(f)
#     def decorated_function(*args, **kws):
#             if not 'Authorization' in request.headers:
#                abort(401)

#             user = None
#             data = request.headers['Authorization'].encode('ascii','ignore')
#             token = str.replace(str(data), 'Bearer ','')
#             try:
#                 user = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=['HS256'])['sub']
#             except:
#                 abort(401)
#             checkpms(permission,user)
#             return f(user, *args, **kws)
#     return decorated_function
