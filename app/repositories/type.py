from typing import Protocol


class Repository(Protocol):
    def save(self, password: str) -> None:
        ...
