import random as r

import typer

from .pass_gen import generate_password

app = typer.Typer()


@app.command()
def main(
    random: bool = True,
    length: int = typer.Option(8, help="Length of the generated password."),
    numbers: bool = typer.Option(
        True, help="If the generated password should include numeric characters."
    ),
    symbols: bool = typer.Option(
        False, help="If the generated password should include special characters."
    ),
) -> None:
    seed = r.randint(0, 100) if random else 0
    typer.echo(generate_password(seed, length, symbols, numbers))


if __name__ == "__main__":
    app()  # pragma nocover
