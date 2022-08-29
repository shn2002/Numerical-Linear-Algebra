# coding: utf8
import numpy as np
import copy


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


def func1(x1, x2):
    return x1 + 2 * x2 - 2


def func2(x1, x2):
    return x1 * x1 + 4 * x2 * x2 - 4


def partial_diff_func1_x1(x1, x2):
    return 1


def partial_diff_func1_x2(x1, x2):
    return 2


def partial_diff_func2_x1(x1, x2):
    return 2 * x1


def partial_diff_func2_x2(x1, x2):
    return 8 * x2


if __name__ == "__main__":
    np.set_printoptions(suppress=True)
    x = np.array([[1], [2]], dtype=float)
    i = 0
    flag = True

    while flag:
        print('--------------------', 'Iteration' + str(i), '--------------------')
        fx = np.array([func1(x[0], x[1]), func2(x[0], x[1])], dtype=float)
        negative_fx = np.array([(-1) * copy.deepcopy(fx[0]), (-1) * copy.deepcopy(fx[1])], dtype=float)
        if i == 0:
            negative_fx_prev = np.array([(-1) * copy.deepcopy(fx[0]), (-1) * copy.deepcopy(fx[1])], dtype=float)
            b = np.array(
                [[partial_diff_func1_x1(copy.deepcopy(x[0]), copy.deepcopy(x[1])),
                partial_diff_func1_x2(copy.deepcopy(x[0]), copy.deepcopy(x[1]))],
                [partial_diff_func2_x1(copy.deepcopy(x[0]), copy.deepcopy(x[1])),
                partial_diff_func2_x2(copy.deepcopy(x[0]), copy.deepcopy(x[1]))],
                ],
                dtype=float)
            s = np.round(guass_elimination_partial_pivoting(copy.deepcopy(b), copy.deepcopy(negative_fx)), 2)
            print('xbar' + str(i), '=', x.transpose())
            print('fx' + str(i), '=', fx.transpose())
            print('B' + str(i), '=', b)
            print('sbar' + str(i), '=', s)
            x = np.round(x + s, 2)
            y = np.array([0, 0], dtype=float)
        else:
            y = np.round(negative_fx_prev + fx,2)
            print('ybar' + str(i - 1), '=', y)
            b = np.round(copy.deepcopy(b)+(y-copy.deepcopy(b) @ s) @ s.transpose()/(s[0]*s[0]+s[1]*s[1]),2)
            s = np.round(guass_elimination_partial_pivoting(copy.deepcopy(b), copy.deepcopy(negative_fx)), 2)
            print('fx' + str(i), '=', fx.transpose())
            print('B' + str(i), '=', b)
            print('sbar' + str(i), '=', s)
            negative_fx_prev = np.array([(-1) * copy.deepcopy(fx[0]), (-1) * copy.deepcopy(fx[1])], dtype=float)
            print('xbar' + str(i), '=', x.transpose())
            x = np.round(x + s, 2)
        i = i + 1
        if abs(s[0]) <= 0.00001 and abs(s[1]) <= 0.00001:
            flag = False
