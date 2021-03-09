import numpy as np

def best_match(sample_points, sample_std, point, std):
	w1, w2 = 0.5, 0.5
	best_dist = np.inf
	best_dist_index = 0
	for i in len(sample_points):
		current_dist = w1 * np.linalg.norm(sample_points[i], point) + w2 * np.linalg.norm(sample_std[i], std)
		if current_dist <= best_dist:
			best_dist = current_dist
			best_dist_index = i
	return best_dist_index

def transfer(sample_points, sample_std, target_image, target_std):
	colored_img = np.zeros_like(target_image)
	for i in range(target_image.shape[0]):
		for j in range(target_image.shape[1]):
			best_sample_index = best_match(sample_points, sample_std, target_image[i, j], target_std[i, j])
			colored_img[i, j, 2:] = sample_points[best_sample_index][2:]
	return colored_img
