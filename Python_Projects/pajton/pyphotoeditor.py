# it needs pillow python library
import os
from PIL import Image, ImageEnhance, ImageFilter

path = "./imgs"
pathout = "/pyimgs"

for filename in os.listdir(path):
    if filename == ".DS_Store":
        continue
    img = Image.open(f"{path}/{filename}")
    edit = img.filter(ImageFilter.SHARPEN).convert('L')

    clean_name = os.path.splitext(filename)[0]
    edit.save(f".{pathout}/{clean_name}_edited.jpg")