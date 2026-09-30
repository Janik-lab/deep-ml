import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	# Your code here, make sure to round
	
	X = np.array(X)
	y = np.array(y)
	
	beta = np.linalg.lstsq(X, y, rcond = None)[0]

	beta = np.round(beta, 4).tolist()

	return beta