from src.quantize import popularity
from src.quantize import median_cut
from src.quantize import floyd_steinberg

from src.quantize import exhaustive_search

from src import util

import cv2 as cv
import argparse
import numpy as np
# import sys
# np.set_printoptions(threshold=sys.maxsize)

median_cut_depth = 5

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Color Quantization")
	parser.add_argument("-rf", "--representative-finder", choices=["popularity", "median_cut"], required=True)
	parser.add_argument("-s", "--search", choices=["exhaustive", "locally_sorted", "kdtree"], required=True)
	parser.add_argument("-d", "--dithering", action="store_true")
	parser.add_argument("-o", "--output", type=str, help="Output file to save the quantized image as")
	parser.add_argument("input_image", type=str, help="Path of image to quantize")
	args = parser.parse_args()
	# print(args)

	img = cv.imread(args.input_image)

	representives = popularity.median_cut.algorithm(img) if args.representative_finder=="popularity" else median_cut.algorithm(img, median_cut_depth)
	quantized_img = None
	if args.search=="exhaustive":
		quantized_img = exhaustive_search.quantize(img, representives)
	elif args.search=="locally_sorted":
		pass
	else:
		pass
		
	final_img = floyd_steinberg.dithering_algorithm(img, quantized_img) if args.dithering else quantized_img
	if args.output:
		cv.imwrite(args.output)
	showcase_img = np.concatenate((img, quantized_img), axis=1)
	util.showimage("side-by-side", showcase_img)