import cv2
import numpy as np

image = cv2.imread('mau5.jpg')

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
        if b == True:
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

check=[]
demM=0
demG=0
AM,BM,RHM=catanh(edgeM)
AG, BG,RHG=catanh(edgeG)
fillM=catanh(edgeM)
fillG=catanh(edgeG)
if AM and BM and RHM and AG and BG and RHG > 200: #Xet tat ca duong
  if AM and AG > 300 and abs(AM-AG) >10:
      check.append(True)
  else:
      check.append(False)
  if BM and BG > 300 and abs(BM-BG) >10:
      check.append(True)
  else:
      check.append(False)
  if RHM and RHG > 300 and abs(RHM-RHG) >10:
      check.append(True)
  else:
      check.append(False)

else:
    for t in fillM:
        if t == 0:
            demM += 1
    for t in fillG:
        if t == 0:
            demG += 1
    print(demM)
    print(demG)
    if demM == 1 and demG == 1:
        for t in fillM:
            for i in fillG:
                if t == 0 and i == 0:
                    check.append(False)
                elif t > 100 and i > 100:
                    check.append(True)
    if demM != 0 and bool(AG and BG and RHG > 300) or demG != 0 and bool(AM and BM and RHM > 300):
        if AM == 0 or AG == 0:
            check.append(False)
        else:
            check.append(True)
        if BM == 0 or BG == 0:
            check.append(False)
        else:
            check.append(True)
        if RHM == 0 or RHG == 0:
            check.append(False)
        else:
            check.append(True)



print(bool(AG and BG and RHG > 300))
print(demM != 0)
xetnhommau(check[0], check[1], check[2])
#print(check)