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
    def __init__(self, size=0, position=(0, 0)):
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
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The size of one side of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The size of the square's side.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
