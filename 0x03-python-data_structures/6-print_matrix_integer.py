#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for rows in matrix:
        for y in rows:
            print("{:d}".format(y), end=" " if y != rows[-1] else "")
        print()
