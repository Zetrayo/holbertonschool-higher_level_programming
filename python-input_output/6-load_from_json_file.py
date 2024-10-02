#!/usr/bin/python3
import json

"""not empty"""


def load_from_json_file(filename):
    """not empty"""
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
