import pytest
from faker import Faker


@pytest.fixture(scope="function")
def faker() -> Faker:
    return Faker()
