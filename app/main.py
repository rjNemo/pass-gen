import random as r

import typer

from .pass_gen import generate_password

app = typer.Typer()


@app.command()
def main(
    random: bool = True,
    length: int = typer.Option(8, help="Length of the generated password."),
) -> None:
    seed = r.randint(0, 100) if random else 0
    typer.echo(generate_password(seed, length))


if __name__ == "__main__":
    app()
