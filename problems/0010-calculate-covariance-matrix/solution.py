import numpy as np

def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	# Your code here
	vectors = np.array(vectors)

	covarinace_matrix = np.cov(vectors)

	covarinace_matrix = covarinace_matrix.tolist()

	


	return covarinace_matrix