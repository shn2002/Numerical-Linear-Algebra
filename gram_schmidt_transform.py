# coding: utf8
import copy
import numpy as np


class gram_schmidt_transform:
    def __init__(self, mat_a, mat_b, x_number):
        self.a = mat_a
        self.b = mat_b
        self.x_number = x_number
        self.execution()

    def calculation(self, r_mat, t):
        col_size = np.size(self.a, 1)
        row_size = np.size(self.a, 0)
        count = 0
        for i in range(t, col_size):
            if count == 0:
                a1 = np.array([self.a[:, t]], dtype=float).transpose()
                str1 = 'r' + str(t + 1) + str(t + 1) + ' = ||a' + str(t + 1) + '||2 ='
                r = float(round(np.linalg.norm(a1, 2), 4))
                print(str1, r)
                str2 = 'q' + str(t + 1) + ' =a' + str(t + 1) + ' /r' + str(t + 1) + str(t + 1) + '='
                q1 = np.round(a1 / r, 4)
                print(str2, '\n', q1)
                r_mat[t][i] = r
                for j in range(0, row_size):
                    self.a[j][t] = np.round(q1[j], 4)
                count = count + 1
            else:
                g = np.array([self.a[:, t]])
                h = np.array([self.a[:, i]]).transpose()
                str3 = 'r' + str(t + 1) + ',' + str(i + 1) + ' = q' + str(t + 1) + 'T' + 'a' + str(i + 1) + '='
                r_next = round(np.matmul(g, h)[0][0], 4)
                r_mat[t][i] = r_next
                new_a_col = (np.array([self.a[:, i]]) - r_next * g).transpose()
                for j in range(0, row_size):
                    self.a[j][i] = np.round(new_a_col[j], 4)
                print(str3, r_next)
        print('this is ', t + 1, 'iteration and a  =\n', self.a)
        print('-----------------------------------')

        return r_mat

    def execution(self):
        print('-------------this calculation by using gram_schmidt_transform----------------------')
        np.set_printoptions(suppress=True)
        r_mat = np.zeros((self.x_number, np.size(self.a, 1)))
        for k in range(0, self.x_number):
            r_mat = self.calculation(r_mat, k)
        print('this is R matrix\n', r_mat)
        print('-----------------------------------')
        self.b = np.matmul(self.a.transpose(), self.b)
        print('Q1Tb = (a) T * b = ', self.b)
        result = np.round(np.matmul(np.linalg.inv(r_mat), self.b), 0)
        print('final result is x = %s' % result)
    # if __name__ == "__main__":
    # np.set_printoptions(suppress=True)
    # a = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1], [-1, 1, 0], [-1, 0, 1], [0, -1, 1]], dtype=float)
    # b = np.array([[1237, 1941, 2417, 711, 1177, 475]], dtype=float).transpose()
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
