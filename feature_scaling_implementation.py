import numpy as np

def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
    # Standardization
    mean = np.mean(data, axis=0)
    std = np.std(data, axis=0)
    standardized_data = (data - mean) / std

    # Min-Max Normalization
    max_v, min_v = np.max(data, axis=0), np.min(data, axis=0)
    normalized_data = (data - min_v) / (max_v - min_v)
    
    return np.round(standardized_data.flatten(), 4), np.round(normalized_data.flatten(), 4)

data = np.array([[1, 2], [3, 4], [5, 6]])
print(feature_scaling(data))
