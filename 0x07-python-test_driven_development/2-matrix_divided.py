#!/usr/bin/python3
"""
Matrix Divider Script
ARGS:
    matrix: the matrix to evaluate
    div: number to divide

Return:
    matrix that has been divided
"""


def matrix_divided(matrix, div):
    """Matrix Divide"""
    error_messag = "matrix must be a matrix (list of lists) of integers/floats"
    error_2 = "Each row of the matrix must have the same size"
    if not matrix:
        raise TypeError(error_messag)
    if not isinstance(matrix, list):
        raise TypeError(error_messag)
    for lists in matrix:
        if not isinstance(lists, list):
            raise TypeError(error_messag)
        for index in lists:
            if not isinstance(index, int) and not isinstance(index, float):
                raise TypeError(error_messag)
    for lists in matrix:
        if len(lists) == 0:
            raise TypeError(error_messag)
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if not all(len(lists) == len(matrix[0]) for lists in matrix):
        raise TypeError(error_2)
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(item / div, 2) for item in lists] for lists in matrix]
