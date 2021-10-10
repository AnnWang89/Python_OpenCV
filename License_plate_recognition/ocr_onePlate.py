# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 22:45:54 2021

@author: 安ㄢ
"""

import cv2
import sys
from PIL import Image
import pyocr
import pyocr.builders
import re

image= cv2.imread('assember.jpg')

tools = pyocr.get_available_tools()
if len(tools) == 0:
    print('No OCR tool found')
    sys.exit(1)
tool = tools[0]

result = tool.image_to_string(Image.open('assember.jpg'),builder = pyocr.builders.TextBuilder())

txt = result.replace("!","1")
real_txt = re.findall(r'[A-Z]+|[\d]+',txt)

txt_Plate =""
for char in real_txt:
    txt_Plate += char 
    
print("ocr辨識結果:",result)
print("優化後ocr辨識結果:",txt_Plate)

cv2.imshow("image",image)
cv2.moveWindow("image",580,640)
key = cv2.waitKey(0)
cv2.destroyAllWindows()
