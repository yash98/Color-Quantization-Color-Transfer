import cv2 as cv
import matplotlib.pyplot as plt

def plot_histogram(img):
    for i, col in enumerate(['b', 'g', 'r']):
        hist = cv.calcHist([img], [i], None, [256], [0, 256])
        print(hist)
        plt.plot(hist, color = col)
        plt.xlim([0, 256])
    
    plt.show()