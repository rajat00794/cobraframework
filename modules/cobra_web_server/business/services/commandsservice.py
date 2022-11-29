import abc
from typing import List, Optional


class CommandService(abc.ABC):
    @abc.abstractmethod
    def __init__(self, app: object, type_: Optional[str] = None) -> None:
        self.app = app
        self.type = type_

    @abc.abstractmethod
    def get_existing_commands(self) -> List[function]:
        return

    @abc.abstractmethod
    def load_cobra_commands(self) -> List[function]:
        return

    def all_commands_service(self) -> List[function]:
        if self.type is None:
            return self.load_cobra_commands()
        else:
            return self.get_existing_commands()
