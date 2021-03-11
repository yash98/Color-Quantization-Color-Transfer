from src import util
from src.transfer import statistics
from src.transfer import jittered_sampling
from src.transfer import histogram_equalization
from src.transfer import color_map

import argparse
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import multiprocessing
# import sys
# np.set_printoptions(threshold=sys.maxsize)

sample_size_global = 200
sample_size_swatch = 50
neighbor_std_side_global = 2
neighbor_std_side_swatch = 2

def global_transfer(gray_image_lab, color_image_lab, neighbor_std_side, sample_size, showcase):
	# util.histogram(gray_image_lab)
	
	gray_neighbor_std = statistics.neighbor_std(gray_image_lab, neighbor_std_side)
	color_neighbor_std = statistics.neighbor_std(color_image_lab, neighbor_std_side)

	equalized_img = histogram_equalization.equalize(gray_image_lab, color_image_lab).astype(np.uint32)
	sample_points, sample_std = jittered_sampling.sample(color_image_lab, color_neighbor_std, sample_size)

	colored_img_lab = color_map.transfer_global(sample_points, sample_std, equalized_img, gray_neighbor_std)

	# util.histogram(color_image_lab)
	# util.histogram(equalized_img)
	# util.histogram(colored_img_lab)
	# util.histogram(color_image)

	if showcase:
		gray_image_rgb = cv.cvtColor(gray_image_lab, cv.COLOR_LAB2RGB)
		color_image_rgb = cv.cvtColor(color_image_lab, cv.COLOR_LAB2RGB)
		colored_image_rgb = cv.cvtColor(colored_img_lab.astype(np.uint8), cv.COLOR_LAB2RGB)
		plt.axis('off')
		plt.subplot(1, 3, 1)
		plt.imshow(color_image_rgb)
		plt.subplot(1, 3, 2)
		plt.imshow(gray_image_rgb)
		plt.subplot(1, 3, 3)
		plt.imshow(colored_image_rgb)
		plt.show()

	return colored_img_lab

def swatch_transfer(gray_image, color_image, rectangles, showcase):
	gray_image_lab = cv.cvtColor(gray_image, cv.COLOR_BGR2LAB)
	color_image_lab = cv.cvtColor(color_image, cv.COLOR_BGR2LAB)
	equalized_image = histogram_equalization.equalize(gray_image_lab, color_image_lab)

	plt.axis('off')
	colored_swatch_list = []
	rect_index = 0
	for rect1, rect2 in rectangles:
		(x1, y1), (x2, y2) = rect1
		(a1, b1), (a2, b2) = rect2
		# inclusive end points
		gray_swatch = equalized_image[x1:x2+1,y1:y2+1]
		color_swatch = color_image_lab[a1:a2+1,b1:b2+1]
		colored_swatch = global_transfer(gray_swatch, color_swatch, neighbor_std_side_swatch, sample_size_swatch, False)
		colored_swatch_list.append(colored_swatch)
		plt.subplot(len(rectangles), 3, 3 * rect_index + 1)
		plt.imshow(cv.cvtColor(color_swatch, cv.COLOR_LAB2RGB))
		plt.subplot(len(rectangles), 3, 3 * rect_index + 2)
		plt.imshow(cv.cvtColor(gray_swatch.astype(np.uint8), cv.COLOR_LAB2RGB))
		plt.subplot(len(rectangles), 3, 3 * rect_index + 3)
		plt.imshow(cv.cvtColor(colored_swatch.astype(np.uint8), cv.COLOR_LAB2RGB))
		rect_index += 1
	
	plt.show()

	sampled_points_dict = {}
	for colored_swatch_id in range(len(colored_swatch_list)):
		sampled_points_dict[colored_swatch_id] = jittered_sampling.coord_sample(colored_swatch_list[colored_swatch_id], sample_size_swatch, neighbor_std_side_swatch)
	
	colored_img_lab = color_map.transfer_swatch(equalized_image, sampled_points_dict, colored_swatch_list, neighbor_std_side_swatch)

	if showcase:
		gray_image_rgb = cv.cvtColor(gray_image, cv.COLOR_BGR2RGB)
		color_image_rgb = cv.cvtColor(color_image, cv.COLOR_BGR2RGB)
		colored_image_rgb = cv.cvtColor(colored_img_lab.astype(np.uint8), cv.COLOR_LAB2RGB)
		plt.axis('off')
		plt.subplot(1, 3, 1)
		plt.imshow(color_image_rgb)
		plt.subplot(1, 3, 2)
		plt.imshow(gray_image_rgb)
		plt.subplot(1, 3, 3)
		plt.imshow(colored_image_rgb)
		plt.show()

	return colored_img_lab

def plot_show(gray_image, color_image):
	gray_image_rgb = cv.cvtColor(gray_image, cv.COLOR_BGR2RGB)
	color_image_rgb = cv.cvtColor(color_image, cv.COLOR_BGR2RGB)
	plt.axis('off')
	plt.subplot(1, 2, 1)
	plt.imshow(gray_image_rgb)

	plt.subplot(1, 2, 2)
	plt.imshow(color_image_rgb)

	plt.show()

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Color Transfer")
	parser.add_argument("-s", "--swatches", action="store_true", help="To enable user interactive swatch selection")
	parser.add_argument("gray_image", type=str, help="Path of grayscale image to colorize")
	parser.add_argument("color_image", type=str, help="Path of color image based on which colorization is done")
	# parser.add_argument("-o", "--output", type=str, help="Output file to save the colored image as")
	args = parser.parse_args()

	gray_image = cv.imread(args.gray_image)
	color_image = cv.imread(args.color_image)

	if gray_image is None:
		print("Path for grey image is incorrect")
		exit()

	if color_image is None:
		print("Path for color image is incorrect")
		exit()

	if args.swatches:
		plot_proc = multiprocessing.Process(target=plot_show, args=(gray_image, color_image))
		plot_proc.start()

		rectangles = []
		while True:
			rect1 = input("Rectangle for grey image: ").split(" ")
			rect2 = input("Rectangle for color image: ").split(" ")
			if rect1[0] == '' or rect2[0] == '':
				print("Done inputting")
				break
			if len(rect1) != 4 or len(rect2) != 4:
				print("Input format is wrong")
				exit()
			rect1 = [int(x) for x in rect1]
			rect2 = [int(x) for x in rect2]
			rect1 = ((rect1[1], rect1[0]), (rect1[3], rect1[2]))
			rect2 = ((rect2[1], rect2[0]), (rect2[3], rect2[2]))
			rectangles.append((rect1, rect2))
		
		plot_proc.terminate()
		plot_show(*util.mark_swatches(gray_image, color_image, rectangles))
		swatch_transfer(gray_image, color_image, rectangles, True)
	else:
		gray_image_lab = cv.cvtColor(gray_image, cv.COLOR_BGR2LAB)
		color_image_lab = cv.cvtColor(color_image, cv.COLOR_BGR2LAB)
		global_transfer(gray_image_lab, color_image_lab, neighbor_std_side_global, sample_size_global, True)