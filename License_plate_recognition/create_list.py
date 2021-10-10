# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 16:42:55 2021

@author: 安ㄢ
"""

import glob,os

fp = open('Haar-Training_carPlate/training/negative/bg.txt','w')
files = glob.glob("Haar-Training_carPlate/training/negative/*.jpg")
print('strat to create bg.txt')
text=""
for file in files:
    basename = os.path.basename(file)
    filename = "negative/" + basename
    text += filename + "\n"
    print(text)
    
fp.write(text)
fp.close()
print('bg.txt finish')
