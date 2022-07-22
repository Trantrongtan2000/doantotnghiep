from cv2 import *
import time
import os

# initialize the camera

cam = VideoCapture(0)   # 0 -> index of camera
s, img = cam.read()

localtime=time.localtime()
now=time.strftime("%d_%m_%Y_%H_%M_%S",localtime)
os.system('mkdir %s'%now)
imwrite("%s/%s.png"%(now,now),img)

