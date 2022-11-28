from abc import ABC
import abc

from typing import *


class AutoTestService(ABC):
    @abc.abstractmethod
    def __init__(self, app: object, utils: object) -> None:
        pass

    def load_test_conf(self) -> Dict[str, Any]:
        return

    def test_routes_functions(self) -> List[function]:
        return

    def test_apps_utils(self) -> Union[List[function], None]:
        return

    def test_other_validations(self) -> Union[List[function], None]:
        return

    def all_test_functions(self) -> List[Dict[str, List[function]]]:
        return
