#!/usr/bin/python3
def square_matrix_simple(matrix=None) :
    """function get matrix squares"""
    if matrix is None :
        matrix = []
    return [list(map(lambda x: x ** 2,row)) for row in matrix]
