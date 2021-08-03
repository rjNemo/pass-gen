from sqlite3 import Cursor
from typing import Any, Protocol


class DBConnector(Protocol):
    def commit(self) -> None:
        ...

    def execute(self, query: str, *args: Any) -> Cursor:
        ...
