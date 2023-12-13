#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []
    for row in matrix:
        new_row = []
        for element in row:
            sqr = element*element
            new_row.append(sqr)
        result.append(new_row)
    return result
