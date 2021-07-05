import random
import string
from typing import Protocol


def generate_password(
    seed: int, length: int = 8, symbols: bool = False, numbers: bool = True
) -> str:
    characters = _build_characters(symbols=symbols, numbers=numbers)

    random_generator = _new_random_generator(seed)

    return "".join(random_generator.sample(characters, length))


class RandomSampler(Protocol):
    def sample(self, population: str, k: int) -> list[str]:
        ...  # pragma nocover


def _new_random_generator(seed: int) -> RandomSampler:
    return random.Random(seed)


def _build_characters(symbols: bool, numbers: bool) -> str:
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase

    characters = lowercase + uppercase

    if symbols:
        characters += string.punctuation
    if numbers:
        characters += string.digits

    return characters
