# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 10:37:10 2021

@author: 安ㄢ
"""

import cv2
def show(image):
    for y in range(8,14):
        for x in range(6,10):
            print(image[y,x],end=" ")
        print()
    print()
gray = cv2.imread("media\\face.jpg",0)
print("gray.shape=", gray.shape)
show(gray)
#_,thresh = cv2.threshold(gray,187,200,cv2.THRESH_BINARY_INV)
_,thresh = cv2.threshold(gray,187,255,cv2.THRESH_BINARY)
print("gray.shape=", gray.shape)
show(thresh)

cv2.namedWindow("Facegray",cv2.WINDOW_KEEPRATIO)
cv2.imshow("Facegray",thresh)
cv2.waitKey(0)
cv2.destroyWindow("Facegray")