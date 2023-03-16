import enchant
from Spellcheck import config


def main(file):
    d = enchant.Dict(config.dic_language)
    open_file = open(file, "r+")
    words = []
    for i in open_file.readlines():
        if i == "\n":
            pass
        else:
            words.append(i.split(sep=None))

    for _x in range(len(words)):
        for _a in range(len(words[_x])):
            for char in config.charachter_filter:
                words[_x][_a] = words[_x][_a].replace(char, "")

            if d.check(words[_x][_a]):
                pass
            else:
                print(f"{words[_x][_a]} might be wrong")
