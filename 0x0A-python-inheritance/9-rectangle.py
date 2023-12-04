#!/usr/bin/python3
"""
Rectangle Class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """" Rectangle Class """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """ Area of Rectangle """
        return self.__width * self.__height
