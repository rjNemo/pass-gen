from typing import Protocol

from app.models.password import Password


class Repository(Protocol):
    def save(self, service: str, password: str) -> None:
        ...  # pragma nocover

    def list_all(self) -> list[Password]:
        ...  # pragma nocover

    def exists(self, service: str) -> bool:
        ...  # pragma nocover
