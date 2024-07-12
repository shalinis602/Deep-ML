# https://www.deep-ml.com/problem/10

import numpy as np

def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    nV = len(vectors) # no of vectors
    lV = len(vectors[0]) # len of vectors
    cov_matrix = np.zeros((nV, nV)) 

    # Calculate mean
    mean = [0] * nV # matrix w/ mean values 
    for i in range(nV):
        mean[i] = sum(vectors[i])/lV 

    # Calculate covariance of vectors
    cov_v = [0] * nV
    for i in range(nV):
        sq_sum = 0
        for j in range(lV):
            sq_sum += pow((vectors[i][j]-mean[i]), 2)
        cov_v[i] = (1/(lV-1)) * sq_sum

    for i in range(nV):
        cov_matrix[i][i] = cov_v[i]

    # Calculate covariance wrt each other
    for i in range(nV):
        for j in range(i+1, nV):
            prod_sum = sum((vectors[i][k]-mean[i]) * (vectors[j][k] - mean[j]) for k in range(lV))
            cov_matrix[i,j] = (1/(lV-1)) * prod_sum
            cov_matrix[j,i] = cov_matrix[i,j]

    return cov_matrix.tolist()

vectors = [[1, 2, 3], [4, 5, 6]]
print(calculate_covariance_matrix(vectors))