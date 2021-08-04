from __future__ import annotations

from pydantic import SecretStr

from app.models.password import Password


class FakeRepository:
    def save(self, service: str, password: str) -> None:
        ...

    def list_all(self) -> list[Password]:
        return [
            Password(id=0, service="first", password=SecretStr("2yW4AcqG")),
            Password(id=1, service="second", password=SecretStr("iK2ZWeqh")),
        ]

    def exists(self, service: str) -> bool:
        return False

    @classmethod
    def get_instance(cls) -> FakeRepository:
        return FakeRepository()
