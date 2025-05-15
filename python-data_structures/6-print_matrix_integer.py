#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    list_var = len(matrix)
    for x in range(list_var):
        for y in range(len(matrix[x])):
            print('{:d}'.format(matrix[x][y]), end='')
            if y is not (len(matrix[x]) - 1):
                print(end=" ")
        print("")

