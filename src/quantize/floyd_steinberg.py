import numpy as np
from .. import util

def dithering_algorithm(img, quantized_img):
    new_img = quantized_img.copy()
    for y in range(img.shape[1]-1):
        for x in range(1,img.shape[0]-1):
            oldpixel = img[x][y]
            newpixel = quantized_img[x][y]

            quant_error = oldpixel - newpixel
            new_img[x+1][y] = new_img[x+1][y] + np.round(quant_error * 7/16)
            new_img[x-1][y+1] = new_img[x-1][y+1] + np.round(quant_error * 3/16)
            new_img[x][y+1] = new_img[x][y+1] + np.round(quant_error * 5/16)
            new_img[x+1][y+1] = new_img[x+1][y+1] + np.round(quant_error * 1/16)

    # util.showimage("new_img", new_img)
    return new_img