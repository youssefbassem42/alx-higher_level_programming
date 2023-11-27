#!/usr/bin/python3
"""


"""


def text_indentation(text):
    """"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in text:
        if char == '.' or char == ':' or char == '?':
            print(char + "", end="\n", sep="")
            print("")
        else:
            print(char, end="")
text_indentation("""test function that make 2 new lines after.
and after?
and after:""")