import numpy as np
import random

def sample(img, neighbor_std_img, num_sample_points):
	random.seed(0)
	sampled_points = []
	sample_std = []
	block_size = np.floor(np.sqrt(img.shape[0]*img.shape[1]/num_sample_points))
	for i in range(0, img.shape[0], block_size):
		for j in range(0, img.shape[1], block_size):
			end_i = min(i, img.shape[0])
			end_j = min(j, img.shape[1])
			img_block = img[i:end_i, j:end_j]
			img_block.reshape(img_block.shape[0]*img_block.shape[1], 3)
			neighbor_std_img_block = neighbor_std_img[i:end_i, j:end_j]
			neighbor_std_img_block.reshape(img_block.shape[0]*img_block.shape[1], 3)
			index = random.randint(0, len(img_block))
			sampled_points.append(img_block[index])
			sample_std.append(neighbor_std_img_block[index])
	return sampled_points, sample_std
