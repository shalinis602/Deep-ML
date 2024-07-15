# https://www.deep-ml.com/problem/11 

import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
    size = len(b)
    x = np.zeros(size)
    for _ in range(n):
        x_new = np.zeros(size)    
        for i in range(size):
            sum_ax = np.dot(A[i, :], x) - (A[i,i] * x[i]) 
            x_new[i] = (1/A[i][i]) * (b[i] - sum_ax)
        x = x_new
    return [float(f'{val:.4f}') for val in x]

A = np.array([[5, -2, 3], [-3, 9, 1], [2, -1, -7]])
b = np.array([-1, 2, 3])
n = 2
print(solve_jacobi(A, b, n))