from typing import List

from modules.user_activity_log.business.services.user_activity_log import (
    VentureService as venture,
)


class UserActivityServices(venture):
    """_summary_

    Args:
        venture (_type_): _description_
    """

    def __init__(self, dbmanager: object, mixin: object) -> None:
        """_summary_

        Args:
            dbmanager (object): _description_
            mixin (object): _description_
        """
        super().__init__(dbmanager, mixin)
