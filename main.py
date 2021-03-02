import popularity
import median_cut
import floyd_steinberg

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
    img = cv.imread("images/parrot.jpg")
    showimage("img", img)

    popularity.plot_histogram(img)