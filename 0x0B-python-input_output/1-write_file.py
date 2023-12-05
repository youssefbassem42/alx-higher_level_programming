#!/usr/bin/python3
""" Write function """


def write_file(filename="", text=""):
    """ Write function in Python """
    with open(filename, 'w', encoding="UTF-8") as w:
        return w.write(text)
