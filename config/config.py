import typer
import os
import json

from Spellcheck import __version__, __appname__, ERRORS, spellcheck

app = typer.Typer()


@app.command()
def set():
    pass


@app.command()
def get():
    pass


@app.command()
def list():
    config_return("dsda")


def config_return(setting):
    with open("./config/config.json", "r") as f:
        f = json.load(f)
        return f['SPELLCHECK'][setting]
