import typer
import os
import json

from Spellcheck import __version__, __appname__, ERRORS, spellcheck

app = typer.Typer()


@app.command()
def set(setting: str = typer.Argument(..., help="""command that you want to change"""),
        value: str = typer.Argument(..., help="""The value you want to set.""")):
    try:
        setting = setting.upper()

        with open("./config/config.json", "r") as fr:
            file = json.load(fr)
            file['SPELLCHECK'][setting] = value
            fr.close()
            with open("./config/config.json", "w") as fw:
                json.dump(file, fw, indent=4)
    except KeyError:
        print("[ERROR] " + setting + " is not a setting that you can change")


@app.command()
def get(setting: str = typer.Argument(..., help="""Command that you want to see.""")):
    """Retrieve the value from a configured setting."""
    try:
        setting = setting.upper()
        returned_value = config_return(setting)
        if isinstance(returned_value, list):
            print(*returned_value, sep=" ")
        else:
            print(f"{setting}: {returned_value}")
    except KeyError:
        print("[ERROR] " + setting + " is not a setting.")


@app.command()
def List():
    with open("./config/config.json", "r") as f:
        f = json.load(f)
        for setting in f['SPELLCHECK']:
            print(setting)


def config_return(setting):
    with open("./config/config.json", "r") as f:
        f = json.load(f)
        return f['SPELLCHECK'][setting]
