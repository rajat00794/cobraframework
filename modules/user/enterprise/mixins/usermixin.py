"""user mixin"""
from typing import List

from modules.user.business.dtos.blacklistoken import BlacklistToken
from modules.user.business.mixins.usermixin import UserMixin as user


class UserMixin(user):
    """_summary_

    Args:
        user (_type_): _description_
    """

    def __init__(self, dbmanager: object, utils: object) -> None:
        super().__init__(dbmanager, utils)

    def create(self, dto: object) -> str:
        passh = self.utils.hash_pass(dto.password)
        dto.password = passh
        return self.dbmanager.save(dto)

    def get(self, instance: object, objectid={}) -> object:
        """_summary_

        Args:
            instance (object): _description_
            objectid (dict, optional): _description_. Defaults to {}.

        Returns:
            object: _description_
        """
        return self.dbmanager.get_one_email(instance, objectid)

    def get_id(self, instance: object, objectid={}) -> object:
        """_summary_

        Args:
            instance (object): _description_
            objectid (dict, optional): _description_. Defaults to {}.

        Returns:
            object: _description_
        """
        return self.dbmanager.get_one(instance, objectid)

    def all(self) -> List[object]:
        """_summary_

        Returns:
            List[object]: _description_
        """
        return super().all()

    def update(self, instance: object, objectid: object, data: dict) -> object:
        """_summary_

        Args:
            instance (object): _description_
            objectid (object): _description_
            data (dict): _description_

        Returns:
            object: _description_
        """
        return self.dbmanager.update_one(instance, objectid, data)

    def delete(self, instance: object, objectid: object) -> str:
        """_summary_

        Args:
            instance (object): _description_
            objectid (object): _description_

        Returns:
            str: _description_
        """
        return self.dbmanager.delete_one(instance, objectid)

    def login(self, instance: object):
        """_summary_

        Args:
            instance (object): _description_

        Returns:
            _type_: _description_
        """
        return self.dbmanager.login(instance)

    def logout(self, token: str):
        """_summary_

        Args:
            token (str): _description_

        Returns:
            _type_: _description_
        """
        data = BlacklistToken(token=token)
        return self.dbmanager.save(data)

    def get_all(self, instance):
        return self.dbmanager.get_all(instance)

    def get_permission(self, instance: object, objectid=object) -> object:
        """_summary_

        Args:
            instance (object): _description_
            objectid (_type_, optional): _description_. Defaults to object.

        Returns:
            object: _description_
        """
        return self.dbmanager.get_one(instance, objectid)

    def create_permission(self, dto: object) -> str:
        """_summary_

        Args:
            dto (object): _description_

        Returns:
            str: _description_
        """
        return self.dbmanager.save(dto)

    def get_role(self, instance: object, objectid=object) -> object:
        """_summary_

        Args:
            instance (object): _description_
            objectid (_type_, optional): _description_. Defaults to object.

        Returns:
            object: _description_
        """
        return self.dbmanager.get_one(instance, objectid)

    def create_role(self, dto: object) -> str:
        """_summary_

        Args:
            dto (object): _description_

        Returns:
            str: _description_
        """
        return self.dbmanager.save(dto)

    def reset_password(self, instance: object, objectid: object, data: dict):
        passh = self.utils.hash_pass(data["password"])
        data["password"] = passh
        return (self.dbmanager.update_one(instance, objectid, data),)
