import numpy as np

def k_means_clustering(points: list[tuple[float, ...]], k: int, initial_centroids: list[tuple[float, ...]], max_iterations: int) -> list[tuple[float, ...]]:
	# Your code here

	

	points = np.array(points, dtype = float)
	initial_centroids = np.array(initial_centroids, dtype = float)


	dx = np.subtract.outer(points[:, 0], initial_centroids[:, 0])
	dy = np.subtract.outer(points[: , 1], initial_centroids[:,1])


	distance = np.sqrt(dx**2 + dy**2)

	labels = np.argmin(distance, axis=1)

	
	for i in range (max_iterations):
		updated_centroid = []

		for label_centroid in range(k):
			
			cluster_points = points[label_centroid == labels]
			new_centroid = np.mean(cluster_points, axis = 0)

			updated_centroid.append(new_centroid)


		updated_centroid = np.array(updated_centroid)
		
		dx_new = np.subtract.outer(points[:, 0], updated_centroid[:, 0])
		dy_new = np.subtract.outer(points[: , 1], updated_centroid[:,1])

		distance_new = np.sqrt(dx_new**2 + dy_new**2)
		labels = np.argmin(distance_new, axis=1)

	final_centroids = list(map(tuple, updated_centroid.tolist()))
	return final_centroids