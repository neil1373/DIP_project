import numpy as np
import random


def SIPassignment(img, share1, share2, share3, Z0):
	
	c0 = np.array([[0,0,1,1],[0,1,0,1],[0,1,1,0]])
	c1 = np.array([[1,1,0,0],[1,0,1,0],[1,0,0,1]])
	
	img_height, img_width = img.shape
	m, n = share1.shape
	
	
	for i in range(img_height):
		for j in range(img_width):
			location = findSIP(Z0)
			assign(share1, share2, share3, img[i][j], location)


	return 0

def assign(share1, share2, share3, pixelvalue, location):
	
	if (pixelvalue == 0):
		M = c0
	else:
		M = c1

	r = random.randint(1, 6)
	if (r == 1):
		for a in range(len(location)):
			share1[location[a][0]][location[a][1]] = M[0][a]
			share2[location[a][0]][location[a][1]] = M[1][a]
			share3[location[a][0]][location[a][1]] = M[2][a]
	elif (r == 2):
		for a in range(len(location)):
			share1[location[a][0]][location[a][1]] = M[0][a]
			share2[location[a][0]][location[a][1]] = M[2][a]
			share3[location[a][0]][location[a][1]] = M[1][a]
	elif (r == 3):
		for a in range(len(location)):
			share1[location[a][0]][location[a][1]] = M[1][a]
			share2[location[a][0]][location[a][1]] = M[0][a]
			share3[location[a][0]][location[a][1]] = M[2][a]
	elif (r == 4):
		for a in range(len(location)):
			share1[location[a][0]][location[a][1]] = M[1][a]
			share2[location[a][0]][location[a][1]] = M[2][a]
			share3[location[a][0]][location[a][1]] = M[0][a]
	elif (r == 5):
		for a in range(len(location)):
			share1[location[a][0]][location[a][1]] = M[2][a]
			share2[location[a][0]][location[a][1]] = M[0][a]
			share3[location[a][0]][location[a][1]] = M[1][a]
	else:
		for a in range(len(location)):
			share1[location[a][0]][location[a][1]] = M[2][a]
			share2[location[a][0]][location[a][1]] = M[1][a]
			share3[location[a][0]][location[a][1]] = M[0][a]

	return


def findSIP(Z0):
	location = []
	for x in range(i, i+3):
		for y in range(j, j+3):
			if (Z0[x][y] == 255):
				location.append([x,y])
	return location
