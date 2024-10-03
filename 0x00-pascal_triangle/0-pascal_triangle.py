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
            current_arr.insert(0, 1)
            for j in range(1, i):
                current_arr.insert(j, previous_arr[j - 1] + previous_arr[j])
            current_arr.insert(i, 1)
            triangle_list.append(current_arr)
            previous_arr = current_arr
            current_arr = []
    return triangle_list
