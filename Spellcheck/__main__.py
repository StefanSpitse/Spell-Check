import typer

from Spellcheck import __version__, __appname__, check
from config import config


def main():
    app = typer.Typer()
    app.add_typer(config.app, name="config")
    app.add_typer(check.app, name="check")
    app()


if __name__ == "__main__":
    main()
