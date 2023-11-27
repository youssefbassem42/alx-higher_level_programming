#!/usr/bin/python3
"""
say_my_name.py
ARGS:
    first_name: first name of person
    last_name: last name of person
Raises:
    first_name must be a string
    last_name must be a string
Return:
       My name is {first_name} {last_name}
"""


def say_my_name(first_name, last_name=""):
    """ Hay Say My Name """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}",end="")
