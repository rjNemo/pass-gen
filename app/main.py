import typer

from .pass_gen import generate_password

app = typer.Typer()


@app.command()
def main() -> None:
    typer.echo(generate_password(0))


if __name__ == "__main__":
    app()
