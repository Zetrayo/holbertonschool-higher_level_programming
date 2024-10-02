#!/usr/bin/python3
"""not empty"""


def append_write(filename="", text=""):
    """not empty"""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
