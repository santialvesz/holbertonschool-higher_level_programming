#!/usr/bin/python3
"""My Square"""


class Square:
    """class name: Square"""
    def __init__(self, size=0):
        """def name: __init__"""
        if int(size) < 0:
            raise ValueError("size must be >= 0")
        elif type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            self.__size = size
