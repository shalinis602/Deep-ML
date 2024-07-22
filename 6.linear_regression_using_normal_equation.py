import numpy as np

def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    X_np = np.array(X)
    y_np = np.array(y)

    X_transpose = X_np.T
    product = X_transpose @ X_np

    inverse = np.linalg.inv(product)

    X_transpose_y = X_transpose @ y_np
    theta = inverse @ X_transpose_y
    return theta.tolist()

'''
X = [[1, 1], [1, 2], [1, 3]] 
y = [1, 2, 3]
print(linear_regression_normal_equation(X, y))
'''