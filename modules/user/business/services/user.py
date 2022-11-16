"""user service"""
import abc
from typing import List


class UserService(abc.ABC):
    """_summary_

    Args:
        abc (_type_): _description_
    """

    def __init__(self, dbmanager: object, usermixin: object) -> None:
        self.dbmanager = dbmanager
        self.mixin = usermixin

    @abc.abstractmethod
    def create(self, dto: object) -> str:
        """_summary_

        Args:
            dto (object): _description_

        Returns:
            str: _description_
        """
        return self.mixin.create(dto)

    @abc.abstractmethod
    def get(self, instance: object, objectid: dict) -> object:
        """_summary_

        Args:
            instance (object): _description_
            objectid (dict): _description_

        Returns:
            object: _description_
        """
        return self.mixin.get(instance, objectid)

    @abc.abstractmethod
    def all(self) -> List[object]:
        """_summary_

        Returns:
            List[object]: _description_
        """
        return self.mixin.all()

    @abc.abstractmethod
    def update(self, instance: object, objectid: object, data: dict) -> object:
        """_summary_

        Args:
            instance (object): _description_
            objectid (object): _description_
            data (dict): _description_

        Returns:
            object: _description_
        """
        return self.mixin.update(instance, objectid, data)

    @abc.abstractmethod
    def delete(self, instance: object, objectid: object) -> str:
        """_summary_

        Args:
            instance (object): _description_
            objectid (object): _description_

        Returns:
            str: _description_
        """
        return self.mixin.delete(instance, objectid)

    @abc.abstractmethod
    def login(self, instance: object) -> str:
        """_summary_

        Args:
            instance (object): _description_

        Returns:
            str: _description_
        """
        return self.mixin.login(instance)

    @abc.abstractmethod
    def logout(self, token: object):
        """_summary_

        Args:
            token (object): _description_

        Returns:
            _type_: _description_
        """
        return self.mixin.logout(token)

    @abc.abstractmethod
    def get_all(self, instance):
        """_summary_

        Args:
            instance (_type_): _description_

        Returns:
            _type_: _description_
        """
        return self.mixin.get_all(instance)

    @abc.abstractmethod
    def get_id(self, instance, objectid):
        """_summary_

        Args:
            instance (_type_): _description_
            objectid (_type_): _description_

        Returns:
            _type_: _description_
        """
        return self.mixin.get_id(instance, objectid)

    @abc.abstractmethod
    def create_permission(self, dto: object) -> str:
        """_summary_

        Args:
            dto (object): _description_

        Returns:
            str: _description_
        """
        return self.mixin.create_permission(dto)

    @abc.abstractmethod
    def get_permission(self, instance, objectid):
        """_summary_

        Args:
            instance (_type_): _description_
            objectid (_type_): _description_

        Returns:
            _type_: _description_
        """
        return self.mixin.get_permission(instance, objectid)

    @abc.abstractmethod
    def create_role(self, dto: object) -> str:
        """_summary_

        Args:
            dto (object): _description_

        Returns:
            str: _description_
        """
        return self.mixin.create_role(dto)

    @abc.abstractmethod
    def get_role(self, instance, objectid):
        """_summary_

        Args:
            instance (_type_): _description_
            objectid (_type_): _description_

        Returns:
            _type_: _description_
        """
        return self.mixin.get_role(instance, objectid)

    def reset_password(self, instance: object, objectid: object, data: dict):
        """_summary_

        Args:
            instance (object): _description_
            objectid (object): _description_
            data (dict): _description_

        Returns:
            _type_: _description_
        """
        return self.mixin.reset_password(instance, objectid, data)
