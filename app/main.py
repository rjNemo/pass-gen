import random as r
from typing import Optional

import typer

import app.usecases.pass_gen as pass_gen
import app.usecases.utils as utils

app = typer.Typer()


@app.command()
def main(
    length: int = typer.Option(
        8,
        "--length",
        "-l",
        help="Length of the generated password.",
    ),
    numbers: bool = typer.Option(
        True,
        "--numbers",
        "-n",
        help="If the generated password should include numeric characters.",
    ),
    symbols: bool = typer.Option(
        False,
        "--symbols",
        "-s",
        help="If the generated password should include special characters.",
    ),
    file: Optional[str] = typer.Option(
        None,
        "--file",
        "-f",
        help="Path to the file where the generated password should be saved.",
    ),
    random: bool = True,
) -> None:
    seed = r.randint(0, 100) if random else 0
    options = pass_gen.PassGenOptions(
        seed=seed,
        length=length,
        symbols=symbols,
        numbers=numbers,
    )

    password = pass_gen.generate_password(options)

    typer.echo(typer.style(f"🔐 {password}", fg=typer.colors.GREEN, bold=True))

    if file is not None:
        utils.save_to_file(file, password)
        return typer.echo(f"The password has been saved to: {file} 🗄")

    utils.copy_to_clipboard(password)
    return typer.echo("The password has been copied to your clipboard 😉\nPaste it using cmd + v")
