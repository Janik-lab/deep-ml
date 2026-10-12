import numpy as np

def predict_logistic(X: np.ndarray, weights: np.ndarray, bias: float) -> np.ndarray:
	"""
	Implements binary classification prediction using Logistic Regression.

	Args:
		X: Input feature matrix (shape: N x D)
		weights: Model weights (shape: D)
		bias: Model bias

	Returns:
		Binary predictions (0 or 1)
	"""
	z = X @ weights + bias

	sigmoid = 1 /(1+ np.exp(-z))

	predictions = np.where(sigmoid >= 0.5, 1, 0)
	# Your code here
	return predictions