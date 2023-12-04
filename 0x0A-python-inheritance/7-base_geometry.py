#!/usr/bin/python3
"""
BaseGeometry Class
"""


class BaseGeometry:
    """BaseGeometry"""
    def area(self):
        """Area Not implemented"""
        raise NotImplementedError("area() is not implemented")

    def integer_validator(self, name, value):
        """ intger Validator """
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
