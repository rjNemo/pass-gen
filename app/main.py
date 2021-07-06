import random as r
import subprocess
from typing import Optional

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
    file: Optional[str] = typer.Option(
        None, help="Path to the file where the generated password should be saved."
    ),
) -> None:
    seed = r.randint(0, 100) if random else 0
    password = generate_password(seed, length, symbols, numbers)

    typer.echo(typer.style(f"🔐 {password}", fg=typer.colors.GREEN, bold=True))

    if file is not None:
        with open(file, "w") as f:
            f.write(password)
            return

    subprocess.run("pbcopy", universal_newlines=True, input=password)
    typer.echo("The password has been copied to your clipboard 😉\nPaste it using cmd + v")
