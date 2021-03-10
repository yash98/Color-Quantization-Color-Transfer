import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

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

def coord_array(x, y, w):
	global coord_array_dict
	if (x, y, w) in coord_array_dict:
		return coord_array_dict[(x, y, w)]
	
	coord_arr = np.zeros((x-w, y-w, 2))
	for i in range(x-w):
		for j in range(y-w):
			coord_arr[i, j] = np.array([w+i, w+j]) 

	coord_array_dict[(x, y, w)] = coord_arr
	return coord_arr
