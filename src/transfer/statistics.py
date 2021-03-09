import numpy as np
import cv2 as cv

def neighbor_std(img, each_side):
	padded_img = cv.copyMakeBorder(img, each_side, each_side, each_side, each_side, borderType=cv.BORDER_CONSTANT, value=[0,0,0])
	std_matrix = np.zeros((img.shape[0], img.shape[1]))
	for i in range(each_side, img.shape[0]):
		for j in range(each_side, img.shape[1]):
			# only std of luminance is needed
			block = padded_img[i-each_side:i+each_side, j-each_side:j+each_side, 0]
			std_matrix[i-each_side, j-each_side] = np.std(block)
	return std_matrix
