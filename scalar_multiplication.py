import numpy as np

def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    matrix_np = np.array(matrix)
    result = scalar * matrix_np
    return result

matrix = [[1, 2], [3, 4]]
scalar = 2
print(scalar_multiply(matrix, scalar))