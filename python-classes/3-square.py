#!/usr/bin/python3
class Square:
    """
    A class representing a square.
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        x = self.__size ** 2
        return x
