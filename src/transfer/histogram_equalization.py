import numpy as np

def equalize(target_img, template_img):
	mean_target = np.mean(target_img)
	mean_template = np.mean(template_img)

	std_target = np.std(target_img)
	std_template = np.std(template_img)

	return (target_img - mean_target) * (std_template/std_target) + mean_template
