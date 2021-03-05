from sklearn import neighbors
import numpy as np

def quantize(img, representative_points):
	quantized_img = np.zeros_like(img)
	tree = neighbors.KDTree(representative_points, leaf_size=30)
	for x in range(img.shape[0]):
		for y in range(img.shape[1]):
			dist, index = tree.query([img[x][y]], k=1)
			quantized_img[x][y] = representative_points[index][0]
	return quantized_img


