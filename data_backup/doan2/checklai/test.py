from PIL import Image, ImageTk
import cv2
import numpy as np
from matplotlib import pyplot as plt
import os

def catanh(img):
    width = int(img.shape[1])
    crop = img[:, 0:int(width / 3)]
    cv2.imwrite('Anti-A.jpg',crop)
    crop2 = img[:, int(width / 3):int(width / 3 * 2)]
    cv2.imwrite('Anti-B.jpg',crop2)
    crop3 = img[:, int(width / 3 * 2):int(width)]
    cv2.imwrite('Anti-D.jpg',crop3)

def process1(p,r):  # Extracting the Green plane
    img = cv2.imread(p)
    gi = img[:, :, 1]
    cv2.imwrite("p1"+r+".png", gi)
    return gi

def process2( p,r):  # Obtaining the threshold
    gi = process1(p,r)
    _, th = cv2.threshold(gi, 0, 255, cv2.THRESH_OTSU)
    cv2.imwrite("p2"+r+".png", th)

def process3( p,r):  # Obtaining Ni black image
    img = cv2.imread('p2'+r+'.png', 0)
    th4 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 14)
    cv2.imwrite("p3"+r+".png", th4)

def process4(r):  # Morphology: fill holes
    gi = cv2.imread('p3'+r+'.png', cv2.IMREAD_GRAYSCALE)
    th, gi_th = cv2.threshold(gi, 220, 255, cv2.THRESH_BINARY_INV)
    gi_floodFill=gi_th.copy()
    h, w = gi_th.shape[:2]
    mask = np.zeros((h+2, w+2), np.uint8)
    cv2.floodFill(gi_floodFill, mask, (0, 0), 255)
    gi_floodFill_inv = cv2.bitwise_not(gi_floodFill)
    gi_out = gi_th | gi_floodFill_inv
    cv2.imwrite('p4'+r+'.png', gi_out)

def process5(r):  # Morphing To eliminate small objects
    img = cv2.imread('p4'+r+'.png')
    kernel = np.ones((5, 5), np.uint8)
    open = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    close = cv2.morphologyEx(open, cv2.MORPH_CLOSE, kernel)
    cv2.imwrite('p5'+r+'.png', close)

def process7(r):  #Histogram
    img = cv2.imread('p5'+r+'.png', 0)
    img2 = cv2.imread('p1'+r+'.png', 0)
    mask = np.ones(img.shape[:2], np.uint8)
    hist = cv2.calcHist([img2], [0], mask, [256], [0, 256])
    min = 2000
    max = 0
    n = 0
    s = 0
    ss = 0
    for x, y in enumerate(hist):
        if y > max:
            max = y
        if y < min:
            min = y
        s += y
        n += 1

    mean = s/n
    for x, y in enumerate(hist):
        ss += (y-mean)**2
    ss /= n
    sd = abs(ss)**0.5
    print(r,"-",sd)
    mix=r+" "+str(sd)+'\n'
    log.write(mix)
    if sd < 580:
        return 1
    else:
        return 0

def start( p,r):
        global blood
        process1(p,r)
        process2(p,r)
        process3(p,r)
        process4(r)
        process5(r)
        a = process7(r)
        print(a," - ",r)
        if a == 1:
            if r == "Anti A":
                blood[0]=True
            elif r == "Anti B":
                blood[1]=True
            elif r == "Anti D":
                blood[2]=True
            elif r == "Control":
                blood[3]=True

blood=[False,False,False,False]

for t in range(1,15):
    ten='/run/media/trongtan/228426F38426C8DD/doan2/Blood-group-Detection-using-python/New folder/mau%s.jpg'%t
    print(ten)
    tenfile='mau%s'%t
    image = cv2.imread(ten)
    p=['Anti-A.jpg','Anti-B.jpg','Anti-D.jpg']
    r=["Anti A","Anti B","Anti D"]
    log=open('/run/media/trongtan/228426F38426C8DD/doan2/Blood-group-Detection-using-python//New folder/log.txt','a')
    log.write('\n' + tenfile +'\n')
    os.mkdir(tenfile)
    os.chdir(tenfile)
    catanh(image)

    for i in range(0,3):
        start(p[i],r[i])

    print('Done %s'%t)
    os.chdir('/run/media/trongtan/228426F38426C8DD/doan2/Blood-group-Detection-using-python//New folder/')