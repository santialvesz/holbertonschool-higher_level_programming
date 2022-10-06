#!/usr/bin/python3
"""Append write"""


def append_write(filename="", text=""):
    """Append a string at the end of a text file"""
    with open(filename, 'a') as f:
        return f.write(text)
