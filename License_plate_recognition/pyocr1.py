# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 20:32:28 2021

@author: 安ㄢ
"""

from PIL import Image
import sys
import pyocr
import pyocr.builders
tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)
tool = tools[0]
txt = tool.image_to_string(Image.open('test.jpg'),builder = pyocr.builders.TextBuilder())
print("result=",txt)
