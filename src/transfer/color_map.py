import numpy as np

from transfer.statistics import neighbor_std

def best_match_global(sample_points, sample_std, point, std):
	w1, w2 = 0.5, 0.5
	best_dist = np.inf
	best_dist_index = 0
	for i in range(len(sample_points)):
		current_dist = w1 * np.linalg.norm(sample_points[i][0] - point[0]) + w2 * np.linalg.norm(sample_std[i] - std)
		if current_dist <= best_dist:
			best_dist = current_dist
			best_dist_index = i
	return best_dist_index

def transfer_global(sample_points, sample_std, target_image, target_std):
	colored_img = np.zeros_like(target_image)
	for i in range(target_image.shape[0]):
		for j in range(target_image.shape[1]):
			best_sample_index = best_match_global(sample_points, sample_std, target_image[i, j], target_std[i, j])
			colored_img[i, j, 0] = target_image[i, j, 0]
			colored_img[i, j, 1:] = sample_points[best_sample_index][1:]
	return colored_img

def transfer_swatch(target_image, sample_points_dict, swatch_list, neighbor_side):
	colored_img = np.zeros_like(target_image)
	for i in range(target_image.shape[0]):
		for j in range(target_image.shape[1]):
			best_dist = np.inf
			best_point = None
			for swatch_id in sample_points_dict:
				swatch_samples = sample_points_dict[swatch_id]
				swatch = swatch_list[swatch_id]
				for sample_point in swatch_samples:
					summation = 0.0
					sample_point_x, sample_point_y = sample_point
					for x in range(-1*neighbor_side, neighbor_side):
						for y in range(-1*neighbor_side, neighbor_side):
							try:
								summation += (swatch[sample_point_x + x, sample_point_y + y] - target_image[i+x, j+y])**2
							except IndexError:
								pass
					if summation <= best_dist:
						best_dist = summation
						best_point = sample_point[sample_point_x, sample_point_y]

			colored_img[i, j, 0] = target_image[i, j, 0]
			colored_img[i, j, 1:] = best_point[1:]
	return colored_img
