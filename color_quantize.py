from src.quantize import popularity
from src.quantize import median_cut
from src.quantize import floyd_steinberg

from src import util

import cv2 as cv
import argparse
# import sys
# import numpy as np
# np.set_printoptions(threshold=sys.maxsize)

if __name__ == "__main__":
	img = cv.imread("images/fox.jpg")
	# util.showimage("img", img)

	# popularity.plot_histogram(img)
	# floyd_steinberg.dithering_algorithm(img)
	print(median_cut.algorithm(img))