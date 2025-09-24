"""Task71"""
import numpy as np


def is_identity(arr):
    eye_arr = np.eye(arr.shape[0])
    return np.all(eye_arr == arr)


def is_diagonal(arr):
    result = arr * np.eye(arr.shape[0])
    return np.array_equal(result,arr)


def is_scalar(arr):
    if is_diagonal(arr):  
        diagonal = np.diag(arr)    
        return np.all(diagonal == arr[0,0])
    else:
        return False


def is_sparse(arr):
    """a sparse matrix is a matrix in which most of the elements are zero."""
    arr_zeros = np.zeros(arr.shape)
    sum_of_zeros = np.sum(arr_zeros== arr)
    return sum_of_zeros >= (arr.shape[0] * arr.shape[1]/2)


def check_matrix_type(arr):
    if is_identity(arr) == True:
        return 'Identity Matrix'
    if is_scalar(arr):
        return 'Scalar Matrix'
    if is_diagonal(arr) == True:
        return 'Diagonal Matrix'
    if is_sparse(arr):
        return  'Parse Matrix'
    else:
        return f'matrix is a normal array of type {arr.shape}'


if __name__ == "__main__":
    arr = np.array([[0,1,0],[0,2,0],[0,0,2]])
    matrix_type = check_matrix_type(arr)
    print(matrix_type)
