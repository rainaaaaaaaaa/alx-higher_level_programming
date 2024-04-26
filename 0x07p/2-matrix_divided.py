#!/usr/bin/python3
"""
This is '2-matrix_divided' module.
Functions:
    matrix_divided(matrix, div)
"""

def matrix_divided(matrix, div):
    if not all(isinstance(row, list) for row in matrix) or not all(isinstance(val, (int, float)) for row in matrix for val in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = [round(elem / div, 2) for elem in row]
        new_matrix.append(new_row)

    return new_matrix
