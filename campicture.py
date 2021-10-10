# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 21:38:21 2021

@author: 安ㄢ
"""

import cv2
cv2.namedWindow("frame")
cap = cv2.VideoCapture(0)
while(cap.isOpened()):
    ret,img = cap.read()
    if ret == True:
        cv2.imshow("frame",img)
        k = cv2.waitKey(100)
        if k == ord("z") or k == ord("Z"):
            cv2.imwrite("media\\catch.jpg",img)
            break
cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows() 