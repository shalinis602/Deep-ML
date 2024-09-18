import numpy as np

def inverse_2x2(matrix: list[list[float]]) -> list[list[float]]:
    matrix_np = np.array(matrix)
    inverse = np.linalg.inv(matrix_np)
    return inverse

matrix = [[4, 7], [2, 6]]
print(inverse_2x2(matrix))