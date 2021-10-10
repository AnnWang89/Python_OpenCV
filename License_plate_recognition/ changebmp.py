# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 15:52:43 2021

@author: 安ㄢ
"""

from PIL import Image
import glob
import os

myfile = glob.glob( 'carPlate/*.JPG')
print(' 開始轉換圖形格式! ')
for f in myfile:
    namespilt = f.split("\\")  #??
    img = Image.open(f)
    outname = namespilt[1].replace('resizejpg','bmpraw')
    outname = outname.replace('.jpg', '.bmp')
    img.save('carPlate/' + outname, 'bmp')
    os.remove(f)
print(' 晚換圖形格式結束! ')
