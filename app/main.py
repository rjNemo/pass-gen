import random as r
import subprocess

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
    password = generate_password(seed, length, symbols, numbers)

    subprocess.run("pbcopy", universal_newlines=True, input=password)

    typer.echo(typer.style(f"🔐 {password}", fg=typer.colors.GREEN, bold=True))
    typer.echo(
        "The password has been copied to your clipboard 😉\nPaste it using cmd + v"
    )


if __name__ == "__main__":
    app()  # pragma nocover
