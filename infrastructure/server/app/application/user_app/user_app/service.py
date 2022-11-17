"""infrastructure utilies for server use"""
import json
from functools import wraps
from typing import Any, Optional
import pydantic
from flask import request
from jwt.exceptions import ExpiredSignatureError
from infrastructure.shared_di.di import obj_graph
from modules.user.business.dtos.blacklistoken import BlacklistToken
from modules.user.business.dtos.permission import Permission
from modules.user.business.dtos.role import Role
from modules.user.business.dtos.user import User
from modules.user.business.utils.token import Token
from modules.user.enterprise.services.user import UserServices
import importlib
from flask_mailing import Message
import random as r
from adaptors.sms_service.sms import Smsservice
from adaptors.email_service.email import EmailMessage
import requests
import os


class OtpVerify(pydantic.BaseModel):
    user_id: str
    otp: int


class OtpSender(pydantic.BaseModel):
    """_summary_

    Args:
        pydantic (_type_): _description_
    """

    email: str
    phone: str
    user_id: str


class UserLogin(pydantic.BaseModel):
    """_summary_

    Args:
        pydantic (_type_): _description_
    """

    email: str
    password: str


class Path(pydantic.BaseModel):
    """_summary_

    Args:
        pydantic (_type_): _description_
    """

    id: str


class ResetPassword(pydantic.BaseModel):
    email: str


class Response(pydantic.BaseModel):
    """_summary_

    Args:
        pydantic (_type_): _description_
    """

    data: Any
    status_code: int


class ResponseHandler:
    """_summary_"""

    def __init__(self, request, data) -> None:
        """_summary_

        Args:
            request (_type_): _description_
            data (_type_): _description_
        """
        self.request = request
        self.data = data

    def response(self, status_code):
        """_summary_

        Args:
            status_code (_type_): _description_

        Returns:
            _type_: _description_
        """
        if isinstance(self.data, list):
            return Response(
                data=[json.loads(x.json()) for x in self.data], status_code=status_code
            ).json()
        else:
            if isinstance(self.data, dict):
                return Response(data=self.data, status_code=status_code).json()
            else:
                return Response(
                    data=json.loads(self.data.json()), status_code=status_code
                ).json()


class Auth:
    """_summary_

    Returns:
        _type_: _description_
    """

    @classmethod
    def get_permission_lavel(cls, request):
        """_summary_

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        authtoken = request.headers["Authorization"]
        authtoken = authtoken.replace("Bearer", "").strip()
        datatoken = Token().decode_token(authtoken)
        service = obj_graph.provide(UserServices)
        try:
            data = service.get(User, dict(email=datatoken["email"]))
        except Exception as e:
            return e, 401
        permission = []
        if isinstance(User, data):
            if data.role is not None:
                try:
                    role = service.get_id(Role, dict(id=data.role))
                except Exception as e:
                    return e, 401
                if role:
                    for i in role.permissions:
                        permission.append(i.dict())
            else:
                return dict(msg="role not found"), 401
        return dict(data=permission), 200

    @classmethod
    async def get_logged_in_user(cls, new_request):
        """_summary_

        Args:
            new_request (_type_): _description_

        Returns:
            _type_: _description_
        """
        auth_token = new_request.headers.get("Authorization")
        if auth_token:
            auth_token = str.replace(str(auth_token), "Bearer ", "")
            blu = await cls.check_blacklist(auth_token)
            if not blu:
                return dict(msg="blacklisted token"), 401
            try:
                resp = Token().decode_token(auth_token)
            except ExpiredSignatureError:
                return dict(msg="blacklisted token"), 401
            response_object = {
                "status": "success",
            }
            response_object["data"] = resp
            return response_object, 200
        else:
            response_object = {
                "status": "fail",
                "message": "Provide a valid auth token.",
            }
            return response_object, 401

    @classmethod
    async def check_blacklist(cls, token):
        """_summary_

        Args:
            token (_type_): _description_

        Returns:
            _type_: _description_
        """
        service = obj_graph.provide(UserServices)
        data = service.get(BlacklistToken, dict(token=token))
        data = await data
        if data:
            return False
        else:
            return True

    @classmethod
    async def get_user_objects(cls, new_request):
        data = await cls.get_logged_in_user(new_request)
        data = data[0]["data"]
        service = obj_graph.provide(UserServices)
        data = service.get(User, dict(email=data["email"]))
        data = await data
        return data


def permission(lavel: str):
    """_summary_

    Args:
        lavel (str): _description_
    """

    def wrapper(func):
        @wraps(func)
        async def wrapped(*args, **kwargs):
            data = await Auth.get_logged_in_user(request)
            ser = obj_graph.provide(UserServices)
            if "data" in data[0].keys():
                data = data[0].get("data")
            else:
                return dict(msg="blacklisted token"), 401
            if "email" not in data.keys():
                return dict(msg="blacklisted token"), 401
            data = ser.get(User, dict(email=data["email"]))
            data = await data
            if data.role is None:
                return dict(msg="no roles assigned"), 401
            else:
                role = ser.get_id(Role, dict(id=str(data.role)))
                role = await role
                for i in role.permissions:
                    per = ser.get_id(Permission, dict(id=str(i)))
                    per = await per
                    if per.permissionname == lavel:
                        return await func(*args, **kwargs)
            return dict(msg="not allowed"), 401

        return wrapped

    return wrapper


def str_import(module, classname):
    """_summary_

    Args:
        name (_type_): _description_

    Returns:
        _type_: _description_
    """
    module = importlib.import_module(module)
    return getattr(module, classname)


async def email_sender(mail, **kwargs):
    email = obj_graph.provide(EmailMessage)
    return await email.send_mail_async(
        [mail], kwargs.get("subject"), kwargs.get("text")
    )


def otp_generator():
    """_summary_

    Returns:
        _type_: _description_
    """
    otp = ""
    for i in range(4):
        otp += str(r.randint(1, 9))
    return int(otp)


def send_phone_otp(phone, msg):
    """_summary_

    Args:
        phone (_type_): _description_

    Returns:
        _type_: _description_
    """
    sms = obj_graph.provide(Smsservice)
    return sms.send_msg(phone, msg)
