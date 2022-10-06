#!/usr/bin/python3
"""JSON"""


import json


def from_json_string(my_str):
    """returns an object representend by a JSON string"""
    return json.loads(my_str)
