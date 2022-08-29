# coding: utf8
import copy
import numpy as np


class householder_transform_QR:
    def __init__(self, mat_a, mat_b, x_number):
        self.a = mat_a
        self.b = mat_b
        self.a_mod = mat_a
        self.x_number = x_number
        self.execution()

    def householder_transform(self,t):
        col_size = np.size(self.a, 1)
        row_size = np.size(self.a, 0)
        new_matrix = copy.deepcopy(self.a)
        a1 = np.array([self.a[:, t]], dtype=float).transpose()
        a1_mod = np.array([self.a_mod[:, t]], dtype=float).transpose()
        e1 = np.zeros((np.size(self.a, 0), 1))
        e1[t] = 1
        str1 = '\u03B1 = - sgn(a' + str(t + 1) + ')||a' + str(t + 1) + '||2 ='
        alfa = float(round(np.linalg.norm(a1_mod, 2), 4) * a1_mod[t] / abs(a1_mod[t]) * (-1))
        print(str1, alfa)
        print('----------------------------------')
        str2 = 'v' + str(t + 1) + ' = a' + str(t + 1) + ' - \u03B1e' + str(t + 1) + ' = '
        v = a1_mod - alfa * e1
        print(str2,'\n', a1_mod, '-', '(', alfa, ')', '*', '\n',e1, ' = \n', v)
        for i in range(t, col_size):
            print("-------------------------------------------------------")
            print("this is Round %s,%s" % (t, i))
            print("-------------------------------------------------------")
            a_temp = np.array([self.a[:, i]], dtype=float).transpose()
            a_temp_mod = np.array([self.a_mod[:, i]], dtype=float).transpose()
            str3 = 'H' + str(t + 1) + 'a' + str(i + 1) + ' = 2(Vt*a' + str(i + 1) + '/Vt*V)*v = '
            # print(2 * (np.matmul(v.transpose(), a_temp) / np.matmul(v.transpose(), v)))
            VtaVtVa = round(float(2 * (np.matmul(v.transpose(), a_temp_mod) / np.matmul(v.transpose(), v))), 4)
            Ha = np.round(a_temp - VtaVtVa * v, 4)
            # print(str3, a_temp, '-2*(', v.transpose(), '*', a_temp, '/', v.transpose(), '*', v, ' )*', v)
            print('VtaVtVa =', VtaVtVa)
            print('H', str(t + 1), 'a', str(i + 1), ' =\n', a_temp, '-', VtaVtVa, '*', '\n',v, Ha)

            for m in range(0, row_size):
                new_matrix[m][i] = round(float(Ha[m]), 4)
            # print(new_matrix)
            # print('---------------------------')
        new_a = copy.deepcopy(new_matrix)
        VtaVtVa_for_b = round(float(2 * (np.matmul(v.transpose(), self.b) / np.matmul(v.transpose(), v))), 4)
        new_b = np.round(self.b - VtaVtVa_for_b * v, 0)
        print('H%s(b) = \n%s' % (str(t + 1), new_b))
        for m in range(1, col_size):
            for n in range(0, m):
                new_matrix[n][m] = 0
        return new_a, new_b, new_matrix

    def execution(self):
        print('-------------this calculation by using householder_transform_QR----------------------')
        np.set_printoptions(suppress=True)
        for k in range(0, self.x_number):
            self.a, self.b, self.a_mod = self.householder_transform(k)

        elimination_a = np.zeros((self.x_number, np.size(self.a, 1)))
        elimination_b = np.zeros((self.x_number, 1))
        for i in range(0, self.x_number):
            elimination_a[i] = self.a[i]
            elimination_b[i] = self.b[i]
        print('elimination_a =\n %s' % elimination_a)
        print('elimination_b =\n %s' % elimination_b)

        result = np.round(np.matmul(np.linalg.inv(elimination_a), elimination_b), 0)
        print('final result is x = \n%s' % result)

    # if __name__ == "__main__":

    # a = np.array([[1, -2], [-1, -2], [-2, 1], [-1, 2]], dtype=float)
    # b = np.array([[-1, -3, -1, 1]], dtype=float).transpose()
    # a_mod = a
    # x_number = 2
