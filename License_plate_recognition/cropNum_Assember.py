# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 22:44:10 2021

@author: 安ㄢ
"""

def area(row,col):
    global nn
    if bg[row][col] != 255:
        return
    bg[row][col] = lifearea
    if col>1:
        if bg[row][col-1]==255:
            nn+=1
            area(row,col-1)
    if col<w-1:
        if bg[row][col+1]==255:
            nn+=1
            area(row,col+1)
    if row>1:
        if bg[row-1][col]==255:
            nn+=1
            area(row-1,col)
    if row<h-1:
        if bg[row+1][col]==255:
            nn+=1
            area(row+1,col)
            
import cv2
import numpy as np

image =cv2.imread('7238N2.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)
#cv2.imshow('thresh',thresh)
contours1 = cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
contours = contours1[0]

letter_image_regions =[]
for contour in contours:
    (x,y,w,h) = cv2.boundingRect(contour)
    letter_image_regions.append((x,y,w,h))
letter_image_regions = sorted(letter_image_regions,key = lambda x: x[0])

count = 0
for box in letter_image_regions:
    x,y,w,h = box
    #print(x,y,w,h)
    if x>=2 and x<=125 and w>=5 and w<=26 and h>=20 and h<40:
        count +=1

print('count =%d'%count)
if count < 6:
    wmax = 35
else:
    wmax = 26
    
nChar = 0
letterlist=[]
for box in letter_image_regions:
    x,y,w,h = box
    #print(x,y,w,h)
    if x>=2 and x<=125 and w>=5 and w<=wmax and h>=20 and h<40:
        nChar +=1
        print(x,y,w,h)
        letterlist.append((x,y,w,h))
        
for i in range(len(thresh)):
    for j in range(len(thresh[i])):
        if thresh[i][j] == 255:
            count = 0
            for k in range(-2,3):
                for l in range(-2,3):
                    try:
                        if thresh[i+k][j+l] == 255:
                            count+=1
                    except IndexError:
                        pass    
            if count <= 6:
                thresh[i][j] = 0
                
#cv2.imshow('thresh',thresh)
real_shape =[]
for i,box in enumerate(letterlist):
    x,y,w,h = box
    bg = thresh[y:y+h,x:x+w]
    
    if i==0 or i==nChar:
        #cv2.imshow('bg1',bg)
        #cv2.moveWindow("bg1",200,250)
        lifearea = 0
        nn=0
        life =[]
        for row in range(0,h):
            for col in range(0,w):
                if bg[row][col] == 255:
                    nn=1
                    lifearea = lifearea + 1
                    area(row,col)
                    life.append(nn)
                    
        maxlife = max(life)
        indexmaxlife = life.index(maxlife)
        #cv2.imshow('bg2',bg)
        #cv2.moveWindow("bg2",200,350)
        for row in range(0,h):
            for col in range(0,w):
                if bg[row][col] == indexmaxlife + 1:
                    bg[row][col] = 255
                else:
                    bg[row][col] = 0
        
        
                    
    real_shape.append(bg)
    
    
newH,newW = thresh.shape

space = 8
offset = 2
bg = np.zeros((newH +space*2,newW + space*2 + nChar*3,1),np.uint8)
bg.fill(0)

for i,letter in enumerate(real_shape):
     h = letter.shape[0]
     w = letter.shape[1]
     x = letterlist[i][0]
     y = letterlist[i][1]
     for row in range(h):
         for col in range(w):
             bg[space + y+ row][space + x +col +i*offset] = letter[row][col]
             
_,bg = cv2.threshold(bg,127,255,cv2.THRESH_BINARY_INV)

cv2.imwrite('assember.jpg',bg)

cv2.imshow('image',image)
cv2.imshow('bg',bg)
cv2.moveWindow("image",500,250)
cv2.moveWindow("bg",500,350)
key = cv2.waitKey(0)
cv2.destroyAllWindows()