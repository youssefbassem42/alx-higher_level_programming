#!/usr/bin/python3
"""
text_indentation script
"""


def text_indentation(text):
    """ text_indentation script """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in text:
        if char == '.' or char == ':' or char == '?':
            print(char + "", end="\n", sep="")
            print("")
        else:
            print(char, end="")
