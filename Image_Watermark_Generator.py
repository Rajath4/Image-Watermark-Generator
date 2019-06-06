import os
from random import randint
path_orig = './Original Image/'
path_modif = './Watermarked Image/'

from PIL import Image
import os
from pylab import *
import re
from PIL import Image, ImageChops, ImageEnhance

folder_orig = os.listdir()
folder_modif = os.listdir()

strings = []

for file in os.listdir(path_orig):
  try:
    if file.endswith('jpg'):
      line =  path_orig + file
      fake_image =  path_modif + file
      photo = Image.open(line).convert("RGBA")
      watermark = Image.open('watermark.png').convert("RGBA")
      width, height = photo.size
      positionX = randint(1,width)
      positionY = randint(1,height)
      photo.paste(watermark, (positionX,positionY))    
      photo.save(fake_image, 'PNG')

  except Exception as e: 
      print(e)


