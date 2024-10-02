#!/usr/bin/python3
"""not empty"""


def read_file(filename=""):
    """not empty"""
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read, end="")
