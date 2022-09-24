from random import randint
from typing import Optional

from rich import print
from rich.console import Console
from typer import Argument, Option, Typer, echo

from app.repositories import sqlite
from app.usecases.pass_gen import (
    PassGenOptions,
    generate_password,
    list_all_saved_passwords,
)
from app.usecases.utils import copy_to_clipboard, save_to_file

app = Typer()
sqlite_repo = sqlite.instance()


@app.command()
def save(
    service: str = Argument(..., help="Name of the service associated to the password"),
    length: int = Option(
        8,
        "--length",
        "-l",
        help="Length of the generated password.",
    ),
    numbers: bool = Option(
        True,
        "--numbers",
        "-n",
        help="If the generated password should include numeric characters.",
    ),
    symbols: bool = Option(
        False,
        "--symbols",
        "-s",
        help="If the generated password should include special characters.",
    ),
    file: Optional[str] = Option(
        None,
        "--file",
        "-f",
        help="Path to the file where the generated password should be saved.",
    ),
    random: bool = True,
) -> None:
    seed = randint(0, 100) if random else 0  # nosec
    options = PassGenOptions(
        service=service,
        seed=seed,
        length=length,
        symbols=symbols,
        numbers=numbers,
    )

    try:
        password = generate_password(sqlite_repo, options)

        print(f"🔐 [green]{password}[/green]")

        if file is not None:
            save_to_file(file, password)
            return print(f"The password has been saved to: {file} 🗄")

        copy_to_clipboard(password)
        return print("The password has been copied to your clipboard 😉\nPaste it using cmd + v")
    except ValueError as error:
        err_console = Console(stderr=True)
        err_console.print(f"[red]error: {error}[/red]")


@app.command()
def read() -> None:
    stored_passwords = list_all_saved_passwords(sqlite_repo)
    for p in stored_passwords:
        echo(f"{p.service}: {p.password.get_secret_value()}")
