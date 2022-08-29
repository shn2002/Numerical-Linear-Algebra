import np as np
from numpy.ma import zeros

x0 = np.array([1, 1, 1], dtype = float)

# x0 = np.array([0, 1], dtype = float)
errorTol = 0.1
currentError = 10 * errorTol
n = len(x0)
count = 1
normx0_old = 100

print('k ', '     xk ', '      ratio')

while currentError > errorTol:
    A = np.array([[1, -1, 0], [0, -4, 2], [0, 0, -2]], dtype=float)
    # A = np.array([[3, 1], [1, 3]], dtype=float)

    x = zeros(n, float)
    for k in range(n-1):
        if A[k][k] != 0:
            for i in range(k+1, n):
                m = A[i][k] / A[k][k]
                for j in range(k, n):
                    A[i][j] = A[i][j] - m * A[k][j]
                x0[i] = x0[i] - m * x0[k]
        else:
            continue

    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            x0[i] = x0[i] - A[i][j] * x[j]
        x[i] = x0[i] / A[i][i]

    normx0 = np.linalg.norm(x, np.inf)
    x0 = x / normx0
    print(str(count), str(np.round_(x0, 4)), str(format(normx0, ".4f")))
    count += 1
    currentError = abs(normx0 - normx0_old) / normx0_old * 100
    normx0_old = normx0