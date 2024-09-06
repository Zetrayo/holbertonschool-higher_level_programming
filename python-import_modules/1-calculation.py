#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
def main():
    a = 10
    b = 5
    print("{} + {} = {}\n".format(a, b, add(a, b)), end="")
    print("{} - {} = {}\n".format(a, b, sub(a, b)), end="")
    print("{} * {} = {}\n".format(a, b, mul(a, b)), end="")
    print("{} / {} = {}\n".format(a, b, div(a, b)), end="")

if __name__ == "__main__":
    main()
