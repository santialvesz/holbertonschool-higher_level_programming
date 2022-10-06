#!/usr/bin/python3
"""JSON file"""


import json


def load_from_json_file(filename):
    """load from json file"""
    with open(filename, 'r') as fn:
        files = json.load(fn)
        return files
