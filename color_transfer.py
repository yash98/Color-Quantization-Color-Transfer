from src import util
from src.transfer import statistics
from src.transfer import jittered_sampling
from src.transfer import histogram_equalization
from src.transfer import color_map

import argparse
import cv2 as cv
import numpy as np
# import sys
# np.set_printoptions(threshold=sys.maxsize)

sample_size = 200
neighbor_std_side = 2

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Color Transfer")
	parser.add_argument("-s", "--swatches", action="store_true", help="To enable user interactive swatch selection")
	parser.add_argument("gray_image", type=str, help="Path of grayscale image to colorize")
	parser.add_argument("color_image", type=str, help="Path of color image based on which colorization is done")
	parser.add_argument("-o", "--output", type=str, help="Output file to save the colored image as")
	args = parser.parse_args()

	gray_image = cv.imread(args.gray_image)
	color_image = cv.imread(args.color_image)

	if gray_image is None:
		print("Path for grey image is incorrect")
		exit()

	if color_image is None:
		print("Path for color image is incorrect")
		exit()

	gray_image_lab = cv.cvtColor(gray_image, cv.COLOR_BGR2LAB)
	color_image_lab = cv.cvtColor(color_image, cv.COLOR_BGR2LAB)

	# util.histogram(gray_image_lab)
	# util.histogram(color_image)
	
	gray_neighbor_std = statistics.neighbor_std(gray_image_lab, neighbor_std_side)
	color_neighbor_std = statistics.neighbor_std(color_image_lab, neighbor_std_side)

	equalized_img = histogram_equalization.equalize(gray_image_lab, color_image_lab).astype(np.uint8)
	sample_points, sample_std = jittered_sampling.sample(color_image_lab, color_neighbor_std, sample_size)

	# util.histogram(equalized_img)

	colored_img_lab = color_map.transfer(sample_points, sample_std, gray_image_lab, gray_neighbor_std)
	util.histogram(color_image_lab)
	colored_img = cv.cvtColor(colored_img_lab, cv.COLOR_LAB2BGR)
	util.histogram(color_image)

	util.showimage("color", color_image)
	showcase_img = np.concatenate((gray_image, colored_img), axis=1)
	util.showimage("side-by-side", showcase_img)