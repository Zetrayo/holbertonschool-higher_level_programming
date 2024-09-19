#!/usr/bin/python3
"""
Module of square.
"""
class Square:
    """
    A class representing a square.

    Attributes:
        size (int): The size of one side of the square.
    """
    def __init__(self, size):
        """
        Initializes the square with a size and position.

        Args:
            size (int): The size of one side of the square (default is 0).
            position (tuple): The position of the square when printed,
            defined as a tuple of 2 positive integers (default is (0, 0)).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
            TypeError: If position is not a tuple of 2 positive integers.
        """
        self.__size = size
