# coding: utf8
import numpy as np

if __name__ == "__main__":
    a = np.array([[1,0], [0,1], [1,1]])
    # a = np.array([[-1.6, 1.2]]).transpose()
    print('norm 1 for this array ||x||1 = ', np.linalg.norm(a, 1))
    # print('norm 1 for this array ||x||2 = ', np.linalg.norm(a, 2))
    # print('norm 1 for this array ||x||inf = ', np.linalg.norm(a, np.inf))

    # c = np.array([[1, 0], [-1, -2], [1, 1]])
    # print(np.linalg.inv(c))


    # d=np.matmul(c.transpose(),c)
    # print('d = ', d)
    #
    # print('d-1',np.linalg.inv(d))


