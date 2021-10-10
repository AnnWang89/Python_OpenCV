# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 16:13:40 2021

@author: 安ㄢ
"""

def emptydir(dirname):
    if os.path.isdir(dirname):
        shutil.rmtree(dirname)
        sleep(2)
    os.mkdir(dirname)
    
import PIL
from PIL import Image
import glob
import shutil,os
from time import sleep

myfiles = glob.glob("carNegative_sr/*.JPG")
emptydir('carNegative')
print(' 開始轉換尺寸及灰階')
for i,f in enumerate(myfiles):
    img = Image.open(f)
    img_new = img.resize((500,375),PIL.Image.ANTIALIAS)
    img_new = img_new.convert('L')
    outname = str("negGray") + str('{:0>3d}').format(i+1) +'.jpg'
    img_new.save( 'carNegative/' + outname)

print(' 轉換灰階及尺寸完成!\n')