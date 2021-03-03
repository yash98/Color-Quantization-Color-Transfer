import cv2 as cv
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

def dithering_algorithm(img):
    for y in range(img.shape[1]-1):
        for x in range(1,img.shape[0]-1):
            oldpixel = img[x][y]
            newpixel = find_closest_palette_color(oldpixel,5)
            img[x][y] = newpixel

            quant_error = oldpixel - newpixel
            img[x+1][y] = img[x+1][y]+ np.round(quant_error * 7/16)
            img[x-1][y+1] = img[x-1][y+1] + np.round(quant_error * 3/16)
            img[x][y+1] = img[x][y+1] + np.round(quant_error * 5/16)
            img[x+1][y+1] = img[x+1][y+1] + np.round(quant_error * 1/16)

    showimage("newimg", img)