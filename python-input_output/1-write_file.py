#!/usr/bin/python3
"""not empty"""


def write_file(filename="", text=""):
    """not empty"""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
