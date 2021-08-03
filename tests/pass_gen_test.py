import pytest
from pydantic import SecretStr

from app.models.password import Password
from app.repositories.fake import FakeRepository
from app.usecases.pass_gen import PassGenOptions, generate_password, list_all_saved_passwords

fake_repo = FakeRepository.get_instance()
service = "service_name"


@pytest.mark.parametrize(
    ("seed", "expected"),
    [
        (0, "2yW4AcqG"),
        (1, "iK2ZWeqh"),
    ],
)
def test_can_generate_random_password(seed: int, expected: str) -> None:
    options = PassGenOptions(seed=seed, service=service)
    assert generate_password(fake_repo, options) == expected


@pytest.mark.parametrize(
    ("seed", "length", "expected"),
    [
        (0, 6, "2yW4Ac"),
        (1, 10, "iK2ZWeqhF5"),
    ],
)
def test_control_password_length(seed: int, length: int, expected: str) -> None:
    options = PassGenOptions(seed=seed, length=length, service=service)
    assert generate_password(fake_repo, options) == expected


@pytest.mark.parametrize(
    ("seed", "symbols", "expected"),
    [
        (0, True, """X"fH.+ZM"""),
        (1, True, """r?iGp,&)"""),
    ],
)
def test_password_can_contain_symbols(seed: int, symbols: bool, expected: str) -> None:
    options = PassGenOptions(seed=seed, symbols=symbols, service=service)
    assert generate_password(fake_repo, options) == expected


@pytest.mark.parametrize(
    ("seed", "numbers", "expected"),
    [
        (0, False, "yWAcqGFz"),
        (1, False, "iKWeqhFC"),
    ],
)
def test_password_can_contain_numbers(seed: int, numbers: bool, expected: str) -> None:
    options = PassGenOptions(seed=seed, numbers=numbers, service=service)
    assert generate_password(fake_repo, options) == expected


@pytest.mark.parametrize(
    "expected",
    [
        [
            Password(id=0, service="first", password=SecretStr("2yW4AcqG")),
            Password(id=1, service="second", password=SecretStr("iK2ZWeqh")),
        ],
    ],
)
def test_can_read_all_saved_passwords(expected: list[str]) -> None:
    assert list_all_saved_passwords(fake_repo) == expected
