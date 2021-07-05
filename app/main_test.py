from typer.testing import CliRunner
from .main import app

runner = CliRunner()


def test_cli_print_password() -> None:
    result = runner.invoke(app)
    assert result.exit_code == 0
    assert "2yW4AcqG" in result.stdout
