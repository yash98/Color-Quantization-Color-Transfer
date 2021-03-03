import numpy as np

def medians(bucket, depth, meds=[]):
    if bucket = []:
        return
    if depth == 0:
        meds.append()
        return meds
    medians(bucket[],depth-1,meds)
    medians(bucket[],depth-1,meds)

def algorithm(img):
    r_bucket = []
    g_bucket = []
    b_bucket = []
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            r_bucket.append(img[x][y][0])
            g_bucket.append(img[x][y][1])
            b_bucket.append(img[x][y][2])
    
    r_range = max(r_bucket) - min(r_bucket)
    g_range = max(g_bucket) - min(g_bucket)
    b_range = max(b_bucket) - min(b_bucket)

    bucket = [(r_bucket[i], g_bucket[i], b_bucket[i]) for i in range(len(r_bucket))]

    color_ranges = {'r': r_range, 'g': g_range, 'b': b_range}
    chosen_color = max(color_ranges, key=color_ranges. get)

    sorted_bucket = []

    if chosen_color == 'r':
        sorted_bucket = sorted(bucket, key = lambda x: x[0])
    elif chosen_color == 'g':
        sorted_bucket = sorted(bucket, key = lambda x: x[1])
    else:
        sorted_bucket = sorted(bucket, key = lambda x: x[2])

    