# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 23:14:24 2021

@author: 安ㄢ
"""

def emptydir(dirname):
    if os.path.isdir(dirname):
        shutil.rmtree(dirname)
        sleep(2)
    os.mkdir(dirname)
    
def dirResize(src,dst):
    myfiles = glob.glob(src + '/*.JPG')
    emptydir(dst)
    print(src + '資料夾:')
    print('開始轉換圖形尺寸')
    for f in myfiles:
        fname = f.split("\\")[-1]
        img = Image.open(f)
        img_new = img.resize((300,225),PIL.Image.ANTIALIAS)
        img_new.save(dst + '/' + fname)
    print('轉換圖形尺寸完成!\n')
    
def area(row,col):
    global nn
    if bg[row][col] != 255:
        return
    bg[row][col] = lifearea
    if col > 1:
        if bg[row][col-1] == 255:
            nn += 1
            area(row,col-1)
    if col < w-1:
        if bg[row][col+1] == 255:
            nn += 1
            area(row,col+1)
    if row > 1: 
        if bg[row-1][col] == 255:
            nn += 1
            area(row-1,col)
        
    if row < h - 1:
        if bg[row+1][col] == 255:
            nn += 1
            area(row+1,col)
import PIL
from PIL import Image
import numpy as np 
import glob
import cv2
import shutil, os
from time import sleep
import sys
import pyocr
import pyocr.builders
import re
dirResize('predictPlate_sr','predictPlate')

print('開始擷取車牌!')
print('無法擷取車牌的圖片:')
dstdir = 'cropPlate'
myfiles = glob.glob('predictPlate\*.JPG')
emptydir(dstdir)
for imgname in myfiles:
    filename = imgname.split('\\')[-1]
    img = cv2.imread(imgname)
    detector = cv2.CascadeClassifier('haar_carplate2.xml')
    signs = detector.detectMultiScale(img, scaleFactor = 1.1 , minNeighbors = 10,minSize = (20,20))
    
    if len(signs) > 0:
        for (x,y,w,h) in signs:
            image1 = Image.open(imgname)
            image2 = image1.crop((x,y,x+w,y+h))
            image3 = image2.resize((140,40),Image.ANTIALIAS)
            img_gray  = np.array(image3.convert('L'))
            _, img_thre = cv2.threshold(img_gray, 127,255,cv2.THRESH_BINARY)
            cv2.imwrite(dstdir + '/' + filename, img_thre)
    else:
        print(filename)
        
print('擷取車牌結束!')

myfiles = glob.glob('cropPlate\*.jpg')
for file in myfiles:
    image = cv2.imread(file,0)
    _, thresh = cv2.threshold(image,127,255,cv2.THRESH_BINARY_INV)
    contour1 = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    contours = contour1[0]
    
    letter_image_regions = []
    for contour in contours:
        (x,y,w,h) = cv2.boundingRect(contour)
        letter_image_regions.append((x,y,w,h))
        
    letter_image_regions = sorted(letter_image_regions,key = lambda x: x[0])
    print(letter_image_regions)
    
    count = 0
    for box in letter_image_regions:
        x, y, w,h = box
        if x>=2 and x<=125 and w>=5 and w<=26 and h>=20 and h<40:
            count += 1
            
    if count < 6:
        wmax = 35
    else:
        wmax = 26
        
    nChar = 0
    letterlist = []
    for box in letter_image_regions:
        x, y, w,h = box
        if x>=2 and x<=125 and w>=5 and w<=wmax and h>=20 and h<40:
            nChar += 1
            letterlist.append((x,y,w,h))
            
    for i in range(len(thresh)):
        for j in range(len(thresh[i])):
            if thresh[i][j] == 255:
                count = 0
                for k in range(-2,3):
                    for l in range(-2,3):
                        try:
                            if thresh[i+k][j+l] == 255:
                                count += 1
                        except IndexError:
                            pass
                if count <= 6:
                    thresh[i][j] = 0
            
    real_shape = []
    for i,box in enumerate(letterlist):
        x,y,w,h = box
        bg = thresh[y:y+h,x:x+w]
        
        if i==0 or i==nChar:
            lifearea = 0
            nn=0
            life=[]
            for row in range(0,h):
                for col in range(0,w):
                    if bg[row][col] == 255:
                        nn = 1
                        lifearea += 1
                        area(row,col)
                        life.append(nn)
            maxlife = max(life)
            indexmaxlife = life.index(maxlife)
            for row in range(0,h):
                for col in range(0,w):
                    if bg[row][col] == indexmaxlife + 1:
                        bg[row][col] = 255
                    else:
                        bg[row][col] = 0
        real_shape.append(bg)
        
    image2 = thresh.copy()
    newH, newW = image2.shape
    space = 10
    bg = np.zeros((newH +space*2, newW + space*2 + 20 ,1),np.uint8)
    bg.fill(0)
        
    for i,letter in enumerate(real_shape):
        h = letter.shape[0]
        w = letter.shape[1]
        x = letterlist[i][0]
        y = letterlist[i][1]
        for row in range(h):
            for col in range(w):
                bg[space+y+row][space + x + col + i*3] = letter[row][col]
                
    _,bg = cv2.threshold(bg, 127, 255,cv2.THRESH_BINARY_INV)
    basename = os.path.basename(file)
    cv2.imwrite('result/' + basename,bg)    
    
    tools = pyocr.get_available_tools()
    if len(tools) <= 0 :
        print("No OCR tool found")
        sys.exit(1)
    tool = tools[0]
    
    result = tool.image_to_string(Image.open('result/'+ basename),builder = pyocr.builders.TextBuilder())
    
    txt = result.replace("!","1")
    real_txt = re.findall(r'[A-Z]+|[\d]+',txt)
    
    txt_Plate =""
    for char in real_txt:
        txt_Plate += char
    print("ocr 辨識結果: ",result)
      
    if basename.split(".")[0]==txt_Plate:
        mess = "V"
    else:
        mess = "X"
    print("優化後:{}   檔名:{}   辨識結果:{} ".format(txt_Plate,basename,mess))
    
    cv2.imshow('image',image)
    cv2.imshow('bg',bg)
    cv2.moveWindow("image",500,250)
    cv2.moveWindow("bg",500,350)
    key = cv2.waitKey(0)
    cv2.destroyAllWindows()
    if key ==113 or key == 81:
        break
    
                
    