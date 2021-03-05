from src.quantize import popularity
from src.quantize import median_cut
from src.quantize import floyd_steinberg

from src.quantize import exhaustive_search
from src.quantize import kdtree_search

from src import util

import cv2 as cv
import argparse
import numpy as np
# import sys
# np.set_printoptions(threshold=sys.maxsize)

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Color Quantization")
	parser.add_argument("-rf", "--representative-finder", choices=["popularity", "median_cut"], required=True)
	parser.add_argument("-s", "--search", choices=["exhaustive", "kdtree"], required=True)
	parser.add_argument("-k", "--num-colors", type=int, required=True)
	parser.add_argument("-d", "--dithering", action="store_true")
	parser.add_argument("-o", "--output", type=str, help="Output file to save the quantized image as")
	parser.add_argument("input_image", type=str, help="Path of image to quantize")
	args = parser.parse_args()
	# print(args)

	img = cv.imread(args.input_image)
	if img is None:
		print("Could not find input image: {}\n Please ensure file path is correct".format(args.input_image))
		exit()

	representatives = popularity.algorithm(img, args.num_colors) if args.representative_finder=="popularity" else median_cut.algorithm(img, args.num_colors)
	# print(len(representatives))

	quantized_img = exhaustive_search.quantize(img, representatives) if args.search=="exhaustive" else kdtree_search.quantize(img, representatives)
		
	final_img = floyd_steinberg.dithering_algorithm(img, quantized_img) if args.dithering else quantized_img
	if args.output:
		cv.imwrite(args.output)
	showcase_img = np.concatenate((img, quantized_img), axis=1)
	util.showimage("side-by-side", showcase_img)