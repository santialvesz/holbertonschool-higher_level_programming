#!/usr/bin/python3
"""Read"""


def read_file(filename=""):
    """Read file"""
    with open(filename, 'r') as f:
        print(f.read(), end="")
