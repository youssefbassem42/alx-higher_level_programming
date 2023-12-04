#!/bin/python3
"""" inherits from where"""


def inherits_from(obj, a_class):
    """" is direct of not """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
