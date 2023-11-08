#!/usr/bin/python3
def square_matrix_map(matrix=None):
    """square_matrix_map"""
    if matrix is None:
        matrix=[]
    return list(map((lambda row: list(map((lambda x: x * x), row))), matrix))
