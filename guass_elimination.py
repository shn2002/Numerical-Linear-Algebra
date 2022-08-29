# coding: utf8
import copy
import numpy as np


def guass_elimination(matrix_a, vector_b):
    col_size = np.size(matrix_a, 1)
    for j in range(0, col_size):
        if matrix_a[j][j] == 0:
            print('first element is zero')
            return
        for i in range(j + 1, col_size):
            print_result(matrix_a, i, j, 1)
            vector_b[i] = vector_b[i] + (-matrix_a[i][j] / matrix_a[j][j]) * vector_b[j]
            matrix_a[i] = matrix_a[i] + (-matrix_a[i][j] / matrix_a[j][j]) * matrix_a[j]
            print('matrix A=\n %s' % matrix_a)
            print('vector B=\n %s' % vector_b)
            print('--------------------------------------------------------------------')
    calc_xbar(matrix_a, vector_b)
    return None


def guass_elimination_partial_pivoting(matrix_a, vector_b):
    col_size = np.size(matrix_a, 1)
    for j in range(0, col_size):
        max_index = get_max_col_index(matrix_a, j)
        if j != max_index:
            matrix_a = swap(matrix_a, j, max_index)
            vector_b = swap(vector_b, j, max_index)
            print_result(matrix_a, j, max_index, 0)
            print('matrix A=\n %s' % matrix_a)
            print('vector B=\n %s' % vector_b)
        for i in range(j + 1, col_size):
            print_result(matrix_a, i, j, 1)
            vector_b[i] = vector_b[i] + (-matrix_a[i][j] / matrix_a[j][j]) * vector_b[j]
            matrix_a[i] = matrix_a[i] + (-matrix_a[i][j] / matrix_a[j][j]) * matrix_a[j]
            print('matrix A=\n %s' % matrix_a)
            print('vector B=\n %s' % vector_b)
            print('--------------------------------------------------------------------')
    calc_xbar(matrix_a, vector_b)
    return None


def swap(mat, i, j):
    temp = copy.deepcopy(mat[i])
    mat[i] = mat[j]
    mat[j] = copy.deepcopy(temp)
    return mat


def get_max_col_index(mat, i):
    max_value = -np.inf
    max_index = -1
    for j in range(i, np.size(mat, 0)):
        if abs(mat[j, i]) > max_value:
            max_value = abs(mat[j, i])
            max_index = j
    return max_index


def print_result(mat_a, m, n, print_type):
    if print_type == 1:
        print('R%s = R%s - %sR%s' % (m + 1, m + 1, mat_a[m][n] / mat_a[n][n], n + 1))
    else:
        print('Exchange R%s <=> R%s' % (n + 1, m + 1))
    return None


def calc_xbar(mat, vec):
    xbar = np.zeros((np.size(mat, 0), 1))
    col_size = np.size(mat, 1)
    row_size = np.size(mat, 0)
    for i in range(col_size - 1, -1, -1):
        y = vec[i]
        for j in range(0, row_size):
            if j != i:
                y = y - mat[i, j] * xbar[j]
        xbar[i] = y / mat[i][i]
    print('xbar= %s' % xbar)
    return None


if __name__ == "__main__":
    # a = np.array([[1, 3, 0 ], [0, 1, -3], [2, 0, 1]], dtype=float)
    # b = np.array([[-2], [-1], [2]], dtype=float)
    a = np.array([[0, 1], [1, 0]], dtype=float)
    b = np.array([[0], [1]], dtype=float)
    np.set_printoptions(suppress=True)
    print('------------------- Implement the Gauss Elimination algorithm-------------------------')
    guass_elimination(copy.deepcopy(a), copy.deepcopy(b))
    print('-----------Implement the Gauss Elimination using partial pivoting algorithm-----------')
    guass_elimination_partial_pivoting(copy.deepcopy(a), copy.deepcopy(b))
