#!/usr/bin/python3
"""Square"""


class Square:
    """class name: Square"""
    def __init__(self, size=0):
        """def name: __init__"""
        if int(size) < 0:
            raise ValueError("size must be >=")
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
        if int(value) < 0:
            raise ValueError("size must be >=")
        if type(value) is not int:
            raise TypeError("size must be an integer")
        self.__size = value

    def area(self):
        """def name: area"""
        return self.__size * self.__size

    def my_print(self):
        """def name: my_print"""
        if self.__size == 0:
            print()
        else:
            i = 0
            j = 0
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
