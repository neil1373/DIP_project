import numpy as np
import cv2
from error_diffusion import error_diffusion



if __name__ == "__main__":
	img = cv2.imread("input1.png", cv2.IMREAD_GRAYSCALE)
	cv2.imwrite("inputBW.png", img)
	output = error_diffusion(img)
	cv2.imwrite("e_01.png", output)

	k = 3
	n = 3
	q = 9
	r = 4

	c0 = np.array([[0,0,1,1],[0,1,0,1],[0,1,1,0]])
	c1 = np.array([[1,1,0,0],[1,0,1,0],[1,0,0,1]])
