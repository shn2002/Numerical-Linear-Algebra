import numpy as np


# from scipy import linalg

# a = np.array([[2, -1, 1], [1, 0, 1], [3, -1, 4]])
# a = np.array([[4, 0, 0], [0, -5, 0], [0, 0, 10]])
# 求a的逆矩阵

def get_inverse_matrix(array):
    print("a的逆矩阵是 = \n", np.linalg.inv(array))
    return np.linalg.inv(a)


def cond_1(array):
    print("cond(1)(A) = ", np.linalg.cond(array, 1))
    return np.linalg.cond(array, 1)


def cond_inf(array):
    print("cond(INF)(A) = ", np.linalg.cond(array, np.inf))
    return np.linalg.cond(array, np.inf)


def norm_1(array):
    print("将矩阵竖过来的元素取绝对值相加，找出最大的一列的和就是结果")
    print("1-norm = ", np.linalg.norm(array, 1))
    return None


def norm_2(array):
    print("将矩阵横过来的元素取平方数相加，然后开根号，就是结果")
    print("2-norm = ", np.linalg.norm(array, 2))
    return None


def norm_inf(array):
    print("将矩阵横过来的元素取绝对值相加，找出最大的一行的和就是结果")
    print("inf-norm = ", np.linalg.norm(array, np.inf))
    return None


def euclidean_norm(array):
    np.zeros((2, 1))
    print("euclidean-norm = ", np.linalg(array))
    return None


if __name__ == '__main__':
    a = np.array([[1, -2, 3], [0, 2, -1], [0, 0, -1]])
    b= np.array([[-3], [0], [2]])
    print(np.dot(np.linalg.inv(a), b))
    print("----------------")
    #get_inverse_matrix(a)

    d= np.array([[5, 0, 0], [0, 2, 0], [0, 0, 10]])
    get_inverse_matrix(d)
    cond_1(d)
    cond_inf(d)


    # "例题：Example 2.5: Find the 1-norm and ∞ −norm of the following matrix 调用 norm_1 和 norm_inf"
    a = np.array([[2, -1, 1], [1, 0, 1], [3, -1, 4]])
    norm_1(a)
    norm_inf(a)
    #euclidean_norm(a)
    b = np.array([[-1, 1], [0, 1], [-1, 4]])
    print(len(b))
    print(len(b[0]))
    c = np.zeros(2*2)
    print(c)
    # print(np.matrix.transpose(a))
    print(np.dot(a, np.matrix.transpose(a)))
    # cond_inf(a)
    # "例题：Example 2.6: Find the 1-norm and ∞ −norm of the following matrix 调用 find_1_norm 和 find_inf_norm"
