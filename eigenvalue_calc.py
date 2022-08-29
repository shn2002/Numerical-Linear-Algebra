# coding: utf8
import numpy as np
import copy
import math


def guass_elimination_partial_pivoting(matrix_a, vector_b):
    col_size = np.size(matrix_a, 1)
    for j in range(0, col_size):
        max_index = get_max_col_index(matrix_a, j)
        if j != max_index:
            matrix_a = swap(matrix_a, j, max_index)
            vector_b = swap(vector_b, j, max_index)
        for i in range(j + 1, col_size):
            vector_b[i] = vector_b[i] + (-matrix_a[i][j] / matrix_a[j][j]) * vector_b[j]
            matrix_a[i] = matrix_a[i] + (-matrix_a[i][j] / matrix_a[j][j]) * matrix_a[j]
    x_bar = calc_xbar(matrix_a, vector_b)
    return x_bar


def swap(mat, i, j):
    temp = copy.deepcopy(mat[i])
    mat[i] = mat[j]
    mat[j] = copy.deepcopy(temp)
    return mat


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
    return xbar


def get_max_col_index(mat, i):
    max_value = -np.inf
    max_index = -1
    for j in range(i, np.size(mat, 0)):
        if abs(mat[j, i]) > max_value:
            max_value = abs(mat[j, i])
            max_index = j
    return max_index


def inverse_iteration(mat_a, mat_b):
    print('k ', '     xk ', '      ratio')
    flag = True
    k = 1
    while flag:
        if 'yk_norm' in locals():
            temp_norm = copy.deepcopy(yk_norm)
        else:
            temp_norm = math.inf
        yk = guass_elimination_partial_pivoting(copy.deepcopy(mat_a), mat_b)
        yk_norm = np.linalg.norm(yk, np.inf)
        mat_b = yk / yk_norm
        print(str(k), str(np.round(mat_b.transpose(), 4)), str(format(yk_norm, ".4f")))
        k = k + 1
        if abs(temp_norm - yk_norm) / abs(temp_norm) < 0.00001:
            flag = False


def rayleigh_quotient_iteration(mat_a, mat_b):
    print('k ', '     xk ', '      sigma')
    flag = True
    k = 0
    while flag:
        if 'sigma' in locals():
            temp_sigma = copy.deepcopy(sigma)
        else:
            temp_sigma = math.inf
        sigma = np.asscalar((mat_b.transpose() @ mat_a @ mat_b) / (mat_b.transpose() @ mat_b))
        yk = guass_elimination_partial_pivoting(mat_a - sigma * np.identity(mat_a.shape[0]), mat_b)
        yk_norm = np.linalg.norm(yk, np.inf)
        mat_b = yk / yk_norm
        print(str(k), str(np.round(mat_b.transpose(), 4)), str(format(sigma, ".4f")))
        k = k + 1
        if abs(temp_sigma - sigma)/abs(temp_sigma) < 0.0007:
            flag = False


if __name__ == "__main__":
    a = np.array(
        [[1, -1, 0],
         [0, -4, 2],
         [0, 0, -2]],
        dtype=float)
    b = np.array([[1], [1], [1]], dtype=float)
    # a = np.array(
    #     [[3, 1],
    #      [1, 3]],
    #     dtype=float)
    # b = np.array([[0], [1]], dtype=float)
    np.set_printoptions(suppress=True)
    inverse_iteration(copy.deepcopy(a), copy.deepcopy(b))
    rayleigh_quotient_iteration(copy.deepcopy(a), copy.deepcopy(b))
