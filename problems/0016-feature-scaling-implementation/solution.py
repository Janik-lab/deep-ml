import numpy as np

def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	# Your code here

	# standardized_data

	mean = np.mean(data, axis = 0)
	std = np.std(data, axis=0)

	z_socre = (data - mean)/std

	standardized_data = z_socre

	# normalized_data

	data_min = np.min(data, axis = 0)
	data_max = np.max(data, axis = 0)

	normalized_data = (data - data_min)/(data_max - data_min)
	
	return standardized_data, normalized_data