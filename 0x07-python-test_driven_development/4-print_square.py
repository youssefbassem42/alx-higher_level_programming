#!/usr/bin/python3
"""
print_square.py
ARGS:
    size: the size of the square
Raises:
    size must be an integer
    size must be >= 0
Return:
    print a square of #
"""


def print_square(size):
    """ print sqaure """
    if not isinstance(size, int) or (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")
    if size < 0 :
        raise ValueError("size must be >= 0")
    for dashes in range(0,size):
        print("#" * size)
