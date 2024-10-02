#!/usr/bin/python3
"""not empty"""


import json


def load_from_json_file(filename):
    """not empty"""
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
