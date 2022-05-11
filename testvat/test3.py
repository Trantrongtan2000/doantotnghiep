import cv2
import numpy as np
from matplotlib import pyplot as plt
# read image


image = cv2.imread('mau3.jpg')
img=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Fillter
blurM = cv2.medianBlur(img, 5)
edgeM = cv2.Canny(blurM, 100, 200)

blurG = cv2.GaussianBlur(img, (9, 9), 0)
edgeG = cv2.Canny(blurG, 50, 100)

img=edgeG
# height, width, number of channels in image
height = img.shape[0]
width = int(img.shape[1])

#print(height)
#print(width)
#img[start row, end row, start col and col]
crop=img[:,0:int(width/3)]
crop2=img[:,int(width/3):int(width/3*2)]
crop3=img[:,int(width/3*2):int(width)]

'''
cv2.imwrite('crop.jpg', crop)
cv2.imwrite('crop2.jpg', crop2)
cv2.imwrite('crop3.jpg', crop3)


c1 = cv2.imread('crop.jpg')
c2 = cv2.imread('crop2.jpg')
c3 = cv2.imread('crop3.jpg')
'''

#Show anwser image
fig = plt.figure(figsize=(10, 7))

rows = 1
columns = 3

fig.add_subplot(rows, columns, 1)
# showing image
plt.imshow(crop)
plt.axis('off')
plt.title("Anti-A")

# Adds a subplot at the 2nd position
fig.add_subplot(rows, columns, 2)

# showing image
plt.imshow(crop2)
plt.axis('off')
plt.title("Anti-B")

# Adds a subplot at the 3rd position
fig.add_subplot(rows, columns, 3)

# showing image
plt.imshow(crop3)
plt.axis('off')
plt.title("Anti-Rh")
fig.suptitle('Nhom mau:', fontsize=20)
plt.show()