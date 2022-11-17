from typing import List, Optional

from modules.venture_capital.business.mixins.venturemixin import VentureMixin as venture


class UserActivityMixin(venture):
    """_summary_

    Args:
        VentureMixin (_type_): _description_
    """

    def __init__(self, dbmanager: object, utils: Optional[object] = None) -> None:
        """_summary_

        Args:
            dbmanager (object): _description_
            utils (Optional[object], optional): _description_. Defaults to None.
        """
        super().__init__(dbmanager, utils)

    def create(self, dto: object) -> str:
        return self.dbmanager.save(dto)

    def get(self, instance: object, objectid: object) -> object:
        """_summary_

        Args:
            instance (object): _description_
            objectid (object): _description_

        Returns:
            object: _description_
        """
        return self.dbmanager.get_one(instance, objectid)
