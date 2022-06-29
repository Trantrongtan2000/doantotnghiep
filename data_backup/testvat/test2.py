import cv2
import numpy as np
# read image

for i in range(2,15):
    image = cv2.imread('mau'+str(i)+'.jpg')
    print('\nAnh mau: '+str(i))
    img=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # get dimensions of image
    blurM = cv2.medianBlur(img, 5)
    edgeM = cv2.Canny(blurM, 100, 200)

    blurG = cv2.GaussianBlur(img, (9, 9), 0)
    edgeG = cv2.Canny(blurG, 50, 150)

    img=edgeM
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
    a1=np.concatenate((crop,crop2,crop3),axis=0)
    cv2.imshow('',a1)
    cv2.waitKey(0)
    '''

    hist, bin=np.histogram(crop)
    print('')
    #print(hist)
    #print('')
    #print(bin)
    a=hist[-1]
    hist, bin=np.histogram(crop2)
    #print('')
    #print(hist)
    #print('')
    #print(bin)
    b=hist[-1]
    hist, bin=np.histogram(crop3)
    #print('')
    #print(hist)
    #print('')
    #print(bin)
    c=hist[-1]
    print('')
    print('%s %s %s'%(a,b,c))
    m=min(a,b,c)
    a1=a-m
    b1=b-m
    c1=c-m
    print('%s %s %s'%(a1,b1,c1))
    tong=np.mean([a1,b1,c1,m])
    print(m)
    print(np.mean([a1,b1,c1]))
    print(tong)
