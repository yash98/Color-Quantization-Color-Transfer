from src import util
from src.transfer import statistics
from src.transfer import jittered_sampling
from src.transfer import histogram_equalization
from src.transfer import color_map

import argparse
import cv2 as cv
import numpy as np

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
	gray_image_lab = cv.cvtColor(gray_image, cv.COLOR_RGB2LAB)
	color_image_lab = cv.cvtColor(color_image, cv.COLOR_RGB2LAB)
	
	gray_neighbor_std = statistics.neighbor_std(gray_image_lab, neighbor_std_side)
	color_neighbor_std = statistics.neighbor_std(color_image_lab, neighbor_std_side)

	equalized_img = histogram_equalization.equalize(gray_image_lab, color_image_lab)
	sample_points, sample_std = jittered_sampling.sample(color_image_lab, color_neighbor_std, sample_size)

	colored_img_lab = color_map.transfer(sample_points, sample_std, gray_image_lab, gray_neighbor_std)
	colored_img = cv.cvtColor(colored_img_lab, cv.COLOR_LAB2RGB)

	showcase_img = np.concatenate((gray_image, color_image, colored_img), axis=1)
	util.showimage("side-by-side", showcase_img)