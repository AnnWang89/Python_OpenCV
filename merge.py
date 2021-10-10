# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 21:03:16 2021

@author: 安ㄢ
"""

import cv2,glob
import numpy as np
files = glob.glob("cropMono\*.jpg")
n = len(files)
spaceX = 10
spaceY = 8
offset = 1
img = cv2.imread(files[0])
h,w = img.shape[0],img.shape[1]

bg = np.zeros((4*(2*spaceY+h),4*(n*(w + offset)-offset+2*spaceX),1),dtype="uint8")
print(bg.shape)
bg.fill(255)

for m,file in enumerate(files):
    gray = cv2.imread(file,0)
    _,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
    for row in range(h):
        for col in range(w):
            bg[spaceY+row*4][spaceX+(col+(w+offset)*m)*4] = thresh[row][col]
    cv2.imwrite("merge.jpg",bg)
    
merge = cv2.imread("merge.jpg")
cv2.imshow("merge",merge)
cv2.waitKey(0)
cv2.destroyAllWindows()