#!/usr/bin/python3
"""Fcuntion that returns True if the object is an instance"""


def inherits_from(obj, a_class):
    """def name: inherits_from"""
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    return False
