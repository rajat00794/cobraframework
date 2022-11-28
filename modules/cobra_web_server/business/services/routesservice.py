from abc import ABC
import abc
from typing import List, Dict


class Routeservice(ABC):
    @abc.abstractmethod
    def __init__(self, services: List[Dict[str, object]], utils: object) -> None:
        pass

    @abc.abstractmethod
    def routes(self) -> List[object]:
        return
