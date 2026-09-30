import numpy as np

def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here
	matrix = np.array(matrix)

	scaled_matrix = matrix * scalar
	return scaled_matrix