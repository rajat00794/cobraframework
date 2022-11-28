from abc import ABC
import abc

from typing import *


class AutoTestService(ABC):
    @abc.abstractmethod
    def __init__(self, app: object, utils: object) -> None:
        pass
    @abc.abstractmethod
    def load_test_conf(self) -> Dict[str, Any]:
        return
    @abc.abstractmethod
    def test_routes_functions(self) -> List[function]:
        return

    @abc.abstractmethod
    def test_apps_utils(self) -> Union[List[function], None]:
        return

    @abc.abstractmethod
    def test_other_validations(self) -> Union[List[function], None]:
        return

    @abc.abstractmethod
    def all_test_functions(self) -> List[Dict[str, List[function]]]:
        return
