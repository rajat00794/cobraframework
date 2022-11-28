from abc import ABC
from typing import List, Any


class TestRunner(ABC):
    def run(self, tests: List[function]) -> Any:
        return

    def run_with_coverage(self, tests: List[function]) -> Any:
        return

    def reports_(self, type_: str) -> Any:
        return
