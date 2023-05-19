from PIL import Image

import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'tesseract'

print(pytesseract.image_to_string(Image.open('i1.png'), lang='tha'))