import numpy as np

def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	matrix_a = np.array(a)
	vektor_b = np.array(b)

	if matrix_a.shape[1] == vektor_b.shape[0]:
		result = matrix_a @ vektor_b
		result.tolist()
	else:
		result = -1
	return result