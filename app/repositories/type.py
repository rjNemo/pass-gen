from typing import Protocol

from app.models.password import Password


class Repository(Protocol):
    def save(self, service: str, password: str) -> None:
        ...

    def list_all(self) -> list[Password]:
        ...

    def exists(self, service: str) -> bool:
        ...
