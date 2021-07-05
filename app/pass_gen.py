import random
import string
from typing import Protocol


def generate_password(seed: int, length: int = 8, symbols: bool = False) -> str:
    characters = _build_characters(symbols)

    random_generator = _new_random_generator(seed)

    return "".join(random_generator.sample(characters, length))


class RandomSampler(Protocol):
    def sample(self, population: str, k: int) -> list[str]:
        ...  # pragma nocover


def _new_random_generator(seed: int) -> RandomSampler:
    return random.Random(seed)


def _build_characters(symbols: bool) -> str:
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation

    characters = lowercase + uppercase + digits

    if symbols:
        characters += punctuation

    return characters
