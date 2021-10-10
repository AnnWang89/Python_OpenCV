# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 00:13:47 2021

@author: 安ㄢ
"""

from PIL import Image
import glob
path = 'Haar-Training_carPlate/training/positive/'
fp = open(path + 'info.txt','r')
lines = fp.readlines()
count = len(glob.glob("carPlate/*.bmp"))
if len(lines) > count:
    print("新圖片已產生過")
else:
    rettext = ''
    print('開始產生新圖片')
    for line in lines:
        data = line.split(' ')
        img = Image.open(path + data[0])
        x = int(data[2])
        y = int(data[3])
        w = int(data[4])
        h = int(data[5])
        reduceW = 30
        reduceH = int(reduceW*0.75)
        multi = float(300/(300-reduceW))
        neww = int(w*multi)
        newh = int(h*multi)
        
        #left top
        if (x-reduceW)>5 and (y-reduceH)>5:
            count+=1
            newing = img.crop((reduceW,reduceH,300,225))
            newing = newing.resize((300,225),Image.ANTIALIAS)
            newing.save(path + 'rawdata/bmpraw{:0>3d}.bmp'.format(count),'bmp')
            newx = int((x-reduceW)*multi)
            newy = int((y-reduceH)*multi)
            rettext = rettext + 'rawdata/bmpraw{:0>3d}.bmp'.format(count) + ' '+ '1 ' + str(newx) + ' ' + str(newy) + ' ' +str(neww) + ' ' + str(newh)+'\n' 
            
        #right top
        if (x+w)<(300 - reduceW-5) and (y-reduceH)>5:
            count+=1
            newing = img.crop((0,reduceH,(300-reduceW),225))
            newing = newing.resize((300,225),Image.ANTIALIAS)
            newing.save(path + 'rawdata/bmpraw{:0>3d}.bmp'.format(count),'bmp')
            newx = int(x*multi)
            newy = int((y-reduceH)*multi)
            rettext = rettext + 'rawdata/bmpraw{:0>3d}.bmp'.format(count) + ' '+ '1 ' + str(newx) + ' ' + str(newy) + ' ' +str(neww) + ' ' + str(newh)+'\n' 
            
        #left buttom
        if (x-reduceW)>5 and (y+h)<(225 - reduceH-5):
            count+=1
            newing = img.crop((reduceW,0,300,225-reduceH))
            newing = newing.resize((300,225),Image.ANTIALIAS)
            newing.save(path + 'rawdata/bmpraw{:0>3d}.bmp'.format(count),'bmp')
            newx = int((x-reduceW)*multi)
            newy = int(y*multi)
            rettext = rettext + 'rawdata/bmpraw{:0>3d}.bmp'.format(count) + ' '+ '1 ' + str(newx) + ' ' + str(newy) + ' ' +str(neww) + ' ' + str(newh)+'\n' 
            
        #right buttom
        if (x+w)<(300 - reduceW-5) and (y+h)<(225 - reduceH-5):
            count+=1
            newing = img.crop((0,0,300-reduceW,225-reduceH))
            newing = newing.resize((300,225),Image.ANTIALIAS)
            newing.save(path + 'rawdata/bmpraw{:0>3d}.bmp'.format(count),'bmp')
            newx = int(x*multi)
            newy = int(y*multi)
            rettext = rettext + 'rawdata/bmpraw{:0>3d}.bmp'.format(count) + ' '+ '1 ' + str(newx) + ' ' + str(newy) + ' ' +str(neww) + ' ' + str(newh)+'\n' 
            
    fp.close()
    
    fpmake = open(path +'info.txt','a')
    fpmake.write(rettext)
    fpmake.close()
    print('產生圖片結束')