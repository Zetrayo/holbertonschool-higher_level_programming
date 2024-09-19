#!/usr/bin/python3
class Square:
    """
    A class representing a square.
    """
    '''setter'''
    def size(self, value):
        self.size = value

    '''getter'''
    def size(self):
        return self.size

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.size == 0:
            print("")
            return
        for i in range(self.size):
            for x in range(self.size):
                print("#", end="")
            print("")
