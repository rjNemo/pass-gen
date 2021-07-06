import pytest
from app.pass_gen import generate_password


@pytest.mark.parametrize(
    ("seed", "expected"),
    [
        (0, "2yW4AcqG"),
        (1, "iK2ZWeqh"),
    ],
)
def test_can_generate_random_password(seed: int, expected: str) -> None:
    assert generate_password(seed) == expected


@pytest.mark.parametrize(
    ("seed", "length", "expected"),
    [
        (0, 6, "2yW4Ac"),
        (1, 10, "iK2ZWeqhF5"),
    ],
)
def test_control_password_length(seed: int, length: int, expected: str) -> None:
    assert generate_password(seed, length) == expected


@pytest.mark.parametrize(
    ("seed", "symbols", "expected"),
    [
        (0, True, """X"fH.+ZM"""),
        (1, True, """r?iGp,&)"""),
    ],
)
def test_password_can_contain_symbols(seed: int, symbols: bool, expected: str) -> None:
    assert generate_password(seed, symbols=symbols) == expected


@pytest.mark.parametrize(
    ("seed", "numbers", "expected"),
    [
        (0, False, "yWAcqGFz"),
        (1, False, "iKWeqhFC"),
    ],
)
def test_password_can_contain_numbers(seed: int, numbers: bool, expected: str) -> None:
    assert generate_password(seed, numbers=numbers) == expected
