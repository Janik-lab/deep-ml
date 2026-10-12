import math
import numpy as np

def softmax(scores: list[float]) -> list[float]:
	numpy_scores = np.array(scores)

	numpy_scores = numpy_scores - np.max(numpy_scores)

	exp_scores = np.exp(numpy_scores)

	probabilities = exp_scores / np.sum(exp_scores)

	return probabilities.tolist()