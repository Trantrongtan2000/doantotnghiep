# Khai bao thu vien
import cv2
import numpy as np

# Ham xu li
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

# Nhap mau
nhapmau= input('Vui long nhap mau mau: ')
#nhapmau='12'
mau = 'mau'+nhapmau + '.jpg'
print('\nBan da nhap mau mau: '+nhapmau)

# Doc anh
image = cv2.imread(mau)

# Bien doi anh sang anh xam
img=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Fillter
blurM = cv2.medianBlur(img, 5)
edgeM = cv2.Canny(blurM, 100, 200)

blurG = cv2.GaussianBlur(img, (9, 9), 0)
edgeG = cv2.Canny(blurG, 50, 150)

blurM2 = cv2.medianBlur(img, 5)
edgeM2 = cv2.Canny(blurM2, 10, 150)

blurG2 = cv2.GaussianBlur(img, (9, 9), 0)
edgeG2 = cv2.Canny(blurG2, 10, 100)

# Khai bao list, dem
check=[]
demM=0
demG=0

# Cat anh
AM,BM,RHM=catanh(edgeM)
AG, BG,RHG=catanh(edgeG)

# Su dung fillter va lau histogram
fillM=catanh(edgeM)
fillG=catanh(edgeG)

fillM2=catanh(edgeM2)
fillG2=catanh(edgeG2)
AG2, BG2,RHG2=catanh(edgeG2)

# Dieu kien
if AM > 200 and BM > 200 and RHM > 200 and AG > 200 and BG > 200 and RHG > 200: #Xet tat ca duong
  if AM > 300 and AG > 300 and abs(AM-AG) >10:
      check.append(True)
  else:
      check.append(False)
  if BM > 300 and BG > 300 and abs(BM-BG) >10:
      check.append(True)
  else:
      check.append(False)
  if RHM > 300 and RHG > 300 and abs(RHM-RHG) >10:
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
    if demM == 1 and demG == 1:
        count=0
        for t in fillM:
            for i in fillG:
                if t == 0 and i == 0:
                    check.append(False)
                elif t > 100 and i > 100:
                    check.append(True)
                else:
                    continue
                if t == fillM[count]:
                    count+=1
                    break
    if demM != 0 and AG > 300 and BG > 300 and RHG > 300 or demG != 0 and AM > 300 and BM > 300 and RHM > 300:
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
    else:
        for i in fillG2:
            if AG2 < 100 and BG2 < 100 and RHG2 < 100:
                if i>0:
                    check.append(True)
                else:
                    check.append(False)
            else:
                if i<100:
                    check.append(False)
                else:
                    check.append(True)
# Ket qua
xetnhommau(check[0], check[1], check[2])