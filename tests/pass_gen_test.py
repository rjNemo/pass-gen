import pytest
from faker import Faker

from app.repositories.fake import FakeRepository
from app.usecases.pass_gen import (
    PassGenOptions,
    generate_password,
    list_all_saved_passwords,
)

fake_repo = FakeRepository.instance()


@pytest.mark.parametrize(
    ("seed", "expected"),
    [
        (0, "2yW4AcqG"),
        (1, "iK2ZWeqh"),
    ],
)
def test_can_generate_random_password(faker: Faker, seed: int, expected: str) -> None:
    options = PassGenOptions(seed=seed, service=faker.pystr())
    assert generate_password(fake_repo, options) == expected


@pytest.mark.parametrize(
    ("seed", "length", "expected"),
    [
        (0, 6, "2yW4Ac"),
        (1, 10, "iK2ZWeqhF5"),
    ],
)
def test_control_password_length(faker: Faker, seed: int, length: int, expected: str) -> None:
    options = PassGenOptions(seed=seed, length=length, service=faker.pystr())
    assert generate_password(fake_repo, options) == expected


@pytest.mark.parametrize(
    ("seed", "symbols", "expected"),
    [
        (0, True, """X"fH.+ZM"""),
        (1, True, """r?iGp,&)"""),
    ],
)
def test_password_can_contain_symbols(
    faker: Faker, seed: int, symbols: bool, expected: str
) -> None:
    options = PassGenOptions(seed=seed, symbols=symbols, service=faker.pystr())
    assert generate_password(fake_repo, options) == expected


@pytest.mark.parametrize(
    ("seed", "numbers", "expected"),
    [
        (0, False, "yWAcqGFz"),
        (1, False, "iKWeqhFC"),
    ],
)
def test_password_can_contain_numbers(
    faker: Faker, seed: int, numbers: bool, expected: str
) -> None:
    options = PassGenOptions(seed=seed, numbers=numbers, service=faker.pystr())
    assert generate_password(fake_repo, options) == expected


@pytest.mark.parametrize("expected", [8])
def test_can_read_all_saved_passwords(expected: int) -> None:
    assert len(list_all_saved_passwords(fake_repo)) == expected


def test_cannot_save_password_for_service_twice(faker: Faker) -> None:
    with pytest.raises(ValueError, match="already been set"):
        options = PassGenOptions(seed=0, service=faker.pystr())
        generate_password(fake_repo, options)
        generate_password(fake_repo, options)
