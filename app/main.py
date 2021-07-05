import random
import string

import typer


def generate_password(seed: int) -> str:
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits

    letters = lowercase + uppercase + digits

    random_generator = random.Random(seed)

    return "".join(random_generator.sample(letters, 8))


app = typer.Typer()


@app.command()
def main() -> None:
    typer.echo(generate_password(0))


if __name__ == "__main__":
    app()
