#!/usr/bin/python3
""" Square Class """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square Class"""

    def __init__(self, size):
        """ initial """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
