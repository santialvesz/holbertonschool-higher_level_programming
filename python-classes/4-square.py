#!/usr/bin/python3
"""Square"""


class Square:
    """class name: Square"""
    def __init__(self, size=0):
        """class name: __init__"""
        if int(size) < 0:
            raise ValueError("size must be >= 0")
        if type(size) is not int:
            raise TypeError("size must be an integer")
        self.__size = size

    @property
    def size(self):
        """def name: size"""
        return self.__size

    @size.setter
    def size(self, value):
        """def name: size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif int(value) < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """def name: area"""
        return self.__size * self.__size
