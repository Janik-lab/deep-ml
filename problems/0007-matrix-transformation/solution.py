import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:

	A = np.array(A)
	T = np.array(T)
	S = np.array(S)

	if np.linalg.det(T) and np.linalg.det(S) != 0:
		transformed_matrix = np.linalg.inv(T) @ A @ S
		transformed_matrix = transformed_matrix.tolist()
	else:
		transformed_matrix = -1



	return transformed_matrix