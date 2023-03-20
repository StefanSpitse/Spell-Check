import typer

from Spellcheck import check as ch
from Spellcheck import __version__, __appname__
from config import config

app = typer.Typer()


def main():
    app.add_typer(config.app, name="config")
    app()


@app.command()
def check(file: str = typer.Argument(..., help="""File that gets checked for errors"""),):
    """Checks the given file for any spelling errors."""
    ch.main(file)


if __name__ == "__main__":
    main()
