"""user route"""
import asyncio
from datetime import datetime
from datetime import timedelta
from flask import request
from flask_openapi3 import APIBlueprint
from infrastructure.server.app.application import user_tag
from infrastructure.server.app.application.service import (
    Path,
    ResetPassword,
    Response,
    ResponseHandler,
    UserLogin,
    permission,
    email_sender,
    OtpSender,
    otp_generator,
    send_phone_otp,
    OtpVerify,
)

from infrastructure.shared_di.di import obj_graph
from modules.user.business.dtos.permission import Permission
from modules.user.business.dtos.role import Role
from modules.user.business.dtos.user import User
from modules.user.business.dtos.otp import Otp
from modules.user.business.utils.password import Password
from modules.user.business.utils.token import Token
from modules.user.enterprise.services.user import UserServices
from adaptors.mongodb.mongoadaptor import DataBaseManager

user_bp = APIBlueprint(
    "/user", __name__, url_prefix="/api", abp_tags=[user_tag], doc_ui=True
)


@user_bp.post(
    "user/",
    responses={"201": Response},
    description="User create API takes firstname, lastname, email, password"
    "that is required to create user. Role field assigned role of user",
)
async def user_create(body: User):
    """This API create User"""
    service = obj_graph.provide(UserServices)
    data = service.create(body)
    awt = await data
    return ResponseHandler(request, awt).response(201), 201


@user_bp.get(
    "/user/getall/",
    responses={"200": Response},
    description="User get all provide all user and detail about User",
)
@permission("user_getall")
async def user_getall():
    """This API get all User"""
    service = obj_graph.provide(UserServices)
    data = await service.get_all(User)
    return ResponseHandler(request, data).response(200), 200


@user_bp.get(
    "user/get/<id>/",
    responses={"200": Response},
    description="User get takes user id and give a detail about of user",
)
@permission("user_get")
async def user_get(path: Path):
    """This API get User by ID"""
    service = obj_graph.provide(UserServices)
    data = await service.get_id(User, dict(id=path.id))
    return ResponseHandler(request, data).response(200), 200


@user_bp.put(
    "user/update/<id>/",
    responses={"206": Response},
    description="User update takes User ID to update the connected ID user",
)
@permission("user_put")
async def user_put(path: Path):
    """This API update User"""
    data = request.json
    service = obj_graph.provide(UserServices)
    data = service.update(User, dict(id=path.id), data)
    awt = await data
    return ResponseHandler(request, awt).response(206), 206


@user_bp.delete(
    "user/delete/<id>/",
    responses={"204": Response},
    description="User delete takes ID of user which wants to delete",
)
@permission("user_delete")
async def user_delete(path: Path):
    """This API delete user"""
    service = obj_graph.provide(UserServices)
    data = request.json
    data = service.delete(User, dict(id=path.id))
    await data
    return (
        ResponseHandler(
            request, dict(id=path.id, msg="data deleted succesfully")
        ).response(204),
        204,
    )


@user_bp.post(
    "user/login/",
    responses={"200": Response},
    description="User login provide a token and refresh token for using any API permission of",
)
async def user_login(body: UserLogin):
    """This API login user"""
    service = obj_graph.provide(UserServices)
    obj = await service.get(User, objectid=dict(email=body.email))
    if obj is None:
        return (
            ResponseHandler(
                request,
                await service.dbmanager.errors(
                    "email or password is invalid", obj.id, User
                ),
            ).response(400),
            400,
        )
    if obj.verfiy is False:
        return (
            ResponseHandler(
                request,
                await service.dbmanager.errors("phone not verified", obj.id, User),
            ).response(401),
            401,
        )
    if obj.email == body.email:

        if Password().check_pass(body.password, obj.password):
            data2 = Password().check_pass(body.password, obj.password)
            if data2:
                token = Token().generate_auth_tokens(body.dict())
                return ResponseHandler(request, token).response(200), 200
    else:
        return (
            ResponseHandler(
                request,
                await service.dbmanager.errors(
                    "email or password is invalid", obj.id, User
                ),
            ).response(400),
            400,
        )


@user_bp.get(
    "user/logout/",
    responses={"401": Response},
    description="User logout provide us facility to blacklist the token",
)
@permission("user_logout")
async def user_logout():
    """This API logout user"""
    auth_token = request.headers.get("Authorization")
    if auth_token:
        auth_token = str.replace(str(auth_token), "Bearer ", "")
    service = obj_graph.provide(UserServices)
    data = await service.logout(auth_token)
    return ResponseHandler(request, data).response(401), 401


