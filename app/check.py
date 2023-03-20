import typer
import os

from colorama import init, Fore, Style
from app import __version__, __appname__, ERRORS, spellcheck

app = typer.Typer(),
init()


def main(file: str):
    """Checks the given file for any spelling errors."""
    file = os.path.abspath(file)
    if os.path.exists(file):
        spellcheck.main(file)
    else:
        print(Fore.RED + "Error: " + ERRORS[1] + f" could not find {file}")
