#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix2 = [
        [matrix[0][0] ** 2, matrix[0][1] ** 2, matrix[0][2] ** 2],
        [matrix[1][0] ** 2, matrix[1][1] ** 2, matrix[1][2] ** 2],
        [matrix[2][0] ** 2, matrix[2][1] ** 2, matrix[2][2] ** 2]
    ]
    return matrix2
