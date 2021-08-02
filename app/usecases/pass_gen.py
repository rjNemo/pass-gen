import random
import string
from typing import Protocol

from pydantic import BaseModel

from app.repositories.sqlite import PasswordRepository


class PassGenOptions(BaseModel):
    seed: int
    length: int = 8
    symbols: bool = False
    numbers: bool = True


def generate_password(repo: PasswordRepository, options: PassGenOptions) -> str:
    characters = _build_characters(symbols=options.symbols, numbers=options.numbers)
    random_generator = _new_random_generator(options.seed)
    password = "".join(random_generator.sample(characters, options.length))
    repo.save(password)
    return password


class RandomSampler(Protocol):
    def sample(self, population: str, k: int) -> list[str]:
        ...  # pragma nocover


def _new_random_generator(seed: int) -> RandomSampler:
    return random.Random(seed)


def _build_characters(symbols: bool, numbers: bool) -> str:
    return "".join(
        [
            string.ascii_letters,
            string.punctuation if symbols else "",
            string.digits if numbers else "",
        ]
    )
