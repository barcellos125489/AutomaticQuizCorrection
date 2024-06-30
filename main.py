import cv2
import pytesseract
import os
from pathlib import Path

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
folderPath = Path("images")

for filename in os.listdir(folderPath):
    print(filename)
    filePath = os.path.join(folderPath, filename)
    imagem = cv2.imread(filePath)
    assert imagem is not None, "file could not be read, check with os.path.exists()"
    texto = pytesseract.image_to_string(imagem, lang= "por")
    print(texto)