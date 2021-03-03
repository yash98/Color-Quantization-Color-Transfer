import popularity
import median_cut
import floyd_steinberg
# import sys
# np.set_printoptions(threshold=sys.maxsize)

import cv2 as cv

def showimage(imglabel, img):
	cv.imshow(imglabel, img)
	while True:
		k = cv.waitKey(0) & 0xFF
		if k == 27:         # wait for ESC key to exit
			cv.destroyAllWindows()
			break
	cv.destroyAllWindows()

if __name__ == "__main__":
	img = cv.imread("images/fox.jpg")
	# showimage("img", img)

	# popularity.plot_histogram(img)
	# floyd_steinberg.dithering_algorithm(img)
	print(median_cut.algorithm(img))