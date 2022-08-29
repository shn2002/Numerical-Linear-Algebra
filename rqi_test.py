import numpy as np

A = np.array([[1, 2, 0], [-2, 1, 2], [1, 3, 1]])
x = np.ones(A.shape[0])
for k in range(10): # 幂迭代，迭代次数为10
    x = A @ x
x = x / np.linalg.norm(x)
print('Dominant eigenvector:')
print(x)
print()
print('Dominant eigenvalue:')
lambda1 = A @ x @ x / (x @ x) # 瑞利商
print(lambda1)