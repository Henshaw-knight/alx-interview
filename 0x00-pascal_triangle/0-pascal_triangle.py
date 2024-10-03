#!/usr/bin/python3
"""pascal_triangle function module"""


def pascal_triangle(n):
    """Function that returns a list of lists of integers
    representing the Pascal’s triangle of n"""
    triangle_list = []
    previous_arr = [1]
    current_arr = []

    for i in range(n):
        if (i == 0):
            triangle_list.append(previous_arr)
        else:
            current_arr[0] = 1
            for j in range(1, i):
                current_arr[j] = previous_arr[j - 1] + previous_arr[j]
            current_arr[i] = 1
        triangle_list.append(current_arr)
        previous_arr = current_arr
