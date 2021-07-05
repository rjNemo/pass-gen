from typing import Any

from typer.testing import CliRunner, Result

from app.main import app

runner = CliRunner()


def test_cli_print_password() -> None:
    result = _run_cli()
    assert "2yW4AcqG" in result.stdout


def test_cli_can_set_password_length() -> None:
    args = ["--length", 10]
    result = _run_cli(*args)
    assert "2yW4AcqGFz" in result.stdout


def test_cli_can_set_symbols() -> None:
    args = ["--symbols"]
    result = _run_cli(*args)
    print(result.stdout)
    assert """X"fH.+ZM""" in result.stdout


def test_cli_can_set_numbers() -> None:
    args = ["--no-numbers"]
    result = _run_cli(*args)
    print(result.stdout)
    assert "yWAcqGFz" in result.stdout


def test_cli_can_save_to_file() -> None:
    args = ["--file", "test.txt"]
    _ = _run_cli(*args)
    with open("test.txt", "r") as f:
        content = f.read()
        assert "2yW4AcqG" in content


def _run_cli(*args: Any) -> Result:
    result = runner.invoke(app, ["--no-random", *args])
    assert result.exit_code == 0
    return result
