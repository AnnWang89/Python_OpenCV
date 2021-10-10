# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 10:11:45 2021
show and save image
"""
import cv2
cv2.namedWindow("Image")
image = cv2.imread("media\\img.jpg", 0)
cv2.imshow("Image", image)
cv2.imwrite("media\\imagecopy1.jpg", image)
cv2.imwrite("media\\imagecopy2.jpg", image, [int(cv2.IMWRITE_JPEG_QUALITY), 20])
cv2.waitKey(0)
cv2.destroyAllWindows()
