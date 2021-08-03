from typing import Protocol


class Repository(Protocol):
    def save(self, password: str) -> None:
        ...

    def list_all(self) -> list[str]:
        ...
