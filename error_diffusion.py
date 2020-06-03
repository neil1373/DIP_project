import numpy as np
from numba import jit
<<<<<<< HEAD

@jit # by Stanford - 死電肥爾

def error_diffusion(img):
	img_height = img.shape[0]
	img_width = img.shape[1]
=======
# from distributionOfSIP import SIPassignment

@jit
def error_diffusion(img):
	img_height, img_width = img.shape
>>>>>>> 7d8c1151d69f0cbebfe4ae61ac6fc06e90c49319
	thres = 0.5
	F = img / 255
	total_error = np.zeros((img_height, img_width))
	floyd_mask = np.array([[0, 0, 0], [0, 0, 7], [3, 5, 1]]) / 16
	error = np.zeros((img_height, img_width))

	
	for i in range(img_height):
		for j in range(img_width):
			if (F[i,j] >= 0.5):
				error[i,j] = F[i,j] - 1
			else:
				error[i,j] = F[i,j]
<<<<<<< HEAD
	for i in range(img_height):
		for j in range(img_width):
			for m in range(3):
				for n in range(3):
					if ((i + m - 1) >= 0 and (i + m - 1) < img_height and (j + n - 1) >= 0 and (j + n - 1) < img_width):
						total_error[i+m-1, j+n-1] += error[i,j] * floyd_mask[m,n]
	F += total_error
=======
			for m in range(3):
				for n in range(3):
					try:
					# if ((i + m - 1) >= 0 and (i + m - 1) < img_height and (j + n - 1) >= 0 and (j + n - 1) < img_width):
						F[i+m-1, j+n-1] += error[i,j] * floyd_mask[m,n]
					except:
						pass
>>>>>>> 7d8c1151d69f0cbebfe4ae61ac6fc06e90c49319

	G = np.zeros((img_height, img_width))
	full = False
	for i in range(img_height):
		if full == True:
			break

		for j in range(img_width):
<<<<<<< HEAD
			if (SIPassignment()):
				full = True
				break
=======
			# if (SIPassignment(i, j)):
			# 	full = True
			# 	break
>>>>>>> 7d8c1151d69f0cbebfe4ae61ac6fc06e90c49319

			if (F[i,j] >= 0.5):
				G[i][j] = 255

	return G
