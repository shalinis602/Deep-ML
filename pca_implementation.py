import numpy as np 

def pca(data: np.ndarray, k: int):
    # Standardization
    mean = np.mean(data, axis=0)
    std = np.std(data, axis=0)
    std_data = (data - mean) / std

    # Calcuate covariance matrix
    cov_matrix = np.cov(std_data, rowvar=False)
    # rowvar=False ensures features are considered cols and obs rows

    # Compute eigenvalues and eigenvectors
    evals, evecs = np.linalg.eigh(cov_matrix)

    # Sort eigenvalues and corresponding eigenvectors in desc order
    sorted_indices = np.argsort(evals)[::-1]
    sorted_evecs = evecs[:, sorted_indices]

    # Select the top k eigenvectors
    top_k = sorted_evecs[:, :k]

    # Adjust the signs for consistency
    for i in range(top_k.shape[1]):
        if top_k[0, i] < 0:
            top_k[:, i] *= -1

    return np.round(top_k, 4).tolist()

data = np.array([[4,2,1],[5,6,7],[9,12,1],[4,6,7]])
k = 2
print(pca(data, k))