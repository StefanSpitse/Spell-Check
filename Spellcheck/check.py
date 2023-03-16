import typer
import os

from Spellcheck import __version__, __appname__, ERRORS, spellcheck

app = typer.Typer()


@app.callback()
def check(file: str = typer.Argument(..., help="""File that gets checked for errors"""),
          update: bool = typer.Option(False,
                                      help="after getting feedback on the text when turned on it wil give you a "
                                           "change to immedtialy change it")):
    """Checks the given file for any spelling errors."""
    file = os.path.abspath(file)
    if os.path.exists(file):
        print(spellcheck.main(file))
    else:
        print("Error: " + ERRORS[1] + f" could not find {file}")


