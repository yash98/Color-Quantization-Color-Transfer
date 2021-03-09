from src import util

import argparse
import cv2 as cv

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
	
