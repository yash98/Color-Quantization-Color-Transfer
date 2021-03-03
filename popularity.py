import cv2 as cv
import matplotlib.pyplot as plt

def plot_histogram(img):
    freq_b, freq_g, freq_r = [], [], []
    for i, col in enumerate(['b', 'g', 'r']):
        hist = cv.calcHist([img], [i], None, [256], [0, 256])
        if col == 'b':
            freq_b = hist
        elif col == 'g':
            freq_g = hist
        else:
            freq_r = hist
    freq = [(int(freq_r[i][0]),int(freq_g[i][0]),int(freq_b[i][0])) for i in range(len(freq_r))]
    
    for f in freq:
        print(f)
    
    print(len(set(freq)))
    print(len(freq))