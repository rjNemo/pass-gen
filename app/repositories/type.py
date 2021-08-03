from typing import Protocol

from app.models.password import Password


class Repository(Protocol):
    def save(self, password: str) -> None:
        ...

    def list_all(self) -> list[Password]:
        ...
