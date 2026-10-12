import numpy as np
def relu(z: float) -> float:
	# Your code here
	result = np.where(z >= 0, z, 0)
	return result
