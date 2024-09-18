import numpy as np

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    matrix_np = np.array(matrix)
    if mode == 'column':
        means = np.mean(matrix_np, axis=0)
    else:
        means = np.mean(matrix_np, axis=1)
    return means

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mode = 'column'
print(calculate_matrix_mean(matrix, mode))

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mode = 'row'
print(calculate_matrix_mean(matrix, mode))