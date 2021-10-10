# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 21:50:06 2021

@author: 安ㄢ
"""

from PIL import Image

img = Image.open("media\\img01.jpg")
img.show()
w,h = img.size
print(w,h)
filename = img.filename
print(filename)