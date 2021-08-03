from __future__ import annotations


class FakeRepository:
    def save(self, password: str) -> None:
        ...

    def list_all(self) -> list[str]:
        return ["2yW4AcqG", "iK2ZWeqh"]

    @classmethod
    def get_instance(cls) -> FakeRepository:
        return FakeRepository()
