#!/usr/bin/python3
"""Script for Intger Addition Function"""


def add_integer(a, b=98):
    """Intger Addition Function"""
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    elif type(b) not in (int, float):
        raise TypeError("b must be an integer")
    else:
        result = int(a) + int(b)
        return result
if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
