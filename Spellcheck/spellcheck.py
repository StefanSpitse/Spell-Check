import enchant

from colorama import init, Fore, Style
from config import config

init(autoreset=True)


def main(file):
    d = enchant.Dict(config.config_return('LANGUAGE'))
    open_file = open(file, "r+")
    words = []
    for i in open_file.readlines():
        words.append(i.split(sep=None))

    for _x in range(len(words)):
        for _a in range(len(words[_x])):
            for char in config.config_return('CHARACHTER_FILTER'):
                words[_x][_a] = words[_x][_a].replace(char, "")

            if d.check(words[_x][_a]):
                pass
            else:
                print(
                    Fore.YELLOW + f"[line:{words.index(words[_x]) + 1}][word: {words[_x].index(words[_x][_a]) + 1}] "
                    + Fore.RED + f"{words[_x][_a]}")
