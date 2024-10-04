#!/usr/bin/python3
"""Module to serialize and deserialize"""


import json


def serialize_and_save_to_file(data, filename):
    """Function to serialize"""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """Function to deserialize"""
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
