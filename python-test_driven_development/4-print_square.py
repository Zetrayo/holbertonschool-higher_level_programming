#!/usr/bin/python3
def print_square(size):
    x = 0
    i = 0
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    while x < size:
        while i < size:
            print("#", end="")
            i += 1
        print()
        i = 0
        x += 1
