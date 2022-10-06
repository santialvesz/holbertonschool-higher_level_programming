#!/usr/bin/python3
"""Technical interview preparation"""


def pascal_triangle(n):
    """Pascal triangle"""
    lis = []
    if n <= 0:
        return lis
    for i in range(n):
        lis.append([1] * (i + 1))
    for i in range(1, len(lis)):
        for j in range(1, len(lis[i]) - 1):
            lis[i][j] = lis[i - 1][j - 1] + lis[i - 1][j]
    return lis
