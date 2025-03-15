from PIL import Image, ImageFilter, ImageEnhance
import os

path = "./images"
pathOut = "./editedimg"

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")
    img.show()

   # edit = img.filter(ImageFilter.BLUR) 
    factor = 1.5
    enhancer = ImageEnhance.Color(img)
    enhancer = ImageEnhance.Sharpness(edit)

    edit = enhancer.enhance(factor) 
    cleanname = os.path.splitext(filename)[0]

    edit.save(f"{pathOut}/{cleanname}_edited.png")
    edit.show()
