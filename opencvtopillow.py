# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 14:06:11 2021

@author: 安ㄢ
"""

import cv2
from PIL import Image
img = cv2.imread("media\\img01.jpg")

cv2.imshow("OpenCV",img)
image = Image.fromarray(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
image.show()
cv2.waitKey(0)
cv2.destroyAllWindows() 