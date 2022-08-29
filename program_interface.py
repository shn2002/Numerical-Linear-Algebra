# coding: utf8
import copy
import numpy as np
from gram_schmidt_transform import gram_schmidt_transform
from householder_transform_QR import householder_transform_QR

if __name__ == "__main__":
    # a = np.array(
    #     [[1, -2],
    #      [-1, -2],
    #      [-2, 1],
    #      [-1, 2]],
    #     dtype=float)

    # b = np.array(
    #     [[-1,
    #       -3,
    #       -1,
    #       1]], dtype=float).transpose()
    # a = np.array(
    #     [[3, 1],
    #      [1, 2]],
    #     dtype=float)
    # b = np.array(
    #     [[2,
    #       1]], dtype=float).transpose()
    a = np.array(
        [[1, -1, 2],
         [2, 2, -1],
         [-1, 1, 1],
         [2, -1, 0],
         [1, 1, -1]],
        dtype=float)
    b = np.array(
        [[4,
          -4,
          1,
          3,
          -2]], dtype=float).transpose()
    x_number = 3
    gs_transform = gram_schmidt_transform(copy.deepcopy(a), copy.deepcopy(b), x_number)
    HH_gs_transform = householder_transform_QR(copy.deepcopy(a), copy.deepcopy(b), x_number)
