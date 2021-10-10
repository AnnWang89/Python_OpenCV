# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 22:34:59 2021

@author: 安ㄢ
"""
import cv2
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
image = cv2.imread("media\\person1.jpg")
faces = faceCascade.detectMultiScale(image, scaleFactor=1.1,minNeighbors=5,minSize=(10,10),flags = cv2.CASCADE_SCALE_IMAGE)
print("image.shape = ", image.shape)
#count = 1
for (x,y,w,h) in faces: #臉部矩形
    #cv2.rectangle(image, (x,y), (x+w,y+h),(255,180,80),2)
    a,b,c,d = x,y,w,h
    face = image[y: y + h, x: x + w]
    for col in range(y,y+h):
        for row in range(x,x+w):
            print(image[col,row],end=" ")
            image[col,row][0]=50    #設定 B 值為 0
            image[col,row][1]=50   #設定 G 值為 50
        print()
    print()
    
    #filename = "media\\face" + str(count)+ ".jpg"
    #cv2.imwrite(filename, image1)
    #count += 1

cv2.namedWindow("FaceDetect",cv2.WINDOW_KEEPRATIO)
cv2.imshow("FaceDetect",image)
cv2.waitKey(0)
cv2.destroyWindow("FaceDetect")