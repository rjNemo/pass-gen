import random
import string
from typing import Protocol

from pydantic import BaseModel


class PassGenOptions(BaseModel):
    seed: int
    length: int = 8
    symbols: bool = False
    numbers: bool = True


def generate_password(options: PassGenOptions) -> str:
    characters = _build_characters(symbols=options.symbols, numbers=options.numbers)
    random_generator = _new_random_generator(options.seed)
    return "".join(random_generator.sample(characters, options.length))


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
