import math
import numpy as np

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float):
    features_np = np.array(features)
    weights_np = np.array(weights)

    # Calculate the weighted sum of inputs plus bias
    z = np.dot(features_np, weights_np) + bias

    # Sigmoid activation function 
    output = 1 / (1+ np.exp(-z))

    # MSE
    mse = np.mean((output - labels) ** 2)
    return np.round(output, 4), round(mse, 4).tolist()

features = [[0.5, 1.0], [-1.5, -2.0], [2.0, 1.5]]
labels = [0, 1, 0]
weights = [0.7, -0.4]
bias = -0.1
print(single_neuron_model(features, labels, weights, bias))