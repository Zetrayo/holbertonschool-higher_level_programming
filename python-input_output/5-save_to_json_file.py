#!/usr/bin/python3
import json

"""not empty"""


def save_to_json_file(my_obj, filename):
    """not empty"""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
