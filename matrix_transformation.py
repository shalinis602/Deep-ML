import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
    A_np = np.array(A)
    S_np = np.array(S)
    T_np = np.array(T)

    if np.linalg.det(T_np) == 0 or np.linalg.det(S_np) == 0:
        return -1
    
    T_inv = np.linalg.inv(T_np)

    m = np.dot(T_inv, A_np)
    transformed_matrix = np.dot(m, S_np)
    return transformed_matrix

print(transform_matrix(A = [[1, 2], [3, 4]], T = [[2, 0], [0, 2]], S = [[1, 1], [0, 1]]))
print(transform_matrix(A = [[2, 3], [1, 4]], T = [[3, 0], [0, 3]], S = [[1, 1], [1, 1]]))