@user_bp.post(
    "permission/",
    responses={"201": Response},
    description="Permission provide a user having which tpye of permission to access the API",
)
@permission("permission_create")
async def permission_create(body: Permission):
    """This API provide permission of user"""
    service = obj_graph.provide(UserServices)
    data = service.create_permission(body)
    awt = await data
    return ResponseHandler(request, awt).response(201), 201


@user_bp.get(
    "permission/get/<id>/",
    responses={"200": Response},
    description="Permission get show us which tpye of permission user having",
)
@permission("permission_get")
async def permission_get(path: Path):
    """This API Show Permission"""
    service = obj_graph.provide(UserServices)
    data = await service.get_permission(Permission, dict(id=path.id))
    return ResponseHandler(request, data).response(200), 200


@user_bp.post(
    "role/",
    responses={"201": Response},
    description="User role assign the role of user and what they access in API",
)
@permission("role_create")
async def role_create(body: Role):
    """This API assign role of user"""
    service = obj_graph.provide(UserServices)
    data = request.json
    data = service.create_role(body)
    awt = await data
    return ResponseHandler(request, awt).response(201), 201


@user_bp.get(
    "role/get/<id>/",
    responses={"200": Response},
    description="Role get API provide user role and Accessibility of user",
)
@permission("role_get")
async def role_get(path: Path):
    """This API Show role of user"""
    service = obj_graph.provide(UserServices)
    data = await service.get_role(Role, dict(id=path.id))
    return ResponseHandler(request, data).response(200), 200


@user_bp.post(
    "user/password_reset/",
    responses={"201": Response},
    description="User reset_password provide a token and refresh token for using any API permission of",
)
async def password_reset(body: ResetPassword):
    """This API user reset password"""
    service = obj_graph.provide(UserServices)
    try:
        obj = await service.get(User, objectid=dict(email=body.email))
    except Exception as Ex:
        return Ex, 404
    if isinstance(obj, User):
        res = dict(email=obj.email, id=str(obj.id))
    else:
        return (
            ResponseHandler(
                request, service.dbmanager.errors("object not found", obj, User)
            ).response(404),
            404,
        )
    awt = await email_sender(
        "rajatm@thoughtwin.com",
        **{
            "subject": "te",
            "text": f"here is your password reset link: {request.base_url}/user/password_confirm/{Token().generate_acess_token(res)}",
        },
    )
    return ResponseHandler(request, res).response(206), 206


@user_bp.put(
    "user/password_confirm/<id>",
    responses={"200": Response},
    description="User reset_password_confirm provide a token and refresh token for using any API permission of",
)
async def reset_password_confirm(path: Path, body: ResetPassword):
    service = obj_graph.provide(UserServices)
    res = {"id": Token().decode_token(path.id)}
    try:
        data = service.update(User, res, body.dict())
    except Exception as e:
        return e, 404
    print(data)
    awt = data
    return ResponseHandler(request, awt).response(206), 206


@user_bp.post("user/sendotp/", responses={"200": Response}, description="otp sender")
async def send_otp_email_phone(body: OtpSender):
    """
    Args:
        body (OtpSender): _description_
    """
    otp = otp_generator()
    data = Otp(otp=otp, user_id=body.user_id, created_at=datetime.now())
    obj = obj_graph.provide(DataBaseManager)
    da = await obj.save(data)
    awt = await email_sender(
        "rajatm@thoughtwin.com", **{"subject": "otp", "text": f"otp:{otp}"}
    )
    try:
        send_phone_otp(body.phone, otp)
    except Exception as a:
        res["phone"] = a
    return ResponseHandler(request, da).response(200), 200


@user_bp.post("user/verifyotp/", responses={"201": Response}, description="otp verify")
async def verify_otp_phone_email(body: OtpVerify):
    """_summary_

    Args:
        body (OtpVerify): _description_

    Returns:
        _type_: _description_
    """
    obj = obj_graph.provide(DataBaseManager)
    print(type(body.user_id), "dddd")
    da = await obj.get_one_email(Otp, dict(user_id=body.user_id))
    ltime = da.created_at + timedelta(seconds=da.expire_time)
    if ltime > datetime.now():
        if da.otp == body.otp:
            us = await obj.update_one(User, dict(id=body.user_id), dict(verfiy=True))
            das = await obj.delete_one(Otp, dict(id=da.id))
            return ResponseHandler(request, us).response(206), 206
        else:
            return ResponseHandler(request, dict(otp="invalid otp")).response(401), 401

    else:
        return ResponseHandler(request, dict(otp="otp expired")).response(401), 401
