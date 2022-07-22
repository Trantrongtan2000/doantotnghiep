import cv2
import numpy as np
import statistics

def sosanh(image):
    A = image[:, 0:int(width / 3)]
    B = image[:, int(width / 3):int(width / 3 * 2)]
    C = image[:, int(width / 3 * 2):int(width)]

    hist, bin = np.histogram(A)
    print('')
    a = hist[-1]

    hist, bin = np.histogram(B)
    b = hist[-1]

    hist, bin = np.histogram(C)
    c = hist[-1]

    return print('%s,%s,%s'%(a,b,c))


ten='mau%s.jpg'%i
image = cv2.imread(ten)
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

width = int(image.shape[1])

img=edgeM
img2=edgeG
img3=edgeG2
print(ten)
print("Filter edgeM")
sosanh(edgeM)
print("Filter edgeG")
sosanh(edgeG)
print("Filter edgeG2")
sosanh(edgeG2)



