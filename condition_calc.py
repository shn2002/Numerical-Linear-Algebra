# coding: utf8
import numpy as np

if __name__ == "__main__":
    # a = np.array([[5, 0, 0], [0, 2, 0], [0, 0, 10]])
    a = np.array([[2, -1, 1], [1, 0, 1], [3, -1, 4]])
    print('this matrix inverse = ', np.linalg.inv(a))
    print('norm 1 for this matrix ||x||1 = ', np.linalg.norm(a, 1))
    print('norm 1 for this matrix s inverse ||(x)-1||1 = ', round(np.linalg.norm(np.linalg.inv(a), 1),4))
    print('(condition 1 norm 1 for this matrix) * (norm 1 for this array s inverse) = cond1(A) = ',
          np.linalg.norm(a, 1) * round(np.linalg.norm(np.linalg.inv(a), 1),4))

    print('norm inf for this matrix ||x||1 = ', np.linalg.norm(a, 1))
    print('norm inf for this matrix s inverse ||(x)-1||1 = ', round(np.linalg.norm(np.linalg.inv(a), np.inf),4))
    print('(condition inf norm inf for this matrix) * (norm 1 for this matrix s inverse) = cond_inf (A) = ',
          np.linalg.norm(a, np.inf) * round(np.linalg.norm(np.linalg.inv(a), np.inf),4))
