#!/usr/bin/python3
"""Write"""


def write_file(filename="", text=""):
    """Writes a string to a text file"""
    with open(filename, 'w') as f:
        return f.write(text)
