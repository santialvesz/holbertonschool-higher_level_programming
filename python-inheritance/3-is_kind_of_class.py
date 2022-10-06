#!/usr/bin/python3
"""Function that returns True if the object is an instance"""


def is_kind_of_class(obj, a_class):
    """def name: is_kind_of_class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
