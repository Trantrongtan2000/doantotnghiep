import numpy as np
import cv2
import matplotlib.pyplot as plt
import os

# read original image
#ten=input('Nhap vo may: ')
for i in range(1,15):
    ten='mau'+str(i)
    tenfile=ten+'.jpg'

    image = cv2.imread(tenfile)
    os.mkdir(ten)
    os.chdir(ten)

    # convert to gray scale image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('gray.png', gray)

    # apply median filter for smoothning
    blurM = cv2.medianBlur(gray, 5)
    cv2.imwrite('blurM.png', blurM)

    # apply gaussian filter for smoothning
    blurG = cv2.GaussianBlur(gray, (9, 9), 0)
    cv2.imwrite('blurG.png', blurG)

    # edge detection using canny edge detector
    edge = cv2.Canny(gray, 100, 200)
    cv2.imwrite('edge.png', edge)

    edgeG = cv2.Canny(blurG, 100, 200)
    cv2.imwrite('edgeG.png', edgeG)

    edgeM = cv2.Canny(blurM, 100, 200)
    cv2.imwrite('edgeM.png', edgeM)
    print('Xong mau '+str(i))
    os.chdir('/media/trongtan/Tanusb/bloodtype/bloodtp')