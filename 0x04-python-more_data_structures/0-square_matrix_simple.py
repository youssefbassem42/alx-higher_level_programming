#!/usr/bin/python3
def square_matrix_simple(matrix=[]) :
    """function get matrix squares"""
    return [list(map(lambda x: x ** 2,row)) for row in matrix]