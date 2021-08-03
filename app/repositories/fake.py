from __future__ import annotations


class FakeRepository:
    def save(self, password: str) -> None:
        ...

    @classmethod
    def get_instance(cls) -> FakeRepository:
        return FakeRepository()
