from __future__ import annotations

from pydantic import SecretStr

from app.models.password import Password


class FakeRepository:
    _values: dict[str, SecretStr] = {}

    def save(self, service: str, password: str) -> None:
        self._values[service] = SecretStr(password)

    def list_all(self) -> list[Password]:
        return [
            Password(id=i, service=v[0], password=v[1]) for i, v in enumerate(self._values.items())
        ]

    def exists(self, service: str) -> bool:
        return service in self._values.keys()

    @staticmethod
    def instance() -> FakeRepository:
        return FakeRepository()
