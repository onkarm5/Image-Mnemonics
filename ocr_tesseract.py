import cv2
import sys
import pytesseract

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

out = list(filter(None, out))
  
  
print(out)