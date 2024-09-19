#!/usr/bin/python3
class Square:
    """
    A class representing a square.

    Attributes:
        size (int): The size of one side of the square.
    """
    def __init__(self, size=0):
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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        x = self.__size ** 2
        return x
