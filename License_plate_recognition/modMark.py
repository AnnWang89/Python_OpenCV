# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 17:45:04 2021

@author: 安ㄢ
"""

fp = open('Haar-Training_carPlate/training/positive/info.txt','r')
lines = fp.readlines()
rettext = ''
print("開始轉換圖框")
for line in lines:
    data = line.split(' ')
    n = data[1]
    rettext += data[0] + ' ' + n +' '
    for i in range(int(n)):
        x = int(data[2+i*4])
        y = int(data[3+i*4])
        w = int(data[4+i*4])
        h = int(data[5+i*4])
        if (w/h) < 3.8:
            newW = h*3.8
            x -= int((newW - w)/2)
            if x <= 0:
                x=0
            w = int(newW)
        rettext = rettext +str(int(x)) + ' ' + data[3+i*4]+' '+str(int(w)) + ' ' +data[5+i*4]
    

fp.close()

fp = open('Haar-Training_carPlate/training/positive/info.txt','w')
fp.write(rettext)
fp.close()
print("轉換圖框結束")