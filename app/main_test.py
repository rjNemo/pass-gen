import pytest

from app.main import generate_password


@pytest.mark.parametrize(
    ("seed", "expected"),
    [
        (0, "2yW4AcqG"),
        (1, "iK2ZWeqh"),
    ],
)
def test_can_generate_random_password(seed: int, expected: str) -> None:
    assert generate_password(seed) == expected
