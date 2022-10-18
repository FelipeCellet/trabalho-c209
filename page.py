import cv2
import pytesseract

from pytesseract import Output

from PIL import Image # Importando o módulo Pillow para abrir a imagem no script

import pytesseract # módulo pra utilização d OCR

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

#utilizando tesseract para ler conteudo da imagem 

print(pytesseract.image_to_string( Image.open('fototrabalho.png'))) 

img = cv2.imread('fototrabalho.png ')
#mostrando palavras identificadas

d = pytesseract.image_to_data(img, output_type=Output.DICT)


n_boxes = len(d['text'])
for i in range(n_boxes):
    if int(d['conf'][i]) > 60:
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)

d['text'][6]