from typing import Any

from faker import Faker
from rich import print
from typer.testing import CliRunner, Result

from app.main import app

runner = CliRunner()


def test_cli_print_password(faker: Faker) -> None:
    result = _run_cli(faker)
    assert "2yW4AcqG" in result.stdout


def test_cli_can_set_password_length(faker: Faker) -> None:
    args = ["--length", 10]
    result = _run_cli(faker, *args)
    assert "2yW4AcqGFz" in result.stdout


def test_cli_can_set_symbols(faker: Faker) -> None:
    args = ["--symbols"]
    result = _run_cli(faker, *args)
    print(result.stdout)
    assert """X"fH.+ZM""" in result.stdout


def test_cli_can_set_numbers(faker: Faker) -> None:
    args = ["-n"]
    result = _run_cli(faker, *args)
    print(result.stdout)
    assert "yWAcqGFz" in result.stdout


def test_cli_can_save_to_file(faker: Faker) -> None:
    args = ["--file", "test.txt"]
    _ = _run_cli(faker, *args)
    with open("test.txt", "r") as f:
        content = f.read()
        assert "2yW4AcqG" in content


def test_cli_can_save_to_db(faker: Faker) -> None:
    _run_cli(faker)
    result = _run_cli_read()
    assert "2yW4AcqG" in result.stdout


def test_cli_cannot_save_password_for_service_twice(faker: Faker) -> None:
    service_name = faker.pystr()
    runner.invoke(app, ["save", service_name, "--no-random"])
    result = runner.invoke(app, ["save", service_name, "--no-random"])
    assert "already been set" in result.stdout


def _run_cli(faker: Faker, *args: Any) -> Result:
    result = runner.invoke(app, ["save", faker.pystr(), "--no-random", *args])
    assert result.exit_code == 0
    return result


def _run_cli_read(*args: Any) -> Result:
    result = runner.invoke(app, ["read", *args])
    assert result.exit_code == 0
    return result
