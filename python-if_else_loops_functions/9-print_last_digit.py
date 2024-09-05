#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        x = -number %10
        print(f"{x}", end="")
    else:
        x = number %10
        print(f"{x}", end="")
    return x
