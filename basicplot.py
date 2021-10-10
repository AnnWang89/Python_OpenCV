# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 10:26:59 2021
draw on image
"""
import cv2, numpy

cv2.namedWindow("Plot",cv2.WINDOW_KEEPRATIO)
image = cv2.imread("media\\img.jpg", 1)
cv2.line(image, (0,0), (600,600),(240,150,80),3)
cv2.rectangle(image, (600,50), (700,150),(240,200,100),3)
cv2.rectangle(image, (700,50), (900,150),(140,100,70),-1)
cv2.circle(image, (500,500),100,(10,10,200),2)
cv2.circle(image, (800,600),100,(210,10,200),-1)
pts = numpy.array([[100,160],[300,280],[150,300]],numpy.int32)
cv2.polylines(image,[pts],True,(100,255,100),2)
cv2.putText(image,"Free",(50,700),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,2,(180,70,20),2)
cv2.imshow("Plot", image)
cv2.imwrite("media\\plotimage.jpg", image)
#cv2.imwrite("media\\imagecopy2.jpg", image, [int(cv2.IMWRITE_JPEG_QUALITY), 20])
cv2.waitKey(0)
cv2.destroyAllWindows()