from PIL import Image
import pytesseract

im = Image.open("sample1.jpg")

txt = pytesseract.image_to_string(im, lang = 'eng')

print(txt)
