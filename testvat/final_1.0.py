import cv2
import numpy as np

image = cv2.imread('mau3.jpg')

#image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
img=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Fillter
blurM = cv2.medianBlur(img, 5)
edgeM = cv2.Canny(blurM, 100, 200)

blurG = cv2.GaussianBlur(img, (9, 9), 0)
edgeG = cv2.Canny(blurG, 50, 150)

'''
# width in image

widthM = int(edgeM.shape[1])

#img[start row, end row, start col and col]
AM=img[:,0:int(widthM/3)]
BM=img[:,int(widthM/3):int(widthM/3*2)]
RHM=img[:,int(widthM/3*2):int(widthM)]

widthG = int(edgeG.shape[1])

#img[start row, end row, start col and col]
AG=img[:,0:int(widthG/3)]
BG=img[:,int(widthG/3):int(widthG/3*2)]
RHG=img[:,int(widthG/3*2):int(widthG)]
'''

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

def xetnhommau(a,b,rh):
    if a == True:
        if b == True:
            if rh == True:
                nm='AB+'
            else:
                nm='AB-'
        else:
            if rh == True:
                nm='A+'
            else:
                nm='A-'
    else:
        if B == True:
            if rh== True:
                nm='B+'
            else:
                nm='B-'
        else:
            if rh == True:
                nm = 'O+'
            else:
                nm= 'O-'
    return print('Nhom mau: '+nm)
AM,BM,RHM=catanh(edgeM)
AG, BG,RHG=catanh(edgeG)

xetnhommau(True,False,False)
