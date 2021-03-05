import cv2 as cv

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
