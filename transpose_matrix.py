import numpy as np

def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    a_np = np.array(a)
    return np.transpose(a_np)

a = [[1,2,3],[4,5,6]]
print(transpose_matrix(a))