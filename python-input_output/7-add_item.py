#!/usr/bin/python3
import sys
import json
from os.path import exists


"""not empty"""


def save_to_json_file(my_obj, filename):
    """not empty"""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)


def load_from_json_file(filename):
    """not empty"""
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


filename = "add_item.json"


if exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

items.extend(sys.argv[1:])

save_to_json_file(items, filename)
