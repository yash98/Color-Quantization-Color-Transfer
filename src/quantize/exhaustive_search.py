import numpy as np

def nearest_neighbor(query_point, representative_points):
	best_point = np.array([0., 0., 0.])
	best_dist = 255.0 * np.sqrt(3)
	for rep_point in representative_points:
		current_dist = np.linalg.norm(rep_point-query_point)
		if current_dist < best_dist:
			best_dist = current_dist
			best_point = rep_point
	return best_point

def quantize(img, representative_points):
	# quantized_img = np.zeros_like(img)
	# for x in img.shape[0]:
	# 	for y in img.shape[1]:
	# 		quantized_img[x, y] = nearest_neighbor(img[x, y], representative_points)
	# return quantized_img

	vf = np.vectorize(lambda x: nearest_neighbor(x, nearest_neighbor))
	return vf(img)
