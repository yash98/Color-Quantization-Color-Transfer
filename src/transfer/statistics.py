import numpy as np
import cv2 as cv

def neighbor_std(img, each_side):
	padded_img = cv.copyMakeBorder(img, each_side, each_side, each_side, each_side, borderType=cv.BORDER_CONSTANT, value=[0,0,0])
	std_matrix = np.zeros_like(img)
	for i in img.shape[0]:
		for j in img.shape[1]:
			block = padded_img[i-each_side:i+each_side, j-each_side:j+each_side]
			std_matrix[i, j] = np.std(block)
	return std_matrix
