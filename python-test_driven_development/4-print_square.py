#!/usr/bin/python3
"""Function that prints a square with the character #"""


def print_square(size):
    """def name: print_square"""
    if !isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(1, size + 1):
        for j in range(1, size + 1):
            print("{}".format(j), end="")
        print()
