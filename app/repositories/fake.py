from __future__ import annotations

from app.models.password import Password


class FakeRepository:
    _values = {}

    def save(self, service: str, password: str) -> None:
        self._values[service] = password

    def list_all(self) -> list[Password]:
        return [
            Password(id=i, service=v[0], password=v[1]) for i, v in enumerate(self._values.items())
        ]

    def exists(self, service: str) -> bool:
        return service in self._values.keys()

    @classmethod
    def get_instance(cls) -> FakeRepository:
        return FakeRepository()
