import numpy as np

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:

	matrix = np.array(matrix)

	trace = np.trace(matrix)
	det = np.linalg.det(matrix)

	first_eigenvalue = - (-trace)/2 + np.sqrt((trace/2)**2 - det)
	second_eigenvalue = - (-trace)/2 - np.sqrt((trace/2)**2 - det)

	eigenvalues = [first_eigenvalue, second_eigenvalue]

	return eigenvalues