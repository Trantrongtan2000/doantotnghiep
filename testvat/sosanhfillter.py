import cv2
import numpy as np
import statistics

# read image
taM=[]
tbM=[]
tcM=[]

taG=[]
tbG=[]
tcG=[]


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
    img2=edgeG
    # height, width, number of channels in image
    height = img.shape[0]
    width = int(img.shape[1])

    #print(height)
    #print(width)

    #img[start row, end row, start col and col]
    eM1=img[:,0:int(width/3)]
    eM2=img[:,int(width/3):int(width/3*2)]
    eM3=img[:,int(width/3*2):int(width)]

    eG1=img2[:,0:int(width/3)]
    eG2=img2[:,int(width/3):int(width/3*2)]
    eG3=img2[:,int(width/3*2):int(width)]
    '''
    a1=np.concatenate((crop,crop2,crop3),axis=0)
    cv2.imshow('',a1)
    cv2.waitKey(0)
    '''

    hist, bin =np.histogram(eM1)
    print('')
    a=hist[-1]


    hist, bin =np.histogram(eM2)
    b=hist[-1]

    hist, bin =np.histogram(eM3)
    c=hist[-1]

    #taM.append(a)
    #tbM.append(b)
    #tcM.append(c)

    print('Fillter M')
    print('%s %s %s'%(a,b,c))

    m = min(a, b, c)
    a1=a-m
    b1=b-m
    c1=c-m
    print('tru so nho nhat')
    print('%s %s %s'%(a1,b1,c1))
    tong=np.mean([a1,b1,c1,m])
    print('so nho nhat')
    print(m)
    print('trung binh cong:')
    print(np.mean([a1,b1,c1]))
    print('phuong phai di do khum nho ten:')
    print(tong)

    m=min(a,b,c)
    a1=a-m
    b1=b-m
    c1=c-m
    print('%s %s %s'%(a1,b1,c1))
    taM.append(a1)
    tbM.append(b1)
    tcM.append(c1)

    '''
    m=min(a,b,c)
    a1=a-m
    b1=b-m
    c1=c-m
    print('%s %s %s'%(a1,b1,c1))
    tong=np.mean([a1,b1,c1,m])
    print(m)
    print(np.mean([a1,b1,c1]))
    print(tong)
    '''

    hist, bin =np.histogram(eG1)
    print('')
    a=hist[-1]
    #taG.append(a)
    hist, bin =np.histogram(eG2)
    b=hist[-1]
    #tbG.append(b)

    hist, bin =np.histogram(eG3)
    c=hist[-1]
    #tcG.append(c)

    print('Fillter G')
    print('%s %s %s'%(a,b,c))

    m = min(a, b, c)
    a1=a-m
    b1=b-m
    c1=c-m
    print('tru so nho nhat')
    print('%s %s %s'%(a1,b1,c1))
    tong=np.mean([a1,b1,c1,m])
    print('so nho nhat')
    print(m)
    print('trung binh cong:')
    print(np.mean([a1,b1,c1]))
    print('phuong phai di do khum nho ten:')
    print(tong)
    taG.append(a1)
    tbG.append(b1)
    tcG.append(c1)


print('Cac ket qua trung binh')
'''
print('Fillter M')
print(statistics.mean(taM))
print(statistics.mean(tbM))
print(statistics.mean(tcM))
print('Fillter G')
print(statistics.mean(taG))
print(statistics.mean(tbG))
print(statistics.mean(tcG))
'''

print('Fillter M')
print(taM)
print(tbM)
print(tcM)
print('Fillter G')
print(taG)
print(tbG)
print(tcG)

print('Do lech chuan')
print('Fillter M')
print(np.std(taM))
print(np.std(tbM))
print(np.std(tcM))
print('Fillter G')
print(np.std(taG))
print(np.std(tbG))
print(np.std(tcG))