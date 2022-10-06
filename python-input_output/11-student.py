#!/usr/bin/python3
"""JSON"""


class Student:
    """class name: Student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        i = {}
        for j in attrs:
            if j in self.__dict__:
                i[j] = self.__dict__[j]
        return i

    def reload_from_json(self, json):
        if json == {}:
            return
        self.__dict__ = json
