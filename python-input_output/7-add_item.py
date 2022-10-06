#!/usr/bin/python3
"""Load, add, save"""


import json


save_file = __import__('5-save_to_json_file').save_to_json_file


load_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    import sys
    i = []
    try:
        i = load_file('add_item.json')
    except:
        pass
    for j in range(1, len(sys.argv)):
        i.append(sys.argv[j])
    save_file(i, 'add_item.json')
