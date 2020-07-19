# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 01:47:42 2020

@author: Onkar
"""

import cv2
import sys
import pytesseract
import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

all_words = pd.read_csv('all_mnemonic_words.csv')
all_words = list(all_words['words'])
all_data = pd.read_csv('all_data.csv',encoding= 'unicode_escape')



if __name__ == '__main__':

  if len(sys.argv) < 2:
    print('Usage: python ocr_simple.py image.jpg')
    sys.exit(1)
  
  # Read image path from command line
  imPath = sys.argv[1]
  
  # Uncomment the line below to provide path to tesseract manually
  pytesseract.pytesseract.tesseract_cmd = 'D:\\Program Files\\Tesseract-OCR\\tesseract'

  # Define config parameters.
  # '-l eng'  for using the English language
  # '--oem 1' for using LSTM OCR Engine
  config = ('-l eng --oem 1 --psm 3')

  # Read image from disk
  im = cv2.imread(imPath, cv2.IMREAD_COLOR)

  # Run tesseract OCR on image
  text = pytesseract.image_to_string(im, config=config)
  #list_words = list(text) 
  # Print recognized text

#img_words are the indivisual words from the input image 
img_words = text.split()
''' 
out = []
buff = []
for c in text:
    if c == '\n':
        out.append(''.join(buff))
        buff = []
    else:
        buff.append(c)
else:
    if buff:
       out.append(''.join(buff))

extracted_words = list(filter(None, out))
'''

common_words = [i for i in all_words if i in img_words]



a = all_data[all_data['word'].isin(common_words)]

print(a)


  