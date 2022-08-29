# coding: utf8
import copy

import numpy as np
import math


# calculate
def step1():
    print("calculate ")


if __name__ == "__main__":
    a = np.array([[1, 2, -1, 0, -1, 2]], dtype=float).transpose()
    e1 = np.array([[1, 0, 0, 0, 0, 0]], dtype=float).transpose()
    str1 = '\u03B1 = - sgn(a1)||a||2 ='
    alfa = float(round(np.linalg.norm(a, 2), 4) * a[0] / abs(a[0]) * (-1))
    print(str1, alfa)
    print('----------------------------------')
    str2 = 'v = a - \u03B1e1 = '
    v = a - alfa * e1
    print(str2, a, '-', alfa, '*', e1, ' = ', v)
    print('----------------------------------')
    str3 = 'Ha = 2(Vt*a/Vt*V)*v = '
    # print(2 * (np.matmul(v.transpose(), a) / np.matmul(v.transpose(), v)))
    VtaVtVa = round(float(2 * (np.matmul(v.transpose(), a) / np.matmul(v.transpose(), v))),4)
    Ha = a-VtaVtVa*v
    print(str3, a, '-2*(', v.transpose(), '*', a, '/', v.transpose(), '*', v, ' )*', v)
    print('----------------------------------')
    print('Ha =', Ha)


