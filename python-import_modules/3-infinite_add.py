#!/usr/bin/env python3
import sys

def main():
    argv = sys.argv[1:]
    total = sum(int(arg) for arg in argv)
    print("{}\n".format(total), end="")

if __name__ == "__main__":
    main()
