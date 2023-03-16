import typer
import os


from Spellcheck import __version__, __appname__, ERRORS, spellcheck

app = typer.Typer()


@app.command()
def check(file: str = typer.Argument(..., help="""File that gets checked for errors""")):
    """Checks the given file for any spelling errors."""
    file = os.path.abspath(file)
    if os.path.exists(file):
        print(spellcheck.main(file))
    else:
        print("Error: " + ERRORS[1] + f" could not find {file}")
