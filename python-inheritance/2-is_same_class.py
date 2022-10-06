#!/usr/bin/python3
"""Function that returns True if the object is an instance, otherwise False"""


def is_same_class(obj, a_class):
    """def name: is_same_class"""
    if type(obj) is a_class:
        return True
    else:
        return False
