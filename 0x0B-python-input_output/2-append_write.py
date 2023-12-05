#!/usr/bin/python3
""" append function in python """


def append_write(filename="", text=""):
    """ append mode in python """
    with open(filename, "a", encoding="UTF-8") as a:
        return a.write(text)
