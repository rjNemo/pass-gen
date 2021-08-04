import subprocess  # nosec


def copy_to_clipboard(password: str) -> None:
    subprocess.run("pbcopy", universal_newlines=True, input=password)  # nosec


def save_to_file(file: str, password: str) -> None:
    with open(file, "w") as f:
        f.write(password)
