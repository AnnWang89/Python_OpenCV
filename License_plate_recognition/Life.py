# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 17:09:43 2021

@author: 安ㄢ
"""

import cv2

def showbitmap(row,col,bg,h,w):
    for y in range(row,row+h):
        print(str('{:0>2d}').format(y) + ":" ,end = "" )
        for x in range(col,col+w):
            print(bg[y][x],end = " ,")
        print()
    print()
    
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
        
      
image = cv2.imread('7.jpg',0)
_,bg2 = cv2.threshold(image, 127,255,cv2.THRESH_BINARY_INV)
h = bg2.shape[0]
w = bg2.shape[1]  
bg=bg2.copy()
showbitmap(0,0,bg,h,w)

lifearea = 0
nn = 0
life = []

for row in range(0,h):
    for col in range(0,w):
        if bg [row][col] == 255:
            nn = 1
            lifearea =  lifearea + 1
            area(row,col)
            life.append(nn)
            
print("lifearea=",lifearea)
print(life)
maxlife = max(life)
indexmaxlife = life.index(maxlife)
showbitmap(0,0,bg,h,w)

for row in range(0,h):
    for col in range(0,w):
        if bg[row][col] == indexmaxlife + 1:
            bg[row][col] = 255
        else:
            bg[row][col] = 0

showbitmap(0,0,bg,h,w)
_,bg = cv2.threshold(bg,127,255,cv2.THRESH_BINARY_INV)
cv2.imwrite('area.jpg',bg)
cv2.imshow('Frame',bg2)
cv2.moveWindow('Frame',500,450)
cv2.imshow('bg',bg)
cv2.moveWindow('bg',500,550)
key = cv2.waitKey(0)
cv2.destroyAllWindows()
