def algorithm(img, k):
	color_counts = {}
	for x in range(img.shape[0]):
		for y in range(img.shape[1]):
			color = img[x, y]
			color = (color[0], color[1], color[2])
			if color in color_counts:
				color_counts[color] += 1
			else:
				color_counts[color] = 1

	color_popularity_list = sorted(color_counts.items(), key=lambda item: -1*item[1])
	color_popularity_list = [color for color, _ in color_popularity_list]

	if k > len(color_popularity_list):
		return color_popularity_list

	return color_popularity_list[:k]
