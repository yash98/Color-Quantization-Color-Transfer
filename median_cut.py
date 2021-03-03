import numpy as np

def select_channel(bucket):
	max_r = 255
	max_g = 255
	max_b = 255
	min_r = 0
	min_g = 0
	min_b = 0

	for r, g, b in bucket:
		max_r = max(max_r, r)
		max_g = max(max_g, g)
		max_b = max(max_b, b)
		min_r = min(min_r, r)
		min_g = min(min_g, g)
		min_b = min(min_b, b)
	
	ranges = [max_r - min_r, max_g - min_g, max_b - min_b]
	return ranges.index(max(ranges))

def median_cut(bucket, depth):
	if depth == 0 or len(bucket) == 1:
		return [bucket]
	channel_for_split = select_channel(bucket)
	to_split = sorted(bucket, key= lambda x: x[channel_for_split])
	median_index = len(to_split)//2
	return median_cut(bucket[:median_index], depth-1) + median_cut(bucket[median_index:], depth-1)

def algorithm(img, depth=4):
	initial_bucket = [img[x][y] for x in range(img.shape[0]) for y in range(img.shape[1])]
	return [np.round(np.mean(bucket, axis=0)) for bucket in median_cut(initial_bucket, depth)]
    