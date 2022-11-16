from user_activity_log.business.services.user_activity_service import (
    UserActivityService,
)

from typing import Dict, List


class UserActivityServices(UserActivityService):
    """_summary_

    Args:
        UserActivityService (_type_): _description_
    """

    async def __init__(self, dbmanager: object) -> None:
        await super().__init__(dbmanager)

    async def log_activity(self, dto: object):
        """_summary_

        Args:
            dto (object): _description_

        Returns:
            _type_: _description_
        """
        return await super().log_activity(dto)

    async def logfilter(self, instance: object, value: Dict[str, str], many=False):
        """_summary_

        Args:
            instance (object): _description_
            value (Dict[str, str]): _description_
            many (bool, optional): _description_. Defaults to False.

        Returns:
            _type_: _description_
        """
        return await super().logfilter(instance, value, many)

    async def delete_logs_list(self, instance: List[object]):
        """_summary_

        Args:
            instance (List[object]): _description_

        Returns:
            _type_: _description_
        """
        return await super().delete_logs_list(instance)

    async def allogs(self, instance: object):
        """_summary_

        Args:
            instance (object): _description_

        Returns:
            _type_: _description_
        """
        return await super().allogs(instance)
