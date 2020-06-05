import numpy as np
from numba import jit
# from distributionOfSIP import SIPassignment

@jit
def error_diffusion(img, r, ensure = False):
	img_height, img_width = img.shape
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
			for m in range(3):
				for n in range(3):
					try:
					# if ((i + m - 1) >= 0 and (i + m - 1) < img_height and (j + n - 1) >= 0 and (j + n - 1) < img_width):
						F[i+m-1, j+n-1] += error[i,j] * floyd_mask[m,n]
					except:
						pass

	G = np.zeros((img_height, img_width))

	for i in range(img_height):
		for j in range(img_width):
			if (F[i,j] >= 0.5):
				G[i][j] = 255

	if (ensure):
		for i in range(0, img_height, 3):
			for j in range(0, img_width, 3):
				SIP = 0
				flag = False
				for x in range(3):
					if (flag):
						break
					for y in range(3):
						if (img[i+x][j+y] == 255):
							SIP += 1
						if (SIP == r):
							flag = True
							break

	return G
