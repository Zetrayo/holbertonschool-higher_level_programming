#!/usr/bin/python3
"""
Module.
"""


def inherits_from(obj, a_class):
    """
    not Module.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
