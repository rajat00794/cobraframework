import abc
from typing import Optional


class UserActivityMixin(abc.ABC):
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
