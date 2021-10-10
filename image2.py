# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 13:33:08 2021

@author: 安ㄢ
"""

from PIL import Image
img = Image.open("media\\img01.jpg")
w,h = img.size

img1 = img.resize((w*2,h),Image.ANTIALIAS)
img1.save("media\\resize01.jpg")

imggray = img.convert('L')
imggray.save("media\\imggray01.jpg")