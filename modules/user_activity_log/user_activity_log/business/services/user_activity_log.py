import abc


class UserActivityService(abc.ABC):
    """_summary_

    Args:
        abc (_type_): _description_
    """

    def __init__(self, dbmanager: object, mixin: object) -> None:
        self.dbmanager = dbmanager
        self.mixin = mixin

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
    def get(self, instance: object, objectid: object) -> object:
        """_summary_

        Args:
            instance (object): _description_
            objectid (object): _description_

        Returns:
            object: _description_
        """
        return self.mixin.get(instance, objectid)
