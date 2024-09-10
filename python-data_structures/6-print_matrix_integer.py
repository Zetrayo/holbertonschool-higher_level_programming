#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        for i, element in enumerate(x):
            if i != 0:
                print(" ", end="")
            print("{}".format(element), end="")
        print()
