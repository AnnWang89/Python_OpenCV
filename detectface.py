# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 11:03:26 2021
detect face
"""
import cv2
from keras.models import load_model
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
classifier = load_model(r'D:\python_practice\Facial_Emotion_Recognition\model.h5')
emotion_labels = ['Angry','Disgust','Fear','Happy','Sad','Surprise','Neutral']
image = cv2.imread("media\\badminton.jpg")
faces = faceCascade.detectMultiScale(image, scaleFactor=1.1,minNeighbors=6,minSize=(10,10),flags = cv2.CASCADE_SCALE_IMAGE)
imgheight = image.shape[0] #圖片高度
imgwidth = image.shape[2] #圖片寬度
cv2.rectangle(image, (10,imgheight-40), (180,imgheight-10),(1,1,1),-1)
cv2.putText(image,"Find "+ str(len(faces)) + " face!",(15,imgheight-20),cv2.FONT_HERSHEY_SIMPLEX,0.75,(255,255,255),2)
count = 1
for (x,y,w,h) in faces: #臉部矩形
    cv2.rectangle(image, (x,y), (x+w,y+h),(255,180,80),2)
    filename = "media\\face" + str(count)+ ".jpg"
    image1 = image[y: y + h, x: x + w]
    cv2.imwrite(filename, image1)
    count += 1

cv2.namedWindow("FaceDetect",cv2.WINDOW_KEEPRATIO)
cv2.imshow("FaceDetect",image)
cv2.waitKey(0)
cv2.destroyWindow("FaceDetect")