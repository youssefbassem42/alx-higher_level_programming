#!/usr/bin/python3
"""Define A Square"""


class Square:
    """ Size of Square """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size*self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        if int(self.__size) == 0:
            print()
        for d in range(0, self.__size):
            for dash in range(0, self.__size):
                print("#", end="")
                print()
