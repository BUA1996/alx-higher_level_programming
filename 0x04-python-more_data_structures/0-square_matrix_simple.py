#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    makeCopy = matrix.copy()
    for num in range(len(matrix)):
        makeCopy[num] = list(map(lambda x: x ** 2, matrix[num]))
    return (makeCopy)
