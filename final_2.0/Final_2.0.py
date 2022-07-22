from cProfile import label
import cv2
from matplotlib.pyplot import text
import numpy as np
import os
import sys
from tkinter import *
import tempfile
from PIL import ImageTk,Image
from tkinter import filedialog
import tkinter as tk
import cv2
import time
import os
import shutil

root = Tk() 
root.title('Xét nghiệm nhóm máu')
root.geometry('600x250')
tght=time.localtime()
dir='log_'+time.strftime("%d_%m_%Y_%H_%M_%S", tght)
if os.path.exists(dir):
    shutil.rmtree(dir)
os.makedirs(dir)

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





def myClick():
    root.filename = filedialog.askopenfilename(initialdir="C:", title="Select A File", filetypes=(("jpg files", "*.jpg"),("all files", "*.*")))
    my_label = Label(root, text = root.filename)
    pic = Image.open(root.filename) 
    pic.thumbnail((350,350))
    pic = ImageTk.PhotoImage(pic)
    pic_label1.configure(image=pic)
    pic_label1.image = pic
    root.mainloop()
def analyze():
    localtime = time.localtime()
    now = time.strftime("%d_%m_%Y_%H_%M_%S", localtime)
    basename=os.path.basename(root.filename)
    image = cv2.imread(root.filename)
    w = 208
    h = int((image.shape[1] * 208) / image.shape[0])
    image = cv2.resize(image, (h, w))
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurM = cv2.medianBlur(img, 5)  
    edgeM = cv2.Canny(blurM, 100, 200)

    blurG = cv2.GaussianBlur(img, (9, 9), 0)
    edgeG = cv2.Canny(blurG, 50, 150)

    blurM2 = cv2.medianBlur(img, 5)
    #edgeM2 = cv2.Canny(blurM2, 10, 150)

    blurG2 = cv2.GaussianBlur(img, (9, 9), 0)
    edgeG2 = cv2.Canny(blurG2, 10, 100)
    os.system('mkdir %s/%s'%(dir,now))
    cv2.imwrite('%s/%s/%s_%s_gray.jpg'%(dir,now,basename,now), img)
    cv2.imwrite('%s/%s/%s_%s_blurM.jpg' % (dir,now,basename,now), blurM)
    cv2.imwrite('%s/%s/%s_%s_edgeM.jpg' % (dir,now,basename,now), edgeM)
    cv2.imwrite('%s/%s/%s_%s_blurG.jpg' % (dir,now,basename,now), blurG)
    cv2.imwrite('%s/%s/%s_%s_edgeG.jpg' % (dir,now,basename,now), edgeG)
    cv2.imwrite('%s/%s/%s_%s_blurG2.jpg' % (dir,now,basename,now), blurG2)
    cv2.imwrite('%s/%s/%s_%s_edgeG2.jpg' % (dir,now,basename,now), edgeG2)
    cv2.imwrite('%s/%s/%s_%s_blurM2.jpg' % (dir,now,basename,now), blurM2)

    check=[]
    demM=0
    demG=0

    AM,BM,RHM=catanh(edgeM)
    AG,BG,RHG=catanh(edgeG)

    fillM=catanh(edgeM)
    fillG=catanh(edgeG)

    #fillM2=catanh(edgeM2)
    fillG2=catanh(edgeG2)

    AG2, BG2,RHG2=catanh(edgeG2)
    count=0
    if AM > 200 and BM > 200 and RHM > 200 and AG > 200 and BG > 200 and RHG > 200: #Xet tat ca duong
      if AM > 300 and AG > 300 and abs(AM-AG) >10 and RHM <2000 and RHG <2000 and AM < 520 and AG < 520:
          check.append(True)
          #print('AM > 300')
      elif AM <1000 and RHM >1400:
          check.append(False)
          #print(' AM =0')
      elif AM >590 and AG >590:
          check.append(True)
          #print('AM>590')
      else:
          check.append(False)
          #print(' AM =0')
      if BM > 300 and BG > 300 and abs(BM-BG) >10 and RHM <2000 and RHG <2000 and BM < 520 and BG < 520:
          check.append(True)
          #print('BM > 300')
      elif BM < 1000 and RHM > 2000:
          check.append(False)
          #print(' AM =0')
      elif BM >590 and BG >590:
          check.append(True)
      else:
          check.append(False)
          #print(' AM =0')
      if RHM > 300 and RHG > 300 and abs(RHM-RHG) >10 and RHM <2000 and RHG <2000:
          check.append(True)
          #print('RHM > 300')
      elif RHM > 2000:
          check.append(True)
          #print('RHM >2000')
      else:
          check.append(False)
          #print(' AM =0')
    else:
        for t in fillM:
            if t == 0:
                demM += 1
        for t in fillG:
            if t == 0:
                demG += 1
        if demM == 1 and demG == 1:
            if AM == 0 and AG==0:
                check.append(False)
                #print(' AM =0')
            elif AM > 100 and AG > 100 and RHM < 1500 and RHG < 1500:
                check.append(True)
                #print('DM > 100')
            elif AM > 1000 and AG > 1000:
                check.append(True)
            else:
                check.append(False)
                #print(' AM =0')
            if BM == 0 and BG==0:
                check.append(False)
                #print(' AM =0')
            elif BM > 100 and BG > 100 and RHM < 1500 and RHG < 1500:
                check.append(True)
                #print('DM > 100')
            elif BM > 1000 and BG > 1000:
                check.append(True)
            else:
                check.append(False)
                #print(' AM =0')
            if RHM == 0 and RHG==0:
                check.append(False)
                #print(' RHM =0')
            elif RHM > 100 and RHG > 100:
                check.append(True)
                #print('RHM > 100')
            else:
                check.append(False)
                #print(' AM =0')
        elif demM != 0 and AG > 310 and BG > 310 and RHG > 310 or demG != 0 and AM > 310 and BM > 310 and RHM > 310:
            if AM == 0 or AG == 0:
                check.append(False)
                #print(' AM =0')
            else:
                check.append(True)
                #print('AM = 0')
            if BM == 0 or BG == 0:
                check.append(False)
                #print(' AM =0')
            else:
                check.append(True)
                #print('ABM = 0')
            if RHM == 0 or RHG == 0:
                check.append(False)
                #print(' RHM =0')
            else:
                check.append(True)
        else:
            for i in fillG2:
                tru1=abs(i-fillM[count])
                tru2=abs(i- fillG[count])
                if sum(fillM) == 0 and sum(fillG) == 0:
                    if i > 100 and sum(fillG2) > 100:
                        check.append(True)
                    elif i < 100 and i > 0 and sum(fillG2) < 100:
                        check.append(True)
                    else:
                        check.append(False)
                elif AG2 < 100 and BG2 < 100 and RHG2 < 100:
                    if i>0:
                        check.append(True)
                        #print('AG2 < 100')
                    else:
                        check.append(False)
                        #print(' AM =0')
                elif i > 1000:
                    check.append(True)
                    #print('AG2 > 1000')
                else:
                    if i<550 and i>100:
                        if tru1>100 or tru2>100:
                            if max(fillG2) < 1500 and i>500:
                                check.append(True)
                                #print(max(fillG2))
                                #print('tru1 >100 or tru2>100')
                            else:
                                check.append(False)
                        else:
                            check.append(False)
                            #print('i<550')
                    elif i>550:
                        check.append(True)
                        #print('i>550')
                    elif i<100 and tru1<100 and tru2<100:
                        if tru1==0 and tru2==0:
                            check.append(False)
                            #print('i=0')
                        else:
                            check.append(True)
                    elif tru1<100 and tru2<100:
                        check.append(True)
                        #print("tru1")
                    else:
                        #print('done')
                        check.append(True)
                count+=1
     # Ket qua
    ketqua=xetnhommau(check[0], check[1], check[2])
    cuoicung='Nhom_mau_%s'%ketqua
    duongdan='%s/%s/%s.txt'%(dir, now,cuoicung)
    noidung='Ket qua phan tich xac dinh nhom mau: %s'%ketqua
    f = open(duongdan, "a")
    f.write(noidung)
    f.close()

    root.mainloop()

def snap():
    cam = VideoCapture(0)  # 0 -> index of camera
    s, img = cam.read()
    localtime = time.localtime()
    now = time.strftime("%d_%m_%Y_%H_%M_%S", localtime)
    os.system('mkdir %s' % now)
    imwrite("%s/%s.jpg" % (now, now), img)
    return None

def xetnhommau(a,b,rh):
    entry1.delete(0, END)
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
    
    text = nm
    entry1.insert(0, text)
    return text
    

    





myButton = Button(root, text="Open",padx=40, pady=20 , command=myClick)
button_quit = Button(root, text="ExitProgram",padx=40, pady=20 , command=root.quit)
pic_label1 = Label(root)
button_analyze = Button(root, text="Analyze",padx=40, pady=20 , command=analyze)
button_snap = Button(root, text="Snap",padx=40, pady=20 , command=snap)
entry1=Entry(root,width=5, borderwidth= 3)




pic_label1.grid(row=0, column=0, columnspan= 4,)
entry1.grid(row=2, column=0, columnspan=3)
myButton.grid(row=1, column=0)
button_analyze.grid(row=1, column=1)
button_snap.grid(row=1, column=3)
button_quit.grid(row=1, column=2)
root.mainloop()