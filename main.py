import numpy as np
import cv2
from error_diffusion import error_diffusion
<<<<<<< HEAD



if __name__ == "__main__":
	img = cv2.imread("input1.png", cv2.IMREAD_GRAYSCALE)
	cv2.imwrite("inputBW.png", img)
	output = error_diffusion(img)
	cv2.imwrite("e_01.png", output)
=======
from distributionOfSIP import SIPassignment

if __name__ == "__main__":
	img = cv2.imread("lena.jpg", cv2.IMREAD_GRAYSCALE)
	cv2.imwrite("input_BlackWhite.png", img)
	
	img = error_diffusion(img)
	cv2.imwrite("input_Halfton.png", img)

>>>>>>> 7d8c1151d69f0cbebfe4ae61ac6fc06e90c49319

	k = 3
	n = 3
	q = 9
	r = 4

<<<<<<< HEAD
	c0 = np.array([[0,0,1,1],[0,1,0,1],[0,1,1,0]])
	c1 = np.array([[1,1,0,0],[1,0,1,0],[1,0,0,1]])
=======
	img_share1 = cv2.imread("moon.png", cv2.IMREAD_GRAYSCALE)

	cv_img = np.zeros((img_share1.shape))
	cv_img += r * 255 / q 
	cv_img = error_diffusion(cv_img)
	cv2.imwrite("cvImg.png", cv_img)

	img_SIP = SIPassignment(img, img_share1, cv_img)

	c0 = np.array([[0,0,1,1],[0,1,0,1],[0,1,1,0]])
	c1 = np.array([[1,1,0,0],[1,0,1,0],[1,0,0,1]])

	# 先把原圖用error diffusion做halfton，然後利用c0, c1將原圖給assign給n個shares，
	# 並利用SIPassignment在過程中來確保每一個halfton cell裡有r個'1'，
	# 
>>>>>>> 7d8c1151d69f0cbebfe4ae61ac6fc06e90c49319
