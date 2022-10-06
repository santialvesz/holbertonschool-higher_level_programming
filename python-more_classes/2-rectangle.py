#!/usr/bin/python3
"""Rectangle"""


class Rectangle:
    """class Rectangle"""

    def __init__(self, width=0, height=0):
        """def __init__"""
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """To retrieve it"""
        return self.__width

    @property
    def height(self):
        """To retrieve it"""
        return self.__height

    @width.setter
    def width(self, value):
        """To set it"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("widht must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """To set it"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """def area"""
        return self.__height * self.__width

    def perimeter(self):
        """def perimeter"""
        per = 2 * (self.__height + self.__width)
        if self.__width == 0 or self.__height == 0:
            per = 0
            return per
        return per
