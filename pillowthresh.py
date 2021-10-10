# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 15:40:43 2021

@author: 安ㄢ
"""

from PIL import Image
img = Image.open("media\\img01.jpg")
w,h = img.size
img = img.convert('L')
for i in range(w):
    for j in range(h):
        if img.getpixel((i,j)) < 99:
            img.putpixel((i,j),(0))
        else:
            img.putpixel((i,j),(250))

img.save("media\\thresh2.jpg")
img.show()