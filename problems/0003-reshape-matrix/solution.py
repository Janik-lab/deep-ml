import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method

	number_of_elements = new_shape[0] * new_shape[1]
	a = np.array(a)

	if a.size == number_of_elements:
		reshaped_a = a.reshape(new_shape).tolist()
	else:
		reshaped_a = []

	return reshaped_a