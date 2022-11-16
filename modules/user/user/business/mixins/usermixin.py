"""user mixin"""
import abc
from typing import List, Optional


class UserMixin(abc.ABC):
    """_summary_

    Args:
        abc (_type_): _description_
    """

    def __init__(self, dbmanager: object, utils: Optional[object] = None) -> None:
        self.dbmanager = dbmanager
        self.utils = utils

    @abc.abstractmethod
    def create(self, dto: object) -> str:
        """_summary_

        Args:
            dto (object): _description_

        Returns:
            str: _description_
        """
        return

    @abc.abstractmethod
    def get(self, objectid: object) -> object:
        """_summary_

        Args:
            objectid (object): _description_

        Returns:
            object: _description_
        """
        return

    @abc.abstractmethod
    def all(self) -> List[object]:
        """_summary_

        Returns:
            List[object]: _description_
        """
        return

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
        return

    @abc.abstractmethod
    def delete(self, instance: object, objectid: object) -> str:
        """_summary_

        Args:
            instance (object): _description_
            objectid (object): _description_

        Returns:
            str: _description_
        """
        return

    @abc.abstractmethod
    def login(self, instance: object):
        """_summary_

        Args:
            instance (object): _description_
        """
        return

    @abc.abstractmethod
    def logout(self, token: object):
        """_summary_

        Args:
            token (object): _description_
        """
        return

    @abc.abstractmethod
    def get_all(self, instance):
        """_summary_

        Args:
            instance (_type_): _description_
        """
        return

    @abc.abstractmethod
    def get_id(self, instance, objectid):
        """_summary_

        Args:
            instance (_type_): _description_
            objectid (_type_): _description_
        """
        return
