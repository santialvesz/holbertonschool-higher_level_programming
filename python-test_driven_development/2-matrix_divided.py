#!/usr/bin/python3
"""Function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """def name: matrix_divided"""
    new_matrix = []
        aux = []
        if type(matrix) is not int and type(matrix) is not float:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if type(div) is not int and type(div) is not float:
            raise TypeError("div must be a number")
        if type(matrix) is float:
            matrix = int(matrix)
        if type(div) is float:
            div = int(div)
        if type(div) == 0:
            raise ZeroDivisionError("division by zero")
        if matrix[0]:
            size = len(matrix[0])
        for i in range(matrix):
            if !isinstance(i, list):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            if len(matrix[i]) != size:
                raise TypeError("Each row of the matrix must have the same size")
            for j in i:
                is !isintance(j, float) or !isinstance(j , int):
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
                aux.append(float("{:.2f}".format(j/div)))
            new_matrix.append(aux)
        return new_matrix
