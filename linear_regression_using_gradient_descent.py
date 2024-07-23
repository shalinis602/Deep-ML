# https://www.deep-ml.com/problem/Linear%20Regression%20Using%20Gradient%20Descent

import numpy as np

def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
    m, n = X.shape

    # convert 1d array y into a 2d column vector
    y = y.reshape(-1, 1)

    theta = np.zeros((n, 1))
    for iteration in range(iterations):
        # Compute predictions
        predictions =  X.dot(theta)

        # Compute residuals
        residuals = predictions - y

        # Compute gradients
        gradients = (1/m) * X.T.dot(residuals)

        # Update theta
        theta = theta - (alpha*gradients)
    return np.round(theta.flatten(), 4)

X = np.array([[1, 1], [1, 2], [1, 3]])
y = np.array([1, 2, 3])
alpha = 0.01 
iterations = 1000
print(linear_regression_gradient_descent(X, y, alpha, iterations))