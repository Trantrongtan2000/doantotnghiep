import cv2
import numpy as np
# read image
image = cv2.imread('mau1341.jpg')
img=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# get dimensions of image
blurM = cv2.medianBlur(img, 5)
edgeM = cv2.Canny(blurM, 100, 200)

blurG = cv2.GaussianBlur(img, (9, 9), 0)
edgeG = cv2.Canny(blurG, 50, 150)

blurM2 = cv2.medianBlur(img, 5)
edgeM2 = cv2.Canny(blurM2, 10, 150)

blurG2 = cv2.GaussianBlur(img, (9, 9), 0)
edgeG2 = cv2.Canny(blurG2, 10, 100)

img=edgeM
# height, width, number of channels in image
height = img.shape[0]
width = int(img.shape[1])

print(height)
print(width)

#img[start row, end row, start col and col]
crop=img[:,0:int(width/3)]
crop2=img[:,int(width/3):int(width/3*2)]
crop3=img[:,int(width/3*2):int(width)]
'''
a1=np.concatenate((crop,crop2,crop3),axis=0)
cv2.imshow('',a1)
cv2.waitKey(0)
'''

hist, bin=np.histogram(crop)
print('')
print(hist)
print('')
print(bin)
a=hist[-1]
hist, bin=np.histogram(crop2)
print('')
print(hist)
print('')
print(bin)
b=hist[-1]
hist, bin=np.histogram(crop3)
print('')
print(hist)
print('')
print(bin)
c=hist[-1]
print('')
print('%s %s %s'%(a,b,c))
'''
min=min(a,b,c)
a1=a-min
b1=b-min
c1=c-min
print('%s %s %s'%(a1,b1,c1))
'''