from typer.testing import CliRunner, Result

from .main import app

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
    assert "X1fH$!ZM" in result.stdout


def _run_cli(*args) -> Result:
    result = runner.invoke(app, ["--no-random", *args])
    assert result.exit_code == 0
    return result
