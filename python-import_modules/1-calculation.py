#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5
    print("{} + {} = {}\n".format(a, b, add(a, b)), end="")
    print("{} - {} = {}\n".format(a, b, sub(a, b)), end="")
    print("{} * {} = {}\n".format(a, b, mul(a, b)), end="")
    print("{} / {} = {}\n".format(a, b, div(a, b)), end="")
