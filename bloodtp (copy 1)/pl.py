import numpy as np
import cv2
import matplotlib.pyplot as plt

# read original image
tenfile=input('Nhap vo may: ')
image = cv2.imread(tenfile)
# convert to gray scale image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite(tenfile+'/gray.png', gray)

# apply median filter for smoothning
blurM = cv2.medianBlur(gray, 5)
cv2.imwrite(tenfile+'blurM.png', blurM)

# apply gaussian filter for smoothning
blurG = cv2.GaussianBlur(gray, (9, 9), 0)
cv2.imwrite(tenfile+'blurG.png', blurG)

# histogram equalization
histoNorm = cv2.equalizeHist(gray)
cv2.imwrite(tenfile+'histoNorm.png', histoNorm)

# create a CLAHE object for
# Contrast Limited Adaptive Histogram Equalization (CLAHE)
clahe = cv2.createCLAHE(clipLimit = 2.0, tileGridSize=(8, 8))
claheNorm = clahe.apply(gray)
cv2.imwrite(tenfile+'claheNorm.png', claheNorm)


# contrast stretching
# Function to map each intensity level to output intensity level.
def pixelVal(pix, r1, s1, r2, s2):
	if (0 <= pix and pix <= r1):
		return (s1 / r1) * pix
	elif (r1 < pix and pix <= r2):
		return ((s2 - s1) / (r2 - r1)) * (pix - r1) + s1
	else:
		return ((255 - s2) / (255 - r2)) * (pix - r2) + s2

	# Define parameters.


r1 = 70
s1 = 0
r2 = 200
s2 = 255

# Vectorize the function to apply it to each value in the Numpy array.
pixelVal_vec = np.vectorize(pixelVal)

# Apply contrast stretching.
contrast_stretched = pixelVal_vec(gray, r1, s1, r2, s2)
contrast_stretched_blurM = pixelVal_vec(blurM, r1, s1, r2, s2)

cv2.imwrite(tenfile+'contrast_stretch.png', contrast_stretched)
cv2.imwrite(tenfile+'contrast_stretch_blurM.png',
			contrast_stretched_blurM)

# edge detection using canny edge detector
edge = cv2.Canny(gray, 100, 200)
cv2.imwrite(tenfile+'edge.png', edge)

edgeG = cv2.Canny(blurG, 100, 200)
cv2.imwrite(tenfile+'edgeG.png', edgeG)

edgeM = cv2.Canny(blurM, 100, 200)
cv2.imwrite(tenfile+'edgeM.png', edgeM)
