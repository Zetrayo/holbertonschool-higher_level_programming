#!/usr/bin/python3
"""
Module of list.
"""


class MyList(list):
    """
    A class of list.
    """
    
    def print_sorted(self):
        """
        prints a sorted list
        """
        print(sorted(self))
