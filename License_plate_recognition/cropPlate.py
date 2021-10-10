# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 16:44:27 2021

@author: 安ㄢ
"""

def emptydir(dirname):
    if os.path.isdir(dirname):
        shutil.rmtree(dirname)
        sleep(2)
    os.mkdir(dirname)
    
import cv2
from PIL import Image
import glob
import shutil,os
from time import sleep
import numpy as np

print('開始擷取車牌')
print('無法擷取車牌的圖片: ')
dstdir = 'cropPlate'
emptydir(dstdir)
myfiles = glob.glob("predictPlate\*.JPG")
for imgname in myfiles:
    filename = (imgname.split('\\'))[-1]
    img = cv2.imread(imgname)
    detector = cv2.CascadeClassifier('haar_carplate.xml')
    signs = detector.detectMultiScale(img, scaleFactor = 1.1 , minNeighbors = 8, minSize = (20,20))
    
    if len(signs) > 0:
        for (x,y,w,h) in signs:
            image1 = Image.open(imgname)
            image2 = image1.crop((x,y,x+w,y+h))
            image3 = image2.resize((140,40),Image.ANTIALIAS)
            image_gray = np.array(image3.convert('L'))
            _,img_thre = cv2.threshold(image_gray,127,255,cv2.THRESH_BINARY)
            cv2.imwrite(dstdir + '/' + filename, img_thre)
    else:
        print(filename)
        
print('擷取車牌結束')