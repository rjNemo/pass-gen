import typer

from .pass_gen import generate_password

app = typer.Typer()


@app.command()
def main(
    length: int = typer.Option(8, help="Length of the generated password."),
) -> None:
    typer.echo(generate_password(0, length))


if __name__ == "__main__":
    app()
