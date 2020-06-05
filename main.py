import numpy as np
import cv2
import os
from error_diffusion import error_diffusion
from scaleImg import scaleImg
# from distributionOfSIP import SIPassignment

if __name__ == "__main__":
	img = cv2.imread("sample/lena.jpg", cv2.IMREAD_GRAYSCALE)
	img_share1 = cv2.imread("sample/baboon.png", cv2.IMREAD_GRAYSCALE)
	img_share2 = cv2.imread("sample/moon.png", cv2.IMREAD_GRAYSCALE)

	# scale original share images to 3x
	img_share1S = scaleImg(img_share1)
	img_share2S = scaleImg(img_share2)
	img_share3S = 255 - img_share2S

	cv2.imwrite("output/baboon_scale.png", img_share1S)
	cv2.imwrite("output/moon_scale.png", img_share2S) 
	cv2.imwrite("output/moonContrast_scale.png", img_share3S) 

	k = 3
	n = 3
	q = 9
	r = 4

	img = error_diffusion(img, r)
	cv2.imwrite("output/input_Halfton.png", img)


	

	cv_img = np.zeros((img_share1.shape))
	cv_img += r * 255 / q 
	cv_img = error_diffusion(cv_img, r, True)

	cv2.imwrite("output/cvImg.png", cv_img)

	img_SIP = SIPassignment(img, img_share1S, img_share2S, img_share3S, cv_img)

	c0 = np.array([[0,0,1,1],[0,1,0,1],[0,1,1,0]])
	c1 = np.array([[1,1,0,0],[1,0,1,0],[1,0,0,1]])



