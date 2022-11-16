import abc
from typing import Dict, List
from user_activity_log.business.dtos.response import ResponseActivity


class UserActivityService(abc.ABC):
    """_summary_

    Args:
        abc (_type_): _description_

    Returns:
        _type_: _description_
    """

    @abc.abstractmethod
    async def __init__(self, dbmanager: object) -> None:
        self.dbmanager = dbmanager

    @abc.abstractmethod
    async def log_activity(self, dto: object):
        """_summary_

        Args:
            dto (object): _description_

        Returns:
            _type_: _description_
        """
        return await self.dbmanager.save(dto)

    @abc.abstractmethod
    async def logfilter(self, instance: object, value: Dict[str, str], many=False):
        """_summary_

        Args:
            instance (object): _description_
            value (Dict[str,str]): _description_

        Returns:
            _type_: _description_
        """
        if not many:
            if "id" in value.keys():
                return await self.dbmanager.get_one(instance, value)
            else:
                return await self.dbmanager.get_one_email(instance, value)
        else:
            return await self.dbmanager.get_all(instance, value)

    @abc.abstractmethod
    async def allogs(self, instance: object):
        """_summary_

        Args:
            instance (object): _description_

        Returns:
            _type_: _description_
        """
        return await self.dbmanager.get_all(instance)

    @abc.abstractmethod
    async def delete_logs_list(self, instance: List[object]):
        """_summary_

        Args:
            instance (List[object]): _description_

        Returns:
            _type_: _description_
        """
        res = []
        for i in instance:
            item = await self.dbmanager.delete_one(i, dict(id=str(i.id)))
            if isinstance(item, i):
                res.append(item.id)
            else:
                res.append(item.error)
        return ResponseActivity(data=res)
