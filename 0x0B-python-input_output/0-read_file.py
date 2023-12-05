#!/usr/bin/python3
""" File for Reading function in Python """


def read_file(filename=""):
    """ Read function """
    with open(filename, 'r', encoding="UTF8") as r:
        print(r.read(), end="")
