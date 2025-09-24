"""Task70"""

import numpy as np
np.random.seed(42)


def read_pisitive_size(no_rows=0, no_columns=0):
    while no_rows < 1:
        no_rows = int(input('Type number of rows(>0): '))
    while no_columns < 1:
        no_columns = int(input('Type number of columns(>0): '))
    return no_rows, no_columns


def generate_array(start, end, size, is_ordered):
    """This function can genereate ranom numbers or ordered numbers"""
    no_rows, no_columns = size
    if is_ordered:
        return np.arange(start, no_rows * no_columns + 1).reshape(size)
    return np.random.randint(start, end, size)


def sum_rows(arr):
    sum_rows = []
    for row in arr:
        sum_rows.append(sum(row))
    return np.array(sum_rows)


def sum_columns(arr):
    sum_cols = []
    for i in range(arr.shape[1]):
        sum_cols.append(sum(arr[:,i]))
    return np.array(sum_cols)


def sum_rows_cols(arr):
    return np.sum(arr, axis=1), np.sum(arr, axis=0)


if __name__ == "__main__":
    size = read_pisitive_size()
    is_ordered = True if input('Fill oredred ? y/n: ').lower() == 'y' else False
    arr = generate_array(1, 100, size, is_ordered)
    print(f'array:\n{arr}\n Shape: {arr.shape}\n Rows: {arr.shape[0]}\n Cols = {arr.shape[1]}')

    arr_sum_rows = sum_rows(arr)
    arr_sum_cols = sum_columns(arr)

    print(f'sum of array rows is: {arr_sum_rows}')
    print(f'sum of array columns is: {arr_sum_cols}')

    # alternative solution np.sum()
    sum_of_rows, sum_cols = sum_rows_cols(arr)
    print(f'sum of rows = {sum_of_rows}')
    print(f'sum of cols = {sum_cols}')
    