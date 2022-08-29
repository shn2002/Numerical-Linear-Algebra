# coding: utf8
import numpy as np

if __name__ == "__main__":
    np.set_printoptions(suppress=True)

    # a = np.array([[5, 0, 0], [0, 2, 0], [0, 0, 10]])
    a = np.array([[0.913, 0.659], [0.457, 0.330]])
    b = np.array([[0.254, 0.127]]).transpose()
    x_hat = np.array([[-0.999, -1.001]]).transpose()
    # x_hat = np.array([[-0.0827, 0.5]]).transpose()
    print(b)
    print(a)
    print(x_hat)
    print('r = b - A * x_hat = ')
    r = b - np.matmul(a, x_hat)
    print(r)
    print('norm 1 for this array ||r||1 = ', np.linalg.norm(r, 1))

    p = np.array([[1, 3, 2]])
    q = np.array([[-1, 0, -2]])
    print('distance is ', np.linalg.norm(p - q, 2))
