import cv2
import numpy as np


def catanh(fillter):
    width= int(fillter.shape[1])
    A = fillter[:, 0:int(width / 3)]
    B = fillter[:, int(width / 3):int(width / 3 * 2)]
    RH = fillter[:, int(width / 3 * 2):int(width)]
    #lay diem anh
    histA, bin = np.histogram(A)
    antiA=histA[-1]
    histB, bin = np.histogram(B)
    antiB=histB[-1]
    histRH, bin = np.histogram(RH)
    antiRH=histRH[-1]
    return (antiA,antiB,antiRH)
'''
for i in range(2,15):
    image = cv2.imread('mau'+str(i)+'.jpg')
    print('\nAnh mau: '+str(i))
    img=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


    blurM = cv2.medianBlur(img, 5)
    edgeM = cv2.Canny(blurM, 10, 150)

    blurG = cv2.GaussianBlur(img, (9, 9), 0)
    edgeG = cv2.Canny(blurG, 10, 100)
    
    print(catanh(edgeM))
    print(catanh(edgeG))
'''
image = cv2.imread('mau7.jpg')
img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blurM = cv2.medianBlur(img, 5)
edgeM = cv2.Canny(blurM, 10, 150)

blurG = cv2.GaussianBlur(img, (9, 9), 0)
edgeG = cv2.Canny(blurG, 10, 100)

print(catanh(edgeM))
print(catanh(edgeG))
