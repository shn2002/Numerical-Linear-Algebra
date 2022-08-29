import np as np
from numpy.ma import zeros

x0 = np.array([1, 1, 1], dtype=float)

# x0 = np.array([0, 1], dtype=float)
n = len(x0)
count = 1
errorTol = 0.7
currentError = 10 * errorTol
normx0_old = 100
sigma_old = 100
print('k ', '      xk ', '      sigma')

while currentError > errorTol:
    A = np.array([[1, -1, 0], [0, -4, 2], [0, 0, -2]], dtype=float)
    # A = np.array([[3, 1], [1, 3]], dtype=float)
    x0t = x0.T
    sigma = np.dot(x0t, np.dot(x0, A)) / np.dot(x0t, x0)

    A = A - (np.dot(sigma, np.identity(n)))

    x = zeros(n, float)
    for k in range(n - 1):
        max = -1
        index = -1

        for i in range(k, n):
            # print (abs(A[i][k]))
            if abs(A[i][k]) > max:
                max = abs(A[i][k])
                index = i
        if k != index:
            A[[k, index]] = A[[index, k]]
            x0[[k, index]] = x0[[index, k]]

        for j in range(k + 1, n):
            m = A[j][k] / A[k][k]
            for p in range(k, n):
                A[j][p] = A[j][p] - m * A[k][p]
            x0[j] = x0[j] - m * x0[k]

    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            x0[i] = x0[i] - A[i][j] * x[j]
        x[i] = x0[i] / A[i][i]

    normx0 = np.linalg.norm(x, np.inf)
    x0 = x / normx0

    print(str(count), str(x0), str(format(normx0, ".4f")), sigma)
    count += 1
    currentError = abs(sigma - sigma_old) / abs(sigma_old) * 100
    print('currentError = ',str(currentError), 'and errorTol =', str(errorTol))
    sigma_old = sigma
