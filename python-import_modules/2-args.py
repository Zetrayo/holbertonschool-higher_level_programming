#!/usr/bin/env python3
import sys

def main():
    argv = sys.argv[1:]
    arg_count = len(argv)
    if arg_count == 0:
        print("{} argument.\n".format(arg_count), end="")
    elif arg_count == 1:
        print("{} argument:\n".format(arg_count), end="")
    else:
        print("{} arguments:\n".format(arg_count), end="")
    for i, arg in enumerate(argv, 1):
        print(f"{i}: {arg}")

if __name__ == "__main__":
    main()
