# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 13:42:27 2021

@author: 安ㄢ
"""

from PIL import ImageDraw
from PIL import Image
img = Image.new("RGB",(300,400),"lightgray")
drawing = ImageDraw.Draw(img)
drawing.ellipse((50,50,250,250),width=3,outline="gold")
drawing.polygon([(100,90),(120,130),(80,130)],fill="lightblue",outline="pink")
drawing.polygon([(200,90),(220,130),(180,130)],fill="lightblue",outline="pink")
drawing.text((130,280),"Try try look",fill = "orange")
img.show()
img.save("media\\happyface.png")