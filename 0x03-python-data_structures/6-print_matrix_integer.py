#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    numrows = len(matrix)
    numcols = len(matrix[0])
    for x in range(0, numrows):
        for y in range(0, numcols):
            if y == numcols - 1:
                print('{:d}'.format(matrix[i][j]), end='')
            else:
                print('{:d}'.format(matrix[i][j]), end=' ')
        print()
