"""user servic"""
from typing import List

from modules.user.business.services.user import UserService


class UserServices(UserService):
    """_summary_

    Args:
        UserService (_type_): _description_
    """

    def __init__(self, dbmanager: object, usermixin: object) -> None:
        """_summary_

        Args:
            dbmanager (object): _description_
            usermixin (object): _description_
        """
        super().__init__(dbmanager, usermixin)

    def create(self, dto: object) -> str:
        """_summary_

        Args:
            dto (object): _description_

        Returns:
            str: _description_
        """
        return super().create(dto)

    def get(self, instance: object, objectid: object) -> object:
        """_summary_

        Args:
            instance (object): _description_
            objectid (object): _description_

        Returns:
            object: _description_
        """
        return super().get(instance, objectid)

    def update(self, instance: object, objectid: object, data: dict) -> object:
        """_summary_

        Args:
            instance (object): _description_
            objectid (object): _description_
            data (dict): _description_

        Returns:
            object: _description_
        """
        return super().update(instance, objectid, data)

    def all(self) -> List[object]:
        """_summary_

        Returns:
            List[object]: _description_
        """
        return super().all()

    def delete(self, instance: object, objectid: object) -> str:
        """_summary_

        Args:
            instance (object): _description_
            objectid (object): _description_

        Returns:
            str: _description_
        """
        return super().delete(instance, objectid)

    def login(self, instance: object) -> object:
        """_summary_

        Args:
            instance (object): _description_

        Returns:
            object: _description_
        """
        return super().login(instance)

    def logout(self, token: object) -> object:
        """_summary_

        Args:
            token (object): _description_

        Returns:
            object: _description_
        """
        return super().logout(token)

    def get_all(self, instance):
        """_summary_

        Args:
            instance (_type_): _description_

        Returns:
            _type_: _description_
        """
        return super().get_all(instance)

    def get_id(self, instance, objectid):
        """_summary_

        Args:
            instance (_type_): _description_
            objectid (_type_): _description_

        Returns:
            _type_: _description_
        """
        return super().get_id(instance, objectid)

    def get_permission(self, instance, objectid):
        """_summary_

        Args:
            instance (_type_): _description_
            objectid (_type_): _description_

        Returns:
            _type_: _description_
        """
        return super().get_permission(instance, objectid)

    def get_role(self, instance, objectid):
        """_summary_

        Args:
            instance (_type_): _description_
            objectid (_type_): _description_

        Returns:
            _type_: _description_
        """
        return super().get_role(instance, objectid)

    def create_permission(self, dto: object) -> str:
        """_summary_

        Args:
            dto (object): _description_

        Returns:
            str: _description_
        """
        return super().create_permission(dto)

    def create_role(self, dto: object) -> str:
        """_summary_

        Args:
            dto (object): _description_

        Returns:
            str: _description_
        """
        return super().create_role(dto)

    def reset_password(self, instance: object, objectid: object, data: dict):
        return super().reset_password(instance, objectid, data)
