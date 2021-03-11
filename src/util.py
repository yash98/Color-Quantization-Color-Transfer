import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np
import random

def showimage(imglabel, img):
	cv.imshow(imglabel, img)
	while True:
		k = cv.waitKey(0) & 0xFF
		if k == 27:         # wait for ESC key to exit
			cv.destroyAllWindows()
			break
	cv.destroyAllWindows()

def find_closest_palette_color(oldpixel, roundby):
	r = round(oldpixel[0] * roundby/255) * (255/roundby)
	g = round(oldpixel[1] * roundby/255) * (255/roundby)
	b = round(oldpixel[2] * roundby/255) * (255/roundby)
	r,g,b = int(r), int(g), int(b)
	return (r,g,b)

def histogram(img):
	color = ('b', 'g', 'r')
	for i, col in enumerate(color):
		histr = cv.calcHist([img], [i], None, [256], [0,256])
		plt.plot(histr, color = col)
		plt.xlim([0, 256])
	plt.show()

coord_array_dict = {}

def coord_array(x, y):
	global coord_array_dict
	if (x, y) in coord_array_dict:
		return coord_array_dict[(x, y)]
	
	coord_arr = np.zeros((x, y, 2)).astype(np.uint32)
	for i in range(x):
		for j in range(y):
			coord_arr[i, j] = np.array([i, j]).astype(np.uint32)

	coord_array_dict[(x, y)] = coord_arr
	return coord_arr

def mark_swatches(img1, img2, rectangles):
	
	colors = [(0,0,204), (0,153,0), (255,0,0), (255,51,153), (255,255,0), (102,255,255), (204,0,204), (255,128,0), (0,102,51), (255,100,255)]
	
	random.shuffle(colors)
	
	img1_copy = img1.copy()
	img2_copy = img2.copy()
	i=0
	for rect1, rect2 in rectangles:
		(x1,y1),(x2,y2) = rect1
		(a1,b1),(a2,b2) = rect2
		img1_copy = cv.rectangle(img1_copy, (y1,x1), (y2,x2), colors[i], 2)
		img2_copy = cv.rectangle(img2_copy, (b1,a1), (b2,a2), colors[i], 2)
		i+=1
	return img1_copy, img2_copy
