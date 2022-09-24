import string
from dataclasses import dataclass
from random import Random

from app.models.password import Password
from app.repositories.type import Repository


@dataclass(frozen=True)
class PassGenOptions:
    service: str
    seed: int
    length: int = 8
    symbols: bool = False
    numbers: bool = True


def generate_password(repo: Repository, options: PassGenOptions) -> str:
    if repo.exists(options.service):
        raise ValueError("password for this service has already been set")

    characters = _build_characters(symbols=options.symbols, numbers=options.numbers)
    random_generator = Random(options.seed)
    password = "".join(random_generator.sample(characters, options.length))
    repo.save(options.service, password)
    return password


def _build_characters(*, symbols: bool, numbers: bool) -> str:
    return "".join(
        [
            string.ascii_letters,
            string.punctuation if symbols else "",
            string.digits if numbers else "",
        ]
    )


def list_all_saved_passwords(repo: Repository) -> list[Password]:
    return repo.list_all()
