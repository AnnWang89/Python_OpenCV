# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 17:25:55 2021

@author: 安ㄢ
"""

def emptydir(dirname):
    if os.path.isdir(dirname):
        shutil.rmtree(dirname)
        sleep(2)
    os.mkdir(dirname)
    
import cv2
import shutil,os
from time import sleep

emptydir('cropMono')
image = cv2.imread('7238N2.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)
contours1 = cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
contours = contours1[0]
letter_image_regions =[]
for contour in contours:
    (x,y,w,h) = cv2.boundingRect(contour)
    letter_image_regions.append((x,y,w,h))
letter_image_regions = sorted(letter_image_regions,key = lambda x: x[0])
print(letter_image_regions)

i=1
for letter_bounding_box in letter_image_regions:
    x,y,w,h =letter_bounding_box
    print(x,y,w,h)
    if w>=5 and h>28 and h<40:
        letter_image = gray[y:y+h,x:x+w]
        letter_image = cv2.resize(letter_image,(18,38))
        cv2.imwrite('cropMono/{}.jpg'.format(i),letter_image)
        i+=1
        
    