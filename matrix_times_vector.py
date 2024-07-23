# https://www.deep-ml.com/problem/1

def matrix_dot_vector(a:list[list[int|float]],b:list[int|float])-> list[int|float]:
	c = [0] * len(a)
	if len(a[0]) != len(b):
		return -1
	for i in range(len(a)):
		for j in range(len(b)):
			c[i] += a[i][j] * b[j]
	return c

matrix = [[1,2],[2,4]]
vector = [1,2]
print(matrix_dot_vector(matrix, vector))